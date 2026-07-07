from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from loguru import logger
from omegaconf import DictConfig, OmegaConf
from openai import OpenAI

from .protocol import Paper


def _get_config_value(config: DictConfig, dotted_key: str, default: Any) -> Any:
    value = OmegaConf.select(config, dotted_key)
    return default if value is None else value


def _run_date() -> datetime:
    raw = os.getenv("DPR_RUN_DATE") or os.getenv("DAILY_PAPER_DATE") or ""
    raw = raw.strip()
    for fmt in ("%Y%m%d", "%Y-%m-%d"):
        if raw:
            try:
                return datetime.strptime(raw, fmt)
            except ValueError:
                pass
    return datetime.now()


def _slugify(value: str, fallback: str = "paper") -> str:
    text = (value or "").strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\-]+", "", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or fallback


def _paper_identifier(paper: Paper) -> str:
    for value in (paper.url, paper.pdf_url):
        if not value:
            continue
        tail = value.rstrip("/").rsplit("/", 1)[-1]
        tail = tail.removesuffix(".pdf")
        if tail:
            return tail
    return _slugify(paper.title)


def _authors_text(authors: list[str]) -> str:
    return ", ".join(a for a in authors if a) or "Unknown authors"


def _affiliations_text(affiliations: list[str] | None) -> str:
    if not affiliations:
        return "Unknown affiliation"
    return ", ".join(str(a) for a in affiliations if a) or "Unknown affiliation"


def _score_text(score: float | None) -> str:
    if score is None:
        return "Unknown"
    return f"{float(score):.1f}"


def _markdown_escape(text: str | None) -> str:
    return (text or "").replace("\r\n", "\n").strip()


def _json_safe_paper(paper: Paper, section: str, paper_path: str, rank: int) -> dict[str, Any]:
    return {
        "id": _paper_identifier(paper),
        "rank": rank,
        "section": section,
        "paper_id": paper_path,
        "source": paper.source,
        "title": paper.title,
        "authors": paper.authors,
        "authors_text": _authors_text(paper.authors),
        "abstract": paper.abstract,
        "url": paper.url,
        "pdf_url": paper.pdf_url,
        "tldr": paper.tldr,
        "detailed_reading": paper.detailed_reading,
        "affiliations": paper.affiliations,
        "affiliations_text": _affiliations_text(paper.affiliations),
        "score": paper.score,
        "score_text": _score_text(paper.score),
    }


def _detailed_reading_block(reading: dict[str, str] | None) -> str:
    if not reading:
        return "## 精读解读（中文）\n\n暂无可展示的详细解读。"

    sections = [
        ("### 一、研究动机", "motivation", "暂无可提取到论文动机。"),
        ("### 二、技术方案（Method）", "method", "暂无可提取到方法细节。"),
        ("### 三、结果（Result）", "result", "暂无可提取到结果说明。"),
        ("### 四、结论（Conclusion）", "conclusion", "暂无可提取到结论。"),
        ("### 五、方法论与关键技术细节", "key_details", "暂无可提取到关键细节。"),
    ]

    lines = ["## 中文解读"]
    for title, key, fallback in sections:
        content = reading.get(key) or fallback
        lines.extend([title, _markdown_escape(content), ""])
    return "\n".join(lines)


def _paper_markdown(paper: Paper, section_label: str, rank: int, include_detailed_reading: bool = False) -> str:
    title = _markdown_escape(paper.title)
    authors = _authors_text(paper.authors)
    abstract = _markdown_escape(paper.abstract)
    tldr = _markdown_escape(paper.tldr) or abstract
    affiliations = _affiliations_text(paper.affiliations)
    pdf_url = paper.pdf_url or paper.url or ""
    source_url = paper.url or paper.pdf_url or ""
    links = []
    if source_url:
        links.append(f"[arXiv / Source]({source_url})")
    if pdf_url:
        links.append(f"[PDF]({pdf_url})")
    links_text = " · ".join(links) if links else "No link available"

    lines = [
        f"# {title}",
        "",
        f"- 区域：{section_label}",
        f"- 排名：{rank}",
        f"- 匹配度：{_score_text(paper.score)}/10",
        f"- 来源：{paper.source}",
        f"- 作者：{authors}",
        f"- 机构：{affiliations}",
        f"- 链接：{links_text}",
        "",
        "## TLDR",
        tldr,
        "",
        "## Abstract",
        abstract or "No abstract available.",
        "",
    ]
    if include_detailed_reading:
        lines.extend(["", _detailed_reading_block(paper.detailed_reading)])
    return "\n".join(lines)


