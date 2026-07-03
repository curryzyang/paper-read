import json
from pathlib import Path

from omegaconf import open_dict

from tests.canned_responses import make_sample_paper, make_stub_openai_client
from zotero_arxiv_daily.web_publish import publish_daily_report


def _configure_web(config, tmp_path):
    with open_dict(config):
        config.web.output_dir = str(tmp_path / "docs")
        config.web.archive_dir = str(tmp_path / "archive")
        config.web.daily_total = 25
        config.web.deep_count = 10
        config.web.quick_count = 15
        config.web.language = "Chinese"


def test_publish_daily_report_splits_deep_and_quick(config, tmp_path, monkeypatch):
    monkeypatch.setenv("DPR_RUN_DATE", "20260703")
    _configure_web(config, tmp_path)
    papers = [
        make_sample_paper(
            title=f"Paper {i:02d}",
            url=f"https://arxiv.org/abs/2607.{i:05d}v1",
            pdf_url=f"https://arxiv.org/pdf/2607.{i:05d}v1",
            score=30 - i,
            tldr=f"TLDR {i}",
        )
        for i in range(30)
    ]

    result = publish_daily_report(papers, config, make_stub_openai_client())

    assert result["count"] == 25
    payload = json.loads(Path(result["recommend_path"]).read_text(encoding="utf-8"))
    assert len(payload["deep_dive"]) == 10
    assert len(payload["quick_skim"]) == 15
    assert payload["deep_dive"][0]["title"] == "Paper 00"
    assert payload["quick_skim"][0]["title"] == "Paper 10"
    assert (tmp_path / "docs" / "2026" / "07" / "03" / "README.md").exists()
    assert (tmp_path / "docs" / "_sidebar.md").exists()


def test_publish_daily_report_generates_empty_day(config, tmp_path, monkeypatch):
    monkeypatch.setenv("DPR_RUN_DATE", "2026-07-03")
    _configure_web(config, tmp_path)

    result = publish_daily_report([], config, make_stub_openai_client())

    payload = json.loads(Path(result["recommend_path"]).read_text(encoding="utf-8"))
    assert result["count"] == 0
    assert payload["deep_dive"] == []
    assert payload["quick_skim"] == []
    readme = (tmp_path / "docs" / "2026" / "07" / "03" / "README.md").read_text(encoding="utf-8")
    assert "今日没有检索到新的候选论文" in readme
