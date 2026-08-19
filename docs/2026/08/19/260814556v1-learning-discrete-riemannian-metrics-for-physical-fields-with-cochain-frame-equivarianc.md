# Learning Discrete Riemannian Metrics for Physical Fields with Cochain-Frame Equivarianc

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Dongzhe Zheng, Christine Allen-Blanchette
- 机构：Princeton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14556v1) · [PDF](https://arxiv.org/pdf/2608.14556v1)

## TLDR
RHMP introduces Riemannian Hodge Message Passing, an architecture that fixes topological coboundaries and learns discrete Riemannian cochain metrics to enforce exact conservation laws and cochain-frame equivariance, achieving state-of-the-art performance across seven physical benchmarks.

## Abstract
Physical fields on meshes require a separation between topology and geometry: conservation laws are topological and should be exact, while geometry, material response, and anisotropic coupling must be learned from data. Existing neural surrogates often mix these roles inside unconstrained message passing. We introduce Riemannian Hodge Message Passing (RHMP), which turns this separation into an architectural principle. RHMP fixes the cellular coboundaries ($d_k$) determined by oriented incidence and learns symmetric positive-definite cochain metrics ($H_k$) for geometry-dependent propagation. Treating $H_k$ as the learned metric motivates cochain-frame equivariance: physical propagation should be invariant to orthogonal changes of the hidden cochain feature basis. RHMP implements this principle with metric-weighted Hodge blocks ($d_k^\top H_{k+1}d_k$), yielding exact cochain-complex identities ($d_{k+1}d_k=0$), nonnegative Hodge energies, positive-semidefinite operators, and exact Abelian curvature invariance. Across seven physical benchmarks spanning fluids, electromagnetism, gauge fields, and variable-mesh CFD, RHMP achieves the best overall performance, with the largest gains when topology, learned geometry, and field structure interact.


## 精读解读（中文）
### 一、研究动机
网格上的物理场往往被不加区分地编码为节点特征，现有神经代理在消息传递中混同了拓扑守恒律与几何/材料响应。该工作提出应将拓扑与几何分离：守恒律由组合结构决定且必须精确，而几何、材料和各向异性耦合应从数据中学习。

### 二、技术方案（Method）
提出黎曼Hodge消息传递(RHMP)。输入为网格上的物理场，按物理类型分配到0/1/2-上链特征；固定由定向关联决定的胞腔上边界算子d_k，不学习d_k。从关于通道帧O(C)不变的统计量（如特征范数和内积）预测SPD上链度量H_k，并用度量加权Hodge块d_k^T H_{k+1} d_k和d_{k-1}H_{k-1}^{↓}d_{k-1}^T构造Hodge消息算子；配合范数门控非线性保持上链帧等变，最后用不变/等变读出得到标量或向量场预测。训练采用监督回归/分类损失端到端优化H_k参数。

### 三、结果（Result）
在覆盖流体、电磁学、阿贝尔/非阿贝尔规范场以及逐样本可变网格CFD的七个物理基准上，RHMP取得总体最佳性能；相对于图网络、胞腔复形网络、流形规范网络和神经算子基线，拓扑、学习几何与场结构相互作用越强的任务提升越大。

### 四、结论（Conclusion）
将物理场学习形式化为固定拓扑上边界算子、仅学习离散黎曼度量的RHMP，是一种有效的架构原则。该设计同时保证精确的d_{k+1}d_k=0、非负Hodge能量、半正定Hodge算子与精确阿贝尔曲率不变性，使网络既保持物理守恒结构又能从数据中适应几何与材料响应。

### 五、方法论与关键技术细节
关键点包括：特征按物理量类型放置到不同上链阶数，而不是全部作为节点特征；d_k固定为定向关联矩阵，不参与学习；H_k通过O(C)不变统计量预测并限制为SPD矩阵，作为离散黎曼度量/质量矩阵；上下Hodge项分别使用d_k^T H_{k+1} d_k与d_{k-1}H_{k-1}^{↓}d_{k-1}^T，保证算子半正定；范数门控非线性避免破坏上链帧等变；Abel规范场通过d(dλ)=0获得精确规范不变性；非阿贝尔场使用上链微分加代数耦合。局限在于SPD度量的表达能力和消息传递的计算开销仍受网格规模影响。
