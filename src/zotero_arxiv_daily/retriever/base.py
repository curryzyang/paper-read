from abc import ABC, abstractmethod
from omegaconf import DictConfig, ListConfig
from ..protocol import Paper, RawPaperItem
from tqdm import tqdm
from typing import Type
from time import sleep
from loguru import logger


class BaseRetriever(ABC):
    name: str

    @staticmethod
    def _normalize_categories(category_cfg) -> list[str]:
        if category_cfg is None:
            raise ValueError("category must be specified for retriever.")

        if isinstance(category_cfg, str):
            categories = [item.strip() for item in category_cfg.split(",") if item.strip()]
        elif isinstance(category_cfg, (list, ListConfig)):
            categories = [str(item).strip() for item in category_cfg if str(item).strip()]
        else:
            raise TypeError("category must be a string or a list of strings.")

        if not categories:
            raise ValueError("category must contain at least one value.")
        return categories

    @staticmethod
    def _get_debug_limit(config: DictConfig) -> int | None:
        if not config.executor.debug:
            return None
        return int(config.get("web", {}).get("daily_total", config.executor.max_paper_num))

    def __init__(self, config:DictConfig):
        self.config = config
        self.retriever_config = getattr(config.source,self.name)
        if "category" in self.retriever_config:
            self.categories = self._normalize_categories(self.retriever_config.get("category"))
        else:
            self.categories = None

    @abstractmethod
    def _retrieve_raw_papers(self) -> list[RawPaperItem]:
        pass

    @abstractmethod
    def convert_to_paper(self, raw_paper:RawPaperItem) -> Paper | None:
        pass

    def retrieve_papers(self) -> list[Paper]:
        raw_papers = self._retrieve_raw_papers()
        logger.info("Processing papers...")
        papers = []
        for raw_paper in tqdm(raw_papers, total=len(raw_papers), desc="Converting papers"):
            try:
                paper = self.convert_to_paper(raw_paper)
            except Exception as exc:
                logger.warning(f"Skipping paper {getattr(raw_paper, 'title', raw_paper)}: {exc}")
                continue
            if paper is not None:
                papers.append(paper)
            sleep(1)
        return papers

registered_retrievers = {}

def register_retriever(name:str):
    def decorator(cls):
        registered_retrievers[name] = cls
        cls.name = name
        return cls
    return decorator

def get_retriever_cls(name:str) -> Type[BaseRetriever]:
    if name not in registered_retrievers:
        raise ValueError(f"Retriever {name} not found")
    return registered_retrievers[name]
