# Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- 区域：精读区
- 排名：5
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Aiden Swann, Mozes Jacobs, Mathilde Papillon, Siddharth Boppana, David Chanin, Dron Hazra, Usha Bhalla, Curt Tigges, Mac Schwager, Owen Lewis, Jack Merullo, Ekdeep Singh Lubana, Atticus Geiger, Thomas Fel, Matthew Kowal
- 机构：Goodfire, Harvard University, Stanford University, University of California, Santa Barbara
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20767v1) · [PDF](https://arxiv.org/pdf/2610.20767v1)

## TLDR
Block-sparse featurizers uncover multi-dimensional, task-relevant features in robot foundation models that enable fine-grained behavioral steering and targeted training-data attribution.

## Abstract
Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an interpretable interface for steering vision-language-action models and shaping the data from which they learn. We show that BSFs recover several multi-dimensional task-relevant features underlying the model's computation (e.g., perception, language, proprioceptive state, episode phase, and control variables). We causally validate these features through fine-grained steering: targeted changes in visual perception, semantic representation, and spatial localization produce predictable changes in downstream action prediction. Finally, we use feature-based data attribution to isolate where a specific behavior (failure recovery) arises in the training dataset, identifying fewer than $1.4\%$ of training tokens whose masking is sufficient to remove the targeted behavior. Overall, our results show how matching featurizers to representation geometry can provide more effective tools for understanding and changing robot behavior.


## 精读解读（中文）
### 一、研究动机
理解 VLA 内部表示对安全部署至关重要，但现有稀疏自编码器（SAE）依赖线性表示假设，可能难以匹配机器人视觉、状态与控制中连续、低维的表示流形。本文动机是检验多维 featurizer 能否为机器人基础模型提供可解释、可因果干预并可用于数据塑造的接口。

### 二、技术方案（Method）
方法上，作者在开源 VLA 的未池化图像、文本和状态 token 激活上训练 block-sparse featurizers（BSF）与匹配的 TopK SAE 基线，BSF 将每个特征建模为低维 block 子空间，编码器为 z=Pi_topk(xW+b)，按 block 的 L2 范数保留 k 个整块，BatchTopK 按范数与解码器尺度评分，解码为各活跃 block 子空间之和。训练目标包括标准平方重建损失，并平行评估功能重建，即用动作 token 教师强制对数似然对激活的梯度构造经验 Fisher 矩阵，惩罚会改变下游动作的激活误差。随后在多个层进行因果 steering，对感知、语义和目标空间定位等变量做定向干预，并用基于特征的数据归因追踪行为到训练 token。SAE 基线使用相同数据和流程，唯一关键差别是 block 维度为 1。

### 三、结果（Result）
结果上，BSF 恢复了感知、语言、本体感觉状态、任务阶段和控制变量等多维任务相关特征，并在多个层上实现细粒度因果 steering：改变视觉感知、语义表示或空间定位会可预测地改变下游动作预测。定量上，BSF 在恢复和干预任务相关结构方面优于匹配 SAE，说明低维子空间几何带来额外收益而非单纯容量。案例研究中，基于 failure-recovery 特征的训练数据归因发现，仅掩码少于 1.4% 的训练 token 就足以移除目标失败恢复行为。这表明方法可定位行为来源并反向塑造数据。

### 四、结论（Conclusion）
结论是，将 featurizer 的归纳偏置与 VLA 表示的低维、多变量几何相匹配，比单方向 SAE 更适合发现、干预和塑造机器人基础模型行为。该工作为 VLA 可解释性、细粒度控制和数据整理提供了统一工具。

### 五、方法论与关键技术细节
关键实现细节包括：训练语料保留每个图像、文本、状态 token 作为独立激活，规模约 5200 万未池化激活，避免先前均值池化或小语料限制；BSF 采用组稀疏而非坐标稀疏，块内坐标有符号且无逐坐标非线性，b=1 时退化为 TopK SAE，对比时匹配活跃特征数或活跃坐标预算。损失同时考察普通重建与 Fisher 加权功能重建，后者关注对动作预测有影响的误差方向。局限在于 block 维度只给出特征内在维度的上界，行为移除结论主要来自 failure-recovery 单案例，且需要与 SAE 在预算匹配下比较。
