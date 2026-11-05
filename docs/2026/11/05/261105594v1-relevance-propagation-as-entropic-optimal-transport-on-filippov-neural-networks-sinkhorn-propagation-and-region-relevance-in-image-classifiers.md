# Relevance Propagation as Entropic Optimal Transport on Filippov Neural Networks: Sinkhorn Propagation and Region Relevance in Image Classifiers

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Olivier Gibaru, Eric Nyiri
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05594v1) · [PDF](https://arxiv.org/pdf/2611.05594v1)

## TLDR
The paper recasts Layer-wise Relevance Propagation as a divergence-free entropic optimal-transport flow on the active computational graph of Filippov neural networks, unifying existing LRP rules—including a new Sinkhorn Relevance Propagation—under one variational principle and enabling exact region-level evidence attribution, validated on VGG-16 and ConvNeXt-Tiny.

## Abstract
Relevance propagation, which redistributes a network's prediction backward through the layers, is usually treated as a heuristic. We show that it is the solution of a single variational problem: Layer-wise Relevance Propagation (LRP) is the divergence-free flow on the active computational graph of zero relative entropy to the backward transition law of the forward activation flow; for a non-negative reference, this is a relative entropy between Markov measures on backward paths. The rules LRP$_0$, LRP$_{z^+}$ and LRP$_{α,β}$ follow from this principle by the choice of a reference, and are instances of one rule, LRPN$_{α,β}$, whose weights may vary from node to node, for instance with the node's activity, in the spirit of Hebb's principle. The principle rests on a measure-theoretic formalization of feed-forward networks as directed acyclic graphs of Filippov operators, which covers piecewise-smooth and discontinuous architectures (e.g. hard-routed Mixture-of-Experts) with a Clarke-Filippov generalized-gradient calculus; it also characterizes backpropagation as the adjoint equation of a Lagrangian relaxation. On networks of ReLU and max-pooling nodes, LRP$_0$ is Gradient$\times$Input, with an explicit jump across a kink where LRP$_{z^+}$ stays continuous. Taking the entropy edge by edge yields a new rule, Sinkhorn Relevance Propagation. Aggregated over an input region, the flow of a non-negative reference tells, with exact accounting, which hidden units carry its evidence, the conditioned flow being a Schrödinger bridge. On VGG-16, the conservation identities hold to round-off, and the rules are told apart by the sign of their maps, the share of the output left to the bias nodes, faithfulness, localization and class dependence; on ConvNeXt-Tiny, LRPN$_{α,β}$ conserves the output and its Hebbian weights give the highest ABPC of the rules tested.


## 精读解读（中文）
### 一、研究动机
LRP等相关性传播长期被视为启发式，缺乏统一变分解释；作者希望证明其是单一变分问题的解，并将多种规则纳入统一框架，同时把理论推广到分段光滑/不连续网络。

### 二、技术方案（Method）
将前馈网络形式化为Filippov算子的有向无环图，用Clarke-Filippov广义梯度处理ReLU、max-pooling及hard-routed MoE等；把LRP定义为活动计算图上与正向激活流后向转移律零相对熵的无散度流，非负参考下为后向路径马尔可夫测度间相对熵。由此选择参考可导出LRP0、LRPz+、LRPαβ，并统一为节点权重可变的LRPNαβ（如按节点活动性设Hebbian权重）；逐边取熵得到Sinkhorn Relevance Propagation，反向传播被刻画为拉格朗日松弛的伴随方程。推理时给定输入前向得到活动图，再按选定参考后向传播相关性，区域聚合时用条件流（Schrödinger bridge）精确分配证据。

### 三、结果（Result）
在VGG-16上守恒恒等式达到舍入误差（约10^-6–10^-7），LRP0在ReLU/max-pooling扭结处等于Gradient×Input并出现显式跳跃，而LRPz+保持连续；规则可由映射符号、偏置节点份额、忠实性、定位和类别依赖性区分，LRPαβ点定位0.990、质量定位0.855，高于随机约0.575。ConvNeXt-Tiny上LRPNαβ保持输出守恒（约5×10^-6），其Hebbian权重在测试规则中取得最高ABPC。

### 四、结论（Conclusion）
该工作把相关性传播从经验规则提升为基于相对熵/最优传输的统一变分理论，给出可计算的后向流与区域证据核算，并证明不同LRP规则只是参考选择或节点权重的特例；Sinkhorn传播和Filippov形式化扩展了适用架构。实验支持守恒性、忠实性与定位优势，但主要在VGG-16和ConvNeXt-Tiny上验证。

### 五、方法论与关键技术细节
关键实现包括：以非负参考定义相对熵并保证无散度流；LRPNαβ允许逐节点权重（如Hebbian活动依赖）；Sinkhorn规则逐边做熵正则归一化；区域解释用条件流/Schrödinger bridge精确记账；守恒以数值误差检验（VGG约10^-6，ConvNeXt约5×10^-6）。实验使用200张图像、50类设置，比较LRP0、LRPz+、LRPαβ、SRP及随机基线；局限在于依赖参考与活动图、需广义梯度处理不连续节点，且评测架构和样本规模有限。
