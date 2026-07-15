# Daily Zotero arXiv Reader

This project is a personal daily paper recommender built from
[`zotero-arxiv-daily`](https://github.com/curryzyang/zotero-arxiv-daily) with
the email delivery path replaced by a lightweight
[`daily-paper-reader`](https://curryzyang.github.io/daily-paper-reader/#/)-style
GitHub Pages site.

## What It Does

- Reads your Zotero library and uses paper abstracts as your research profile.
- Retrieves fresh arXiv papers from configured categories.
- Reranks new papers by embedding similarity to your Zotero corpus.
- Generates TLDRs, affiliations, and a daily briefing with an OpenAI-compatible LLM.
- Publishes a static web report under `docs/`, with structured archives under `archive/`.

Each daily report contains 25 papers:

- top 10 by matching score: 精读区
- next 15 by matching score: 速读区

## Configure

Set repository secrets:

- `ZOTERO_ID`
- `ZOTERO_KEY`
- `OPENAI_API_KEY`
- `OPENAI_API_BASE`

Set repository variables:

- `INCLUDE_CROSS_LIST`（可选；设置为 `true` 以包含 arXiv cross-list 论文，默认为 `false`）
- `CUSTOM_CONFIG`（可选的 YAML 覆盖配置）

`CUSTOM_CONFIG` 的最小示例：

```yaml
source:
  arxiv:
    category: ["cs.AI", "cs.CV", "cs.LG", "cs.CL"]
    include_cross_list: false  # 也可由 Repository Variable INCLUDE_CROSS_LIST 控制

zotero:
  include_path: null
  ignore_path: null

llm:
  generation_kwargs:
    model: gpt-4o-mini

executor:
  source: ["arxiv"]
  reranker: local

reranker:
  # 默认只使用最相似的 20 篇 Zotero 文献计算分数；设为 null 可恢复全库平均。
  top_k: 20

web:
  daily_total: 25
  deep_count: 10
  quick_count: 15
  language: Chinese
  detailed_reading: true  # Generate structured Chinese detailed reading for deep-read section only.
```

`detailed_reading` 开关说明：
- `true`（默认）：精读区生成“研究动机/方法/结果/结论/关键细节”五段中文解读，速读区不生成。
- `false`：全部文章仅保留 TL;DR，不输出中文详细解读。

关闭开关示例（放在 `CUSTOM_CONFIG`）：

```yaml
web:
  detailed_reading: false
```

If you use `CUSTOM_CONFIG`, keep it as a partial override (not a full replacement).
At minimum, ensure `executor.source` exists:

```yaml
executor:
  source: ["arxiv"]   # or ["arxiv", "biorxiv", "medrxiv"]
```

## Run Locally

```bash
uv run src/zotero_arxiv_daily/main.py
```

Then serve the repository root or open it through any static server:

```bash
python -m http.server 8000
```

Visit `http://127.0.0.1:8000`.

一键预览（推荐）：

```bash
chmod +x scripts/preview.sh
./scripts/preview.sh         # 默认 8010 端口
./scripts/preview.sh 8011    # 指定端口
```

如果你希望只生成报告文件并快速确认（不打开浏览器），可设置：

```bash
PREVIEW_OPEN_BROWSER=0 ./scripts/preview.sh
```

## GitHub Pages

Enable Pages in repository settings and publish from the default branch root.
The scheduled workflow writes `docs/` and `archive/`, then commits the generated
daily report.
