# From Atoms to Entropy: Optimal Noise Allocation for Diffusion Training in the Convex Regime

- 区域：精读区
- 排名：8
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Luca Ambrogioni, Giulio Franzese, Alberto Foresti, Gabriel Raya, Bac Nguyen, Georgios Batzolis, Yuhta Takida, Naoki Murata, Chieh-Hsin Lai, Yuki Mitsufuji
- 机构：Sony Group Corporation, University of Cambridge, EURECOM, Tilburg University & JADS, Sony AI, Radboud University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20540v1) · [PDF](https://arxiv.org/pdf/2607.20540v1)

## TLDR
This paper develops a theoretical framework showing that optimal noise schedules for diffusion training are atomic (concentrated on finitely many levels) under convexity assumptions, and simplify to a square-root entropy rate schedule under a decoupled regime, with experimental validation.

## Abstract
How should a diffusion model decide which noise levels to train on, and how much? Despite the importance of this choice, current noise schedules are based largely on heuristics or empirical tuning. Here, we develop a general statistical framework for studying asymptotically optimal noise-level allocation in diffusion training. Our first main result concerns the fully coupled regime, where information can spread between different time points. Under convexity or Polyak-Lojasiewicz-type assumptions, we show that the optimized training schedule admits an atomic minimizer, concentrated on finitely many noise levels. Our second main result specializes this framework to an idealized independent-learner regime, intended to model temporal specialization in neural networks. Under an additional feature-noise decoupling condition, a random-matrix analysis leads to an information-theoretic proxy: the decoupled sampling density is proportional to the square root of the generative entropy rate, the rate at which conditional entropy grows along the forward process. We test these predictions in controlled settings where the coupled objective can be optimized directly, including Dirac mixtures, low-dimensional manifolds, and MNIST. In these settings, the optimized schedules are consistently finite-support, while the smooth entropic proxy closely tracks the atomic optimum in neural-network models and breaks down mainly in the fully coupled parametric case, as the theory suggests. We then evaluate the entropic schedule in larger-scale experiments, where full schedule optimization is currently intractable. The results indicate that square-root entropy scheduling can substantially improve training efficiency on discrete domains and remains competitive with standard EDM-style heuristics on continuous images.


## 精读解读（中文）
### 一、研究动机
当前扩散模型的噪声调度主要基于启发式方法或经验调参，缺乏统一的理论框架来理解为何某些调度有效而其他调度显著次优。本文旨在建立一个统计框架，从理论上研究扩散训练中渐近最优的噪声分配，揭示最优调度的结构并为实际调度设计提供指导。

### 二、技术方案（Method）
将训练调度建模为噪声水平上的概率测度，优化ELBO加权的渐近期望预测误差。在凸性或Polyak–Łojasiewicz假设下，利用流式SGD的渐近分析导出预测误差与调度测度的显式关系。通过谱分解和随机矩阵分析，分别在耦合（特征共享）和去耦（时间特化）场景中获得理论结果：耦合场景下最优调度是有限个狄拉克原子的混合；去耦场景下在特征-噪声解耦条件下得到闭式解，即采样密度正比于生成熵率的平方根。在受控实验（狄拉克混合、低维流形、MNIST）中直接优化耦合目标验证原子性，并在大规模实验（离散域和连续图像）中评估熵调度。

### 三、结果（Result）
在受控设置中，优化后的调度始终支持在有限个噪声水平上（原子性），而平滑的熵代理在神经网络模型中紧密跟踪原子最优，但在完全耦合参数情形下失效，符合理论预测。在大规模实验中，平方根熵调度在离散域上显著提升训练效率，在连续图像上与EDM启发式调度具有竞争力但仍略逊。

### 四、结论（Conclusion）
扩散训练中的最优噪声分配具有原子结构（耦合场景）或可由生成熵率平方根近似（去耦场景），前者提供了理论表征，后者给出了可解释且实用的调度公式。该理论为噪声调度的设计提供了统计学习基础，并支持熵调度作为实际深度学习中的有效启发式方法。

### 五、方法论与关键技术细节
假设包括损失函数在最优解附近的凸性或Polyak–Łojasiewicz条件、流式SGD的渐近均衡以及冻结特征（lazy/NTK）局部线性化。关键先验是特征-噪声解耦条件用于导出平方根熵调度。损失采用加权平方预测误差，权重由SNR导数给定。超参数涉及总采样预算K的渐近极限以及时间T的选择。复杂度方面，原子调度能显著减少需优化的噪声水平数量，但位置需由数据驱动确定；局限性在于理论限于凸区域和特定假设，实际深度学习中调度优化仍不透明，且熵调度在强耦合时次优。
