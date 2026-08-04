# Physically Consistent SINDy (Sparse Identification of Nonlinear Dynamics) for Microgrid Identification and Real-Time Frequency Control

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Mohan Du, Jiayi Lai, Rong-Peng Liu, Xiaozhe Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00213v1) · [PDF](https://arxiv.org/pdf/2608.00213v1)

## TLDR
PC-SINDYc is a physically consistent SINDy-based framework that robustly identifies microgrid frequency dynamics from noisy PMU data under delays and constraint activations, integrates a model predictive controller for real-time frequency control with asymptotic stability guarantees, and outperforms PI, conventional SINDYc, and reinforcement learning methods in simulations.

## Abstract
This paper proposes PC-SINDYc, a novel framework for the identification and frequency control of microgrids (MGs) with distributed energy resources. By leveraging physics-guided library construction, total least squares regression, and random sample consensus, the regression algorithm of PC-SINDYc robustly identifies the true frequency dynamics of MGs from phasor measurement unit (PMU) data, considering noise, delays, and constraint activations. Based on the identified model, the PC-SINDYc framework further incorporates a model predictive controller (MPC) for real-time frequency control. We prove that, under mild conditions, PC-SINDYc ensures asymptotic stability of the MG. Simulations on 4-bus and 13-bus MGs demonstrate that PC-SINDYc effectively controls MG's frequency across various disturbances unseen during the offline identification, outperforming PI controllers, conventional SINDYc, and state-of-the-art reinforcement learning methods.


## 精读解读（中文）
### 一、研究动机
微电网中分布式能源的随机性和缺乏惯量给频率稳定带来挑战，而现有模型驱动方法依赖难以获取的精确参数，黑箱数据驱动方法（如神经网络、强化学习）缺乏物理可解释性和稳定性保证，传统SINDy方法也不能识别真实物理模型且对噪声和约束激活敏感。因此需要一种能识别真实频率动态、鲁棒抗噪、可解释且保证控制性能的数据驱动方法。

### 二、技术方案（Method）
PC-SINDYc框架：首先基于物理指导构建候选函数库，显式考虑采用下垂控制和虚拟同步发电机控制的GFM变换器以及GFL变换器的不同控制模式，确保候选库包含与真实动态等价的项；然后利用PMU数据，结合总体最小二乘回归抑制测量噪声，并采用RANSAC自动剔除因变换器约束激活而产生的异常数据，从而离线辨识微网的频率动态模型；最后基于辨识出的模型设计模型预测控制器，在实时控制中根据当前测量状态滚动优化控制输入，实现频率恢复。辨识过程中仅需对系统施加±0.001至±0.01 p.u.的小信号激励，并采集约10秒的PMU数据。

### 三、结果（Result）
在4母线和13母线微电网仿真中，针对离线辨识阶段未见的多种扰动，PC-SINDYc均能有效控制频率，性能优于PI控制器、传统SINDYc和最先进的强化学习方法。理论分析还证明在温和条件下PC-SINDYc可保证微电网的渐近稳定性。

### 四、结论（Conclusion）
PC-SINDYc为含分布式能源的微电网提供了一种纯数据驱动、最小侵入且物理一致的识别与控制框架，能在噪声、延迟和约束激活下辨识真实频率动态，并基于该模型实现有稳定性保证的实时频率控制，克服了现有方法依赖精确参数、缺乏可解释性与泛化性的局限。

### 五、方法论与关键技术细节
关键细节包括：物理指导的库构造确保识别模型与真实方程等价；总体最小二乘用于消除回归稀释；RANSAC自动拒绝约束激活导致的异常样本；小信号激励幅度为±0.001至±0.01 p.u.，数据窗口约10秒；基于MPC的控制设计具有渐近稳定性证明；不依赖网络和变换器参数。局限性可能在于需要PMU测量数据的质量与时间同步，以及离线辨识后在线控制对计算实时性的要求。
