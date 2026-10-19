# Learning smooth dynamics via Kinematic Interpolants

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Yiheng, Jiang, Youssef Marzouk, Avishek Joey Bose, Aram-Alexandre Pooladian
- 机构：Yale University, Mila, Imperial College London, Massachusetts Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22519v1) · [PDF](https://arxiv.org/pdf/2610.22519v1)

## TLDR
Kinematic Interpolants (KI) extend stochastic interpolants to learn smooth second-order dynamics from multiple position–velocity snapshots in phase space, enabling simulation-free, scalable training and more accurate reconstruction of underlying dynamics than existing baselines at a fraction of the training time.

## Abstract
Inferring dynamics from real-world experimental data is inherently ambiguous, as many plausible dynamical systems can explain the same positional observations at measurement times. For higher fidelity modeling of applications ranging from single-cell RNA to vortex dynamics and even flocking of birds, scientific observables increasingly also include velocity estimates that serve to resolve this issue. However, incorporating this rich information in a scalable manner, free of simulation or unnecessary approximations, has remained a difficult challenge. In this paper, we introduce Kinematic Interpolants (KI), a novel framework that extends the seminal methodology of stochastic interpolants to infer nonlinear dynamics across multiple snapshots in phase space, i.e., observables with position and velocity measurements. Empirically, we demonstrate that across several scientific datasets, KI achieves superior reconstruction of the underlying dynamics compared to existing baselines while requiring only a fraction of the training time.


## 精读解读（中文）
### 一、研究动机
从群体快照推断动力学时，仅凭测量时刻的位置观测往往存在多解，旋转对称等系统尤其难以辨识；速度观测能提供额外约束，但现有方法常需昂贵模拟、预填缺失速度或构建参考场，难以可扩展地纳入二阶概率建模。本文旨在直接从位置-速度快照学习平滑非线性动力学。

### 二、技术方案（Method）
将各观测时刻的位置-速度联合分布视为相空间边缘分布，选取多边缘耦合，并在相邻快照间构造相空间插值：位置写为 I_t 加噪声项 G_tξ，速度强制为位置的时间导数，且插值与噪声在端点满足位置、速度及零噪声约束。对插值速度再求时间导数得到闭式加速度目标，以条件期望加速度场 a_t(x,v)=E[加速度|X=x,V=v] 为学习对象，用神经网络做回归训练；采样时求解二阶动力学 dx=v dt、dv=a_t(x,v)dt，也可引入扩散并用学习的速度得分修正漂移以支持随机采样。

### 三、结果（Result）
在多个科学数据集上，KI 对底层动力学的重建精度优于现有基线，同时训练时间仅为基线的一小部分；学习到的过程还能在中间时刻生成一致的位置-速度联合样本。结果支持其在不同噪声调度和确定性/随机采样设置下有效。

### 四、结论（Conclusion）
KI 将随机插值推广到相空间并直接学习加速度场，实现了无需轨迹模拟、无需预填速度、无需参考场的 simulation-free 二阶动力学推断，为带速度观测的轨迹推断提供了更准确且高效的建模范式。

### 五、方法论与关键技术细节
关键实现点包括多边缘耦合与插值函数、噪声调度的选择，端点位置/速度及噪声导数约束，以及由插值二阶导得到的闭式加速度回归目标；条件均值加速度保证插值路径的单时刻边缘被保持，随机采样还需学习速度得分并用扩散系数修正漂移。局限在于方法依赖速度观测质量与充分平滑假设，跨快照无个体配对，耦合、插值和噪声设计会影响性能，高维场景下得分学习与二阶建模的计算和稳定性仍需关注。
