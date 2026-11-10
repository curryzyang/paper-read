# All roads lead to Markov kernel networks: A representation theorem for discretization-stable learning

- 区域：精读区
- 排名：1
- 匹配度：5.7/10
- 来源：arxiv
- 作者：S David Mis, Trevor Teolis, Ivan Dokmanić, Matti Lassas, Maarten V. de Hoop
- 机构：Rice University, University of Helsinki, University of Basel
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10051v1) · [PDF](https://arxiv.org/pdf/2611.10051v1)

## TLDR
The paper proves that all uniformly discretization-stable operators can be represented exactly as stable Markov kernel networks—a general architecture subsuming transformers, Fourier neural operators, and Flowers—and provides a variational framework for systematically designing such discretization-stable architectures.

## Abstract
Operator learning seeks to approximate function-to-function maps in a way that remains stable when the input discretization changes, a property sometimes called "discretization invariance". We consider a quantitative refinement of this idea, called $\textit{uniform discretization stability}$, which builds on a common representation of input functions and their discretizations as probability measures and provides a Hölder bound relating output changes to the Wasserstein distance between these measures. Our main result is a representation theorem showing all uniformly discretization stable operators can be written exactly as a $\textit{stable Markov kernel network}$---an abstract architecture that is a joint generalization of transformers, Fourier neural operators (FNO), Flowers, and other successful learned operators. Our representation theorem characterizes a design space for discretization-stable operator learning; designing new architectures becomes a question of which parts of a Markov kernel network to parameterize, and how. We further show that the read kernels of these networks can be realized as solutions of regularized variational problems, with particular choices of costs and regularizers recovering the kernels of transformers, FNO, Flowers, their hybrids, and beyond. This variational formulation provides a systematic approach to architecture design, together with sufficient conditions for uniform discretization stability.


## 精读解读（中文）
### 一、研究动机
算子学习需要逼近函数到函数的映射，并在输入离散化改变时保持稳定；仅有离散化细化下的收敛还不够，训练后的网络需要定量的稳定性保证。论文因此提出统一的概率测度视角，将连续输入函数与含噪离散样本都表示为图测度，并用关于 Wasserstein 距离的 Hölder 界刻画称为一致离散化稳定性的性质。其目标是回答哪些稳定性性质 relevant、哪些架构满足这些性质、以及如何系统刻画并探索这类架构的设计空间。

### 二、技术方案（Method）
论文将紧度量空间上的函数 f 与其图测度 gamma_f 等同，将有限样本或含噪样本表示为 Dirac 混合测度 mu，并把算子学习视为从图测度到输出函数的映射；一致离散化稳定性要求输出变化受输入图测度间 Wasserstein 距离的 Hölder 界控制。核心建模对象是稳定 Markov 核网络，它交替使用由 Markov 核构成的非线性积分算子进行空间信息混合，以及逐点的通道混合算子进行嵌入空间信息混合。主定理通过构造性表示证明任一一致离散化稳定算子都可精确写成稳定 Markov 核网络；进一步将读出核刻画为正则化变分问题的解，通过选择代价函数与正则项获得 transformer、FNO、Flowers 及其混合架构的核，并给出保证一致离散化稳定性的充分条件。该工作以理论构造为主，不涉及端到端训练算法；推理时网络接收经验图测度并在任意空间点上输出函数值。

### 三、结果（Result）
核心结果是表示定理：一致离散化稳定算子类与稳定 Markov 核网络类精确等价，而非近似等价；只要各组件满足相应稳定性，整个 Markov 核网络即具有一致离散化稳定性。变分刻画表明，特定代价与正则项可恢复 transformer 注意力、FNO、Flowers 及其混合形式的读出核，从而把新架构设计转化为选择 Markov 核网络中被参数化的部分以及参数化方式。论文还给出变分定义核的稳定性界和 Markov 核网络的通用逼近结果，提供了可复现的架构对应关系与充分条件，但未报告数值基准指标。

### 四、结论（Conclusion）
Markov 核网络为离散化稳定算子学习提供了自然且由表示定理固定的设计空间，使架构设计从经验拼装转为在统一抽象结构内选择参数化位置与变分正则化方式。该框架统一解释了 transformer、FNO、Flowers 等成功算子网络，并为自适应、混合及面向智能体的算子学习提供原则性设计语言。其理论价值在于把离散化与测量噪声误差纳入同一稳定性分析，并为系统探索新架构给出充分条件。

### 五、方法论与关键技术细节
关键实现细节包括将函数嵌入图空间上的 Radon 概率测度，使用 Wasserstein 距离与 Hölder 指数定义稳定性，并要求空间紧、输出集紧凸、基准测度支撑全空间等正则性条件。Markov 核网络的稳定化依赖空间混合核与通道混合算子的联合约束；变分读出核需要选择代价函数、正则项及相应参数，并通过充分条件验证稳定性。局限性在于表示定理是抽象存在性与精确表示，未直接给出有限样本训练、参数估计误差或计算复杂度的实用保证；变分问题可能仍需额外求解与近似，实际架构设计还需在表达能力、计算成本与稳定性条件之间权衡。
