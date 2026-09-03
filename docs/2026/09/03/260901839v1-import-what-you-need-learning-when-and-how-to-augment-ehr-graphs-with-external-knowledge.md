# Import What You Need: Learning When and How to Augment EHR Graphs with External Knowledge

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Chen Chen, Mohsen Nayebi Kerdabadi, Dongjie Wang, Mei Liu, Zijun Yao
- 机构：University of Florida, University of Kansas
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01839v1) · [PDF](https://arxiv.org/pdf/2609.01839v1)

## TLDR
ReTA is a reinforcement learning-based framework that dynamically decides, per patient visit and under a budget, whether and how to import external knowledge-graph information into EHR visit graphs—via Soft Import, Hard Import, or Skip—improving prediction accuracy and efficiency across MIMIC-III/IV tasks.

## Abstract
Longitudinal prediction from electronic health records (EHRs) is limited by the sparsity and irregularity in patient trajectories, and knowledge augmentation with external knowledge graphs (KGs) offers a promising way to alleviate these issues. However, most existing methods perform fixed, context-agnostic topology augmentation by adding the same KG nodes and edges regardless of a patient's evolving state. We propose ReTA, a Reinforcement learning-based dynamic Topology Augmentation framework that casts KG import as a per-visit, budget-aware policy. ReTA first constructs an offline refined pool of KG-grounded templates, then learns a policy to select one augment action per visit from three options: Soft Import, which enriches node features without modifying graph topology, Hard Import, which grafts a compact KG subgraph onto the visit graph to create message-passing shortcuts, and Skip, which leaves the visit unaugmented when the base encoder is already confident. To stabilize learning, ReTA employs a decoupled encoder that processes semantic and structural signals in separate channels and fuses them via adaptive gating. Experiments on MIMIC-III and MIMIC-IV across diagnosis prediction, mortality, and readmission show that ReTA consistently outperforms strong baselines while remaining efficient, transfers across datasets and knowledge graphs, and yields interpretable augmentation patterns. The robust gains under sparse supervision highlight the advantage of ReTA's dynamic decision to import knowledge, boosting accuracy while curbing costs.
