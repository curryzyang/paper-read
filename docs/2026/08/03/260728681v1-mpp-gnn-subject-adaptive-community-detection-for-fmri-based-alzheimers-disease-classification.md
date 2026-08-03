# MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based Alzheimer's Disease Classification

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Yang Zhang, Xiao Zhou, Jonathan Warrell, Avram Holmes, Xuan Zhang, Mark Gerstein
- 机构：Pratt Institute, Rutgers University, Yale University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28681v1) · [PDF](https://arxiv.org/pdf/2607.28681v1)

## TLDR
MPP-GNN introduces a bilevel-optimized, subject-adaptive graph neural network that hierarchically discovers individualized brain communities via affinity propagation and uses them as priors to refine connectivity, achieving state-of-the-art Alzheimer’s disease classification from fMRI while recovering canonical functional networks and revealing AD-related dedifferentiation.

## Abstract
Functional magnetic resonance imaging (fMRI) is a widely used technique for studying the brain. Recent methods that utilize graph neural networks (GNNs) for analysis of brain functional connectivity have shown great potential for the classification of brain disorders, such as Alzheimer's disease (AD). However, these methods often assume a preset number of functional modules across all subjects, which overlooks inter-subject variability. In addition, the discovered modules are rarely used to directly guide the learned connectivity patterns. Here, to address these issues, we propose a Meta Probabilistic Pooling GNN (MPP-GNN). We frame the model's task as a coupled, bilevel optimization that performs adaptive graph partitioning hierarchically to discover subject-specific modules and then uses the discovered brain modules as an explicit prior to guide edge refinement and representation learning. We validate MPP-GNN on two public datasets for AD classification, achieving the highest AUC in comparison to established baselines for both datasets. Furthermore, our analysis demonstrates that MPP-GNN shows significant alignment with the canonical functional-network organization defined by the Yeo brain atlas and reveals a network-level dedifferentiation pattern for AD.
