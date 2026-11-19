# Stability Does Not Mirror Plasticity: A Module-Level View of Declarative and Procedural Learning in Transformers

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Jinjun Peng, Wailiang Zhao, Baishakhi Ray, Zhou Yu, Jufeng Yang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23427v1) · [PDF](https://arxiv.org/pdf/2611.23427v1)

## TLDR
This paper shows at the transformer-module level that plasticity and stability are governed by different aspects of a module’s functional role—QK/VO projections are most plastic for procedural tasks and MLPs for declarative memorization, yet stability depends on broader functional dependencies rather than simply mirroring plasticity.

## Abstract
Plasticity and stability in continual learning are typically studied at the entire-model level and in a task-agnostic manner, yet prior work has reported divergent conclusions across settings. Inspired by cognitive distinctions between declarative and procedural memory, we instead study how plasticity and stability vary across transformer modules and task types. In a controlled synthetic environment with clean measurement, we show a double dissociation: query-key (QK) and value-output (VO) projections are the most plastic on procedural tasks, whereas MLPs are the most plastic on declarative memorization. Stability, however, does not simply mirror plasticity: when learning a new procedure, updating QK retains over half of the stored declarative memory, while updating MLPs retains far less and updating VO loses roughly four-fifths. Targeted module reset-and-recovery experiments explain this asymmetry: plasticity tracks which module is best suited to a task's primary computation or storage, whereas stability depends on all ways the existing capability relies on that module, including access to information stored in other modules. Experiments on a realistic model and tasks broadly echo these asymmetric dynamics. Overall, our work shows that plasticity and stability depend on different aspects of a module's functional role, offering a task-dependent, module-level perspective on continual learning.
