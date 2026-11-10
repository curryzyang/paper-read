# UniLatent: Cross-Embodiment Transfer via Latent Observation Alignment

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yufei Ding, Yi Du, Weiduo Yuan, Hao Jiang, Dylan Goetting, Lawrence Yunliang Chen, Daniel Seita, Yue Wang
- 机构：University of Southern California, UC Berkeley, Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10061v1) · [PDF](https://arxiv.org/pdf/2611.10061v1)

## TLDR
UniLatent enables cross-embodiment robot transfer by rendering paired source–target observations at matched end-effector poses in simulation and aligning a source visual encoder to a frozen target encoder in a shared latent space, allowing policies trained on source demonstrations to deploy directly on target robot observations without pixel-level image translation.

## Abstract
Robot datasets are costly to collect and are usually tied to a specific embodiment, making it difficult to reuse demonstrations across robots with different geometry, appearance, and kinematics. We introduce UniLatent, a cross-embodiment transfer framework that reduces the embodiment-induced observation gap in a shared latent space. UniLatent renders paired source-target robot observations in simulation and aligns a source visual encoder to a frozen target encoder. A policy trained on encoded source demonstrations can then run directly on target observations, with no pixel-level image translation. Across three simulation tasks and two target robot arms, UniLatent reaches up to 93% zero-shot success, exceeding the strongest pixel-translation baseline by over 30 points on average. In real-world xArm-to-Franka transfer, fine-tuning with only 10 target demonstrations per task yields 27/30 successful rollouts. Code, videos and data are available at https://selina2023.github.io/unilatent/.
