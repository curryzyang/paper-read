# Transformers with Signatures: Towards Universal In-Context Learning in Path Space

- 区域：精读区
- 排名：8
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Ziheng Cheng, Xin Guo, Ben Hambly
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31439v1) · [PDF](https://arxiv.org/pdf/2611.31439v1)

## TLDR
The paper proposes a path-signature-based framework for transformer in-context learning, proves finite-sample guarantees for a two-head-per-layer transformer that emulates in-context Lasso under dependent path data, and shows empirically that signature-based transformers match or outperform vanilla baselines with fewer parameters.

## Abstract
In-context learning (ICL) enables transformers to adapt to new tasks from demonstrations without updating their parameters. However, theoretical guarantees for transformers remain limited in general, and elusive in particular when target responses depend nonlinearly on the evolution of observed paths. We establish an ICL framework for path space, using path signature features. Building on the universal linear approximation property of signatures, we construct explicitly a causal softmax transformer with two attention heads per layer that emulates in-context Lasso. Under sparse signature approximation and suitable moment and concentration conditions, we establish finite-sample prediction error bounds. Our analysis goes beyond the IID data setting in the existing ICL theory, allowing dependence among demonstrations and the query.
  Experiments on in-context sparse recovery, nonlinear path regression, execution-cost prediction, and financial payoff inference demonstrate robustness to changes in observation grids and adaptation to unseen market environments. Across these prediction tasks, transformers with signatures match or outperform vanilla transformer baselines with substantially fewer trainable parameters, highlighting the effectiveness and efficiency of signature-based ICL.


## 精读解读（中文）
### 一、研究动机
现有 Transformer 的上下文学习理论多针对向量或独立同分布数据，难以保证目标响应非线性依赖观测路径演化时的泛化；论文旨在为路径空间建立可证明的上下文学习框架，使 Transformer 仅凭示范即可适应路径型任务而不更新参数。

### 二、技术方案（Method）
论文以路径签名作为路径特征映射，利用签名的通用线性逼近性质把路径泛函学习转化为签名特征上的稀疏线性回归；显式构造每层两个注意力头的因果 softmax Transformer，使其前向计算模拟上下文 Lasso，从而在示范与查询组成的序列上完成稀疏恢复与预测。训练/推理均以路径及其响应为输入，先计算签名特征，再通过该结构化注意力执行上下文优化，推理阶段不更新模型参数。

### 三、结果（Result）
在稀疏签名逼近、矩条件与集中条件下，作者给出允许示范与查询相依的非独立同分布有限样本预测误差界；实验覆盖上下文稀疏恢复、非线性路径回归、执行成本预测和金融收益推断，显示模型对观测网格变化更稳健，并能适应未见市场环境。与普通 Transformer 基线相比，签名 Transformer 在显著更少可训练参数下达到相当或更优性能。

### 四、结论（Conclusion）
路径签名可为路径空间中的 Transformer 上下文学习提供通用且可分析的表示基础，使因果 softmax 注意力显式实现上下文 Lasso 并获得依赖数据下的有限样本保证；实证结果表明该方法在路径型预测任务上兼具有效性与参数效率。

### 五、方法论与关键技术细节
关键方法点包括以截断路径签名作为特征、依赖签名的通用线性逼近与稀疏签名近似、每层两个注意力头显式模拟 in-context Lasso，以及非 IID 下示范和查询可相依的矩与集中条件；实验涵盖稀疏恢复、非线性路径回归、执行成本和金融收益任务，并考察观测网格变化与未见市场环境。局限在于理论保证依赖签名稀疏近似和集中条件，实际需选择签名截断阶数与特征规模，签名维度及高阶项会带来计算和存储约束。
