# Efficient Context-Limited Telescope Bibliography Classification for the WASP-2025 Shared Task Using SciBERT

- 区域：速读区
- 排名：15
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Madhusudhana Naidu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01647v1) · [PDF](https://arxiv.org/pdf/2609.01647v1)

## TLDR
TLDR: This paper presents a lightweight SciBERT-based model that, despite truncating text to 512 tokens, achieves top leaderboard performance (macro F1 0.89) in the WASP-2025 telescope bibliography classification task, demonstrating that domain-specific pretraining can outperform large general models under strict computational and context limits.

## Abstract
The creation of telescope bibliographies is a crucial part of assessing the scientific impact of observatories and ensuring reproducibility in astronomy. This task involves identifying, categorizing, and linking scientific publications that reference or use specific telescopes. However, this process remains largely manual and resource intensive. In this work, we present an efficient SciBERT-based approach for automatic classification of scientific papers into four categories - science, instrumentation, mention, and not telescope. Despite strict context-length constraints (maximum 512 tokens) and limited compute resources, our approach achieved a macro F1 score of 0.89, ranking at the top of the WASP-2025 leaderboard. We analyze the effect of truncation and show that even with half the samples exceeding the token limit, SciBERT's domain alignment enables robust classification. We discuss trade-offs between truncation, chunking, and long-context models, providing insights into the efficiency frontier for scientific text curation.
