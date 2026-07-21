# Learning Structural Manipulability in Gate-Level Netlists Using Graph Neural Networks

- 区域：精读区
- 排名：9
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Rupesh Raj Karn, Ozgur Sinanoglu
- 机构：New York University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16245v1) · [PDF](https://arxiv.org/pdf/2607.16245v1)

## TLDR
This paper defines a topology-driven structural manipulability score for gate-level netlists and evaluates how effectively graph neural networks can approximate this score through node-level regression, with hierarchical models yielding the most consistent rankings.

## Abstract
Gate-level netlists exhibit intrinsic structural properties that influence signal propagation independently of functional simulation. We define a topology-driven structural manipulability score that characterizes node-level structural flexibility using path participation, k-core embedding, symmetry, and centrality. Modeling netlists as directed graphs, we formulate node-level regression to learn this topology-derived score using graph neural networks (GNNs). Experiments on ISCAS85 and EPFL benchmarks evaluate how effectively different GNN architectures approximate this metric across held-out circuits, with hierarchical models yielding the most consistent rankings. Component-level and ablation analyses examine the contribution of individual factors. As an illustrative case study, analysis of Trojan-injected circuits using TrustHub templates reveals statistically distinguishable structural patterns, indicating that topology-based scoring provides complementary structural insight.


## 精读解读（中文）
### 一、研究动机
传统的门级网表分析依赖于功能仿真、形式验证和时序分析，主要捕获功能行为而不表征独立于输入激励的结构拓扑属性。随着设计规模增长，理解图级结构组织对于分析连通性、鲁棒性和嵌入模式变得重要，但现有方法缺乏一种输入无关的、基于拓扑的结构特征化方法。

### 二、技术方案（Method）
将门级网表建模为有向图，节点代表逻辑门或时序单元，边代表信号传播。定义结构可操纵性分数M(v)为四个图论属性的加权组合：路径参与比（PI到PO路径经过节点的比例）、k-core嵌入深度（核心分解数）、对称性类大小（1-WL哈希等价类）、标准化中介中心性，权重均等。使用多种图神经网络（GIN、GCN、GraphSAGE、GAT、MPNN、APPNP、HetGNN、g-U-Net、SGNN、GTN）进行节点级回归，输入为图结构和节点特征，损失函数为均方误差，以学习从图结构到预定义分数M(v)的映射。

### 三、结果（Result）
在ISCAS85和EPFL基准测试中，大部分空间消息传递模型（GCN、GSAGE、MPNN）的MSE约为3×10⁻⁴至5×10⁻⁴，Spearman秩相关系数约0.75–0.79；g-U-Net达到最高Spearman相关系数0.8129±0.0205，GCN为0.7881±0.0126。SGNN严重退化（MSE≈0.2086，Spearman≈0.4894）。组件分析显示，核心分解成分M_core与复合分数相关性最强（Spearman=0.763），路径参与成分M_path贡献极低（Spearman=0.144）。

### 四、结论（Conclusion）
提出的拓扑驱动结构可操纵性分数可以通过多种GNN架构有效近似，其中具有层次表示的模型（g-U-Net）产生最一致的排序。核心分解是主导因素，而路径参与贡献有限。对注入木马的电路分析显示统计上可区分的结构模式，表明基于拓扑的评分提供了互补的结构洞察，可用于硬件安全等场景。该分数是一个设计的结构代理，依赖于网表表示，并非工程可行性或功能正确性的验证指标。

### 五、方法论与关键技术细节
数据来源：ISCAS85和EPFL基准门级网表，表示为有向图。先验：各组件权重均匀（α=β=γ=δ）。损失函数：均方误差。超参数：GNN层数、隐藏维度未明示但使用标准化分割和归一化。复杂度/约束：全局路径参与和中介中心性计算昂贵，文中采用近似采样；GNN学习旨在避免重复计算这些全局量。局限性：分数是设计的结构代理，依赖于表示且可能随逻辑保留变换变化；实证中路径参与成分缺乏区分性；不同基准间存在电路级变异性；跨设计迁移需在特定基准范围内解释；分数不是外部验证的地面真值属性。
