"""Tests for ArxivRetriever."""

import time
from types import SimpleNamespace

import feedparser

from zotero_arxiv_daily.retriever.arxiv_retriever import ArxivRetriever, _run_with_hard_timeout
import zotero_arxiv_daily.retriever.arxiv_retriever as arxiv_retriever


def _sleep_and_return(value: str, delay_seconds: float) -> str:
    time.sleep(delay_seconds)
    return value


def _raise_runtime_error() -> None:
    raise RuntimeError("boom")


def test_arxiv_retriever(config, mock_feedparser, monkeypatch):
    monkeypatch.setattr("zotero_arxiv_daily.retriever.base.sleep", lambda _: None)

    # The RSS fixture gives us paper IDs.  After feedparser, the code calls
    # arxiv.Client().results(search) which makes real HTTP requests.  We mock
    # the arxiv Client so the test stays offline.
    new_entries = [
        e for e in mock_feedparser.entries
        if e.get("arxiv_announce_type", "new") == "new"
    ]
    paper_ids = [e.id.removeprefix("oai:arXiv.org:") for e in new_entries]

    # Build fake ArxivResult-like objects matching each RSS entry
    fake_results = []
    for entry in new_entries:
        pid = entry.id.removeprefix("oai:arXiv.org:")
        fake_results.append(SimpleNamespace(
            title=entry.title,
            authors=[SimpleNamespace(name="Test Author")],
            summary="Test abstract",
            pdf_url=f"https://arxiv.org/pdf/{pid}",
            entry_id=f"https://arxiv.org/abs/{pid}",
            source_url=lambda pid=pid: f"https://arxiv.org/e-print/{pid}",
        ))

    class FakeClient:
        def __init__(self, **kw):
            pass
        def results(self, search):
            return iter(fake_results)

    monkeypatch.setattr(arxiv_retriever.arxiv, "Client", FakeClient)

    # Skip file downloads in convert_to_paper
    monkeypatch.setattr(arxiv_retriever, "extract_text_from_html", lambda paper: None)
    monkeypatch.setattr(arxiv_retriever, "extract_text_from_pdf", lambda paper: None)
    monkeypatch.setattr(arxiv_retriever, "extract_text_from_tar", lambda paper: None)

    retriever = ArxivRetriever(config)
    papers = retriever.retrieve_papers()

    assert len(papers) == len(new_entries)
    assert set(p.title for p in papers) == set(e.title for e in new_entries)


def test_arxiv_category_string_is_supported_and_debug_uses_daily_total(config, monkeypatch):
    def _entry(idx: int) -> SimpleNamespace:
        return SimpleNamespace(
            id=f"oai:arXiv.org:2607.{idx:05d}v1",
            title=f"Paper {idx}",
            get=lambda key, default=None, idx=idx: {
                "arxiv_announce_type": "new",
            }.get(key, default),
        )

    mock_entries = [_entry(i) for i in range(30)]
    mock_feed = SimpleNamespace(entries=mock_entries, feed=SimpleNamespace(title="arxiv feed"))
    parsed_urls: list[str] = []

    def _patched_parse(url):
        parsed_urls.append(url)
        return mock_feed

    monkeypatch.setattr("zotero_arxiv_daily.retriever.arxiv_retriever.feedparser.parse", _patched_parse)
    monkeypatch.setattr("zotero_arxiv_daily.retriever.base.sleep", lambda _: None)

    fake_results = [
        SimpleNamespace(
            title=e.title,
            authors=[SimpleNamespace(name="A")],
            summary="test",
            pdf_url=f"https://arxiv.org/pdf/{e.id.removeprefix('oai:arXiv.org:')}",
            entry_id=f"https://arxiv.org/abs/{e.id.removeprefix('oai:arXiv.org:')}",
            source_url=lambda pid=e.id.removeprefix("oai:arXiv.org:"): f"https://arxiv.org/e-print/{pid}",
        )
        for e in mock_entries
    ]

    class FakeClient:
        def __init__(self, **kw):
            pass

        def results(self, search):
            paper_ids = set(search.id_list)
            return (r for r in fake_results if r.entry_id.removeprefix("https://arxiv.org/abs/") in paper_ids)

    monkeypatch.setattr("zotero_arxiv_daily.retriever.arxiv_retriever.arxiv.Client", FakeClient)

    monkeypatch.setattr("zotero_arxiv_daily.retriever.arxiv_retriever.extract_text_from_html", lambda paper: None)
    monkeypatch.setattr("zotero_arxiv_daily.retriever.arxiv_retriever.extract_text_from_pdf", lambda paper: None)
    monkeypatch.setattr("zotero_arxiv_daily.retriever.arxiv_retriever.extract_text_from_tar", lambda paper: None)

    from omegaconf import open_dict

    with open_dict(config):
        config.source.arxiv.category = "eess.SY"
        config.executor.debug = True
        config.web.daily_total = 25

    retriever = ArxivRetriever(config)
    papers = retriever.retrieve_papers()

    assert parsed_urls
    assert "https://rss.arxiv.org/atom/eess.SY" in parsed_urls[0]
    assert len(papers) == 25


def test_run_with_hard_timeout_returns_value():
    result = _run_with_hard_timeout(
        _sleep_and_return, ("done", 0.01), timeout=1, operation="test op", paper_title="paper"
    )
    assert result == "done"


def test_run_with_hard_timeout_returns_none_on_timeout(monkeypatch):
    warnings: list[str] = []
    monkeypatch.setattr(arxiv_retriever, "logger", SimpleNamespace(warning=warnings.append))
    result = _run_with_hard_timeout(
        _sleep_and_return, ("done", 1.0), timeout=0.01, operation="test op", paper_title="paper"
    )
    assert result is None
    assert "timed out" in warnings[0]


def test_run_with_hard_timeout_returns_none_on_failure(monkeypatch):
    warnings: list[str] = []
    monkeypatch.setattr(arxiv_retriever, "logger", SimpleNamespace(warning=warnings.append))
    result = _run_with_hard_timeout(
        _raise_runtime_error, (), timeout=1, operation="test op", paper_title="paper"
    )
    assert result is None
    assert "boom" in warnings[0]
