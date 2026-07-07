from dataclasses import dataclass
from typing import Optional, TypeVar
from datetime import datetime
import re
import tiktoken
from openai import OpenAI
from loguru import logger
import json
RawPaperItem = TypeVar('RawPaperItem')


_DETAILED_READING_KEYS = [
    "motivation",
    "method",
    "result",
    "conclusion",
    "key_details",
]


def _ensure_sections(payload: dict[str, str] | None) -> dict[str, str]:
    default = {
        "motivation": "暂无可提取到的动机信息。",
        "method": "暂无可提取到的方法信息。",
        "result": "暂无可提取到的结果信息。",
        "conclusion": "暂无可提取到的结论信息。",
        "key_details": "暂无可提取到的关键方法论细节。",
    }
    if not isinstance(payload, dict):
        return default
    cleaned: dict[str, str] = {}
    for key in _DETAILED_READING_KEYS:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            cleaned[key] = value.strip()
        else:
            cleaned[key] = default[key]
    return cleaned


def _extract_json_block(text: str) -> dict[str, str]:
    if not text:
        return {}
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        return {}
    block = match.group(0).strip()
    try:
        payload = json.loads(block)
    except Exception:
        return {}
    if not isinstance(payload, dict):
        return {}
    normalized = {str(k): str(v) for k, v in payload.items() if isinstance(v, (str, int, float, bool))}
    return _ensure_sections(normalized)

def _truncate_for_llm(text: str, max_tokens: int) -> str:
    try:
        enc = tiktoken.encoding_for_model("gpt-4o")
        tokens = enc.encode(text)
        return enc.decode(tokens[:max_tokens])
    except Exception as exc:
        logger.debug(f"Failed to load tiktoken encoding, falling back to character truncation: {exc}")
        return text[: max_tokens * 4]

