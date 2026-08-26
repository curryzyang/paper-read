# Social Graph Mamba: Forecasting Pedestrian Movements Based on Social Context

- 区域：精读区
- 排名：7
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Hong-Son Nguyen, Yen-Chen Liu
- 机构：National Cheng Kung University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21411v1) · [PDF](https://arxiv.org/pdf/2608.21411v1)

## TLDR
Social Graph Mamba (SGM) replaces quadratic-complexity attention with linear-complexity Selective State Space Models on dynamic interaction graphs and unsupervised community-aware grouping, achieving competitive pedestrian trajectory prediction on benchmarks and enabling real-world robot deployment.

## Abstract
Forecasting pedestrian motion has always been fundamental for autonomous navigation in crowded environments. While attention-based methods achieve strong performance, they suffer from quadratic computational complexity in modeling social interactions, limiting scalability. Additionally, the existing methods often achieve high accuracy on prediction benchmarks at the individual level, but fail to fully capture the natural movement behaviors of crowds in real-world scenarios, particularly group structures. In this study, we propose Social Graph Mamba (SGM), a novel architecture that replaces attention-based social reasoning with Selective State Space Models (SSMs) operating on dynamically constructed interaction graphs. SGM introduces a dynamic interaction graph with social triplet factorization to decompose crowd interactions sequentially, and a community-aware module to effectively discover group structures via differentiable MinCut optimization and conditions both the embedding space and multi-modal decoder on group membership. Our experiments on standard benchmarks (ETH/UCY, SDD) demonstrate competitive performance with linear sequence complexity compared to quadratic attention-based methods. We further validate SGM in physical robot experiments by integrating predicted trajectories into a Social Force Model (SFM) for real-world implementation.


## 精读解读（中文）
### 一、研究动机
现有基于注意力机制的轨迹预测方法在建模社交交互时具有二次方计算复杂度，限制了在大规模拥挤场景中的可扩展性；同时，这些方法往往在个体层面取得较高精度，却未能充分捕捉真实场景中人群的自然移动行为，尤其是群体结构。为此，需要一种兼顾效率与群体感知的新型预测架构。

### 二、技术方案（Method）
提出Social Graph Mamba (SGM)，以选择性状态空间模型（SSM/Mamba）替代注意力机制进行社交推理。整体流程包括：1）输入多智能体历史轨迹，构建动态交互图，边权重由物理启发式组件（距离、速度一致性、碰撞时间TTC）融合而成，并采用距离阈值和top-k邻居剪枝；2）通过社区感知模块，利用可微MinCut优化无监督发现群体结构，并将群体归属信息嵌入特征空间和条件多模态解码器；3）采用拓扑引导的节点优先排序，依据动态加权度中心性对智能体排序以适应SSM的序列处理；4）提出社交三元组分解，将交互建模为时间分支、自我中心分支和目标中心分支，每个分支使用Cycle Mamba进行双向上下文传播，其中自我和目标token按动态边权重加权，并引入方向感知的目标预测与可学习方向平衡；5）通过动态社交门融合三个分支，再进行全局交互扫描以聚合群体级上下文；6）最后由条件多模态解码器生成K个未来轨迹假设及其概率。

### 三、结果（Result）
在ETH/UCY和SDD标准基准上，SGM取得了与基于二次复杂度注意力的方法相当的性能，同时保持线性序列复杂度。在物理机器人实验中，将预测轨迹集成到社会力模型（SFM）中，验证了真实世界部署的可行性。

### 四、结论（Conclusion）
SGM通过将SSM应用于动态交互图，在保持预测精度的同时显著降低计算复杂度，并通过无监督社区发现提升了对群体结构的建模能力，为实时机器人导航中的行人轨迹预测提供了一种高效且可扩展的解决方案。

### 五、方法论与关键技术细节
动态交互图的边权重为 w_ij = w_dist + w_vel + w_ttc，其中距离项使用高斯核（α=1.0, σ_p=2.0），速度项为余弦相似度（β=0.5），TTC项为逆碰撞时间（γ=2.0，上限10），并设置d_max=10m、top-k=20。排序使用加权度中心性且按升序排列，使高影响力智能体获得更丰富上下文；社区感知模块通过可微MinCut优化软分配，无需真实群体标注。Cycle Mamba通过拼接反向与正向序列进行单次扫描，并用可学习标量θ（初始0）平衡前后向输出；目标预测使用自我智能体最后k=3步特征以编码方向和速度。复杂度为线性O(N)，相比注意力O(N^2)具有优势。局限包括：TTC计算假设速度恒定，且社区分配可能受噪声影响；物理实验仅集成到SFM，尚未在真实高密度人群上全面评估。
