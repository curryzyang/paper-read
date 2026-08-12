# A New Approach for Feedback Stabilization and its Application for Data-Driven Control of Polynomial Systems

- 区域：精读区
- 排名：1
- 匹配度：5.8/10
- 来源：arxiv
- 作者：Diego de S. Madeira, Joao Gabriel N. Silva, Wilkley B. Correia, Antonis Papachristodoulou
- 机构：Federal University of Ceará, University of Oxford
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10158v1) · [PDF](https://arxiv.org/pdf/2608.10158v1)

## TLDR
This paper proposes new dissipativity-inspired sufficient conditions for asymptotic state-feedback stabilization of polynomial systems, which enable two iterative sum-of-squares data-driven control design procedures using noisy measurements that avoid the need for control-Lyapunov function initialization or alternating D-K iterations.

## Abstract
Inspired by recent developments in dissipativity-based control, this work proposes new sufficient conditions for asymptotic stabilization of nonlinear systems using state feedback. We prove that this new framework is well suited for data-driven control of polynomial systems using noisy measurements, a topic that has lately attracted considerable attention. Two iterative procedures for data-based state feedback design are provided using the proposed framework, that use sum-of-squares (SOS) optimization. Typical limitations of conventional SOS methods based on alternating (D-K) procedures for controller design, such as the need to provide an initialization for a control-Lyapunov function (CLF), are overcome in this paper. Numerical examples demonstrate the applicability and the advantages of the new strategies.


## 精读解读（中文）
### 一、研究动机
现有基于SOS的数据驱动多项式系统控制方法多依赖D-K交替迭代，需要为控制Lyapunov函数或控制律提供初值，且某些方法还需要预先指定虚构输出；同时经典耗散性框架通常求解满足耗散不等式的控制律集合，难以直接利用带噪数据刻画与候选CLF相容的闭环动力学。本文因此提出新的反馈镇定性充分条件，并面向带噪测量数据建立无需这些初值和先验指定的数据驱动设计框架。

### 二、技术方案（Method）
考虑输入仿射多项式系统dot x=f(x)+g(x)u，在Assumption 1下将未知f,g表示为dot x=A Z(x)+B W(x)u，其中Z,W为已知单项式基，A,B未知。在时间区间内采集输入状态样本以及带噪导数X1=hat X1+D0，并假设D0D0^T<=R_DR_D^T，从而将可行系统集合C表示为矩阵椭球形式。借鉴耗散性控制，提出了确定与候选CLF相容的闭环动力学集合的新充分条件，而非直接求满足耗散不等式的控制律集合。基于该框架给出两个迭代SOS算法：第一个算法每轮计算复杂度较低，论证风格接近鲁棒控制；第二个算法每轮计算更重但通常仅需很少迭代即可获得镇定控制器。两种算法都不采用D-K交替，也无需提供CLF或控制律初值。

### 三、结果（Result）
数值算例表明两种数据驱动SOS策略都能在带噪测量下获得多项式状态反馈镇定控制器并估计吸引域。相比已有基于D-K交替的SOS方法，本文消除了对CLF初始化的依赖；与需要预设虚构输出的迭代耗散方法相比，也无需该先验设定。第一个算法以较低单轮复杂度进行迭代，第二个算法在更少迭代内收敛，二者为实际使用提供了性能与计算复杂度的折中。

### 四、结论（Conclusion）
本文建立了新的反馈镇定性充分条件，并证明其与带噪数据下可行系统的矩阵椭球表示相容，从而为多项式系统的数据驱动镇定提供了系统化框架。所提出的两种迭代SOS策略避免了传统D-K方法的初值难题，拓展了耗散性与鲁棒Lyapunov思想在数据驱动控制中的应用，并为后续研究如降低复杂度、扩大吸引域、输出反馈等奠定了基础。

### 五、方法论与关键技术细节
关键点：1) 数据与假设：只需状态/输入样本及带噪导数，未知扰动D0满足椭球界D0D0^T<=R_DR_D^T；f,g的度数上界已知且Z(0)=0。2) 模型：连续时间输入仿射多项式系统，[A B]未知但可行集可等价表示为矩阵椭球C={(A,B): (Z_AB-xi)^T A (Z_AB-xi)<=Q}。3) 方法：采用SOS优化处理多项式正定/半正定约束；两个迭代算法分别侧重单轮低复杂度与快速收敛；不需要CLF/控制律初始化，也不需要预先指定虚构输出。4) 优势与局限：避免了D-K交替迭代，但条件是充分而非必要；吸引域估计受候选CLF和SOS松弛影响；第二算法单轮计算量较高，第一算法可能需要更多迭代。5) 本文没有对闭环动力学进行参数化。
