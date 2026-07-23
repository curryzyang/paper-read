# Memory Merge DQN: Sensitivity Weighted Target Updates for Stable Value Learning

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Adrian Ly, Richard Dazeley, Peter Vamplew, Sunil Aryal, Francisco Cruz
- 机构：Deakin University, UNSW, Federation University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19397v1) · [PDF](https://arxiv.org/pdf/2607.19397v1)

## TLDR
Memory Merge DQN replaces the standard hard target copy in Deep Q-Networks with a Q-value sensitivity weighted merging of recent online network copies, preserving useful value function structure and improving stability and final performance across Atari games.

## Abstract
Deep Q-networks use target networks to stabilise bootstrapped value learning, but the standard hard copy update also introduces a tradeoff. Holding the target network fixed, improves short term stability, yet each hard update abruptly replaces the target parameters with the newest online network and discards recent parameter history. This can produce sudden changes in the bootstrap target and may remove value function structure that remains useful later in training. This paper introduces Memory Merge DQN, a target network update mechanism that maintains a short memory of recent historical online network copies and constructs the target network by merging network parameters based on the Q-value sensitivity rather than copying only the newest online network. Memory Merge gives greater influence to parameters that remain locally important for current Q-value behaviour, while using a recency prior to keep the merged target close to the latest online parameters. The method is inspired by Fisher Weight Model Merging, but uses Q-value sensitivity rather than Fisher information as the weighting signal. This paper evaluates Memory Merge DQN on Atari environments against DQN, Averaged DQN, DQN with layer normalisation, and PQN (with gradient clipping). The results show that Memory Merge DQN is highly competitive and it achieves the largest number of first place final performance results among the evaluated methods, beats DQN, Averaged DQN, and PQN (with gradient clipping), and produces substantial gains in several games where preserving useful value-function parameters appears beneficial. These findings suggest that selectively merging recent parameter weights and history can improve the stability and final performance of DQN agents, and that target network design is an important mechanism for preserving useful value function structure during long horizon value learning.


## 精读解读（中文）
### 一、研究动机
标准深度Q网络（DQN）使用目标网络稳定自举值学习，但硬拷贝更新在提供短期稳定性的同时，每次更新会突然替换目标参数并丢弃近期参数历史，可能导致引导目标突变并移除仍有用处价值函数结构。本文旨在通过保留历史在线网络参数并根据Q值敏感性有选择地合并，来改善稳定性和最终性能。

### 二、技术方案（Method）
Memory Merge DQN维护一个最多K个近期在线网络副本的滚动记忆。在目标网络更新时，从回放缓冲中采样N个下一状态观测，用最新网络副本的贪心动作作为锚定动作；对每个副本，计算每个参数对锚定动作Q值的平方梯度作为敏感性权重。然后通过敏感性加权平均合并所有副本参数，并加入近因先验λ偏向最新副本，得到新的目标网络参数。在线网络仍使用标准TD误差损失训练，不改变其他组件。

### 三、结果（Result）
在Atari 10M步环境下，Memory Merge DQN与DQN、Averaged DQN、带层归一化的DQN及PQN（带梯度裁剪）对比，获得了最多的第一名最终性能结果，整体表现优于DQN、Averaged DQN和PQN，并在多个游戏中取得显著提升，表明选择性合并近期参数历史能带来收益。

### 四、结论（Conclusion）
研究表明，选择性合并近期参数权重和历史可以提高DQN智能体的稳定性和最终性能，目标网络设计是长期值学习中保护有用价值函数结构的重要机制，Memory Merge DQN是一个有竞争力的替代方案。

### 五、方法论与关键技术细节
使用Atari 2600游戏，标准预处理；网络采用卷积层+GELU激活+层归一化（除vanilla DQN用ReLU无归一化）；记忆大小K_max=10（实验中），观测样本数N=32；近因先验λ固定为1且未调参；敏感性计算基于平方梯度，需要额外计算存储K个网络副本的梯度，增加计算开销；局限性包括依赖层归一化保持参数兼容性、不适用于连续控制任务，且记忆大小和先验系数需要启发式选择。
