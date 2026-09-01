# Equivariant Sheaf Neural Networks: Learning Geometric Transport on Graphs

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Alessio Borgi, Mario Severino, Fabrizio Silvestri, Pietro Liò
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28853v1) · [PDF](https://arxiv.org/pdf/2608.28853v1)

## TLDR
The paper introduces Equivariant Sheaf Neural Networks (ESNN), a first-order equivariant graph architecture that learns matrix-valued, direction-dependent edge transport between vector features to model anisotropic geometric interactions while preserving exact Euclidean equivariance, improving performance across dynamics, mesh, point-cloud, and molecular tasks.

## Abstract
Equivariant graph neural networks provide a principled way to model geometric systems, but efficient first-order architectures remain limited in how vector information can be transformed as it moves across a graph. We introduce \textsc{ESNN}, an Equivariant Sheaf Neural Network that enriches this interaction by learning directed, matrix-valued transport between neighboring vector features while preserving exact Euclidean equivariance. Rather than increasing the order of the representation, ESNN keeps scalar and vector features first-order and places the additional geometric flexibility in the edge transport itself. We characterize this transport theoretically, showing that when relative displacement is the only covariant geometric input, every linear $O(n)$-equivariant map decomposes into independent radial and tangential components, while learned covariant features enable richer feature-conditioned transformations. We also introduce controlled symmetry relaxation for systems with a preferred ambient direction, which may be prescribed or inferred from data while recovering full $E(n)$-equivariance when the directional pathway is inactive. Across particle dynamics, mesh-based simulation, point-cloud classification, and molecular property prediction, ESNN improves dynamics prediction, recovers the gravity axis when symmetry is broken, yields substantial gains on selected mesh tasks and long-horizon rollouts, and remains robust to unseen rotations. These results show that learning how geometric information is transported across edges offers a complementary route to expressive equivariant message passing without requiring higher-order representations.


## 精读解读（中文）
### 一、研究动机
现有等变图神经网络虽然能高效建模几何系统，但一阶架构在向量信息跨图传输时的变换方式受限，难以刻画方向依赖的各向异性交互；同时，通用sheaf网络虽支持矩阵值边交互，却未考虑欧氏向量特征的变换律。为此，本文提出在保持一阶标量/向量表示的前提下，通过学习边上的矩阵值传输来增强几何信息的传递，并保持精确的E(n)等变性。

### 二、技术方案（Method）
ESNN将节点特征表示为不变标量s_i和协变向量V_i（n×c_v），在消息传递中为每条有向边学习矩阵值传输，将传输分解为O(n)协变的空间作用S_ij与不变的特征通道混合M_ij。具体实现包括：相对位移r_ij作为唯一协变输入时，线性O(n)等变传输被参数化为独立的径向分量（沿r_ij）和切向分量（垂直r_ij），并允许特征依赖的旋转和各向异性缩放；通过可学习的优选方向向量和松弛系数β控制对称性破缺，β=0时恢复完全E(n)等变，β>0时仅保留保持该方向的子群等变性。训练/推理遵循标准消息传递流程：节点特征经传输、聚合、更新，可堆叠多层。

### 三、结果（Result）
在粒子动力学、网格模拟、点云分类和分子性质预测等任务中，ESNN相比基线改善了动力学预测精度；在对称性破缺的系统中能数据驱动地恢复重力轴方向；在选定的网格任务和长时程rollout上取得显著性能提升，并对未见的旋转保持鲁棒性。理论分析表明，当相对位移是唯一协变几何输入时，径向-切向分解捕获了所有线性O(n)等变传输的完整类。

### 四、结论（Conclusion）
学习几何信息在边上的传输方式，为增强等变消息传递的表达力提供了一条不需高阶表示的互补路径。ESNN通过矩阵值传输在保持一阶特征的同时实现各向异性交互，并通过受控对称性松弛适应有优选方向的物理系统，验证了其在不同几何领域的有效性。

### 五、方法论与关键技术细节
关键实现细节包括：特征表示为一阶标量加向量通道，向量通道数c_v可调；传输矩阵的协变性要求满足S'_{ij}=Q S_{ij} Q^T；在径向-切向分解中，沿相对位移方向与正交方向独立缩放，该形式在仅有相对位移协变输入时是完备的；对称性松弛中的优选方向可作为全局可学习参数，松弛系数β可学习，β=0时精确恢复E(n)等变；实验覆盖多领域，但未报告具体数值指标，且理论完备性仅在相对位移为唯一协变输入时成立，对更丰富协变输入的情况依赖学习到的特征条件变换。
