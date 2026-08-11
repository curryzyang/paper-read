# Certified Feedforward Tracking for Unknown Nonlinear Systems via Invertible Neural Networks

- 区域：精读区
- 排名：2
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Berk Altiner, Rajasree Sarkar, Arunava Banerjee, Zongxuan Sun, Kenneth Kim
- 机构：DEVCOM Army Research Laboratory, University of Minnesota--Twin Cities
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06419v1) · [PDF](https://arxiv.org/pdf/2608.06419v1)

## TLDR
This paper proposes using invertible neural networks to eliminate inversion errors in data-driven feedforward control and applies conformal prediction to provide finite-sample probabilistic certificates for the tracking error of unknown nonlinear systems.

## Abstract
In this paper, we address the certification of datadriven feedforward control for periodic tracking of unknown nonlinear systems under partial state measurements. To this end, we adopt an invertible neural network (INN) as a surrogate for the unknown system. This choice allows us to bypass solving a nonconvex inversion problem, eliminating the associated inversion errors and reducing tracking error certification to a surrogate modeling problem. We then apply conformal prediction to provide finite-sample probabilistic guarantees on the surrogate modeling error which, through the derived tracking error bound, yield marginal certificates on feedforward tracking error. Finally, we demonstrate the approach on a DC-motor-driven mechanical load with nonlinear friction.


## 精读解读（中文）
### 一、研究动机
针对部分状态可测的未知非线性系统，数据驱动前馈控制通常需要先学习系统代理模型，再通过非凸优化求逆得到前馈输入；但非凸求逆的局部最优与全局最优之间的误差难以刻画，导致跟踪误差上界无法可靠认证。本文旨在利用可逆神经网络的结构可逆性消除求逆误差，并将跟踪误差认证转化为代理建模误差的统计认证问题。

### 二、技术方案（Method）
方法分为建模、逆计算和认证三个阶段。首先采集有限时域输入输出轨迹对，利用傅里叶变换将数据变换到频域，依据Volterra级数理论保留基频及各次谐波的实部/虚部，构造频域数据集D_omega。然后采用i-ResNet作为未知系统的频域代理模型，结构为F_hat(U)=U+c G_theta(U)，其中G_theta为多层前馈网络，c在(0,1)内固定；训练时对每层权重施加谱归一化保证Lipschitz常数不大于1，从而满足c L_G<1的压缩条件，以回归损失训练该代理模型。推理时，对给定期望输出Y_d，利用Banach不动点迭代计算F_hat^{-1}(Y_d)得到前馈输入，无需求解非凸优化。在认证阶段，将数据划分为训练集和校准集，定义非一致性分数mu_i=||Y_i-F_hat(U_i)||，用分裂保形预测得到1-delta分位数q_{1-delta}，最终给出频域跟踪误差上界L_F L_{F_hat^{-1}} q_{1-delta}。

### 三、结果（Result）
在DC电机驱动、含非线性摩擦的机械负载数值例上验证了该方法。结果表明，采用可逆神经网络作为代理模型后，前馈跟踪误差以至少1-delta的边际概率被限定在有限样本导出的保形分位数乘以Lipschitz常数之内；非凸求逆误差被消除，跟踪误差认证问题被简化为代理建模误差的认证问题。

### 四、结论（Conclusion）
将可逆神经网络与保形预测相结合，能够为未知非线性系统在部分状态测量下的周期跟踪提供可计算、有限样本概率保证的跟踪误差界。该方案不需要求解非凸逆问题，避免了求逆误差对跟踪性能的影响；在参考轨迹与理想前馈输入不超出训练数据分布支持范围时，认证结果有效。

### 五、方法论与关键技术细节
关键点包括：i-ResNet通过压缩条件保证可逆性，训练中使用谱归一化限制G_theta的Lipschitz常数且取c<1；逆映射用不动点迭代计算，误差随迭代次数几何衰减；误差上界依赖真实频域映射Lipschitz常数L_F、代理逆映射Lipschitz常数L_{F_hat^{-1}}以及代理在理想前馈输入处的建模误差；保形预测基于独立同分布假设，且要求参考轨迹与理想输入位于训练分布支撑内，否则外推会导致保证失效；频域表示缓解了高采样率下时域方法的维度灾难。局限在于需要估计或界定Lipschitz常数，且保形预测给出的是边际保证而非条件保证。
