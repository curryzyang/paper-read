# DShuttleNet: A Badminton Doubles Dataset for Evaluating Team Coordination

- 区域：速读区
- 排名：13
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Guan-Yi Jhang, Chiencheng Chiang, Wei-Kai Chen, Hui-Ching Yu, Hsu-Chao Lai, Hwai-Jung Hsu, Wang Chih-Chuan, Jhy-Cheng Huang, Jiun-Long Huang
- 机构：National Yang Ming Chiao Tung University, Feng Chia University, Chang Gung University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14016v1) · [PDF](https://arxiv.org/pdf/2610.14016v1)

## TLDR
DShuttleNet is a new stroke-level badminton doubles dataset from elite BWF tournaments that provides synchronized four-player positions, expert-labeled loss reasons, and coordination-centric features and metrics to evaluate team coordination, showing that models ignoring teammate interactions underfit.

## Abstract
Most existing sports datasets are individual-centric or ball-centric, focusing on individual player actions while ignoring interactions among teammates. In badminton doubles, tactical success is governed by rapid team formation and coordination, yet standard resources for modeling these player interactions are scarce. To bridge this gap, we present DShuttleNet, a comprehensive dataset for badminton doubles curated from elite BWF World Tour tournaments. Beyond trajectory data, DShuttleNet uniquely incorporates expert-labeled "Loss Reasons," transforming the dataset into a diagnostic tool for causal tactical evaluation. We formally define two geometry-driven representations, Teammate-Relative Angle (TRA) and Vertical Shot Angle (VSA), to characterize coordination and shot aggressiveness. To quantify interpersonal synergy, we introduce novel metrics, Court Coverage Efficacy Index (CCEI) and Threat Load Asymmetry Index (TLAI), which evaluate the often-overlooked non-hitting partner's role and defensive coordination. Experimental results demonstrate that conventional models suffer from underfitting when failing to incorporate these coordination-centric features, highlighting the critical importance and potential impact of releasing DShuttleNet. Dataset is available at: https://doi.org/10.34740/kaggle/dsv/16097938.
