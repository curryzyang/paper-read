# TriRoute: Unified Learned Routing for Joint Adaptive Attention, Experts, and KV-Cache Allocation

- 区域：精读区
- 排名：2
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Andrii Balashov, Olena Ponomarova
- 机构：Ukrainian State University of Science and Technologies
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06601v1) · [PDF](https://arxiv.org/pdf/2607.06601v1)

## TLDR
TriRoute introduces a single learned controller that jointly decides attention mode, expert selection, and KV-cache bit-width for every token at every layer, using heterogeneous relaxation and coupling-aware balancing to achieve Pareto-dominant efficiency and tail-case robustness over independent MoD+MoE+KV-quantization combinations.

## Abstract
Conditional computation can decouple language model quality from per-token inference cost, yet leading techniques act on a single axis in isolation: Mixture-of-Experts (MoE) sparsifies the FFN, Mixture-of-Depths (MoD) skips whole transformer blocks, and KV-cache quantization compresses attention memory. We argue these three decisions (attention resolution, expert selection, and cache bit-width) are strongly coupled and should be made jointly: a token rare enough to warrant full attention may also need high-precision caching regardless of which expert processes it. We introduce TriRoute, a single lightweight controller shared across all three axes that, for every token at every layer, emits a coordinated policy: (i) an attention mode (skip/local/full), (ii) a sparse set of FFN experts (with a null expert recovering MoD), and (iii) a KV-cache bit-width. The controller trains end-to-end via a heterogeneous relaxation (Gumbel-Softmax with straight-through estimation for categorical decisions and load-balanced top-k gating for experts) under a Lagrangian budget constraint that turns the average compute and memory cost into a controllable knob. We identify a cross-axis routing-collapse cascade in naive joint training, where collapse on one axis propagates to the others, and address it with per-axis normalization and a coupling-aware balancing loss. On decoder-only models from 160M to 1.3B parameters at compute-optimal token counts, TriRoute Pareto-dominates the best independent MoD+MoE+KV-quantization combination at matched inference FLOPs and memory, while better preserving tail-case robustness on rare entities, code, and arithmetic that pure perplexity optimization erodes. Post-hoc analysis reveals interpretable structure: the controller allocates full attention and high-precision cache to sentence-initial positions, rare subwords, and named entities, while cheaply routing function words.


## 精读解读（中文）
### 一、研究动机
现有条件计算方法（如MoE、MoD和KV缓存量化）各自独立地作用于单一轴，但注意力分辨率、专家选择和缓存位宽这三个决策高度耦合，需要联合进行。本文提出TriRoute，一个轻量级控制器，为每个token每层输出协调策略，以在固定推理预算下更有效地分配计算和内存。

### 二、技术方案（Method）
TriRoute采用单一控制器，对每个token每层输出三个决策：注意力模式（跳过/局部/全局）、稀疏专家集（含空专家模拟MoD）和KV缓存位宽（2/4/8/16比特）。控制器通过端到端训练，使用异构松弛：类别决策用Gumbel-Softmax和直通估计，专家选择用负载平衡top-k门控。训练时引入拉格朗日预算约束将平均计算和内存成本变为可控旋钮，并通过每轴归一化和耦合感知平衡损失解决跨轴路由崩溃级联问题。模型在160M-1.3B参数的仅解码器架构上训练，使用计算最优token数。

### 三、结果（Result）
在匹配推理FLOPs和内存时，TriRoute帕累托支配最佳独立MoD+MoE+KV量化组合，并在稀有实体、代码和算术等尾案例上更好保留鲁棒性，而纯困惑度优化会损伤这些尾案例。后验分析显示控制器学习到可解释结构：在句首位置、稀有子词和命名实体上分配全注意力和高精度缓存，而功能词则廉价路由。

### 四、结论（Conclusion）
联合学习注意力、专家和缓存分配比三个独立手动调优机制更优，TriRoute提供了一种在固定推理预算下按需分配计算和内存的原理性方法。

### 五、方法论与关键技术细节
关键细节包括：异构松弛（Gumbel-Softmax与直通估计用于注意力模式与位宽，负载平衡top-k用于专家选择）；跨轴路由崩溃级联通过每轴归一化和耦合感知平衡损失缓解；单一预算约束通过在线调整拉格朗日乘子实现；训练时温度退火；注意力模式包含跳过、局部窗口和全局三种；KV位宽离散为2/4/8/16；算法复杂度与标准MoE相当，但需要额外控制器参数（轻量级）。局限性在于控制器需要端到端训练，且在大规模部署中可能增加调度复杂度。
