# TriRoute: Unified Learned Routing for Joint Adaptive Attention, Experts, and KV-Cache Allocation

- 区域：精读区
- 排名：7
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Andrii Balashov, Olena Ponomarova
- 机构：Ukrainian State University of Science and Technologies
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06601v1) · [PDF](https://arxiv.org/pdf/2607.06601v1)

## TLDR
TriRoute introduces a single lightweight controller that jointly learns per-token decisions over attention resolution, FFN expert selection, and KV-cache bit-width under a unified compute-memory budget, Pareto-dominating independent combinations of MoD, MoE, and KV-quantization while better preserving tail-case accuracy.

## Abstract
Conditional computation can decouple language model quality from per-token inference cost, yet leading techniques act on a single axis in isolation: Mixture-of-Experts (MoE) sparsifies the FFN, Mixture-of-Depths (MoD) skips whole transformer blocks, and KV-cache quantization compresses attention memory. We argue these three decisions (attention resolution, expert selection, and cache bit-width) are strongly coupled and should be made jointly: a token rare enough to warrant full attention may also need high-precision caching regardless of which expert processes it. We introduce TriRoute, a single lightweight controller shared across all three axes that, for every token at every layer, emits a coordinated policy: (i) an attention mode (skip/local/full), (ii) a sparse set of FFN experts (with a null expert recovering MoD), and (iii) a KV-cache bit-width. The controller trains end-to-end via a heterogeneous relaxation (Gumbel-Softmax with straight-through estimation for categorical decisions and load-balanced top-k gating for experts) under a Lagrangian budget constraint that turns the average compute and memory cost into a controllable knob. We identify a cross-axis routing-collapse cascade in naive joint training, where collapse on one axis propagates to the others, and address it with per-axis normalization and a coupling-aware balancing loss. On decoder-only models from 160M to 1.3B parameters at compute-optimal token counts, TriRoute Pareto-dominates the best independent MoD+MoE+KV-quantization combination at matched inference FLOPs and memory, while better preserving tail-case robustness on rare entities, code, and arithmetic that pure perplexity optimization erodes. Post-hoc analysis reveals interpretable structure: the controller allocates full attention and high-precision cache to sentence-initial positions, rare subwords, and named entities, while cheaply routing function words.


## 精读解读（中文）
### 一、研究动机
现有的条件计算方法如混合专家（MoE）、混合深度（MoD）和KV缓存量化各自独立地在单一轴上优化，但注意力分辨率、专家选择和缓存位宽这三个决策是紧密耦合的：一个稀有 token 可能需要充分注意力但跳过FFN，而功能词则相反。因此需要联合学习一个统一的控制器来协调这些异质资源，以在固定推理预算下实现最优质量。

### 二、技术方案（Method）
TriRoute 是一个轻量级共享控制器，对每个 token 的每一层输出协调策略：(i) 注意力模式（skip/local/full），(ii) 稀疏 FFN 专家集合（含空专家以恢复 MoD），(iii) KV 缓存位宽（2/4/8/16）。训练采用异构松弛：类别决策用 Gumbel-Softmax 加 straight-through 估计，专家选择用负载均衡 top-k 门控。整体在拉格朗日预算约束下与语言建模目标端到端联合训练，该约束将平均计算和内存成本转化为可控旋钮。针对跨轴路由崩溃级联（一个轴崩溃导致其他轴退化），引入每轴归一化和耦合感知平衡损失来稳定训练。

### 三、结果（Result）
在 160M 到 1.3B 参数的解码器模型上（训练于计算最优 token 数），TriRoute 在匹配推理 FLOPs 和内存下帕累托支配最佳独立组合（MoD+MoE+KV量化）。更重要的是，它更好地保留了稀有实体、代码和算术等尾部案例的鲁棒性，而单纯优化困惑度的方法会侵蚀这些能力。后验分析显示控制器学习到可解释结构：将全注意力和高精度缓存分配给句首、稀有子词和命名实体，而对功能词使用廉价路由。

### 四、结论（Conclusion）
共享的控制器比三个独立调优的机制更原则性地将固定推理预算花在最重要的地方。结果表明，一个统一的端到端学习的控制器能够自然地捕捉注意力和缓存精度与专家选择之间的耦合，实现比独立机制更优的权衡。

### 五、方法论与关键技术细节
数据规模：decoder-only 模型，参数 160M–1.3B，训练于计算最优 token 数。先验：空专家恢复 MoD 行为。损失函数：耦合感知平衡损失抑制跨轴崩溃，拉格朗日预算约束控制平均成本。超参：每轴温度退火，梯度归一化处理异质决策空间。复杂度：跨轴路由级联崩溃通过每轴归一化和耦合感知损失缓解。局限性：共享路由器在高稀疏度下可能引入干扰（路由表征共享在高稀疏时效果下降）。
