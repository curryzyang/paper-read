# Major-Minor LQ Mean Field Games with Erroneous Initial Information: Distributed Error Estimation and Strategy Modification

- 区域：精读区
- 排名：2
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Yuxin Jin, Haotian Wang, Wang Yao, Xiao Zhang
- 机构：Beihang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22558v1) · [PDF](https://arxiv.org/pdf/2607.22558v1)

## TLDR
This paper studies major-minor linear-quadratic mean field games with erroneous initial information under constrained observations, deriving linear error propagation, formulating distributed maximum-likelihood estimation for unknown initial errors, and proposing an estimate-based one-shot strategy modification to correct the control law.

## Abstract
This paper studies major-minor linear-quadratic mean field games (MMLQMFGs) with erroneous initial information under a constrained observation structure. Each minor agent observes only its own state and the major agent's state, while the major agent observes its own state and the states of a subset of minor agents; neither side observes the mean field state directly. We show that the initial-information errors propagate linearly through the game dynamics and lead to explicit deviations in the major state, the actual mean field, and the agents' internally updated mean field states. Based on this structure, we formulate distributed error identification as a parameter-estimation problem from discrete-time local observations and construct maximum-likelihood estimators for unknown initial errors. We then propose an estimate-based strategy modification at an intermediate time by reconstructing the current mean field from the estimated errors and switching to the corresponding control law. We also characterize the resulting estimation errors and show that, in the present symmetric setting, the major agent's estimation precision depends on the number of observed minor agents but not on their identities. Numerical results illustrate the proposed method.


## 精读解读（中文）
### 一、研究动机
在major-minor线性二次型均场博弈中，由于初始均场信息错误且观测结构受限（minor仅观测自身和major，major仅观测自身和部分minor，均不直接观测均场），现有标准模型假设理想信息，未能处理此类偏差。本文旨在解决这一实际问题，分析误差传播并提出分布式误差估计与策略修正方法。

### 二、技术方案（Method）
本文考虑包含一个major和大量minor的LQ均场博弈，各agent动力学由线性随机微分方程描述，代价函数为二次型。在正确信息下有已知反馈控制律。当初始均场信息错误时，证明误差在系统中线性传播，并推导出major状态、实际均场与agent内部更新均场之间的显式偏差。基于此，将分布式误差识别转化为从离散时间局部观测中估计未知初始误差的参数估计问题，为每个minor构造关于其私有误差和公共误差分量的最大似然估计，为major构造公共误差分量的最大似然估计。然后提出在中间时刻基于估计值的策略修正：各agent利用估计误差重构当前均场，并切换到对应控制律。

### 三、结果（Result）
本文建立了初始信息误差的线性传播关系，表明误差通过动力学线性演化。最大似然估计方法能够有效识别误差，并且major的估计精度仅取决于其观察到的minor数量，而非其具体身份。数值实验验证了所提方法的有效性，在误差修正后性能接近完美信息情形。

### 四、结论（Conclusion）
本文针对初始信息错误下的major-minor LQ均场博弈，提出了分布式误差估计与策略修正框架。通过将误差识别转化为参数估计并利用一次策略切换，有效补偿了初始信息偏差，保证了系统的鲁棒性。理论分析揭示了误差传播的结构性及估计精度的对称性，为实际应用提供了理论基础。

### 五、方法论与关键技术细节
关键细节包括：误差传播推导基于线性系统结构，得出显式线性偏差公式；估计器为最大似然估计，利用了离散时间局部观测的似然函数；策略修正仅在中间单一时间点进行一次切换，不改变原控制律结构；对称设定下，major的Fisher信息矩阵仅取决于观测minor的数量而非身份，导致估计精度仅与数量相关；方法复杂度低，但假设系统为LQ且对称，限制了非对称或非线性场景的适用性。
