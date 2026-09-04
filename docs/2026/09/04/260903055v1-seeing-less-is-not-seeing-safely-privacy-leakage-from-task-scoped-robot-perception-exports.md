# Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports

- 区域：速读区
- 排名：6
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Yuqiao Xu, Erman Ayday
- 机构：Case Western Reserve University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03055v1) · [PDF](https://arxiv.org/pdf/2609.03055v1)

## TLDR
Task-equivalent robot perception representations can leak very different amounts of private household information even when raw sensor data stay local, so privacy must be evaluated through task-specific, multi-risk profiling rather than assuming that removing fields or increasing abstraction guarantees safety.

## Abstract
Domestic robots rely on rich perception to operate in private homes, but privacy risk persists even when raw sensor data remain local. Structured representations exported to downstream planners, cloud services, logs, or learning pipelines can still reveal household information through semantics, geometry, spatial structure, and task targets. We introduce Task-Functional Perception Distillation (TFPD), a task-scoped representation-export framework that keeps rich perception local and profiles downstream exports according to task utility, direct exposure, and multiple residual inference risks. Using 120 AI2-THOR scenes with scene-disjoint train/validation/test splits, frozen attacker selection, and representation-aware held-out attacks, we evaluate navigation, collision checking, and object-goal execution. Three navigation exports achieve identical success (1.000) and mean path ratio (0.898), yet representation-level linkability ranges from 0.532 to 0.970. Replacing an explicit target label with a target region reduces target-category macro-F1 from 1.000 to 0.077 while preserving success at 0.995, while geometric coarsening reduces object-category macro-F1 from 0.704 to 0.556 at a measurable collision-utility cost. A ProcTHOR replication preserves the navigation task-equivalence/privacy-inequivalence finding while changing the relative ordering of normalized and topological exports. These results show that neither field removal nor stronger abstraction induces a universal privacy ordering and motivate task-specific, multi-risk evaluation of the complete public representation.
