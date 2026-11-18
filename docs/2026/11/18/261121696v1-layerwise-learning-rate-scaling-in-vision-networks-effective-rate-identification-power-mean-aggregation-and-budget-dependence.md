# Layerwise Learning-Rate Scaling in Vision Networks: Effective-Rate Identification, Power-Mean Aggregation, and Budget Dependence

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Chandini Vysyaraju, Raghuvir Duvvuri, Radu Timofte, Dmitry Ignatov
- 机构：University of Würzburg
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21696v1) · [PDF](https://arxiv.org/pdf/2611.21696v1)

## TLDR
In from-scratch vision training, a layerwise learning-rate strategy’s rate-related effect can be summarized by an effective learning rate computed from its multiplier profile—best aggregated with a parameter-weighted power mean (exponent ≈0.35)—enabling training-free recipe ranking, although the effect decays with longer training budgets while architecture-dependent grouping effects can persist.

## Abstract
Layerwise learning-rate scaling assigns different learning rates to different parts of a network. Although established in fine-tuning pretrained models, its effects in vision networks trained from scratch are commonly assessed by training each candidate recipe. We show that, in this setting, the rate-related component of a layerwise strategy is well summarized by an effective learning rate computable directly from its multiplier profile. Across matched-control comparisons, changes in test accuracy closely track changes in training loss (r = -0.996), which supports an optimization-progress explanation of the short-budget rate effect. Increasing the untuned base learning rate tenfold shifts the rate-matched contrast upward in all six tested architectures (p = 0.016) and increases the number of architectures in which a published discriminative schedule, excluded from model fitting, outperforms the uniform control from two to five of six (p = 0.031). Within the evaluated strategy space, a parameter-weighted power mean with exponent 0.35 (95% confidence interval [0.20, 0.50]) accounts for 42.6% of within-architecture variance, compared with 36.4% for the arithmetic mean. Ranking candidates by this scalar without training improves the selected candidate's mean percentile rank from the 26th to the 10th and reduces its mean accuracy shortfall relative to the best candidate from 3.70 to 1.12 points. The rate-related effect decays as the training budget increases; relative to tuned baselines, the overall strategy effect falls within the prespecified practical-equivalence margin in two of three architectures. A separate grouping-related contrast can persist at long budgets, although its direction and magnitude depend on the architecture.


## 精读解读（中文）
### 一、研究动机
逐层学习率缩放已在预训练模型微调中确立，但在从零训练的视觉网络里，其效果通常要靠逐一训练候选配方来评估，成本高且难以区分整体速率变化与分组本身的作用，文献报道也因此不一致。作者希望检验该场景下策略中与速率相关的效应能否由一个直接由乘数配置算出的标量概括，从而在训练前排序候选并厘清速率通道与分组通道。

### 二、技术方案（Method）
作者定义 38 种逐层策略：36 种按参数顺序把张量分成 2–6 个连续深度组、划分比例从均分到 0.95/0.05，另 2 种循环分组，所有乘数均不超过 1。核心建模为速率响应模型 Δ_a(s)=β_a(M_p(s)−M*_a)+ε，其中 M_p 为参数加权幂均值、指数 p 跨架构共享，M*_a 为架构特异的盈亏平衡点，并加入近冻结指示项 −γ·1[m_min≤0.01] 刻画阈值式惩罚。关键操作是先由乘数配置解析计算 M_p，再对每种策略及其均匀对照、速率匹配对照和保均值变体在相同架构与预算下训练并比较测试准确率与训练损失，同时通过提高基础学习率十倍做干预、用未参与拟合的 ULMFiT 判别式调度做分布外验证。统计协议采用聚类稳健推断、小样本精确置换检验与等效性检验，实验覆盖多个视觉架构、21 个实验单元和 936 个策略注入模型。

### 三、结果（Result）
在 21 个实验单元中，测试准确率变化与训练损失变化高度相关（r=−0.996），控制训练损失后与泛化间隙的偏相关为负，支持短预算速率效应的优化进度解释；基础学习率提高十倍使纯速率削减对比在全部 6 个架构中上移（平均 +4.7 个点，p=0.016），并使 ULMFiT 调度在 6 个架构中优于均匀对照的数量从 2 个增至 5 个（p=0.031）。拟合得到幂均值指数 p=0.35（95% CI [0.20,0.50]），解释架构内方差 42.6%，高于算术平均的 36.4%；不训练直接按该标量排序，使所选候选的平均百分位从第 26 升至第 10，与最优候选的平均准确率差距从 3.70 降至 1.12 个点。速率相关效应随训练预算增加而衰减，三个扩展架构中有两个相对调优基线的总体策略效应落在预设实用等效边界内，但分组相关对比可在长预算下持续，例如 ConvNeXt 在 100 轮增至 +6.4 个点而 GoogLeNet 反向。

### 四、结论（Conclusion）
从零训练的视觉网络中，逐层学习率策略的速率相关效应可由乘数配置直接算出的幂均值有效速率较好地概括，且在短预算下主要表现为优化进度而非正则化；提高基础学习率会减弱速率削减的代价，提示从不同基础速率条件出发的研究可能测到不同贡献。参数加权幂均值（p≈0.35）优于算术平均，可作为无需训练的候选排序工具，但速率效应随预算增大而衰减、分组效应依赖架构并可在长预算下持续，因此评估必须区分速率通道与分组通道并明确预算条件。

### 五、方法论与关键技术细节
数据来自 NNGPT/LEMUR 生成的 38 种策略、936 个策略注入模型及全部逐种子记录，策略空间限定为乘数不超过 1 的一侧，观测以训练损失和测试准确率为主，模型为线性速率响应加阈值修正而不引入额外正则化先验；聚合采用参数加权幂均值 M_p=(Σ w_g m_g^p)^{1/p}，以 p=0 的几何平均和 p=1 的算术平均为参照，指数由剖面拟合与聚类自助法给出不确定性。速率响应模型含架构特异 β_a、M*_a 与共享指数 p，近冻结阈值 0.01 并非拟合得到，而是由可用乘数取值决定，残差阈值只能定位在 0.01–0.1 区间；对照包括速率匹配与保均值两种变体，统计上使用聚类稳健推断、精确置换检验和等效性检验。局限在于策略空间未覆盖把部分组速率提高到基率以上的方案，模型只预测干预方向而非幅度，所测架构描述子未能预测架构特异的速率敏感性，且近冻结阈值受乘数取值的离散性约束。
