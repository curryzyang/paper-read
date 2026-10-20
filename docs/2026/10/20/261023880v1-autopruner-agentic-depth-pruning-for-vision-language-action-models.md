# AutoPruner: Agentic Depth Pruning for Vision-Language-Action Models

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Tao Lin, Yikeng Chen, Qiwei Liang, Zinan Xie, Zhengtu Liang, Renjing Xu
- 机构：HKUST (GZ), Shenzhen University, Beijing Jiaotong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23880v1) · [PDF](https://arxiv.org/pdf/2610.23880v1)

## TLDR
AutoPruner is an LLM-agent-driven framework that jointly searches layer-deletion sets and recovery recipes for vision-language-action models via closed-loop task feedback, enabling substantial depth pruning while maintaining over 90% task success and up to 2.50× inference speedups.

## Abstract
Layer pruning reduces the size and inference cost of vision-language-action (VLA) models, but selecting a deployable configuration requires deciding both which layers to remove and how to recover task performance. These decisions depend on the model and task, and a failed trial can reflect either the deletion set or insufficient recovery. We present AutoPruner, an agent-driven framework that jointly searches pruning structures and recovery recipes through closed-loop experimentation. Offline layer interventions measure changes in action output to provide functional evidence. An LLM agent combines this evidence with evaluation history and retained diagnoses to propose deletion sets and recovery recipes within a search budget. Each proposal is executed and evaluated on the target tasks, and the resulting feedback guides the next experiment. Across OpenVLA-OFT, StarVLA, and FastWAM on four LIBERO suites, AutoPruner removes 16.7--87.5% of backbone layers while maintaining task success above 90%, with measured inference speedups of up to 2.50$\times$. Further analysis shows that functional probes identify action-sensitive layers despite high representation similarity, and that recovery can make previously failing structures viable.
