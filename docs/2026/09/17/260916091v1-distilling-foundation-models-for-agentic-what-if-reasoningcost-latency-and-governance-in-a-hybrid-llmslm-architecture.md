# Distilling Foundation Models for Agentic What-If Reasoning:Cost, Latency, and Governance in a Hybrid LLM+SLM Architecture

- 区域：速读区
- 排名：6
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Sourish Dey, Aditya Kumar
- 机构：SumUp, Johannes Gutenberg-Universität Mainz
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16091v1) · [PDF](https://arxiv.org/pdf/2609.16091v1)

## TLDR
The paper distills TabPFN tabular foundation models into tiny feed-forward students and deploys them in a hybrid cloud-LLM/on-prem SLM agentic workflow, achieving up to 6,532× parameter compression and 3.8–4.8× lower latency while retaining 95.4–100.5% accuracy, cutting cloud token cost, and improving data governance for interactive what-if decision reasoning.

## Abstract
Tabular foundation models deliver strong zero-training predictive performance via in-context learning, but their high inference latency makes them impractical as hot-path decision backends in interactive agentic loops. We distill a TabPFN teacher into a compact feed-forward student across a business-decision simulation on UCI Adult and five OpenML benchmarks: the classification head compresses 53.2M parameters to 8,546 (6,220x); the deployed two-head loan pipeline compresses 111.4M parameters to 17,059 (6,532x). The student retains 95.4-100.5% accuracy and 96.8-100.0% AUC, with the lowest accuracy retention on credit-g at 95.4%; an alpha = 0 hard-label control shows that the teacher's soft targets provide a 2.1-7.0 AUC point gain.
