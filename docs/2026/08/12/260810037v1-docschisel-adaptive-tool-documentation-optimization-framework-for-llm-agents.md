# DOCSCHISEL: Adaptive Tool Documentation Optimization Framework for LLM Agents

- 区域：速读区
- 排名：13
- 匹配度：3.2/10
- 来源：arxiv
- 作者：You Lu, Kun Zhang, Bihuan Chen, Xin Peng
- 机构：Fudan University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10037v1) · [PDF](https://arxiv.org/pdf/2608.10037v1)

## TLDR
DocsChisel is an adaptive framework that optimizes tool documentation for LLM agents by analyzing failed execution traces and iteratively adding, removing, or refining information fields, improving task success rates by up to 95.89% over original documentation and 75.15% over existing baselines.

## Abstract
Large language models (LLMs) increasingly rely on external tools to accomplish complex real-world tasks, making tool documentation a critical grounding resource for LLM agents. Existing studies mainly focus on improving the tool-use capabilities of LLM agents, while largely treating tool documentation as a fixed input. Although several recent works attempt to optimize tool documentation through rewriting or compression, little is known about how the information contained in tool documentation affects agent performance across different settings.
  To bridge this gap, we conduct a large-scale empirical study on tool documentation for LLM agents. Our study reveals substantial heterogeneity in the information fields provided by existing tool documentation. Moreover, the effectiveness of different information fields is highly dependent on the task domain, LLM backbone, and agent paradigm, indicating that no fixed tool documentation can consistently generalize across diverse agent settings.
  Motivated by these findings, we propose DocsChisel, an adaptive tool documentation optimization framework for LLM agents. DocsChisel analyzes failed execution traces of a target LLM agent to identify documentation-related issues, and iteratively optimizes tool documentation by adding, removing, and refining information fields for each tool. We evaluate DocsChisel against two state-of-the-art baselines, i.e., EasyTool and DRAFT. Experimental results show that DocsChisel improves the task success rate of LLM agents by 95.89% over the original tool documentation and by 75.15%, on average, over existing baselines, while incurring limited optimization time and token overhead
