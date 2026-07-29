# Lantern: Conflict-Aware Gradient Blending for Physics-Guided Diffusion Models in Calorimeter Simulation

- 区域：精读区
- 排名：10
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Farzana Yasmin Ahmad, Vanamala Venkataswamy, Geoffrey Fox
- 机构：University of Virginia
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.25060v1) · [PDF](https://arxiv.org/pdf/2607.25060v1)

## TLDR
Lantern introduces a conflict-aware gradient blending method (GradBlend) and two physics-aware auxiliary losses (variance-stabilized voxel residual and graph Laplacian) to guide diffusion models in calorimeter simulation, improving correlation fidelity (CFD) and physics distance (FPD) while preventing the generative objective from being degraded.

## Abstract
Monte Carlo simulation of calorimeter showers is a principal bottleneck for the High-Luminosity LHC, and diffusion models have emerged as fast, high-fidelity surrogates. Their denoising objective is purely statistical, however: a model can minimize it while placing the physics wrong. Existing physics-informed generative methods cannot close this gap, because they assume a closed-form law, a governing PDE residual or a hard per-sample constraint, that a shower does not supply: no per-sample PDE governs a stochastic cascade, and energy conservation fixes only one scalar per shower. Standard metrics ignore the correlation structure across calorimeter layers and voxels, comparing showers only in a physics feature space. We address both gaps. We introduce the Correlation Frobenius Distance (CFD), a single normalized score for correlation fidelity at layer-wise and voxel-wise scales. We then encode the soft per-sample structure available in a shower as two physics-aware auxiliary losses: a variance-stabilized voxel residual loss grounded in counting statistics, and a graph Laplacian loss over the detector geometry. We combine both with denoising through GradBlend, which anchors the step magnitude to the denoising gradient while letting the auxiliary steer its direction, yielding Lantern, a physics-guided diffusion surrogate. On CaloChallenge Dataset 2, injecting the physics losses through task-symmetric rules such as PCGrad, GradNorm, IMTL-G, and ConFIG inflates FPD by 2-100x relative to denoising alone, whereas GradBlend admits the same signal without regression and, with the Laplacian loss, Lantern improves both FPD and CFD. Our ablation on the auxiliary loss scheduler shows that the voxel residual loss, whose gradient conflicts with denoising, requires a terminal denoising-only phase to preserve shower fidelity, whereas the non-conflicting Laplacian loss is insensitive to the schedule.


## 精读解读（中文）
### 一、研究动机
蒙特卡洛模拟量热器簇射是高亮度大型强子对撞机的主要计算瓶颈，扩散模型作为快速高保真替代方案，但其去噪目标纯粹是统计的，模型可能在物理上出错。现有物理信息生成方法假设存在封闭形式定律、PDE残差或每样本硬约束，而随机簇射不提供这些。标准评估指标忽略跨层和体素的相关性结构。本文旨在填补这两个空白：引入相关性度量CFD，并设计物理引导扩散模型。

### 二、技术方案（Method）
基于条件扩散模型，将生成分解为能量网络（自回归Transformer预测层能量比）和形状网络（条件Vision Transformer预测噪声）。在形状网络中引入两个物理感知辅助损失：方差稳定化体素残差损失（基于计数统计，对每个体素残差按能量平方根加权并用Huber损失）和图拉普拉斯损失（基于探测器几何的图拉普拉斯惩罚相邻面共享体素差异）。采用GradBlend梯度混合规则：将更新方向与大小分离，步长锚定到去噪梯度，辅助梯度仅通过单位方向影响更新方向（通过余弦相似度门控）。训练时辅助损失通过开关调度（终期仅去噪阶段）。

### 三、结果（Result）
在CaloChallenge Dataset 2上，使用PCGrad、GradNorm、IMTL-G、ConFIG等对称规则注入物理损失使FPD恶化2-100倍，而GradBlend不退化且结合图拉普拉斯损失同时改善FPD和CFD。消融表明：体素残差损失与去噪梯度冲突，需要终期仅去噪阶段保持样本保真度；图拉普拉斯损失非冲突，对调度不敏感。

### 四、结论（Conclusion）
本文提出相关性Frobenius距离（CFD）、两个物理感知辅助损失和GradBlend组合规则，实现了对强生成代理安全的物理引导。证明锚定去噪是必要的，并揭示了体素残差损失与去噪的冲突性质及其调度要求。

### 五、方法论与关键技术细节
数据为CaloChallenge Dataset 2（6480体素量热器）。先验：计数统计（方差稳定化）和探测器几何（图拉普拉斯）。损失：Huber损失（δ=1）结合逆方差权重（ε=1e-6）。超参：体素残差损失只在训练早期激活。复杂度：由于无每样本PDE，物理信息仅通过软损失引入。局限性：能量网络未受物理引导，可能成为瓶颈；图拉普拉斯损失假设简单邻接，可能不足以捕捉长程相关性。
