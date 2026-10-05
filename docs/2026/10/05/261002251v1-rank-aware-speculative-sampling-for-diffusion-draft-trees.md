# Rank-Aware Speculative Sampling for Diffusion Draft Trees

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Marcello Bullo, Yanxiao Liu, Öykü Sıla Güner, Arpan Mukherjee, Deniz Gündüz
- 机构：Imperial College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02251v1) · [PDF](https://arxiv.org/pdf/2610.02251v1)

## TLDR
The paper introduces Rank-Aware Speculative Sampling (RASS), a rank-aware list-coupling verification rule for diffusion draft trees that ranks draft candidates by proposal–target compatibility and optimizes rank weights to preserve exact sampling, achieving up to ~20% fewer target-model evaluations than D-GRS on CIFAR-10 and consistent gains across other benchmarks.

## Abstract
Speculative sampling accelerates diffusion generation by verifying inexpensive draft states in parallel while preserving the target law. Recent tree-based methods allocate the parallel compute budget more effectively than single-chain drafts, as demonstrated by Diffusion Greedy Rejection Sampling (D-GRS). D-GRS generates $K$ conditionally independent candidates per node, and sequentially tests them in their generation order. Yet the sampled candidates admit an informative ranking without additional target-model evaluations. To exploit this, we introduce Rank-Aware Speculative Sampling (RASS), a verification rule for speculative draft trees based on rank-aware list coupling. RASS orders draft candidates along the proposal-target mean displacement and samples a rank with weights optimized to minimize total variation between the selected-proposal and target laws. Finally, the selected candidate is maximally coupled with the target, with residual correction ensuring exact sampling for any choice of rank weights. We evaluate RASS on a Gaussian-mixture target, unconditional pixel-space generation on FFHQ, conditional generation on CIFAR-10, and latent diffusion with Stable Diffusion 3.5 using COCO2014 prompts. Measured by the ratio of standard to speculative sampling's target-model evaluation counts, RASS improves on D-GRS across the evaluated settings, with gains reaching approximately 20% on CIFAR-10 at matched compute budgets.


## 精读解读（中文）
### 一、研究动机
扩散与流模型推理需要多次串行调用大型目标网络，推测采样通过并行验证廉价草稿状态并保持目标分布来加速；树式草稿方法（如 D-GRS）比单链更有效地利用并行预算，但 D-GRS 按生成顺序逐个测试同一节点的 K 个条件独立候选。这些候选实际上可交换，固定顺序约束丢弃了可利用的排序信息，且相对列表耦合可能严格次优。因此需要一种利用草稿候选排序信息、同时保持精确目标分布的验证规则。

### 二、技术方案（Method）
RASS 是一种面向扩散草稿树的秩感知列表耦合验证规则。目标与提议核均为共享协方差的高斯转移：Q_n=N(m_n^q(y),σ_n^2 I)，P_n=N(m_n^p(y),σ_n^2 I)，其中 m_n^p 由廉价延迟目标提议给出。每轮先按树结构递归抽取每节点 K 个 i.i.d. 草稿候选，并一次批量调用目标模型；在节点验证时，将候选按目标-提议似然比或均值位移排序，采样一个秩，其权重通过最小化被选提议分布与目标分布的总变差来优化；随后对选中候选与目标做最大耦合，并用残差校正确保任意可行秩权重下精确采样目标马尔可夫链。

### 三、结果（Result）
在 Gaussian-mixture 目标、FFHQ 无条件像素空间生成、CIFAR-10 条件生成以及 Stable Diffusion 3.5 潜空间扩散（COCO2014 提示）上评估，以标准采样与推测采样的目标模型评估次数之比衡量。RASS 在所评估设置中均优于 D-GRS，匹配计算预算下 CIFAR-10 增益约 20%；理论分析还给出任意列表耦合方案在 i.i.d. 草稿下的接受概率上界，且该界比基于 hockey-stick 散度的界更紧。

### 四、结论（Conclusion）
RASS 表明，树式推测扩散中同一节点的可交换草稿候选不应被固定顺序验证，而应利用其可排序性来构造更强的验证提议。通过秩感知列表耦合和残差校正，RASS 在保持精确目标律的同时持续减少昂贵目标模型调用，为扩散模型推理加速提供了可证明且实用的改进。

### 五、方法论与关键技术细节
关键细节包括：草稿树由每节点 K 个候选和深度 L 定义，并行预算 B=|V|；目标与提议共享协方差、仅均值不同，排序无需额外目标评估；秩权重可随提议-目标差异自适应，在两者接近时趋向均匀选择、差异大时集中在高似然候选；选中候选与目标最大耦合，残差校正保证精确性。理论层面给出 i.i.d. 草稿约束下更紧的接受概率上界。局限在于实验覆盖的目标/提议核与数据集有限，性能依赖草稿质量与提议-目标差异，秩权重优化和树管理带来额外开销，且精确性保证依赖所设高斯转移核和可行秩权重等条件。
