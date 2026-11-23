# Connectivity-Constrained Linear System Realization: Feasibility and Realizable Sets

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Yaozhi Du, Jing Shuang, Li
- 机构：University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26811v1) · [PDF](https://arxiv.org/pdf/2611.26811v1)

## TLDR
This paper shows that finding a state-space realization of a transfer function under an arbitrary connectivity pattern is equivalent to solving multivariate polynomial equations and can be solved exactly using algebraic geometry, while also proving the surprising dichotomy that any connectivity pattern can realize either nearly all transfer functions or very few.

## Abstract
In this paper, we first study the problem of finding a state-space realization of a given transfer function that adheres to a given connectivity pattern (i.e., support). While variants of this problem have been studied in distributed and structured control, existing work typically focuses on connectivity patterns relating to some networked plant. In contrast, we are interested in arbitrary connectivity patterns, which are relevant to modeling problems in sensorimotor neuroscience. We show that this problem is equivalent to solving a system of multivariate polynomial equations, and can be solved exactly without relaxation or approximation. We then study the reverse problem: given a connectivity pattern, what transfer functions have a state-space realization that adheres to this pattern? In other words, what transfer functions can this pattern realize? A surprising finding is that any given pattern can realize nearly all transfer functions, or very few transfer functions. We provide rigorous results and algorithms for both problems, leveraging technical machinery from algebraic geometry. The efficacy of our approach is demonstrated in examples at the end of the paper.


## 精读解读（中文）
### 一、研究动机
论文关注线性控制器或线性动力学系统在任意给定连接模式（支撑集）上的状态空间实现问题，动机来自感觉运动神经科学中神经动力学需在解剖约束的稀疏连接下实现控制计算。与分布式/结构化控制通常要求控制器连接模式与网络化被控对象相关不同，本文允许连接模式完全任意，并进一步研究反向问题：一个连接模式究竟能实现哪些传递函数。

### 二、技术方案（Method）
输入为传递函数矩阵K与支撑S=(A,B,C,D)，先利用最小实现的相似变换不变性，将寻找满足支撑的实现转化为寻找可逆变换T，使T^{-1}AT、T^{-1}B、CT满足给定稀疏支撑；D=lim_{s→∞}K在所有最小实现中固定，故先检查D与D支撑兼容，再分析严格真部分。将支撑约束展开为关于T元素的多元多项式方程组，并用初等置换、行相加和非零缩放矩阵参数化T，从而在复数域/实数域上精确求解，不采用松弛或近似。反向问题则把可实现传递函数视为实现映射的像集，借助代数几何中的消元、投影与维数分析刻画给定支撑的可实现集，并给出判定其是否能实现“几乎全体”传递函数的必要充分条件与算法。

### 三、结果（Result）
论文证明连接约束可实现性等价于多元多项式方程组可解性，并给出复数与实数实现的存在性必要充分条件及对应精确算法；对反向问题发现给定支撑的可实现集呈现二分现象：要么能实现几乎全体传递函数，要么只能实现非常少的传递函数。进一步给出判定一个支撑是否“泛型可实现”的必要充分条件和算法，并通过示例验证方法有效性。

### 四、结论（Conclusion）
该工作将任意连接模式下的线性系统实现问题统一到代数几何框架中，既能精确判定和构造给定传递函数的连接约束实现，也能刻画连接模式本身的可实现能力。其核心结论表明连接约束对可实现传递函数集合的影响具有强二分性，为神经科学建模和结构化控制中的稀疏实现分析提供了严格工具。

### 五、方法论与关键技术细节
关键假设包括仅考虑无零极点相消的最小实现，且D必须满足支撑约束，否则不可实现；实值实现要求相似变换T为实可逆矩阵。技术上利用最小实现间相似变换、初等矩阵参数化、多元多项式方程组、Gröbner基/消元与代数簇维数等代数几何工具；复杂度主要随状态维数、支撑稀疏度和多项式系统规模增长，精确求解可能在大规模问题上昂贵。局限在于聚焦线性、因果、最小实现，连接模式为二进制支撑而非幅值约束，未直接处理噪声、非线性或非最小实现。
