# Gradient-Energy Guided Block-Wise Perturbations for Sharpness-Aware Minimization

- 区域：精读区
- 排名：6
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Zhen Huang, Jiaxin Deng, Junbiao Pang
- 机构：Beijing University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18306v1) · [PDF](https://arxiv.org/pdf/2607.18306v1)

## TLDR
GEAR-SAM improves Sharpness-Aware Minimization by using an exponential moving average of squared block gradients to dynamically and stably allocate a fixed perturbation budget across network blocks, leading to better generalization and robustness.

## Abstract
Sharpness-Aware Minimization (SAM) improves generalization by minimizing the worst-case loss in a local parameter neighborhood. Standard SAM implicitly allocates its global perturbation budget across parameter blocks according to instantaneous minibatch gradient norms. Such an allocation can be noisy and may not reflect the sensitivity that blocks accumulate throughout training. We propose Gradient-Energy Adaptive Radius SAM (GEAR-SAM), which maintains an exponential moving average (EMA) of squared block gradients as a lightweight, curvature-related sensitivity signal and allocates the fixed SAM budget through a closed-form constrained optimization. GEAR-SAM preserves the global SAM radius, requires no Hessian-vector products or explicit Fisher estimation, and adds only scalar state beyond SAM. Experiments on image classification, transfer learning, noisy-label learning, and partition studies demonstrate improved generalization and robustness across architectures and tasks. More broadly, GEAR-SAM provides a dynamic view of sharpness-aware optimization: a fixed perturbation budget should be redistributed as the sensitivity of functional network blocks evolves during training.


## 精读解读（中文）
### 一、研究动机
标准SAM通过瞬时梯度范数隐式分配全局扰动预算，这种分配易受小批量噪声干扰且无法反映参数块在训练过程中的累积敏感性。本文提出基于梯度能量的自适应半径分配方法，利用历史梯度二阶矩作为持久灵敏度信号，在保持全局预算不变的前提下动态调整各功能块的扰动半径。

### 二、技术方案（Method）
将网络划分为功能块（如残差组、分类头部），每个训练迭代中计算各块小批量梯度的平方范数（梯度能量），通过指数移动平均（EMA）维护历史敏感性分数。根据闭式约束优化：在全局扰动预算ρ²下最大化线性替代目标，得到各块分配半径r_b=ρ·s_b/√(∑_j s_j²)，确保全局预算不变。在每个块内沿梯度方向施加扰动后计算损失，完成参数更新。该方法仅需为每个块维护一个标量EMA状态，无需Hessian或显式Fisher计算。

### 三、结果（Result）
在CIFAR-10/100图像分类、迁移学习、噪声标签学习等任务上，GEAR-SAM优于标准SAM及多种变体（ASAM、GSAM等），在不同网络架构（ResNet、VGG、DenseNet等）中一致提升测试准确率和泛化鲁棒性。分区研究验证了基于功能块的划分粒度对性能的有效性。

### 四、结论（Conclusion）
固定全局扰动预算应根据网络功能块在训练过程中的敏感性动态重新分配。GEAR-SAM通过轻量的历史梯度能量代理实现了合理的动态分配，为锐度感知优化提供了训练过程中块敏感性演化的视角，是一种简单且高效的改进策略。

### 五、方法论与关键技术细节
关键点包括：1）使用EMA累积的梯度能量作为曲率相关代理，其理论基础来自梯度二阶矩与经验Fisher及期望Hessian的联系；2）块划分遵循功能单元原则（如残差块、归一化层与权重层同块），避免分割归一化参数；3）闭式分配公式具有尺度不变性，不引入额外超参数（仅EMA衰减系数β，默认0.9）；4）每块仅存储一个标量状态，计算开销极低；5）局限性：未显式建模跨块Hessian交互，且基于一阶方向进行扰动，代理信号在远离稳定点时混合一阶与二阶贡献。
