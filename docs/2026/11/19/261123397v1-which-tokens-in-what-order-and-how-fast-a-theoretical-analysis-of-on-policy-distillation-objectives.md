# Which Tokens, in What Order, and How Fast? A Theoretical Analysis of On-Policy Distillation Objectives

- 区域：精读区
- 排名：7
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Hubert Strauss, Liam Fowl, Noam Razin
- 机构：Princeton University, Bar-Ilan University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23397v1) · [PDF](https://arxiv.org/pdf/2611.23397v1)

## TLDR
This paper theoretically shows that sequence-level on-policy distillation introduces a future-agreement bias and reverse token-learning order that token-level objectives avoid, while the choice of divergence critically affects optimization behavior—with forward KL being better behaved than reverse KL—thereby guiding which OPD objective is appropriate for a given student–teacher–task setting.

## Abstract
On-policy distillation (OPD) trains a student language model to match a teacher model based on its own generations. When using OPD, one must choose whether to apply it at the sequence or token level and which divergence to minimize. However, despite the wide adoption of OPD in practice, the formal understanding of which OPD objective is appropriate for a given setting is limited. Toward addressing this gap, we theoretically analyze how the choice of OPD objective governs which tokens are prioritized, in what order, and how efficiently. Our analysis reveals that sequence-level OPD exhibits a future agreement bias, which myopic token-level objectives avoid. This bias induces a reverse learning order, in which sequence-level OPD first matches the teacher at later token positions, while at earlier positions it can favor tokens that are improbable under the teacher, and thus often undesirable. As for the choice of divergence, we prove that it strongly influences the amenability of OPD to gradient-based optimization. In particular, while the forward KL divergence enjoys a well-behaved objective landscape, other $f$-divergences, such as reverse KL, can suffer from vanishing gradients even when the student and teacher are far apart. Across language model post-training settings, we demonstrate the implications of these theoretical findings for which OPD objective is preferable, highlighting the importance of accounting for the interplay between the student, teacher, and task at hand.


## 精读解读（中文）
### 一、研究动机
On-policy distillation（OPD）已广泛用于语言模型后训练，但序列级与词元级目标以及散度函数的选择缺乏形式化理解；本文关注不同OPD目标如何决定优先匹配哪些词元、以何种顺序学习以及优化效率如何。

### 二、技术方案（Method）
本文将OPD建模为学生模型在其自身生成序列上匹配教师分布，系统比较序列级目标与myopic词元级目标，并对f-散度（包括前向KL与反向KL）分析目标景观和梯度性质；理论上刻画目标对词元位置与概率的加权、序列级未来一致性偏差及学习顺序，并在多种语言模型后训练设置中验证这些理论含义。

### 三、结果（Result）
分析表明序列级OPD存在未来一致性偏差，导致反向学习顺序：先匹配教师在后部词元的行为，而前部位置可能偏向教师低概率甚至不期望的词元；myopic词元级目标可避免该偏差。散度选择显著影响优化，前向KL具有较良好目标景观，而反向KL等f-散度即使学生与教师相距较远也可能出现梯度消失。

### 四、结论（Conclusion）
OPD目标不存在普适最优选择，需综合考虑学生、教师与具体任务的交互来决定序列级或词元级目标及散度函数；理论结果强调未来一致性偏差与梯度可优化性是后训练目标设计的关键因素。

### 五、方法论与关键技术细节
分析以学生自身生成序列和教师分布为输入，围绕序列级与词元级目标、f-散度（含前向KL、反向KL）及梯度行为展开；关键点包括myopic词元级分解、未来一致性偏差、反向学习顺序和梯度消失条件；局限在于结论依赖理论设定与假设，实验主要用于验证理论含义而非提出全新算法。
