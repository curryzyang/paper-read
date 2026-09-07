# Multivariable Extremum Seeking for Locally Lipschitz Objectives

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Alan Williams
- 机构：Los Alamos National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04401v1) · [PDF](https://arxiv.org/pdf/2609.04401v1)

## TLDR
This paper proposes a minimal multivariable extremum-seeking modification—using rationally independent perturbation frequencies with matched demodulation signals—so that for any locally Lipschitz objective, the long-time averaged dynamics are exactly the negative gradient of a kernel-smoothed objective, yielding practical global uniform asymptotic stability under appropriate conditions and enabling nonsmooth and nonconvex optimization.

## Abstract
Classical extremum seeking (ES) is commonly interpreted as approximating gradient descent, but this interpretation is less clear for nonsmooth objectives in the continuous-time multivariable setting. We propose a minimal modification of the classical multivariable perturbation--demodulation architecture: rationally independent perturbation frequencies and matched demodulation signals. For any locally Lipschitz static objective, the Kronecker--Weyl theorem shows that, at every fixed perturbation amplitude, the long-time averaged dynamics are exactly the negative gradient of a kernel-smoothed objective. Because rationally independent frequencies render the perturbation and demodulation signals nonperiodic, we employ general averaging theory rather than periodic averaging theory. If the gradient flow of the smoothed objective is globally uniformly asymptotically stable, then the ES dynamics are practically globally uniformly asymptotically stable. We also derive a general matching condition relating the perturbation occupation density, demodulation signal, and smoothing kernel, yielding a family of alternative designs. Numerical examples include a nonsmooth objective function, which may be interpreted as the penalty function of a nonlinear program, and the Rastrigin function, for which smoothing eliminates all undesired local minima.


## 精读解读（中文）
### 一、研究动机
经典多变量极值搜索（ES）通常被解释为对梯度下降的近似，但当目标函数仅局部Lipschitz、甚至不可微时，这种解释在连续时间多变量设定下不再清晰。传统周期扰动轨迹在高维空间中只是一条闭合一维曲线，无法稠密采样参数邻域，因此难以将平均动力学视为附近梯度的加权平均。本文旨在通过最小化修改经典扰动-解调架构，使任意局部Lipschitz静态目标函数的长时间平均动力学精确等于某个核平滑目标的负梯度，从而为不可微优化提供确定性的无模型梯度类方法。

### 二、技术方案（Method）
提出一种多变量极值搜索设计：扰动信号的分量采用有理无关频率，例如二维时取ω̂1=1、ω̂2=√2，使扰动轨迹S(t)在[-a,a]^n中稠密并具有占据密度；解调信号与占据密度匹配，使每个分量的平均向量场使用同一个平滑核。系统动力学写为dx̂/dτ=-ε J(x̂+aS(τ)) M(τ)，其中ε=k/ω为时间尺度比，a为扰动幅度。利用Kronecker-Weyl定理得到长时间平均动力学精确为dz/dτ=-ε∇J_a(z)，其中J_a(x)=∫ J(x+au)κ(u)du，κ为单位质量平滑核。由于频率有理无关导致信号非周期，采用一般平均理论而非周期平均理论，避免了对目标函数可微性和小a泰勒展开的依赖。稳定性结论：若平滑目标J_a的梯度流全局一致渐近稳定，则ES动力学实用全局一致渐近稳定，误差由时间尺度比ε决定。还推导了扰动占据密度、解调信号与平滑核之间的一般匹配条件，可用于构造替代扰动-解调-核组合。

### 三、结果（Result）
对任意局部Lipschitz静态目标，在固定扰动幅度a下，长时间平均动力学精确等于负梯度流-∇J_a，其中J_a是目标与匹配核κ的卷积平滑；该结果不要求J可微。经典一维正弦设计等价于半圆核平滑，二维及以上采用有理无关频率后，平均场各分量均对应同一平滑目标的梯度分量。数值例子表明：对非光滑惩罚型目标函数，平滑消除尖点并给出连续梯度；对Rastrigin函数，平滑可消除所有不期望的局部极小点。与现有基于随机方向或球面扰动的不可微ES相比，该设计在任意Lipschitz目标上提供固定设计且长期平均动力学精确为显式核平滑目标的梯度，并支持多种扰动-核选择。

### 四、结论（Conclusion）
本文证明了采用有理无关频率和匹配解调信号的多变量ES，其长时间平均动力学严格等于核平滑目标的负梯度流，从而将经典ES的梯度下降解释从光滑目标推广到任意局部Lipschitz目标。该设计在不可微优化中具有确定性和可解释性，能通过选择扰动幅度a控制平滑范围，消除非凸目标中的伪局部极小点，并具有实用全局渐近稳定性保证。匹配条件为设计不同扰动波形与平滑核提供了通用框架，拓展了ES在无模型非光滑优化中的应用。

### 五、方法论与关键技术细节
关键点包括：1）扰动频率必须有理无关以保证轨迹在[-a,a]^n稠密；解调信号需与占据密度匹配，使各分量平均场共享同一核κ，否则会得到分量依赖的核，无法表示为单一平滑目标的梯度。2）平均理论采用一般平均理论而非周期平均理论，因为非周期信号不满足周期平均的前提；Rademacher定理保证局部Lipschitz函数几乎处处可微，Kronecker-Weyl定理保证时间平均等于空间积分。3）平滑目标J_a(x)=∫J(x+au)κ(u)du的梯度流若全局一致渐近稳定，则系统实用全局一致渐近稳定，此处a决定平滑范围，ε=k/ω决定平均误差，二者作用分离。4）一维情形与经典ES重合，核为半圆核κ(u)=(2/π)√(1-u²)；文中给出正弦和三角波两种扰动设计及对应的两种匹配解调信号。5）局限性：需要目标局部Lipschitz以利用几乎处处可微和卷积求导；稳定性依赖平滑后目标的梯度流特性，且全局渐近稳定性结论为实用意义（半全局/实用意义），非精确全局收敛；数值优化前需选择合适扰动幅度a使平滑消除不期望局部极小点。
