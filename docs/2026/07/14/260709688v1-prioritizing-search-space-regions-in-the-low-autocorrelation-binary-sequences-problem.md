# Prioritizing Search Space Regions in the Low Autocorrelation Binary Sequences Problem

- 区域：精读区
- 排名：10
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Blaž Pšeničnik, Borko Bošković, Jan Popić, Janez Brest
- 机构：University of Maribor
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09688v1) · [PDF](https://arxiv.org/pdf/2607.09688v1)

## TLDR
This paper introduces a hybrid search framework that uses Thompson sampling to dynamically allocate computational effort across restriction classes in the low autocorrelation binary sequences problem, achieving new best-known merit factors for long sequences.

## Abstract
Low autocorrelation binary sequences problem (LABS) is a hard combinatorial optimization challenge with important applications in communications, signal processing, and satellite navigation. This paper proposes a hybrid search framework that combines Thompson sampling with parallel self-avoiding walks to adaptively allocate computational effort across restriction classes of the LABS search space. By modeling partitions as arms in a multi-armed bandit setting, the proposed method dynamically shifts search resources toward partitions that empirically produce higher merit factors while maintaining exploration of less-sampled regions. The approach is further accelerated through GPU-parallel execution, shared posterior updates, efficient neighborhood evaluation, and a Bloom filter for cycle prevention. In addition, we use a two-stage optimization strategy that first searches constrained partitioned skew-symmetric spaces and then refines the best candidates in the unrestricted space. Experiments on long binary sequences show that the proposed method improves the previously best-known results for 35 sequence lengths in the range $450 \le L \le 527$ and for $L=573$. In particular, we report a new longest sequence with merit factor exceeding $8.0$, obtained for $L=451$. The results also show that Thompson sampling effectively prioritizes partitions with better observed performance, confirming the value of online, data-driven resource allocation in LABS optimization. Overall, the proposed framework provides a scalable and effective strategy for high-performance merit factor maximization.


## 精读解读（中文）
### 一、研究动机
低自相关二进制序列问题（LABS）的搜索空间随序列长度指数增长，现有方法难以在探索与利用之间取得平衡，且静态分区优先级策略无法适应搜索过程中的动态变化。因此，需要一种在线、自适应的资源分配方法，优先处理有希望的分区，提高高品质因子序列的搜索效率。

### 二、技术方案（Method）
提出混合搜索框架，将搜索空间划分为限制类（分区），每个分区作为多臂赌博机的一个臂。使用Thompson采样在线选择分区，动态分配计算资源。每个选中的分区上并行执行多个自避行走，行走过程使用GPU加速，并采用共享后验更新、线性时间翻转邻域评估和Bloom过滤器防止循环。采用两阶段优化：首先在约束的偏斜对称空间中搜索（分区长度p，固定前p个元素，利用偏斜对称性），然后对最佳候选在无约束空间中精炼。

### 三、结果（Result）
在长序列实验中，该方法改进了35个序列长度（450≤L≤527）以及L=573的先前最佳已知结果，并获得了新的最长序列（L=451）其品质因子超过8.0。Thompson采样有效优先选择了表现更好的分区，验证了在线数据驱动资源分配的价值。

### 四、结论（Conclusion）
提出的混合框架结合Thompson采样和并行自避行走，实现了可扩展且高效的高品质因子最大化策略，显著提升了LABS问题的搜索性能，并为其他组合优化问题中的动态资源分配提供了借鉴。

### 五、方法论与关键技术细节
数据输入为二进制序列长度L和分区集合（基于Dimitrov等人提出的限制类方法，使用最小势或归一化势排序）。建模上使用Beta分布作为Thompson采样的先验，每个臂的参数θ_k表示从分区获得的期望品质因子。自避行走并行执行，每个行走独立且共享全局后验更新。Bloom过滤器用于检测和避免搜索循环。两阶段优化先利用偏斜对称性（奇数长度L=2k+1）将搜索空间减半，再在无约束空间进行局部搜索。复杂度上，并行化实现了数百倍加速，但Thompson采样引入的额外开销较低。局限性：分区的先验选择依赖人工设定，且对极长序列（如L>600）仍可能因搜索空间过大而难以找到全局最优。
