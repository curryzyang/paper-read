# Data-Driven Learning of Unknown Nonlinear Differential Equations Using Functional Analysis

- 区域：精读区
- 排名：3
- 匹配度：5.6/10
- 来源：arxiv
- 作者：Seyyed Shaho Alaviani, Yongzhi Qu, Gregory W. Vogl
- 机构：National Institute of Standards and Technology, University of Minnesota-Twin Cities, University of Utah
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04329v1) · [PDF](https://arxiv.org/pdf/2609.04329v1)

## TLDR
This paper recasts data-driven discovery of nonlinear ODEs by proposing an interpretable machine learning method, FINS, that uses functional analysis and an integral-based cost in function space to learn unknown vector fields—and even external forcing—from a single state trajectory, with an incremental algorithm for online learning across autonomous, non-autonomous, forced, and unforced systems.

## Abstract
In this paper, the problem of data-driven discovery of nonlinear ordinary differential equations (ODEs) is recast, and a new interpretable machine learning (ML) method is proposed. The proposed method aims to learn the unknown vector field of nonlinear dynamics without prior knowledge of the system's physics from only one single state trajectory's data. The proposed method has two fundamental differences with existing methods: 1) the formulation presented in this method is derived based on Functional Analysis and Operator Theory, and 2) the cost function is constructed in the function space as a distance between two functions as an integral, instead of the discrete-sum of errors used in existing ML approaches. An incremental learning algorithm is proposed to learn the unknown vector field to handle new training samples in an online manner. The proposed method can discover the unknown vector field from both forced and unforced autonomous and non-autonomous (or time-varying) dynamical systems. The proposed method is able to simultaneously discover unknown external forces as a function of time and unknown underlying dynamics. Finally, numerical examples are given to demonstrate the advantages of the proposed method.


## 精读解读（中文）
### 一、研究动机
现有数据驱动微分方程发现方法多为黑箱模型，依赖离散误差之和，通常需要大量轨迹数据、数值微分或内嵌ODE求解器，难以处理在线增量学习，也无法在统一框架下同时辨识未知外力与底层动态。因此，本文提出一种基于泛函分析与算子理论的可解释机器学习方法FINS，旨在仅利用单条状态轨迹数据、无需系统物理先验即可学习非线性ODE的未知向量场，并支持受迫及非自治系统。

### 二、技术方案（Method）
FINS将非线性ODE的向量场辨识重新表述为函数空间中的优化问题。输入为单条状态轨迹或输入-状态轨迹数据（允许零或非零初始条件）。建模时利用Hammerstein算子与Hermite多项式等泛函分析工具，将未知向量场表示为有限阶多项式基的线性组合。代价函数定义为两个函数在函数空间中的积分距离，即对时间区间上的函数误差进行积分，并采用梯形法则直接计算该积分误差，从而避免在训练循环中调用ODE求解器。训练过程通过最小化积分误差求解基系数；进一步提出增量学习算法，使模型能在线逐样本更新参数，适应新到达的训练数据，同时适用于自治/非自治以及受迫/不受迫系统，且能同时辨识作为时间函数的未知外力项和状态相关的动力学项。

### 三、结果（Result）
数值算例表明，FINS方法仅凭单条状态轨迹（或输入-状态轨迹）数据即可有效辨识未知非线性向量场，无需任何物理先验。相比依赖离散误差和或ODE求解器的现有方法（如SINDy、神经ODE等），FINS在单一轨迹前提下能够同时发现时变外力与自治动态，且无需求解初值问题或进行数值微分，展示出良好的可解释性和在线学习能力。

### 四、结论（Conclusion）
本文通过泛函分析与算子理论重新构建了非线性ODE的数据驱动发现框架，以积分型代价函数替代离散误差和，并引入增量学习，提供了可解释、初始化无关且无需ODE求解器的学习方案。该方法对自治/非自治、受迫/不受迫系统均适用，为复杂系统建模和数字孪生提供了新思路，但其主要局限是要求完整状态或输入-状态测量，无法仅从输入-输出数据辨识向量场。

### 五、方法论与关键技术细节
关键实现细节包括：数据仅需一条完整状态轨迹或输入-状态轨迹，初始条件可为零或非零；向量场假设可用有限阶多项式表示，适用于HIV、昼夜节律、种群动态等系统；代价函数为函数空间中的积分距离，采用梯形法进行数值积分；方法基于算子理论但无需显式算子求解；增量学习算法能在线处理新样本；不依赖神经网络、符号回归或ODE求解器；限制是要求全状态可测，且多项式表示能力决定了可学习的动力学复杂度；对神经算子类方法而言，单条轨迹不足以训练，而FINS专为此场景设计。
