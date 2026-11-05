# Data-Driven Stochastic LQR Control with Probabilistic Guarantees and Uncertainty Refinement

- 区域：精读区
- 排名：1
- 匹配度：5.9/10
- 来源：arxiv
- 作者：Amir Modares, Charalambous Themistoklis, Hamidreza Modares
- 机构：University of Cyprus, Michigan State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05533v1) · [PDF](https://arxiv.org/pdf/2611.05533v1)

## TLDR
This paper proposes a probabilistic direct data-driven framework for stochastic LQR output-feedback control from noisy input-output data, using lifted parameterization, convex optimization with high-probability mean-square stability and performance guarantees, and Gaussian-zonotope uncertainty refinement to reduce conservatism and approach optimal performance.

## Abstract
This paper presents a probabilistic framework for the direct, data-driven synthesis of the stochastic linear- quadratic output-feedback control for linear systems sub- ject to process and measurement noise. Using delayed input-output measurements, we derive a lifted parameter- ization together with an equivalent lifted linear quadratic cost, enabling controller synthesis without explicitly identi- fying the lifted dynamics. Two complementary closed-loop formulations, based on trajectory and covariance represen- tations, are then developed, whose uncertainties depend only on the realized but unknown lifted noise. We char- acterize the relative performance of the two formulations in finite-data regimes. High-probability uncertainty bounds are developed for realized noises, leading to a convex optimization solution to the problem, whose feasibility cer- tifies probabilistic mean-square stability (p-MSS) and per- formance guarantees. To reduce conservatism, Gaussian zonotopes are used to refine uncertainty sets by elimi- nating noise realizations inconsistent with measured data, and a novel intersection rule enables the consistent fusion of data-driven and physics-informed information. These components are integrated into an adaptive framework that unifies indirect (identification-based) and direct (control- oriented) data-driven linear-quadratic output-feedback con- trol. Unlike existing direct data-driven LQR methods that verify stability a posteriori, our by-construction approach achieves robust stability alongside reduced conservatism and superior performance. Simulation results show that the proposed controller approaches the ideal optimal solution while outperforming existing data-driven methods under noisy measurements.


## 精读解读（中文）
### 一、研究动机
直接数据驱动控制可绕过系统辨识，但现有数据驱动LQR方法多依赖无噪声状态测量，或在含噪输出场景下缺乏非渐近概率稳定性与性能保证，且鲁棒性常依赖保守不确定集和人工正则参数。本文旨在仅利用含过程噪声与测量噪声的单条输入-输出轨迹，直接合成随机LQR输出反馈控制器，并在构造上同时保证概率均方稳定性和近优性能。

### 二、技术方案（Method）
基于单条有限含噪输入-输出轨迹构造延迟Hankel数据与提升状态，并建立等价的提升线性二次代价，从而无需显式辨识提升动态即可直接设计控制器；随后给出轨迹级与协方差级两种闭环参数化，其不确定性仅取决于已实现但未知的提升噪声。为处理提升坐标中状态与噪声的统计相关性，引入延迟工具变量恢复外生性，并利用提升噪声的有限记忆导出非渐近高概率不确定界，将问题转化为凸优化/LMI，其可行性直接认证概率均方稳定性和性能界。进一步采用高斯zonotope剔除与实测数据不一致的噪声实现，并通过新的交集规则融合数据驱动信息与物理先验，形成统一间接与直接数据驱动LQR的自适应框架。

### 三、结果（Result）
理论上刻画了轨迹级与协方差级两种闭环公式在有限数据下的相对性能：随数据长度T增大，协方差级不确定性相对名义项趋于消失，而轨迹级不确定性比值保持O(1)。所提凸优化若可行，即以构造方式认证p-MSS与性能保证，且高斯zonotope不确定性精化可降低保守性；仿真表明控制器接近理想最优解，并在噪声测量下优于现有数据驱动方法。

### 四、结论（Conclusion）
论文提出了一套面向含噪输入-输出数据的概率直接数据驱动随机LQR输出反馈框架，将提升建模、非渐近概率界、凸优化稳定性认证与不确定性精化统一起来。该方法无需状态测量和显式辨识，在构造上保证鲁棒稳定性并降低保守性，实现了接近最优的控制性能，同时统一了直接与间接数据驱动设计思路。

### 五、方法论与关键技术细节
关键实现包括：用深度Ly的输入-输出Hankel矩阵和持续激励条件构造提升数据，Ly需不小于可观测性指数且输入满足相应阶次PE；过程噪声与测量噪声为已知协方差W、V的零均值高斯且互不相关，系统矩阵先验用高斯zonotope表示，并假设(A,B)可控、(A,C)可观测、A非奇异及(A,Q^{1/2}C)可检测。技术核心是延迟工具变量恢复外生性、利用提升噪声有限记忆推导非渐近集中界、以LMI可行性认证p-MSS，以及约束高斯zonotope交集规则融合数据一致性与物理先验；局限在于依赖高斯/已知协方差与先验、单条有限轨迹及仿真验证，LMI规模随提升维数和数据尺度增长，且不确定集精化后仍可能存在一定保守性。
