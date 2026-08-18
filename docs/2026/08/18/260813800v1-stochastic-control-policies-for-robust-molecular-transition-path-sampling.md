# Stochastic Control Policies for Robust Molecular Transition Path Sampling

- 区域：精读区
- 排名：7
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Jingqian Liu, Yu-Hsiang Wang, Yanru Qu, Ge Liu
- 机构：University of Illinois Urbana--Champaign
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13800v1) · [PDF](https://arxiv.org/pdf/2608.13800v1)

## TLDR
TLDR: This paper introduces stochastic control policies (FS-TPS and LaS-TPS) for machine-learning-guided transition path sampling, which improve rare molecular transition sampling success, path quality, and robustness to random initialization across biomolecular systems by recasting rollout-based control as learning a path-space proposal distribution.

## Abstract
Transition path sampling (TPS) aims to efficiently generate rare molecular transition trajectories between metastable states and is essential for understanding biomolecular mechanisms. Beyond traditional molecular dynamics (MD)-based sampling, machine learning has become central to state-of-the-art TPS. One major class of methods learns control forces during explicit MD rollouts. By preserving the underlying molecular dynamics, these methods tend to produce more physically plausible trajectories than endpoint-conditioned generators that construct paths directly. However, rollout-based control methods have been reported to exhibit unstable and strongly seed-dependent performance. We recast rollout-based control as learning a path-space proposal distribution and investigate stochasticity placement as a design choice for improving exploration and optimization robustness. We develop two stochastic policies: FS-TPS, which directly parameterizes a state-dependent Gaussian distribution over the control policy output, and LaS-TPS, which samples a compact latent control variable and decodes it into structured, cross-atom-correlated force variation. We conduct extensive multi-seed experiments on three biomolecular systems of increasing size: alanine dipeptide, chignolin, and BBL, a fast-folding protein. Stochastic policies consistently improve transition success and path quality over deterministic-policy baselines while substantially reducing sensitivity to random initialization.


## 精读解读（中文）
### 一、研究动机
暂无可提取到的动机信息。

### 二、技术方案（Method）
暂无可提取到的方法信息。

### 三、结果（Result）
暂无可提取到的结果信息。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
暂无可提取到的关键方法论细节。