@dataclass
class Paper:
    source: str
    title: str
    authors: list[str]
    abstract: str
    url: str
    pdf_url: Optional[str] = None
    full_text: Optional[str] = None
    tldr: Optional[str] = None
    affiliations: Optional[list[str]] = None
    detailed_reading: Optional[dict[str, str]] = None
    score: Optional[float] = None

    def _generate_tldr_with_llm(self, openai_client:OpenAI,llm_params:dict) -> str:
        lang = llm_params.get('language', 'English')
        prompt = f"Given the following information of a paper, generate a one-sentence TLDR summary in {lang}:\n\n"
        if self.title:
            prompt += f"Title:\n {self.title}\n\n"

        if self.abstract:
            prompt += f"Abstract: {self.abstract}\n\n"

        if self.full_text:
            prompt += f"Preview of main content:\n {self.full_text}\n\n"

        if not self.full_text and not self.abstract:
            logger.warning(f"Neither full text nor abstract is provided for {self.url}")
            return "Failed to generate TLDR. Neither full text nor abstract is provided"
        
        prompt = _truncate_for_llm(prompt, 4000)
        
        response = openai_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"You are an assistant who perfectly summarizes scientific paper, and gives the core idea of the paper to the user. Your answer should be in {lang}.",
                },
                {"role": "user", "content": prompt},
            ],
            **llm_params.get('generation_kwargs', {})
        )
        tldr = response.choices[0].message.content
        return tldr
    
    def generate_tldr(self, openai_client:OpenAI,llm_params:dict) -> str:
        try:
            tldr = self._generate_tldr_with_llm(openai_client,llm_params)
            self.tldr = tldr
            return tldr
        except Exception as e:
            logger.warning(f"Failed to generate tldr of {self.url}: {e}")
            tldr = self.abstract
            self.tldr = tldr
            return tldr

    def _generate_affiliations_with_llm(self, openai_client:OpenAI,llm_params:dict) -> Optional[list[str]]:
        if self.full_text is not None:
            prompt = f"Given the beginning of a paper, extract the affiliations of the authors in a python list format, which is sorted by the author order. If there is no affiliation found, return an empty list '[]':\n\n{self.full_text}"
            prompt = _truncate_for_llm(prompt, 2000)
            affiliations = openai_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an assistant who perfectly extracts affiliations of authors from a paper. You should return a python list of affiliations sorted by the author order, like [\"TsingHua University\",\"Peking University\"]. If an affiliation is consisted of multi-level affiliations, like 'Department of Computer Science, TsingHua University', you should return the top-level affiliation 'TsingHua University' only. Do not contain duplicated affiliations. If there is no affiliation found, you should return an empty list [ ]. You should only return the final list of affiliations, and do not return any intermediate results.",
                    },
                    {"role": "user", "content": prompt},
                ],
                **llm_params.get('generation_kwargs', {})
            )
            affiliations = affiliations.choices[0].message.content

            affiliations = re.search(r'\[.*?\]', affiliations, flags=re.DOTALL).group(0)
            affiliations = json.loads(affiliations)
            affiliations = list(set(affiliations))
            affiliations = [str(a) for a in affiliations]

            return affiliations
    
    def generate_affiliations(self, openai_client:OpenAI,llm_params:dict) -> Optional[list[str]]:
        try:
            affiliations = self._generate_affiliations_with_llm(openai_client,llm_params)
            self.affiliations = affiliations
            return affiliations
        except Exception as e:
            logger.warning(f"Failed to generate affiliations of {self.url}: {e}")
            self.affiliations = None
            return None

    def _generate_detailed_reading_with_llm(self, openai_client:OpenAI, llm_params:dict) -> dict[str, str]:
        prompt = [
            "你是科学文献解读助手，目标是给研究者输出可直接用于日报的中文深度解读。",
            "请基于论文信息，按 JSON 形式返回以下五个字段（中文字符串）：",
            "motivation, method, result, conclusion, key_details。",
            "要求：",
            "1) 每个字段为完整短段落（1-4 句）；",
            "2) method 要给出完整技术方案（数据/输入、建模、关键模块、训练/推理流程或关键操作步骤）；",
            "3) result 要给出核心发现、指标或可复现的对比结论；",
            "4) key_details 要给出方法论与实现细节上的关键点（数据、先验、损失、超参、复杂度/约束、局限性）；",
            "5) 不要输出代码块、列表语法、额外解释，只输出 JSON。",
            "返回示例：{\"motivation\":\"...\",\"method\":\"...\",\"result\":\"...\",\"conclusion\":\"...\",\"key_details\":\"...\"}",
            "",
        ]
        if self.title:
            prompt.append(f"Title: {self.title}")
        if self.abstract:
            prompt.append(f"Abstract: {self.abstract}")
        if self.full_text:
            prompt.append("Full text preview:")
            prompt.append(self.full_text)
        prompt.append("以上为输入材料，不要进行臆测。")
        prompt_text = "\n".join(prompt)
        prompt_text = _truncate_for_llm(prompt_text, 6000)
        response = openai_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "你是一个严谨的论文解读助手，输出必须是有效 JSON，不得添加任何额外文本。",
                },
                {"role": "user", "content": prompt_text},
            ],
            **llm_params.get('generation_kwargs', {})
        )
        raw = response.choices[0].message.content or ""
        if not isinstance(raw, str):
            raw = str(raw)
        payload = _extract_json_block(raw)
        if not payload:
            raise ValueError("LLM response does not contain JSON format detailed reading")
        return _ensure_sections(payload)

    def generate_detailed_reading(self, openai_client:OpenAI, llm_params:dict) -> dict[str, str]:
        try:
            sections = self._generate_detailed_reading_with_llm(openai_client, llm_params)
            self.detailed_reading = sections
            return sections
        except Exception as e:
            logger.warning(f"Failed to generate detailed reading of {self.url}: {e}")
            sections = _ensure_sections({})
            self.detailed_reading = sections
            return sections
@dataclass
class CorpusPaper:
    title: str
    abstract: str
    added_date: datetime
    paths: list[str]