def _fallback_daily_brief(
    papers: list[Paper],
    deep_papers: list[Paper],
    quick_papers: list[Paper],
    deep_target: int,
    quick_target: int,
) -> str:
    if not papers:
        return "今日没有检索到新的候选论文。"
    top_titles = "；".join(p.title for p in deep_papers[:3])
    shortage = []
    if len(deep_papers) < deep_target:
        shortage.append(f"精读只取到{len(deep_papers)}篇，目标{deep_target}篇")
    if len(quick_papers) < quick_target:
        shortage.append(f"速读只取到{len(quick_papers)}篇，目标{quick_target}篇")
    extra = " " + "；".join(shortage) if shortage else ""
    total = len(papers)
    if top_titles:
        return f"今日共推荐 {total} 篇论文，其中精读 {len(deep_papers)} 篇、速读 {len(quick_papers)} 篇。建议优先阅读：{top_titles}。{extra}"
    return f"今日共推荐 {total} 篇论文，主要进入速读区，可按匹配度从高到低快速浏览。{extra}"


def _generate_daily_brief(
    papers: list[Paper],
    deep_papers: list[Paper],
    quick_papers: list[Paper],
    openai_client: OpenAI,
    llm_config: DictConfig,
    language: str,
    deep_target: int,
    quick_target: int,
) -> str:
    if not papers:
        return _fallback_daily_brief(papers, deep_papers, quick_papers, deep_target, quick_target)

    payload = []
    for paper in papers:
        payload.append(
            {
                "title": paper.title,
                "score": paper.score,
                "authors": paper.authors,
                "tldr": paper.tldr,
                "abstract": paper.abstract[:1200] if paper.abstract else "",
            }
        )
    prompt = (
        f"请根据下面的每日论文推荐结果，用{language}写一段简洁的今日阅读简报。"
        "要求：说明总数、精读和速读数量、最值得优先看的主题或论文；不要逐篇罗列；长度控制在150字以内。\n\n"
        + json.dumps(payload, ensure_ascii=False)
    )
    try:
        response = openai_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You write concise daily research briefings for a scientist.",
                },
                {"role": "user", "content": prompt},
            ],
            **llm_config.get("generation_kwargs", {}),
        )
        content = response.choices[0].message.content
        if content:
            return content.strip()
    except Exception as exc:
        logger.warning(f"Failed to generate daily brief: {exc}")
        return _fallback_daily_brief(papers, deep_papers, quick_papers, deep_target, quick_target)


def _daily_readme(
    run_dt: datetime,
    brief: str,
    deep_records: list[dict[str, Any]],
    quick_records: list[dict[str, Any]],
    deep_target: int,
    quick_target: int,
) -> str:
    date_label = run_dt.strftime("%Y-%m-%d")

    def section(records: list[dict[str, Any]]) -> list[str]:
        if not records:
            return ["暂无。"]
        lines = []
        for idx, item in enumerate(records, start=1):
            title = item["title"]
            score = item["score_text"]
            paper_id = item["paper_id"]
            lines.append(f"{idx}. [{title}](/{paper_id}) （{score}/10）")
        return lines

    return "\n".join(
        [
            f"# 日报 · {date_label}",
            "",
            f"- 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"- 当次推荐总数：{len(deep_records) + len(quick_records)}",
            f"- 精读区：{len(deep_records)} / {deep_target}",
            f"- 速读区：{len(quick_records)} / {quick_target}",
            "",
            "## 今日简报",
            brief,
            "",
            "## 精读区",
            *section(deep_records),
            "",
            "## 速读区",
            *section(quick_records),
            "",
        ]
    )


def _discover_day_dirs(docs_dir: Path) -> list[tuple[str, str]]:
    days = []
    if not docs_dir.exists():
        return days
    for year_dir in docs_dir.iterdir():
        if not year_dir.is_dir() or not re.fullmatch(r"\d{4}", year_dir.name):
            continue
        for month_dir in year_dir.iterdir():
            if not month_dir.is_dir() or not re.fullmatch(r"\d{2}", month_dir.name):
                continue
            for day_dir in month_dir.iterdir():
                if day_dir.is_dir() and re.fullmatch(r"\d{2}", day_dir.name):
                    route = f"{year_dir.name}/{month_dir.name}/{day_dir.name}"
                    label = f"{year_dir.name}-{month_dir.name}-{day_dir.name}"
                    days.append((label, route))
    return sorted(days, reverse=True)


def _sidebar(docs_dir: Path, current_route: str, records: list[dict[str, Any]]) -> str:
    days = _discover_day_dirs(docs_dir)
    if not any(route == current_route for _, route in days):
        label = current_route.replace("/", "-")
        days.insert(0, (label, current_route))

    grouped: dict[str, list[dict[str, Any]]] = {}
    for _label, route in days:
        if route == current_route:
            grouped[route] = records
            continue
        meta_path = docs_dir / route / "papers.meta.json"
        if not meta_path.exists():
            grouped[route] = []
            continue
        try:
            payload = json.loads(meta_path.read_text(encoding="utf-8"))
            items = payload.get("papers") if isinstance(payload, dict) else []
            grouped[route] = [item for item in items if isinstance(item, dict)]
        except Exception as exc:
            logger.warning(f"Failed to read sidebar metadata from {meta_path}: {exc}")
            grouped[route] = []

    lines = ["- [首页](/README)", ""]
    for label, route in days:
        lines.append(f"- {label}")
        lines.append(f"  - [日报](/{route}/README)")
        for item in grouped.get(route, []):
            marker = "精读" if item["section"] == "deep" else "速读"
            lines.append(f"  - [{marker} · {item['title']}](/{item['paper_id']})")
    lines.append("")
    return "\n".join(lines)


