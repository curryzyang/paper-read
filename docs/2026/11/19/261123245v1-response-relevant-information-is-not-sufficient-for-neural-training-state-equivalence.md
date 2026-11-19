# Response-Relevant Information Is Not Sufficient for Neural Training-State Equivalence

- 区域：精读区
- 排名：6
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Truong Xuan Khanh
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23245v1) · [PDF](https://arxiv.org/pdf/2611.23245v1)

## TLDR
The paper shows that response-relevant information is insufficient for neural training-state equivalence: although weight, representation, and optimiser descriptors can predict future response deviations, they do not yield the pairwise geometry needed to match checkpoints by training state beyond controls.

## Abstract
Response-relevant information is not sufficient evidence that two neural networks are in the same training state. We define training-state equivalence operationally: two checkpoints are equivalent, relative to an intervention family and horizon, if they respond alike when training is perturbed and continues. On fresh runs of a one-layer transformer learning modular addition, response to a weight-decay pulse is highly reproducible relative to between-checkpoint differences (rho_state = 0.934 at 500 steps), establishing the target as measurable. Fifteen descriptors of weight spectra, representation geometry and optimiser geometry carry within-run response-relevant information beyond weight norm and loss on a development dataset, predicting held-out response deviation across seed blocks. But their apparent 16.1% advantage at matching checkpoints by future response does not separate from a conditional placebo preserving each descriptor's fitted dependence on the conventional observables, and a calibrated positive control makes simple insensitivity an unlikely explanation. Information a decoder can extract need not be organised in the pairwise geometry that similarity judgments require.


## 精读解读（中文）
### 一、研究动机
论文关注如何判定两个神经网络检查点是否处于同一训练状态：仅凭与响应相关的信息是否足以支持这种等价性仍不清楚。作者主张采用可操作定义，即相对于给定干预族和预测时域，两个检查点在训练被扰动并继续后应产生相似响应，并据此检验常用权重谱、表示几何与优化器几何描述符能否超越权重范数和损失来识别等价状态。

### 二、技术方案（Method）
在单层 Transformer 学习模加法的全新训练运行中采集检查点，施加权重衰减脉冲作为干预并继续训练到固定时域，以响应偏差衡量训练状态；先估计该响应目标在运行内的可重复性。随后用十五个权重谱、表示几何和优化器几何描述符，在开发集上预测跨种子块的留出响应偏差，并在按未来响应匹配检查点的任务中评估其相对常规观测量的增益；关键对照是保留各描述符对常规观测量拟合依赖的条件安慰剂，以及校准的正对照。

### 三、结果（Result）
在 500 步时，权重衰减脉冲响应相对于检查点间差异高度可重复，rho_state=0.934，说明目标可测。十五个描述符在开发集上携带超出权重范数和损失的运行内响应相关信息，并能预测跨种子块的留出响应偏差；按未来响应匹配检查点时出现 16.1% 的表观优势，但该优势无法与条件安慰剂区分，校准正对照使简单不敏感性不太可能解释结果。

### 四、结论（Conclusion）
因此，响应相关信息即使可被解码器提取，也不足以证明两个检查点训练状态等价；这类信息未必组织成相似性判断所需的成对几何结构。论文提示用描述符或未来响应信息推断检查点等价性时需谨慎，并应将等价性限定在具体干预族和时域下进行成对响应检验。

### 五、方法论与关键技术细节
实验基于单层 Transformer 的模加法任务、多次全新运行和按种子块划分的检查点，干预为权重衰减脉冲，评价指标为继续训练后的响应偏差，核心可重复性为 500 步时 rho_state=0.934；描述符覆盖权重谱、表示几何与优化器几何共十五项，并控制权重范数和损失。方法上的关键约束是条件安慰剂保留每个描述符对常规观测量的拟合依赖，正对照用于排除度量不敏感；局限在于结论来自单一任务、架构和干预族，且等价性是相对于给定干预与时域的操作性定义。
