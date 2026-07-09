# STAGformer: A Spatio-temporal Agent Graph Transformer for Micro Mobility Demand Forecasting

- 区域：精读区
- 排名：5
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Ye Zihao
- 机构：City University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06614v1) · [PDF](https://arxiv.org/pdf/2607.06614v1)

## TLDR
STAGformer introduces a spatio-temporal agent attention mechanism to achieve linear-complexity global modeling for station-level bike-sharing demand forecasting, consistently outperforming state-of-the-art methods on real-world datasets.

## Abstract
Accurate station-level demand forecasting is essential for the efficient operation of bike-sharing systems, yet it remains challenging due to complex spatio-temporal dependencies and the large scale of urban networks. This paper presents STAGformer, a Spatio-Temporal Agent Graph Transformer that achieves efficient global modeling with linear computational complexity. The model introduces a two-step agent attention mechanism, where a small set of learnable spatial and temporal agent tokens first aggregate global information and then broadcast it back to individual stations and time steps, effectively capturing long-range interactions while reducing the quadratic cost of standard self-attention to O(NT). STAGformer integrates four core modules: a spatio-temporal encoder that fuses dynamic node features with external contextual factors (weather, time, points of interest), a graph propagation module for spatial neighbor aggregation, a temporal convolution module for local pattern extraction, and the agent attention module for global dependency modeling. Extensive experiments on two real-world datasets -- NYC Citi-Bike and Chicago Divvy-Bike -- demonstrate that STAGformer consistently outperforms state-of-the-art baselines across multiple prediction horizons, achieving significant improvements in both RMSE and MAE. Ablation studies validate the contribution of each component, with the agent attention mechanism proving critical for modeling global spatio-temporal dependencies.


## 精读解读（中文）
### 一、研究动机
现有方法在处理大规模车站网络的微出行需求预测时，面临标准自注意力计算复杂度随车站数N和时间步T乘积平方增长（O((NT)^2)）的瓶颈，且难以有效融合天气、时间、兴趣点等多源外部因素，导致预测精度有限。

### 二、技术方案（Method）
STAGformer包含四个核心模块：1) 时空特征编码器，对动态节点特征和全局特征（天气、时间）分别线性投影至隐藏维度d，沿节点维度复制全局特征后与节点特征拼接得C=2d维向量，并添加可学习的时空位置编码；2) 图传播模块，通过外部邻接矩阵或自适应图学习（可学习节点嵌入内积经ReLU、除以温度参数τ、Softmax归一化）得到归一化邻接矩阵，进行K步图传播，各步结果经可学习权重加权融合；3) 时间卷积模块，轻量级卷积提取每个车站的局部时间模式；4) 代理注意力模块，引入少量可学习的空间代理token和时间代理token，先通过标准自注意力聚合全局信息到代理token（O(NT + A^2)，A为代理数，A<<NT），再广播回各个车站和时间步，实现线性复杂度O(NT)的全局依赖建模，同时保留softmax注意力表达能力，并通过深度可分离卷积残差分支补偿特征多样性损失。最后融合特征经输出层生成多步预测。

### 三、结果（Result）
在NYC Citi-Bike和Chicago Divvy-Bike两个真实数据集上，STAGformer在多个预测窗口（如1小时、2小时、4小时）下均一致优于现有最优基线（如DCRNN、STGCN、GMAN、Informer等），在RMSE和MAE指标上取得显著改进。消融实验验证了图传播、时间卷积、代理注意力各模块的贡献，其中代理注意力对全局时空依赖建模最为关键。

### 四、结论（Conclusion）
STAGformer通过引入代理注意力机制，将标准自注意力的二次复杂度降至线性，同时结合图传播模块显式聚合空间邻居信息和时间卷积模块提取局部模式，实现了高效且精准的全局时空依赖建模。该方法为大规模城市系统中微出行需求预测提供了可扩展的解决方案，在真实数据上验证了其优于现有方法的准确性和效率。

### 五、方法论与关键技术细节
1）使用可学习的空间代理token（个数A_s）和时间代理token（个数A_t），A_s、A_t远小于N和T；2）代理注意力保留softmax注意力步骤，并通过深度可分离卷积残差分支避免表达能力损失；3）自适应图学习采用可学习节点嵌入E∈R^{N×d_a}，内积经ReLU后除以可学习温度参数τ再Softmax归一化；4）模型复杂度为O(NT + A_s N + A_t T + A_s^2 + A_t^2)，实践中约O(NT)；5）外部因素包括气象（温度、降水、风速）和时间特征（小时、周天、节假日）；6）实验使用RMSE和MAE作为评价指标；7）未明确讨论局限性，但代理注意力可能对代理数量选择敏感，且模型结构相对复杂需要调参。
