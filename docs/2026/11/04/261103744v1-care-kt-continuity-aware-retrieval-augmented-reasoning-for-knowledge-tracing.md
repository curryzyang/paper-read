# CaRe-KT: Continuity-Aware Retrieval-Augmented Reasoning for Knowledge Tracing

- 区域：速读区
- 排名：6
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Mehrnoush Mohammadi, Kamal Berahmand, Mohammad Morsali, Shazia Sadiq, Wojtek Tomaszewski, Hassan Khosravi
- 机构：Universitat Politècnica de Catalunya, RMIT University, The University of Queensland
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03744v1) · [PDF](https://arxiv.org/pdf/2611.03744v1)

## TLDR
CaRe-KT is a query-adaptive retrieval-augmented knowledge tracing framework that maintains relevance continuity between evidence retrieval and inference through an Evidence-Graph Cache and relevance-informed attention, improving predictive performance and robustness under sparse-history and cold-start conditions.

## Abstract
Knowledge tracing (KT) estimates learners' evolving knowledge states from interaction histories to support adaptive learning. Retrieval-augmented KT improves these estimates using cross-learner behavioral evidence, but existing approaches typically separate evidence retrieval from downstream prediction. This creates a retrieval-inference alignment gap because evidence relevance varies with the learner's evolving state and prediction context. We propose CaRe-KT, a query-adaptive framework that maintains relevance continuity between evidence acquisition and inference without equating retrieval relevance with predictive utility. CaRe-KT introduces an Evidence-Graph Cache (EGC) that combines persistent question-level relational compatibility with interaction-level temporal validity to construct query-specific evidence subgraphs. Historical learning trajectories retrieved through these subgraphs are encoded alongside the target learner's history in a shared representation space using outcome-supervised contrastive learning. An attention mechanism combines acquisition relevance with learned query-evidence compatibility, allowing relevance to inform, rather than determine, each trajectory's predictive influence. Experiments across five benchmarks show that CaRe-KT outperforms strong KT baselines and remains robust under sparse-history and cold-start conditions. These findings support relevance continuity as a design principle for retrieval-augmented knowledge tracing.
