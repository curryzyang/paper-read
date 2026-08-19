# Randomly initialized autoencoders: fixed points and edge-of-chaos

- 区域：精读区
- 排名：6
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Leonid Berlyand, Roman Sarapin, Yitzchak Shmalo, Victor Slavin, Sasha Sodin
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14638v1) · [PDF](https://arxiv.org/pdf/2608.14638v1)

## TLDR
Randomly initialized autoencoders are analyzed via fixed-point existence, stability, and basins of attraction, introducing local and global edge-of-chaos regimes characterized using random matrix theory and Sudakov–Fernique inequality.

## Abstract
In this paper we study autoencoders, a special class of deep neural nets (DNNs) whose performance can be characterized via their fixed points. This perspective naturally raises questions of existence, stability, and basins of attraction of these fixed points. These questions are addressed via the contractive properties of autoencoders, and are closely related to the notion of edge-of-chaos.
  Edge-of-chaos (EoC) is an important notion in the theory of DNNs. It describes the critical regime separating ordered and chaotic signal propagation through a randomly initialized network. Initialization at or near this critical regime offers several theoretical and practical advantages, including stability of the network w.r.t. perturbations of the input. EoC was previously introduced for broad classes of neural networks using mean-field averaging methods. In this paper we modify the notion of EoC for the study of autoencoders. Specifically, we introduce local and global EoC for autoencoders that control local (small) and global (arbitrary) perturbations of the input respectively.
  The study of stability of autoencoders falls within the scope of nonlinear problems in Random Matrix Theory (RMT). Our analysis of local EoC is based on spectral techniques of RMT, whereas global EoC is studied by employing Sudakov-Fernique inequality for Gaussian processes.


## 精读解读（中文）
### 一、研究动机
自编码器作为深度学习网络，其性能可通过固定点刻画，但随机初始化下固定点的存在性、稳定性与吸引域尚不清楚。本文旨在通过自编码器的收缩性质，引入适用于自编码器的边沿混沌（EoC）概念，从而确定随机初始化方差的临界值，以指导初始化设计。

### 二、技术方案（Method）
本文建立理论分析框架：考虑L层全连接自编码器，输入输出维度为N，隐藏层宽度n_k满足cN≤n_k≤CN，权重矩阵元素独立同分布服从N(0,σ²/n_k)，偏置服从N(0,σ̃²)，激活函数为ReLU（α=0）或LeakyReLU（0≤α<1）。定义输入-输出雅可比矩阵J，通过随机矩阵理论（RMT）谱技术分析其算子范数的对数增长率，研究局部EoC；对全局EoC，采用Sudakov-Fernique不等式处理高斯过程，得到自编码器在整个R^N上为收缩映射的概率下界。关键步骤包括推导雅可比矩阵奇异值极限、建立临界方差条件、构造一致概率界。

### 三、结果（Result）
定理1证明：在ReLU、层宽比例存在极限的条件下，对任意输入s，几乎必然有(1/L)log||J|| → 1/2 log(σ²/2)，由此得到局部EoC临界值σ²_{L,crit,loc}趋于2，与标准DNN的σ²_crit=2一致，且σ²_{L,crit,loc}≤σ²_crit。定理2给出无偏置情况下，对于任意α∈[0,1)，存在显式常数β_α^(L)，使得当σ²适当小时，自编码器在整个输入空间上以至少1-exp(-cNL)的概率成为收缩映射，从而保证固定点的全局存在性与吸引域。

### 四、结论（Conclusion）
本文为自编码器定义了局部与全局边沿混沌，将随机初始化方差与固定点稳定性联系起来。结果表明，ReLU自编码器的局部EoC临界方差为2，与经典网络吻合；而全局EoC通过Sudakov-Fernique不等式提供了高概率收缩条件。这些理论发现为自编码器的随机初始化设计提供了依据，有助于确保非线性降维中固定点的存在性和稳定性。

### 五、方法论与关键技术细节
关键细节包括：权重初始化N(0,σ²/n_k)且无偏置是全局结果的前提；局部定理要求α=0（ReLU）且隐藏层宽度极限存在；全局定理允许任意LeakyReLU但要求σ̃²=0。定理2中的β_α^(L)显式依赖于层宽比例c_k和α，用于界定收缩概率。局部EoC与标准EoC之间存在不等式σ²_{L,crit,loc}≤σ²_crit，并在大L时相等。局限性在于该研究仅针对随机初始化，未涉及训练过程；全局收缩条件要求无偏置，且结果以概率形式给出，未刻画数据流形上的行为。
