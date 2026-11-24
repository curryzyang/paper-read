# Algebraic Observability for Power System Dynamic State Estimation

- 区域：精读区
- 排名：8
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Akhila Kandivalasa, Marcos Netto
- 机构：New Jersey Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28305v1) · [PDF](https://arxiv.org/pdf/2611.28305v1)

## TLDR
This paper proposes a scalable algebraic observability framework that tests power system dynamic state estimation directly on nonlinear differential-algebraic equation models—without Kron reduction—using a Jacobian rank test with reduced prolongation, and connects it to hyper-regularity and local observability while demonstrating it on standard power system test cases.

## Abstract
Existing observability methods for dynamic state estimation are developed for ordinary differential equation (ODE) models, whereas power systems are naturally described by differential-algebraic equations (DAEs). Applying these methods generally requires a DAE-to-ODE transformation, usually Kron reduction, which may obscure the role of algebraic variables and network constraints. This paper presents an algebraic observability framework that operates directly on nonlinear power system DAEs and preserves their structure. A Jacobian rank test constructed from the model relations and their successive derivatives certifies the algebraic dependence of differential and algebraic variables on the known inputs and measurements. A reduced prolongation that differentiates only the stator relations keeps the number of latent indeterminates fixed as the prolongation order grows, which makes the test scalable. We establish the relationship between this rank test and hyper-regularity, an alternative framework for algebraic observability, and show that algebraic observability relates to local observability. We demonstrate algebraic observability on a single-machine decentralized setup, the WSCC 9-bus 3-machine system, and the IEEE 39-bus 10-machine system. The 39-bus test, with 257 latent indeterminates, completes in about 30 s.


## 精读解读（中文）
### 一、研究动机
现有动态状态估计的可观测性方法主要针对ODE模型，而电力系统天然由DAE描述；通常需先做Kron reduction等DAE-to-ODE变换，这会掩盖代数变量和网络约束的作用并破坏稀疏结构。因此需要一种不依赖变换、直接在非线性电力系统DAE上判定可观测性的框架。

### 二、技术方案（Method）
本文基于Diop-Fliess微分代数可观测性理论，将系统变量划分为已知变量w（输入与量测）和潜变量ℓ（未测状态及未测代数变量），通过模型关系及其有限阶时间导数构造Jacobian秩检验，以判定ℓ是否代数依赖于w。为使检验可扩展，作者将转子角、母线电压角和电流相量角替换为正余弦对并由单位圆约束联系，形成微分多项式DAE模型；同时采用仅对定子关系求导的约化延拓，并利用电机方程消去高阶导数，使每台电机的潜变量数保持固定。文中还建立该秩检验与Sato超正则性框架的等价关系，并说明其与局部可观测性的联系。

### 三、结果（Result）
在单机分散式设置、WSCC 9-bus 3-machine系统和IEEE 39-bus 10-machine系统上验证了所提代数可观测性方法，全程无需Kron reduction。IEEE 39-bus系统含257个潜变量，秩检验约30秒完成；相比之下，Lie导数法在仅21个状态的Kron约化WSCC模型上约需2小时。

### 四、结论（Conclusion）
该框架可直接在保留网络约束和代数变量的电力系统DAE上联合判定微分变量与代数变量的可观测性，避免了DAE-to-ODE变换带来的结构失真。由于代数可观测性与超正则性等价，通过秩检验还可在正则轨迹上推出非线性DAE的局部可观测性，为动态状态估计提供可扩展的前置分析工具。

### 五、方法论与关键技术细节
方法针对半显式index-1 DAE，要求∂g/∂y局部非奇异，并在正则轨迹条件下讨论局部可观测性；核心检验是有限阶延拓后Jacobian的列满秩。微分多项式化通过正余弦变量和单位圆约束处理角度非线性，约化延拓只对定子关系求导，并通过电机方程消去高阶导数，从而将每台电机的潜变量数固定为17。关键优势是无需Kron reduction且计算可扩展，39-bus、257个潜变量的算例约30秒完成；局限在于结论依赖模型正则性与局部微分代数条件，主要给出可观测性判定而非估计器设计。
