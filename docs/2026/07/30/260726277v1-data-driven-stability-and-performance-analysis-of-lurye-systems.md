# Data-Driven Stability and Performance Analysis of Lurye Systems

- 区域：精读区
- 排名：1
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Sahel Vahedi Noori, Peter Seiler
- 机构：University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26277v1) · [PDF](https://arxiv.org/pdf/2607.26277v1)

## TLDR
This paper develops data-driven convex conditions using only measured trajectory data (either with or without state measurements) to certify internal stability and induced-ℓ₂ performance of Lurye systems with known quadratic constraints on the nonlinearity.

## Abstract
This paper develops data-driven conditions for certifying internal stability and induced-$\ell_2$ performance of discrete-time Lurye systems. The Lurye system is an interconnection of a nominal LTI system in feedback with a static, memoryless nonlinearity. The nonlinearity satisfies a known set of quadratic constraints on the inputs and outputs. Existing conditions for Lurye systems require a state-space realization of the nominal LTI dynamics. Our first data-driven result instead formulates the stability and performance conditions using finite input, output, and state trajectories of the nominal LTI block. Our second condition removes the need for measured state trajectories by reconstructing the state sequence, up to a similarity transformation, from input/output data. This state reconstruction is performed using deterministic subspace-identification techniques. Both data-driven conditions are expressed as convex semidefinite programs. These conditions, given sufficiently exciting inputs, recover the corresponding model-based Lurye condition in the noiseless setting. The proposed methods are illustrated via a simple example with a sector-bounded nonlinearity. Both proposed methods obtain the same induced-$\ell_2$ gain bound as the model-based approach while using only trajectory data from the nominal system.


## 精读解读（中文）
### 一、研究动机
传统Lurye系统稳定性与性能分析需要标称LTI系统的状态空间模型，但在复杂实际系统中建模困难。本文旨在开发仅利用标称系统轨迹数据（无需完整模型）的数据驱动条件，认证Lurye系统的内部稳定性和诱导ℓ2性能。

### 二、技术方案（Method）
本文针对离散时间Lurye系统提出两个数据驱动条件，均表示为凸半定规划。第一个条件利用标称LTI系统的有限输入、输出和状态轨迹数据，结合满足已知二次约束的非线性，构建Lyapunov/耗散不等式。第二个条件仅使用输入/输出数据，通过确定性子空间辨识技术（如N4SID）从输入输出数据重建状态序列（可达相似变换），然后应用类似第一个条件的半定规划。两个条件在充分激励输入及无噪声设定下恢复对应的基于模型条件，并联合优化存储矩阵、QC矩阵和性能界γ。

### 三、结果（Result）
以一个扇区有界非线性为例，两个数据驱动方法得到的诱导ℓ2增益界与基于模型的方法完全相同，验证了方法在无噪声情况下可复现基于模型的分析结果，且仅使用轨迹数据。

### 四、结论（Conclusion）
本文发展了Lurye系统数据驱动稳定性与性能分析的两个凸条件，分别需要或不需要状态测量。通过子空间辨识克服状态不可测问题，示例验证了方法的有效性并与基于模型方法一致。未来可扩展至有噪声情况、控制器综合等问题。

### 五、方法论与关键技术细节
关键细节：1) 非线性需满足已知二次约束（QC矩阵M）；2) 子空间辨识要求输入充分激励且数据长度足够以保证可观测性；3) 无噪声假设保证数据驱动条件精确恢复基于模型结果；4) 优化为凸半定规划，可联合优化QC矩阵与存储矩阵，以获取最优（最小）诱导ℓ2增益界；5) 局限性包括直接扩展到控制器综合时变非凸、未考虑测量噪声、假设系统可观测且状态可重建（相似变换）。
