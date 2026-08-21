# Classifying Directional Trajectories Near Criticality in the Three-State Majority-Vote Model with Deep Belief Networks and Bidirectional GRUs

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Mauricio A. Valle, Gonzalo A. Ruz
- 机构：Universidad Adolfo Ibáñez
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18235v1) · [PDF](https://arxiv.org/pdf/2608.18235v1)

## TLDR
A hierarchical deep learning pipeline combining a Deep Belief Network for latent snapshot encoding and a Bidirectional GRU for temporal sequence classification can almost perfectly distinguish four directional trajectory types (approach/departure from order/disorder) around criticality in the three-state majority-vote model, enabling real-time detection of dynamical regime shifts.

## Abstract
In this work, we investigate whether the latent representations learned by a Deep Belief Network (DBN) and a Bidirectional Gated Recurrent Unit (Bi-GRU) can discriminate among four dynamically distinct trajectory types in the three-state majority vote model (MV3): approach from disorder, approach from order, departure to disorder, and departure to order. The DBN, pre-trained in an unsupervised manner on static equilibrium samples via a Gaussian-Bernoulli Restricted Boltzmann Machine input layer and architecture $784 \to 4096 \to 225 \to 81$, encodes each lattice snapshot into an 81-dimensional latent vector. A t-SNE analysis of the DBN latent space reveals only partial separation of the four trajectory types, reflecting the fact that a model trained on static configurations cannot fully resolve directional temporal structure. A two-layer Bi-GRU classifier, trained on sequences of DBN-encoded snapshots of length $T = 50$, achieves near-perfect separation of all four trajectory types in its hidden state space, as confirmed by t-SNE visualization on both training and test sets. Furthermore, a sliding-window application of the trained Bi-GRU to continuous MV3 dynamics demonstrates its ability to sense the system's current dynamical regime in real-time. These results establish a principled hierarchical architecture for detecting and classifying critical transitions in agent-based opinion dynamics models.


## 精读解读（中文）
### 一、研究动机
三维多数投票模型（MV3）在临界点附近表现出丰富的非平衡动力学，但现有深度学习研究多基于静态构型或忽略轨迹方向，无法回答系统是接近还是离开临界点、来自有序相还是无序相。为支持对临界转变的早期预警，本文提出用深度信念网络（DBN）与双向GRU（Bi-GRU）的层次架构，对四种方向性轨迹进行分类。

### 二、技术方案（Method）
首先在28×28格点上模拟MV3系统，采用异步蒙特卡洛更新，状态映射为{0.0,0.5,1.0}，并以复数向量定义磁化。然后利用随机化速度生成T=50步的准静态轨迹，覆盖四种模式，其中从临界出发的模式先热化300 MCS，并对每个轨迹进行颜色置换增强。DBN由GB-RBM和两个BB-RBM组成，在静态平衡样本上预训练后固定权重，将每个快照编码为81维潜在向量。最后将编码序列输入两层Bi-GRU分类器进行监督多分类，得到四种轨迹类型的判别表示，并可用滑动窗口实时分类。

### 三、结果（Result）
t-SNE分析显示，DBN潜在空间仅对四种轨迹类型产生部分分离，说明基于静态构型训练的表征无法充分捕捉方向性时间结构；而两层Bi-GRU隐状态空间在训练集和测试集上均实现了近乎完美的分离。滑动窗口实验表明，训练后的Bi-GRU能沿连续MV3轨迹实时感知系统当前所处动力学状态，从而有效区分接近/离开临界点及来源/去向的有序或无序特征。

### 四、结论（Conclusion）
结合无监督表示学习（DBN）与双向时序建模（Bi-GRU）的层次架构，为检测和分类观点动力学模型中的临界转变提供了原则性方案，并可作为临界转变早期预警系统的具体步骤。该工作表明，方向性轨迹信息对理解非平衡临界动力学至关重要，静态快照分析不足以刻画时间演化特征。

### 五、方法论与关键技术细节
关键细节包括：数据规模约60,000个快照，观测临界点p_c≈0.894（理论值0.849），状态归一化为{0.0,0.5,1.0}。DBN架构784→4096→225→81，GB-RBM输入，隐藏单元标准差s=0.5，采用对比散度逐层预训练后权重固定。轨迹长度T=50，随机化相位速度u~U(0.65,0.95)，离开临界的模式需在p_c热化300 MCS；颜色置换增强使训练集扩增三倍。局限在于DBN本身基于静态构型，其潜在表达无法完全解析轨迹方向，必须依赖Bi-GRU的时序建模才能获得清晰分离。
