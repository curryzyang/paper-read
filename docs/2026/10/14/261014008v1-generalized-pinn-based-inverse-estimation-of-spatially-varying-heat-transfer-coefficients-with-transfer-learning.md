# Generalized PINN-Based Inverse Estimation of Spatially Varying Heat Transfer Coefficients with Transfer Learning

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Pradipan Maitra, Jariful Hassan, Arijit Hazra
- 机构：Indian Institute of Technology Palakkad
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14008v1) · [PDF](https://arxiv.org/pdf/2610.14008v1)

## TLDR
This paper shows that generalized PINN boundary representations can estimate spatially varying convective heat transfer coefficients from transient interior temperature data without a prescribed quadratic form, while transfer learning cuts target-training time by roughly 50–85% with accuracy depending on source-target compatibility.

## Abstract
This study investigates generalized boundary representations and transfer learning for physics-informed neural-network (PINN) estimation of spatially varying convective heat transfer coefficients (HTCs) in jet impingement cooling. Piecewise-linear (PWL) and neural-network boundary estimators are inferred from transient interior-temperature measurements and evaluated against CFD-CHT reference HTC profiles at Reynolds numbers of 5000, 10000 and 15000. A discrete Adjoint-FEM formulation with gradient regularization based on the $H^1$-seminorm provides an independent inverse-method comparison. Transfer learning is investigated under two source-target conditions: transfer between noise levels at the same Reynolds number, and transfer from a controlled Gaussian-profile problem to CFD-CHT-derived target problems at different Reynolds numbers. For the representative Re = 5000 target with 5% measurement noise, quadratic, PWL, and neural-network PINNs achieve relative HTC-profile errors of 5.08, 5.31 and 5.19%, respectively, while generalized representations reduce the error for the Re = 15000 target from 16.76% for the quadratic PINN to 14.41% and 14.46%. Transfer learning reduces target-training time by 57.86-81.71% for fixed-Reynolds-number transfer and by 50.59-84.94% for Gaussian-to-CHT transfer. Its effect on reconstruction accuracy is target dependent: fixed-profile PWL transfer remains within 0.30 percentage points of scratch training, whereas Gaussian-to-CHT transfer produces differences of 0.10-1.52 percentage points across targets and representations. These results demonstrate that generalized PINN representations can accommodate spatially varying HTC profiles without a prescribed quadratic form, while transfer learning can substantially reduce target-training cost for repeated inverse estimation, with the resulting reconstruction accuracy depending on source-target compatibility.


## 精读解读（中文）
### 一、研究动机
空间变化的对流换热系数（HTC）反演常依赖预设函数形式，难以适应射流冲击冷却中复杂边界；同时重复开展 PINN 反演训练代价较高。本文因此研究广义边界表示与迁移学习，以提升 PINN 反演的适应性和效率。

### 二、技术方案（Method）
研究以瞬态内部温度测量为输入，在射流冲击冷却问题中用 PINN 反演空间变化 HTC，并比较二次型、分段线性（PWL）和神经网络边界估计器；同时采用基于 H^1 半范数梯度正则化的离散 Adjoint-FEM 作为独立逆方法对照。评估对象为 Reynolds 数 5000、10000 和 15000 下的 CFD-CHT 参考 HTC 剖面，迁移学习设置两类源到目标条件：同一 Reynolds 数下不同噪声水平之间迁移，以及从受控 Gaussian 剖面问题迁移到不同 Reynolds 数的 CFD-CHT 目标问题，并与从头训练比较训练时间和重建精度。

### 三、结果（Result）
在 Re=5000 且 5% 测量噪声的代表性目标上，二次型、PWL 和神经网络 PINN 的相对 HTC 剖面误差分别为 5.08%、5.31% 和 5.19%；对于 Re=15000 目标，广义表示把误差从二次型 PINN 的 16.76% 降至 14.41% 和 14.46%。迁移学习将目标训练时间在同 Reynolds 数迁移中减少 57.86-81.71%，在 Gaussian-to-CHT 迁移中减少 50.59-84.94%，但精度影响依赖目标：固定剖面 PWL 迁移与从头训练的差异在 0.30 个百分点内，而 Gaussian-to-CHT 迁移在不同目标和表示下的差异为 0.10-1.52 个百分点。

### 四、结论（Conclusion）
结果表明，广义 PINN 表示无需预设二次形式即可容纳空间变化 HTC 剖面；迁移学习能显著降低重复逆估计的目标训练成本，但最终重建精度取决于源目标兼容性。

### 五、方法论与关键技术细节
摘要给出的关键细节包括：数据为瞬态内部温度测量，含 5% 测量噪声情形，参考真值为 Re=5000、10000、15000 的 CFD-CHT HTC 剖面；方法比较二次型、PWL、神经网络边界估计器，并用离散 Adjoint-FEM 配合 H^1 半范数梯度正则化独立对照；迁移学习考察同 Reynolds 数噪声水平迁移与 Gaussian-profile 到 CFD-CHT 目标迁移，指标为相对 HTC 剖面误差、目标训练时间降幅及与从头训练精度差。局限性方面，迁移效果和重建精度依赖源目标兼容性，且给定材料未披露 PINN 网络结构、损失函数细节、优化器、训练轮数和计算复杂度等超参或实现约束。
