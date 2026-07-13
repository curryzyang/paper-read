# Sticky Routing: Training MoE Models for Memory-Efficient Inference

- 区域：精读区
- 排名：7
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Ali Kayyam
- 机构：BrainChip Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08780v1) · [PDF](https://arxiv.org/pdf/2607.08780v1)

## TLDR
StickyMoE introduces a differentiable routing consistency loss that penalizes abrupt expert switches between adjacent tokens during pretraining, reducing expert switch rates by up to 60% and cache misses by up to 3.92× with minimal perplexity degradation, thereby enabling memory-efficient MoE inference without architectural changes.

## Abstract
Mixture-of-Experts (MoE) models activate only a sparse subset of experts per token, yet consecutive tokens frequently activate different experts -- causing constant weight swapping between slow storage and fast memory on edge devices. Existing remedies are either system-level (caching heuristics) or post-hoc (router fine-tuning), leaving the root cause unchanged during pretraining. We propose StickyMoE, a differentiable routing consistency loss that penalises abrupt expert switches between adjacent tokens, encouraging the router to maintain the same expert assignment across semantically coherent spans. StickyMoE requires no architectural changes, adds a single hyperparameter lambda, and unlike post-hoc methods, allows expert representations and routing decisions to co-adapt from the first training step. Experiments on small-scale MoE language models show that StickyMoE reduces the expert switch rate by up to 60% with less than 4% perplexity degradation, Pareto-dominating post-hoc fine-tuning on the quality-locality frontier. Routing temporal locality is most efficiently instilled at training time.


## 精读解读（中文）
### 一、研究动机
MoE模型在边缘设备上存在严重的专家交换问题：由于路由器独立地为每个token选择专家，相邻token频繁激活不同专家，导致推理时不断从慢速存储加载专家权重到快速内存，造成显著的延迟瓶颈。现有解决方案要么是系统级的缓存启发式方法，只能被动利用局部性；要么是后处理的路由器微调方法，但专家表示已在训练中固化，无法从根本上解决不匹配问题。因此，需要一种在预训练阶段就显式优化路由时间局部性的方法。

### 二、技术方案（Method）
提出StickyMoE方法，其核心是添加一个可微分的路由一致性损失函数：对于每个MoE层，计算相邻token的softmax门控概率向量之间的L2距离，并在序列长度和层数上平均，形成一致性损失L_cons。总训练损失为L_CE + λ L_cons + μ L_bal，其中L_CE为标准交叉熵语言建模损失，L_bal为负载均衡损失，λ为单个超参数（如λ=0.1）。方法不改变MoE架构，仅需在训练时计算该损失并反向传播，梯度同时更新路由器权重和隐藏表示，使得专家表示与路由决策从训练第一步起共同适应局部一致性。还提出了一个软-硬变体，添加段级锚定约束以应对长程漂移。训练数据使用WikiText-2，模型为小型（4层，4专家）和中型（6层，8专家）MoE语言模型。

### 三、结果（Result）
在小型MoE模型上，StickyMoE将专家切换率降低高达60%，且困惑度退化小于4%；在中型模型上，不仅降低了切换率，还改善了困惑度（优于基线）。缓存未命中次数减少最多3.92倍。在质量-局部性前沿上，StickyMoE优于后处理微调方法（ReMoE）和简化的Oracle-MoE实现，实现了Pareto优势。专家利用率熵保持在1.92比特以上（最大2.0比特），证明一致性损失未导致专家坍塌。

### 四、结论（Conclusion）
路由时间局部性最有效的注入方式是在训练阶段。StickyMoE通过简单的可微损失实现了显著的专家切换率和缓存未命中降低，无需修改架构，且与系统级方法互补。实验表明，协同训练专家表示和路由决策比后处理微调更有效，为边缘设备上的高效MoE推理提供了一种实用且通用的解决方案。

### 五、方法论与关键技术细节
数据：使用WikiText-2训练小/中型MoE语言模型。损失：L_cons为相邻门控向量的L2距离（取值[0,2]），λ为超参数（实验中使用λ=0.1或其他值），与交叉熵和负载平衡损失联合优化。超参：仅λ一个额外超参数，负载平衡损失权重μ保持标准值。复杂度：计算开销可忽略（仅增加一个向量距离计算），无需存储额外参数。局限性：方法需要从零训练，无法直接应用于预训练好的MoE检查点；软-硬变体可能增加少量训练复杂度；长序列上的局部性保持需要进一步验证（但软-硬变体已部分解决）。
