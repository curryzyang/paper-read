# Structure-preserving uncertainty quantification for GENERIC dynamics

- 区域：精读区
- 排名：1
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Zequn He, Celia Reina
- 机构：University of Pennsylvania
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12624v1) · [PDF](https://arxiv.org/pdf/2608.12624v1)

## TLDR
S-PENNs extend epistemic neural networks to hard-constrained GENERIC dynamics, attaching lightweight epinets to each building block to ensure thermodynamically consistent, physically admissible uncertainty realizations and calibrated prediction intervals at 1–3 orders of magnitude lower cost than deep ensembles.

## Abstract
Structure-preserving machine learning embeds physical structure directly into model architectures, yet uncertainty quantification (UQ) for such hard-constrained models remains limited because standard UQ methods may violate the encoded admissibility conditions, require architectural modifications, or impose substantial computational costs. In this work, we propose Structure-Preserving Epistemic Neural Networks (S-PENNs), a general framework for UQ in scientific machine learning models with hard architectural constraints, and instantiate it for GENERIC (General Equation for Non-Equilibrium Reversible-Irreversible Coupling) dynamics. S-PENNs preserve the structural constraints of a pretrained model by attaching lightweight epinets to its constrained components, ensuring that every sampled realization remains physically admissible by construction. When applied to GENERIC dynamics, such a proposed framework yields thermodynamically consistent rollouts that preserve the first and second laws. Furthermore, we combine S-PENNs with split conformal prediction as a post-hoc calibration method to produce prediction intervals with finite-sample marginal coverage guarantees. We validate S-PENNs on three numerical examples: a harmonic oscillator coupled to a heat bath and an idealized chemical motor, both governed by ODEs, and a one-dimensional viscoplastic model governed by PDEs. Across all three examples, S-PENNs produce thermodynamically consistent stochastic realizations and well-calibrated prediction intervals while reducing the computational cost by about one to three orders of magnitude compared to deep ensembles. Although the present study focuses on GENERIC dynamics, S-PENNs can be extended more broadly to scientific machine learning models in computational mechanics with either hard or soft constraints.


## 精读解读（中文）
### 一、研究动机
结构保持机器学习通过架构硬编码物理结构，但此类硬约束模型的不确定性量化仍受限：标准UQ方法可能破坏可容许性条件、需要修改架构或带来高昂计算成本。现有UQ方法多针对软约束或物理正则化代理，难以在每次采样实现中同时满足多个耦合的约束条件，因此需要一种能在结构保持模型内部注入不确定性且不违反物理约束的通用框架。

### 二、技术方案（Method）
提出结构保持认知神经网络（S-PENNs），以预训练的GENERIC动力学模型（N-GENNs）为基础网络，对其每个受约束的构建块（能量E、熵S、泊松算子L、耗散势Ξ）分别附加轻量epinet。每个epinet继承对应构建块的架构属性，以该块的stop-gradient特征和相同输入为条件，并通过共享的epistemic index耦合各块扰动；扰动后的构建块经N-GENNs相同的结构保持重参数化组装，从而保证每个采样实现都满足退化条件、反对称性和凸性等热力学约束。训练时结合split conformal prediction作为后处理校准，以获得具有有限样本边际覆盖保证的预测区间。

### 三、结果（Result）
在三个数值算例（耦合热浴的谐波振荡器、理想化学马达的ODE系统，以及一维粘塑性PDE模型）中，S-PENNs均产生热力学一致的随机实现和良好校准的预测区间，同时与深度集成相比将训练计算成本降低约1至3个数量级。

### 四、结论（Conclusion）
S-PENNs为具有硬约束的科学机器学习模型提供了一种通用的不确定性量化框架，在GENERIC动力学上展示了保持热力学第一、第二定律的随机展开和可靠预测区间。该方法可推广到计算力学中具有硬约束或软约束的更广泛科学机器学习模型，为结构保持模型的不确定性量化提供了实用且高效的解决方案。

### 五、方法论与关键技术细节
关键细节包括：针对全局（与输入无关）参数专门设计了epinet构造，通过架构强制输入独立性，无需软惩罚方差项；split conformal prediction提供分布无关的有限样本边际覆盖保证；N-GENNs基础通过反对称矩阵Q_S实现可逆退化条件，通过投影矩阵P_E和凸耗散势PICNN实现不可逆退化条件；共享epistemic index确保跨模块扰动一致传播；局限性是当前工作聚焦GENERIC动力学，但框架可扩展至其他硬/软约束模型。
