# CLEAN: Psychometrically Consistent Incremental Cognitive Diagnosis under Concept-Space Expansion via Architectural Isolation

- 区域：速读区
- 排名：2
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Tao He, Jinxing Xiang, Fan Jiang
- 机构：Guangdong Polytechnic Normal University, Shenzhen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02278v1) · [PDF](https://arxiv.org/pdf/2610.02278v1)

## TLDR
CLEAN is an incremental cognitive diagnosis framework that uses architectural isolation, frozen historical pathways, and orthogonal masking to support concept-space expansion with zero representation drift, preserving old-item diagnostic performance while remaining competitive on new items.

## Abstract
Cognitive diagnosis (CD) is a fundamental task in intelligent education that profiles learner proficiency over knowledge concepts. In real-world learning platforms, newly added items continually introduce previously unseen concepts, necessitating dynamic expansion of the underlying concept space. Yet existing incremental CD models assume a fixed concept space, allowing gradients from new items to overwrite historical pathways and induce catastrophic forgetting. More critically, these methods rely solely on soft constraints to preserve historical diagnoses. Such constraints may fail to satisfy the requirement of diagnostic invariance after incremental updates, a requirement known as psychometric consistency in cognitive diagnosis. Therefore, we propose CLEAN (Continual Learning with Expandable and Architecturally Isolated Networks), a novel incremental CD framework supporting concept-space expansion while providing structural guarantees for pointwise invariance of historical diagnoses. Specifically, CLEAN first introduces a strict topological bipartition protocol, freezes historical diagnostic functions and applies deterministic orthogonal column masking to sever gradient interference. Second, to accommodate concept expansion, expandable full-rank branches with micro-variance initialization are deployed to learn novel concepts. Finally, to verify that this architectural design achieves invariance by construction, we formalize Representation Drift (RD) to quantify the perturbation of historical traits. Extensive experiments on three large-scale educational datasets demonstrate that CLEAN achieves zero RD, preserving old-item metrics identically to static anchors through architectural isolation while remaining competitive with or superior to strong continual-learning baselines on new items.
