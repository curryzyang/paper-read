# Density Feedback Control for Transferability of Generative Sparse Adversarial Attacks

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Dongsu Song, Jay Hoon Jung
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25001v1) · [PDF](https://arxiv.org/pdf/2611.25001v1)

## TLDR
**TLDR:** Density Feedback Control (DFC) dynamically adjusts the sparsity coefficient each epoch based on the gap between observed and target perturbation density, allowing generator-based sparse adversarial attacks to hit a desired density in one run without changing the generator or loss and improving transfer attack success for several base attacks.

## Abstract
Generator-based sparse adversarial attacks train encoder--decoder networks to produce transferable sparse perturbations for black-box robustness evaluation. Their perturbation density, however, is set only indirectly by a fixed sparsity coefficient whose mapping to density is unknown and shifts during training, so reaching a target density requires re-tuning; this fixed pressure also yields little transferability gain once density reduction begins. We propose Density Feedback Control (DFC), which tightens or relaxes this coefficient at the end of each epoch according to the gap between the observed hard-mask density and the target, without changing the generator architecture or loss. At a 10\% target density, DFC brings the mean density of three base attacks within one percentage point of the target in a single run and improves the transfer attack success rate (ASR) of two of them on CNN and Transformer targets, including under per-image $\ell_0$ budgets, while perturbing fewer pixels. Tracing GPG's training, we observe that as DFC relaxes the coefficient, the transfer ASR recovers with the density and overtakes the fixed-coefficient baseline with fewer pixels. For EGS-TSSA, which restricts perturbations to source-model feature-importance regions, DFC yields no consistent gain; we analyze how this restriction interacts with density feedback.


## 精读解读（中文）
### 一、研究动机
基于生成器的稀疏对抗攻击通过编码器—解码器网络生成可迁移稀疏扰动，但其扰动密度仅由固定稀疏系数间接控制，该系数与密度的映射未知且会在训练中漂移，导致达到目标密度需要反复调参；同时固定压力在密度下降后带来的迁移性收益有限。

### 二、技术方案（Method）
论文提出密度反馈控制（DFC）：在每轮训练结束时计算生成扰动硬掩码的实际密度与目标密度之间的差距，并据此收紧或放松稀疏系数，下一轮继续训练；该方法不改变生成器架构，也不改变原有损失函数，仅对稀疏系数做轮级反馈调节，从而在单次训练中把硬掩码密度推向目标值。

### 三、结果（Result）
在10%目标密度下，DFC在单次运行中使三个基础攻击的平均密度进入目标值一个百分点以内，并提升其中两个攻击在CNN与Transformer目标模型上的迁移攻击成功率，包括逐图像ℓ0预算场景，同时扰动像素更少；追踪GPG训练可见，随着DFC放松系数，迁移ASR随密度恢复并超过固定系数基线且使用更少像素。

### 四、结论（Conclusion）
DFC通过密度反馈直接控制生成式稀疏攻击的扰动密度，在不改网络与损失的情况下改善密度可控性和迁移性，并减少像素扰动；但对于将扰动限制在源模型特征重要性区域的EGS-TSSA，DFC没有稳定增益，说明该区域限制会与密度反馈产生交互并限制其效果。

### 五、方法论与关键技术细节
关键实现是以硬掩码密度作为反馈信号，在每个epoch末根据观测密度与目标密度的差距调节稀疏系数；实验围绕10%目标密度、三个基础攻击、CNN和Transformer目标以及逐图像ℓ0预算展开，强调单次运行达到目标密度并减少扰动像素；局限性在于EGS-TSSA的源模型特征重要性区域限制与密度反馈的交互会导致不一致收益。
