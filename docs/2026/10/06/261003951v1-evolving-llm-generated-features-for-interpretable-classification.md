# Evolving LLM-Generated Features for Interpretable Classification

- 区域：速读区
- 排名：12
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Jack Butler, Zainab Afolabi, Nikita Kozodoi
- 机构：Amazon Web Services
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03951v1) · [PDF](https://arxiv.org/pdf/2610.03951v1)

## TLDR
This paper proposes an evolutionary framework that iteratively refines LLM-generated natural-language binary features (rubrics) to train transparent classifiers, improving performance over single-shot LLM rubrics and zero-shot LLM classification while providing auditable decision logic and exposing hidden per-class biases.

## Abstract
Large language models (LLMs) are increasingly used as classifiers, yet they operate as opaque systems whose decisions are difficult to interpret, which complicates their use in regulated domains such as credit scoring or medical diagnosis. We propose an evolutionary framework that iteratively discovers natural language feature definitions (rubrics) for interpretable classification. An LLM generates candidate binary features, evaluates each sample against them, and the resulting vectors can be used to train a transparent classifier such as logistic regression. The feature set evolves over multiple iterations guided by classification errors, per-class activation rates, and feature ablation scores. We evaluate across three benchmarks, including a credit risk dataset representative of regulated domains, comparing single-shot LLM rubrics, evolved rubrics, and direct zero-shot LLM classification. Evolved features improve over single-shot rubrics by +2.9 pp on average and outperform zero-shot LLM classification on two of three tasks, while providing fully auditable decision logic. On the credit risk task, the zero-shot LLM performs at chance (50.7%) with a strong bias toward a single class, whereas evolved features achieve balanced, interpretable predictions. Crucially, this failure is invisible in aggregate accuracy and surfaces only under per-class auditing. Analysis reveals that evolution is most effective when label boundaries cannot be inferred from category names alone or when the LLM lacks reliable domain-specific reasoning.
