# Topological Simplification in Predictive Coding Networks

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Adam Shaw, Jiayu Li, Michael Sperling, Michael Kim, Alvin Jin
- 机构：University of Southern California
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02816v1) · [PDF](https://arxiv.org/pdf/2608.02816v1)

## TLDR
Using persistent homology, the paper shows that predictive coding networks progressively simplify representation topology across layers, with smaller models collapsing components earlier, earlier simplification correlating with poorer reconstruction, and PCNs simplifying later than matched MLPs.

## Abstract
We study the topology of learned representations in predictive coding networks (PCNs), a neuro-inspired bidirectional architecture, using a quantitative layer-wise persistent homology analysis. We train well-performing PCNs on a synthetic classification dataset ($\geq 99.9\%$ test accuracy) and on MNIST ($\geq 95\%$ test accuracy), and measure how topological features change across layers for different architectures and activation functions. We find that smaller PCNs collapse connected components across layers earlier than larger models (Spearman $\unicode{x1D70C} \in [0.72, 0.79]$ across activations), with model size measured as the sum of hidden-layer widths. We also observe a strong negative correlation ($\unicode{x1D70C} = -0.58$) between the depth at which simplification occurs and reconstruction error; i.e., architectures that simplify later reconstruct better. Finally, a seed-level bootstrap comparison across architectures and activations shows that PCNs consistently collapse connected components later than matched MLPs, with an average difference of $3.6$ layers. These results suggest that persistent homology offers a useful quantitative lens on the compression--reconstruction tradeoff in PCNs, and that both model capacity and the recurrent, bidirectional dynamics of predictive coding inference shape when this tradeoff is resolved across layers.


## 精读解读（中文）
### 一、研究动机
现有拓扑简化研究多针对前馈网络，而预测编码网络作为同时支持推断与重构的双向神经形态架构，其表征拓扑的跨层演化尚不清楚。本研究用持久同调定量分析PCN表示拓扑，以理解拓扑简化与重构能力之间的权衡。

### 二、技术方案（Method）
训练8隐藏层PCN，在合成数据集（九圆盘嵌入九洞流形）和MNIST上达到高准确率，系统变化隐藏层宽度（均匀、递增、递减、瓶颈）与激活函数（ReLU、Leaky ReLU、tanh），每配置30个随机种子。对每层固定数据点构造度量空间（合成用归一化k-NN图加无权重测地距离，MNIST用归一化欧氏距离），计算持久同调并在固定过滤尺度eta下提取beta0和beta1；定义加权Betti和及running minimum得到分层简化量，由此计算COM（简化质心）作为简化时机指标。重构质量用MRD衡量：将one-hot输出经PCN反演过程得到重构，计算其到训练集最近同类邻居的平均欧氏距离。最后与匹配MLP做种子级bootstrap比较COM差异。

### 三、结果（Result）
合成数据上，模型大小（隐藏宽度之和）与COM正相关：ReLU rho=0.76、Leaky ReLU rho=0.79、tanh rho=0.72；线性拟合中ReLU斜率约为Leaky ReLU和tanh的两倍，R^2分别为0.59、0.63、0.41。COM与MRD强负相关（rho=-0.58，p<0.001），即简化越晚重构越好。MNIST上观察到与合成实验一致的渐进拓扑简化趋势。PCN比匹配MLP平均晚3.6层发生连通分量坍塌，bootstrap检验p<0.0001。

### 四、结论（Conclusion）
PCN表征拓扑沿层逐步简化，且简化时机由模型容量、激活函数和重构压力共同决定。较早拓扑简化会损害重构质量，而PCN相比MLP更晚简化，说明预测编码的循环双向动力学在压缩与可逆性之间取得平衡。持久同调为定量研究生成型架构中的压缩-重构权衡提供了有效视角。

### 五、方法论与关键技术细节
所有模型固定8隐藏层以保证逐层拓扑可比；拓扑计算仅针对单类（合成数据取Ma，MNIST取数字0）以避免类别混合。PCN通过最小化能量泛函进行训练和推断，使用局部误差而非反向传播；MNIST的过滤尺度eta取0.2和0.3以平衡碎片化与平凡连通。MRD使用最近同类欧氏邻居而非固定目标，允许合理的全新重构；MNIST重构不稳定故不报告，且因计算代价仅用代表架构、相关分析统计功效不足。局限包括持久同调参数（k、eta）选择依赖数据，合成数据具有人工拓扑先验。