def _home_readme(latest_route: str, run_dt: datetime, total: int) -> str:
    return "\n".join(
        [
            "# Daily Paper Reader",
            "",
            "这里是基于 Zotero 文献库画像生成的每日 arXiv 推荐页。",
            "",
            f"- 最新日报：[{run_dt.strftime('%Y-%m-%d')}](/{latest_route}/README)",
            f"- 最新推荐数量：{total}",
            "",
        ]
    )


def publish_daily_report(
    papers: list[Paper],
    config: DictConfig,
    openai_client: OpenAI,
) -> dict[str, Any]:
    output_dir = Path(_get_config_value(config, "web.output_dir", "docs"))
    archive_dir = Path(_get_config_value(config, "web.archive_dir", "archive"))
    deep_count = int(_get_config_value(config, "web.deep_count", 10))
    quick_count = int(_get_config_value(config, "web.quick_count", 15))
    language = str(_get_config_value(config, "web.language", "Chinese"))

    run_dt = _run_date()
    date_token = run_dt.strftime("%Y%m%d")
    route = run_dt.strftime("%Y/%m/%d")
    day_dir = output_dir / run_dt.strftime("%Y") / run_dt.strftime("%m") / run_dt.strftime("%d")
    recommend_dir = archive_dir / date_token / "recommend"

    output_dir.mkdir(parents=True, exist_ok=True)
    day_dir.mkdir(parents=True, exist_ok=True)
    recommend_dir.mkdir(parents=True, exist_ok=True)

    sorted_papers = sorted(
        papers,
        key=lambda p: float(p.score if p.score is not None else float("-inf")),
        reverse=True,
    )
    requested_deep_count = deep_count
    requested_quick_count = quick_count
    deep_papers = sorted_papers[:deep_count]
    quick_papers = sorted_papers[deep_count : deep_count + quick_count]

    records: list[dict[str, Any]] = []
    deep_records: list[dict[str, Any]] = []
    quick_records: list[dict[str, Any]] = []

    for section, section_label, section_papers in (
        ("deep", "精读区", deep_papers),
        ("quick", "速读区", quick_papers),
    ):
        for rank, paper in enumerate(section_papers, start=1):
            pid = _paper_identifier(paper)
            slug = f"{_slugify(pid)}-{_slugify(paper.title)}"
            paper_route = f"{route}/{slug}"
            record = _json_safe_paper(paper, section, paper_route, rank)
            records.append(record)
            if section == "deep":
                deep_records.append(record)
            else:
                quick_records.append(record)
            should_show_detailed = section == "deep" and bool(paper.detailed_reading)
            (day_dir / f"{slug}.md").write_text(
                _paper_markdown(paper, section_label, rank, include_detailed_reading=should_show_detailed),
                encoding="utf-8",
            )

    brief = _generate_daily_brief(
        sorted_papers,
        deep_papers,
        quick_papers,
        openai_client,
        config.llm,
        language,
        requested_deep_count,
        requested_quick_count,
    )
    readme = _daily_readme(
        run_dt,
        brief,
        deep_records,
        quick_records,
        requested_deep_count,
        requested_quick_count,
    )
    (day_dir / "README.md").write_text(readme, encoding="utf-8")

    meta = {
        "label": run_dt.strftime("%Y-%m-%d"),
        "date": run_dt.strftime("%Y-%m-%d"),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "count": len(records),
        "papers": records,
        "errors": [],
    }
    (day_dir / "papers.meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    payload = {
        "mode": "standard",
        "generated_at": datetime.now().isoformat(),
        "stats": {
            "deep_selected": len(deep_records),
            "quick_selected": len(quick_records),
            "daily_total": len(records),
            "deep_count": deep_count,
            "quick_count": quick_count,
        },
        "deep_dive": deep_records,
        "quick_skim": quick_records,
    }
    recommend_path = recommend_dir / f"arxiv_papers_{date_token}.standard.json"
    recommend_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    (output_dir / "_sidebar.md").write_text(_sidebar(output_dir, route, records), encoding="utf-8")
    (output_dir / "README.md").write_text(_home_readme(route, run_dt, len(records)), encoding="utf-8")

    logger.info(f"Published daily web report with {len(records)} papers to {day_dir}")
    return {
        "docs_dir": str(day_dir),
        "recommend_path": str(recommend_path),
        "count": len(records),
    }
