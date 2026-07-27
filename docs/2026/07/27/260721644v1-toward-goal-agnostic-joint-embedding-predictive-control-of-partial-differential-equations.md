# Toward Goal-Agnostic Joint-Embedding Predictive Control of Partial Differential Equations

- 区域：精读区
- 排名：2
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Jonathan Gallagher, Roberto Guglielmi
- 机构：University of Waterloo
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21644v1) · [PDF](https://arxiv.org/pdf/2607.21644v1)

## TLDR
A goal-agnostic joint-embedding predictive control framework for PDEs trains a frozen latent world model offline without rewards, then achieves superior multi-task control by planning with a learned kinetic-energy probe rather than raw latent L2 distance, as demonstrated on 2D Navier-Stokes with improved tracking and reward.

## Abstract
We present a goal-agnostic control framework for partial differential equations (PDEs) built around a joint-embedding predictive architecture (JEPA). The small 2D ViT encoder and action-conditioned latent dynamics are trained offline without a reward or downstream goal, frozen, and reused by a model-predictive path integral (MPPI) controller. We find that when available, the control objective is better applied to an explicit physical observable (provided injectivity) than to minimizing raw Euclidean distance ($L^2$) in the learned latent space. For a learned linear kinetic-energy (KE) probe on frozen latent rollouts we can reproduce held-out trajectories with $R^2=0.989$, while requiring no change to the underlying world model. On the PDE Control Gym 2D Navier--Stokes benchmark, using KE-probe planning improves the matched 50-episode native reward from $-12.08\pm0.86$ for latent-$L^2$ planning to $-10.90\pm0.91$ (95\% CI), while lowering last-quarter velocity-field RMSE from $0.0765$ to $0.0692$. Across three intentionally withheld, dissimilar, aperiodic targets, KE planning lowers late field RMSE by $53\%$ relative to latent-$L^2$ planning ($0.0220$ versus $0.0469$), winning all 30 paired episodes. The same frozen model also supports controls targeting stabilization around a steady configuration via direct regulation of KE achieving $2.7\%$ mean relative error. While the latent probe is brittle to measurement noise and missing pixels, we believe the results support the claim that latent dynamics can remain both dynamic and goal-agnostic while calibrated observables (granted they guarantee unique continuation) may be a better objective for state control


## 精读解读（中文）
### 一、研究动机
现有PDE控制方法如模型控制、学习替代模型和强化学习存在局限性，需要问题特定分析、重训练或精心设计的奖励函数。本文提出一种目标无关的联合嵌入预测控制框架，旨在部署时改变控制目标而不需重训练世界模型，并解决潜在空间中欧氏距离未校准的问题。

### 二、技术方案（Method）
使用轻量级2D ViT编码器（256维输出，3×3 patch，4个transformer块，4注意力头）和动作条件潜在预测器（2层MLP，512隐藏单元，输入4步历史，自回归滚动12潜在步，步长2）。训练时对状态随机掩码（掩码比例0.3-0.9，类型包括矩形、像素、行条带），采用复合损失：预测L2损失、VICReg方差协方差惩罚、时间拉直损失和Delta-JEPA动作解码损失。离线数据集含6930条轨迹（每轨迹200场+199动作），训练50k步（lr 3e-4）再微调50k步（lr 6e-5）。部署时用MPPI控制器（512样本，3迭代，规划5潜在步）最小化潜在L2或动能探针（线性探针，R^2=0.989）的跟踪误差。

### 三、结果（Result）
在PDE Control Gym 2D Navier-Stokes基准上，动能探针规划相比潜在L2规划提升本征奖励（-10.90±0.91 vs -12.08±0.86）和后期速度场RMSE（0.0692 vs 0.0765）。在三个不同非周期目标上，动能规划降低后期RMSE达53%（0.0220 vs 0.0469），赢得所有30个配对episode。同一冻结模型还支持稳定控制，达到2.7%平均相对误差。

### 四、结论（Conclusion）
潜在动力学可在保持目标无关性的同时保持动态，而经过校准的物理可观测量（保证唯一延续性）作为控制目标优于原始潜在空间距离。尽管动能探针对测量噪声和缺失像素敏感，但结果支持目标无关联合嵌入预测架构在PDE控制中的有效性。

### 五、方法论与关键技术细节
数据：2D Navier-Stokes，21×21网格，ν=0.1，动作a∈[0,4]。先验：VICReg防止表示崩溃，时间拉直损失（λ_str=0.1），Delta-JEPA动作解码（λ_Δa=10）。超参：batch size 128，lr 3e-4→6e-5，权重衰减1e-2。MPPI：H=5潜在步（10本征步），温度T=0.1。局限：动能探针对测量噪声和缺失像素脆弱，需进一步验证可观测量的可逆性条件。
