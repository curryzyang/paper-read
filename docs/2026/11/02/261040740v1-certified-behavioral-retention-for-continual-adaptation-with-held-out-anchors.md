# Certified Behavioral Retention for Continual Adaptation with Held-Out Anchors

- 区域：精读区
- 排名：8
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Ahanaf Hasan Ariq, Abrar Shahid
- 机构：Ideal School and College, Notre Dame College
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40740v1) · [PDF](https://arxiv.org/pdf/2610.40740v1)

## TLDR
The paper introduces Certified Anchor-Based Adaptation (CABA), a candidate-agnostic post-update gate that uses held-out historical anchors and worst-anchor forward KL on frozen representations to accept the largest interpolation step within a declared behavioral-change budget, providing an auditable retention check with conditional off-anchor guarantees and illustrating a retention–plasticity trade-off.

## Abstract
Continual adaptation requires deciding not only how to update a model, but whether to commit an update without exceeding a declared budget for changes to protected behavior. We introduce Certified Anchor-Based Adaptation (CABA), a candidate-agnostic post-update gate that reserves historical observations from candidate optimization, compares old and candidate policies on frozen representations, and selects the largest tested interpolation coefficient whose worst-anchor forward KL divergence remains within budget. The finite check requires neither action labels nor complete trajectories. We develop a theory-led certification framework that separates measured anchor retention from conditional off-anchor guarantees. Under explicit representation-coverage and Lipschitz assumptions, an accepted update satisfies a uniform behavioral-divergence bound on protected support. The analysis gives regularity bounds for affine softmax heads, probabilistic coverage and compression guarantees, interpolation monotonicity conditions, grid-resolution bounds, and trajectory-level and sequential-composition guarantees. In a controlled UCI Human Activity Recognition study used as a non-stationary sensor-policy proxy, CABA reduces mean forgetting from 1.01 percent for unconstrained adaptation to 0.00 percent at budget epsilon = 0.05, while reducing final average accuracy from 93.04 percent to 88.48 percent. The experiment illustrates a retention-plasticity trade-off and does not establish foundation-model or robotic performance. CABA provides an auditable retention check for candidate generators exposing comparable policy distributions and a declared update path, while deployment also requires separate evidence of current-task utility.


## 精读解读（中文）
### 一、研究动机
持续适应中，模型更新既要提升当前任务，也必须避免破坏已受保护的历史行为，因此需要一个候选无关的提交门控来判断是否提交以及提交多大比例的更新，并在预声明预算内提供可审计证据。现有回放、正则化和信任域方法多在候选优化过程中施加约束，缺少将优化与最终接受分离的保留性检查。

### 二、技术方案（Method）
CABA将历史观测或冻结表示保留为不参与候选优化的审计锚点，对任意候选更新构造旧参数与候选参数之间的插值路径，在累积的held-out锚点上计算旧策略到插值候选策略的前向KL散度，并以最坏锚点散度作为约束，在有限网格中选择满足预算的最大插值系数，不需要动作标签或完整轨迹。理论部分将有限锚点测量与锚点外保证分离：在表示覆盖为ρ-net且散度关于表示L-Lipschitz的假设下，被接受更新在受保护支撑上满足ε+Lρ的一致散度界，并给出高概率覆盖、压缩锚点惩罚、网格分辨率、轨迹级和序列组合界。

### 三、结果（Result）
在UCI-HAR的非平稳传感器策略代理实验中，使用561维冻结特征和线性softmax头、5个按受试者时间段划分的流式任务、3个随机种子，当预算ε=0.05时，CABA将无约束微调的平均遗忘从1.01个百分点降至0.00个百分点，但最终平均准确率从93.04%降至88.48%，显示明确的保留性—可塑性权衡。理论上，接受更新在覆盖与Lipschitz假设下获得均匀行为散度界，压缩锚点将界扩展为ε+L(ρ+η)，序列组合界则表明逐次可接受更新仍可能累积退化。

### 四、结论（Conclusion）
CABA为暴露可比策略分布和声明更新路径的候选生成器提供可审计的保留性门控，其有限检查适合作为部署前的第二把钥匙，但不等同于当前任务效用、公平性、安全性或全局安全保证。部署时仍需在路径选择后用新鲜数据单独验证当前任务效用，并注意重复接受或拒绝反馈仍可能泄露锚点信息。

### 五、方法论与关键技术细节
实验每个进入训练组最多贡献256个表示作为未来锚点，总锚点数上限1280，候选训练从不使用CABA审计锚点，插值网格为{0,0.05,…,1}，采用最坏锚点而非平均散度，空锚点分数记为零，并可在有数值误差界e_num时要求估计散度加e_num不超过预算。理论关键点包括ρ-net覆盖、散度Lipschitz性、高概率覆盖所需的独立采样条件、压缩表示带来的η惩罚、网格分辨率下相对连续最优系数的损失，以及单调性仅对仿射softmax头插值成立而不保证一般LoRA因子插值。局限是锚点集完整性、覆盖假设、评估代码可信性和受保护支撑外风险均未由有限检查解决，也不能防御恶意候选或证明任务准确率保持。
