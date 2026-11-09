# What Are LLM Agents Actually Learning on Low-Budget Molecular Optimization Benchmarks?

- 区域：速读区
- 排名：13
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Jiayu Qin, Zhengquan Luo, Changyou Chen, Zhiqiang Xu
- 机构：Mohamed bin Zayed University of Artificial Intelligence, University at Buffalo
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08522v1) · [PDF](https://arxiv.org/pdf/2611.08522v1)

## TLDR
The paper shows that reported LLM-agent gains on low-budget molecular-optimization benchmarks are largely explained by retrievable task/reference information and permissive oracle landscapes rather than genuine online optimization, and it recommends retrieval-safe prompts and random-walk baselines as inexpensive sanity checks.

## Abstract
Recent work reports large gains for LLM agents on low-budget molecular optimization. We measure the contributions of online optimization, retrievable task information, and permissive oracle landscapes. On PMO at 50 oracle calls, a GPT-4o mini agent's sum AUC falls from 14.44 to 4.85 after task names and curated reference compounds are hidden. An identity-blinded condition that states only the oracle form (e.g., similarity to a hidden reference) scores 5.39, while a deterministic retrieval-only baseline with no LLM reaches 12.16 (84% of the full agent). A full 23-task 2x2 ablation and a three-seed replication on eight tasks support this interpretation. On a protein-targeted benchmark with an AutoDock Vina composite oracle, a single-edit random walk is a strong lower bound; across three seeds it obtains composite 0.636 +/- 0.008 and docking improvement -1.11 +/- 0.04 kcal/mol. As a positive control, a retrieval-free population agent exceeds REINVENT at a matched 50-call AUC budget, with its strongest result at 100 calls. These results motivate two inexpensive sanity checks: retrieval-safe PMO prompts and a random-walk floor for docking-based optimization.
