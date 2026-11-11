# Proportional Neuro-Impulsive Control of SISO LTI Systems

- 区域：精读区
- 排名：1
- 匹配度：5.6/10
- 来源：arxiv
- 作者：Christian Fernandez Lorden, Elena Petri, W. P. M. H. Heemels, Alessio Franci
- 机构：WEL Research Institute, Eindhoven University of Technology, University of Liège
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13043v1) · [PDF](https://arxiv.org/pdf/2611.13043v1)

## TLDR
This paper proves that a proportional neuro-impulsive controller—an integrate-and-fire neuron whose spike amplitude scales with the plant output—can semi-globally asymptotically stabilize any static output-feedback stabilizable SISO LTI system, and provides a parameter-selection algorithm illustrated on a linearized inverted pendulum.

## Abstract
This paper explores a controller that is at the crossroads of neuromorphic, i.e., spike-based, and impulsive control systems. The controller consists of a single integrate-and-fire-like neuron that generates an input proportional to the system output when the neuron variable reaches a threshold. We prove that any static output-feedback stabilizable single-input single-output (SISO) linear time-invariant (LTI) plant can be made semi-globally asymptotically stable (sGAS) in closed loop with the proposed neuro-impulsive controller. This improves on existing fixed-amplitude neuromorphic controllers, which only achieve practical stability, but at the price of using graded spiking inputs. Moreover, we provide an algorithm for choosing appropriate controller parameters given a set of admissible initial conditions. A numerical example of an inverted pendulum linearized around its upright equilibrium illustrates the method.


## 精读解读（中文）
### 一、研究动机
现有固定幅值神经形态脉冲控制器在目标附近只能实现实际稳定，因为每次脉冲的修正量不随系统输出缩放，导致振荡与远距离脉冲频率之间存在矛盾。比例型、状态依赖的脉冲有望像连续控制一样随状态缩放修正量，从而获得渐近稳定并减少远距离所需脉冲次数。已有脉冲控制工具通常要求跳变矩阵严格收缩或在流动-跳变循环上满足离散 Lyapunov LMI，不适用于本文的神经形态控制场景。

### 二、技术方案（Method）
针对静态输出反馈可稳定的 SISO LTI 系统，构建由单个类积分-发放神经元驱动的混合闭环 NICS，其流动阶段为 xdot=Ax、xidot=|Cx|+Ib，跳变阶段为 x+=(I-alpha BC)x、xi+=0，参数为阈值 Delta、偏置电流 Ib 和脉冲增益 alpha。控制器在神经元变量达到阈值时产生与输出 y=Cx 成比例的脉冲输入，用脉冲序列逼近连续静态输出反馈 K 的作用。由于 BC 为秩一矩阵且 I-alpha BC 通常非收缩，分析采用冲击映射并借鉴 emulation 思路，证明对任意 SOF 可稳定的 SISO LTI 被控对象均可通过选择 Delta、Ib、alpha 使闭环半全局渐近稳定。给定紧凑的容许初始条件集合，算法返回使 NICS 从该集合 sGAS 的控制器参数，并用线性化倒立摆进行数值验证。

### 三、结果（Result）
论文证明任何静态输出反馈可稳定的 SISO LTI 系统都可由所提出的比例神经脉冲控制器实现半全局渐近稳定，而现有固定幅值神经形态控制器通常只能达到实际稳定。该优势的代价是需要使用幅值随输出分级变化的脉冲输入，单个神经元即可携带输出符号并避免用两个神经元表示正负脉冲。作者给出了按给定初始条件集合选取 Delta、Ib、alpha 的算法，并通过倒立摆直立平衡点线性化模型的数值例子说明方法有效。

### 四、结论（Conclusion）
比例神经脉冲控制把神经形态脉冲控制与脉冲控制联系起来，在保留单个积分-发放神经元结构的同时，用输出比例脉冲消除了固定幅值脉冲导致的实际稳定限制。由于分级脉冲执行器可能不易获得，该工作被视为迈向由不同输出尺度固定幅值神经元阵列实现类似设计的第一步。整体结果强调比例脉冲可实现半全局渐近稳定，但远距离脉冲频率仍随距离增长，只是每次脉冲修正更大、所需脉冲更少。

### 五、方法论与关键技术细节
模型要求 A 非 Hurwitz 且存在正 K 使 A-BKC Hurwitz，若仅负 K 可稳定则可交换反馈符号；Ib>0 用于保证最大驻留时间 Delta/Ib，并防止原点附近有效增益 alpha/T 趋零。分析关键点是 BC 秩一导致跳变矩阵 I-alpha BC 对 n>1 不可能收缩，且开环流动也不收缩，因此稳定性来自流动与跳变的联合效应并用冲击映射处理。算法根据容许初始条件集合选择 Delta、Ib、alpha，理论上保证 sGAS 而非全局渐近稳定；数值例子为倒立摆线性化模型，代码与数据公开。局限包括需要比例分级脉冲、远离目标时脉冲频率仍会增大，以及结论依赖静态输出反馈可稳定性和半全局框架。
