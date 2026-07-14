# Manifold Constrained Tabular Deep Neural Networks

- 区域：精读区
- 排名：6
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Tian Li, Lucy Robinson, Varun Ojha, Huizhi Liang
- 机构：Newcastle University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09710v1) · [PDF](https://arxiv.org/pdf/2607.09710v1)

## TLDR
HDE-Net introduces a hyperbolic manifold-constrained deep neural network with Latent Decision Nodes and Soft Decision Routing to overcome the geometric mismatch between Euclidean representations and the hierarchical, rule-based structures of tabular data, achieving state-of-the-art average rank on the TALENT-tiny-core benchmark.

## Abstract
Tabular classification is often governed by local, condition-triggered rules rather than smooth global patterns. However, tabular deep neural networks (DNNs) are typically built upon Euclidean representations that favor smooth variations and semantic locality. This potential geometric mismatch can make it challenging for tabular DNNs to efficiently represent the discrete, rule-partitioned structures often underlying tabular classification. To address this issue, we propose HDE-Net, a manifold-constrained DNN that enables hierarchical decision modeling in hyperbolic space. We first abstract heterogeneous features into unified Latent Decision Nodes (LDNs) and embed them in the Poincaré ball, forming a continuous representation that resembles tree-structured reasoning. For numerical features, we introduce a Soft Decision Routing mechanism that approximates range-based local rules in a differentiable manner, bringing their LDN semantics closer to those of categorical features. An entropy-aware capacity allocation algorithm further adapts the number of LDNs per numerical feature to balance expressiveness and complexity. On the TALENT-tiny-core classification benchmark (30 datasets), HDE-Net achieves the \textit{best average rank}, outperforming both industrial GBDTs and recent tabular DNNs while maintaining high efficiency.


## 精读解读（中文）
### 一、研究动机
表格分类通常受局部、条件触发的规则主导，而非平滑全局模式。然而，现有表格深度神经网络基于欧几里得表示，倾向于平滑变化和语义局部性，这种几何不匹配使得它们难以有效表示离散、规则划分的结构。为了克服这一挑战，作者提出了HDE-Net。

### 二、技术方案（Method）
HDE-Net首先将异构表格特征抽象为统一的潜在决策节点（LDN），并将这些LDN嵌入到庞加莱球中，形成类似树结构推理的连续表示。对于数值特征，引入软决策路由机制，以可微分方式近似基于范围的局部规则，使得数值LDN的语义更接近类别特征。此外，提出信息熵感知容量分配算法，自适应调整每个数值特征对应的LDN数量，以平衡表达能力和复杂度。最终，将双曲嵌入投影到欧几里得切空间，通过轻量级MLP分类器进行预测。

### 三、结果（Result）
在包含30个数据集的TALENT-tiny-core分类基准上，HDE-Net取得了最优平均排名，超越了工业级梯度提升决策树（如XGBoost、CatBoost）以及最新的表格深度神经网络（如FT-Transformer、ExcelFormer），同时保持了高计算效率。

### 四、结论（Conclusion）
HDE-Net通过将双曲几何引入表格深度神经网络，有效对齐了树结构的决策规则，解决了欧几里得表示与表格数据离散规则结构之间的几何不匹配问题。实验验证了其优越性能，表明双曲空间为表格表征学习提供了一个有效的归纳偏置。

### 五、方法论与关键技术细节
关键细节包括：(1) 输入为包含数值和类别特征的异构表格数据；(2) 数值特征通过软决策路由生成多个LDN，每个LDN对应一个范围；(3) LDN嵌入在庞加莱球中初始化，曲率c是超参数；(4) 容量分配基于Shannon熵的直方图估计；(5) 模型使用交叉熵损失端到端训练；(6) 相比复杂Transformer，HDE-Net参数量更少、推理更快；(7) 局限性：熵分配是启发式方法，可能不适用于所有情况；层次结构隐式而非显式。
