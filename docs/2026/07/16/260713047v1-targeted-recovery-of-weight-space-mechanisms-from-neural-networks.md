# Targeted Recovery of Weight-Space Mechanisms From Neural Networks

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Antoine Vigouroux, Lee Sharkey
- 机构：Goodfire, MATS
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13047v1) · [PDF](https://arxiv.org/pdf/2607.13047v1)

## TLDR
The paper introduces targeted parameter decomposition (tPD), which efficiently identifies interpretable neural network components for specific inputs of interest by introducing a high-rank catch-all component for non-target data, enabling scalable mechanistic interpretability with reduced compute.

## Abstract
Parameter decomposition (PD) decomposes neural networks into interpretable computational components that faithfully reflect the original network's operations. However, scaling PD to large models requires vast compute, making it a costly and risky endeavor. Here we propose targeted PD (tPD), which identifies only the components that process specific inputs of interest -- from isolated prompts to large subtasks -- by introducing a high-rank catch-all component that handles all non-target data. We validate tPD on toy models and on transformer language models trained on The Pile, where it recovers reproducible, mechanistically faithful circuits. We extract a CSS-only submodel of a 4-block transformer using 7% of the FLOPs of its published decomposition, and in a 12-block transformer we surgically ablate and rewire memorized sequences, with negligible side effects on other inputs.


## 精读解读（中文）
### 一、研究动机
全参数分解（PD）将神经网络分解为可解释的计算组件，但扩展到大型模型需要巨大计算量，成本高昂且风险高。因此提出针对性参数分解（tPD），仅识别处理特定输入（从孤立提示到大型子任务）的机制，通过引入高秩catch-all组件处理所有非目标数据，大幅降低计算需求。

### 二、技术方案（Method）
tPD使用两个并行数据流：目标数据集（需解释的输入）和非目标流（模型原始训练分布采样）。分解模型由rank-1子组件和全秩catch-all组件Δ组成，其中Δ定义为原始权重与子组件之和的残差。训练时，目标数据必须仅由稀疏子组件重建（Δ组件被对抗性消融0-100%），而非目标数据则始终使用Δ组件及可选的子组件。重要性最小化损失同时作用于两个流，确保非目标机制被移入Δ，而处理目标数据的子组件不干扰非目标数据。为保持机械忠实，还通过对抗性消融（同时消融非活动组件和Δ）最大化重建损失，迫使模型输出在混合权重矩阵下不变。

### 三、结果（Result）
在玩具模型（TMCC）上，tPD针对3个输入特征的目标仅需500步收敛（全模型需2500步），且正确恢复地面真相机制。在4-block Pile transformer上，针对'import numpy as'和'import pandas as'的分解，不同随机种子间V向量（输入方向）高度相似，嵌套目标分解中77个子组件有69个匹配。提取CSS-only子模型（1638个组件，占全分解7% FLOPs），其CSS数据KL散度约0.6，其他语言KL≥2。在12-block transformer（85M参数）上，消融np/pd特定子组件可精准擦除对应知识（KL<1e-2），通过交换U方向可重写记忆（import numpy as预测为pd），且副作用极小。

### 四、结论（Conclusion）
tPD是PD的针对性变体，能以极低成本恢复机械忠实的分解，支持子组件消融和重写等干预，适用于窄范围可解释性（电路定位、遗忘、编辑）。但需注意：子组件仅处理目标数据激发的激活子空间，编辑案例较为简单（短记忆序列），冗余机制可能被Δ吸收，且当前模型规模仍远小于前沿模型。

### 五、方法论与关键技术细节
数据：目标数据需精心选择以完整捕获感兴趣行为，非目标数据来自原始训练分布（如The Pile）。先验：假设机制可分解为rank-1子组件，每个子组件实现单一功能角色。损失：包括重建损失、重要性最小化损失（L0稀疏性）、以及对抗性消融损失（确保机械忠实）。超参：子组件槽位数可远小于全模型（如TMCC从100降至5），Δ对抗性消融比例每批次随机0-100%。复杂度：tPD计算成本仅为全分解的一小部分（4-block transformer用7% FLOPs），但子组件可能不直接等价于全分解组件。局限性：神经网络常使用冗余机制，tPD可能丢失部分机制；编辑实验仅针对短记忆序列，世界知识编辑需要更复杂工程；尚未在更大模型上验证。
