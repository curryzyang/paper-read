# Structured Latent Space Modeling over Multi-Scale Temporal Patches for Multivariate Time Series Forecasting

- 区域：精读区
- 排名：7
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Xingsheng Chen, Deyu Yi, Siu-Ming Yiu
- 机构：The University of Hong Kong, Macau University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19404v1) · [PDF](https://arxiv.org/pdf/2607.19404v1)

## TLDR
M2Patch introduces a CNN-based multivariate time series forecasting architecture that organizes multi-scale temporal patches into a structured latent space via intra-scale smoothness and inter-scale alignment constraints, achieving state-of-the-art accuracy with linear computational complexity.

## Abstract
Multivariate time series encode structural patterns that unfold across multiple temporal scales, yet most forecasting backbones treat learned representations as transient byproducts of prediction, leaving the organizational geometry of these patterns underexploited. We introduce M2Patch, a CNN-based forecasting architecture that maps channel-independent multivariate observations into a structured latent space through two complementary differentiable constraints. Multi-scale patching decomposes the input into overlapping temporal granularities; depthwise separable convolutions with progressive dilation extract scale-specific features in linear time; and per-scale learned projections compress these features into a compact latent representation. The latent space is organized by an intra-scale smoothness constraint that enforces temporal continuity between adjacent patches, and an inter-scale alignment constraint, realized through learnable cross-scale mappings, that restores cross-granularity interaction within the channel-independent design, ensuring that all scales encode mutually consistent representations of the underlying dynamics. Experiments on ten real-world benchmarks show that M2Patch achieves 57 best and 34 second-best results across 40 forecasting settings, matching or exceeding representative baselines on most benchmarks while maintaining linear computational complexity and robustness to patch-level input corruption.


## 精读解读（中文）
### 一、研究动机
现有时间序列预测方法大多将学习到的中间表示视为预测的副产品，忽略了多尺度时间模式的结构化组织。Transformer类方法具有二次复杂度，而现有的多尺度方法缺乏跨尺度一致性约束，限制了模型对内在动态的捕获能力。为此，我们提出M2Patch，通过CNN主干和结构化潜在空间约束，实现高效、鲁棒且可解释的多变量时间序列预测。

### 二、技术方案（Method）
输入为多元时间序列X∈R^{L×N}，先通过可逆实例归一化缓解分布偏移。然后执行多尺度分解：对K个尺度定义不同的patch长度和步长，生成重叠的patch序列。每个尺度独立地用线性嵌入+位置编码映射到d维空间。特征提取采用深度可分离卷积（depthwise temporal conv + pointwise feed-forward），每层膨胀率指数增长，形成层次化感受野。每个尺度的特征通过可学习的投影头压缩到低维潜在空间（维度d_m）。潜在空间受两个辅助损失约束：1）intra-scale smoothness：相邻patch的L2距离鼓励时间连续性；2）inter-scale consistency：通过可学习映射Φ将细尺度特征对齐到粗尺度，强制跨尺度一致性。总损失为预测损失（MSE）加上λ1L_intra和λ2L_inter。训练中所有模块联合反向传播。推理时仅使用预测分支。

### 三、结果（Result）
在10个真实世界基准数据集（涵盖电力、交通、天气、ECG等）的40个预测设定中，M2Patch取得了57个最佳和34个次佳结果，匹配或超过PatchTST、iTransformer、TimesNet等代表性基线。模型保持线性计算复杂度，并对patch级输入损坏具有鲁棒性。消融实验验证了多尺度分解和两个辅助损失的有效性。

### 四、结论（Conclusion）
M2Patch通过将多尺度时间patch组织在受可微分结构约束的潜在空间中，成功捕获了多变量时间序列的内在动态，将数据挖掘导向的结构先验转化为预测精度和鲁棒性的提升。该框架证明了CNN主干结合结构化正则化可以达到甚至超越复杂Transformer架构的性能，同时提供更好的可解释性和效率。

### 五、方法论与关键技术细节
数据：10个基准（含ETTh1、ETTm1、Weather、Electricity等），变量数从7到321。先验：局部性（平移等变）、多尺度耦合、时间连续性和跨尺度对齐。损失：预测MSE + λ1 L_intra（相邻patch间L2距离）+ λ2 L_inter（通过可学习映射对齐不同尺度特征）。超参数：尺度数K（默认3-5）、patch长度和步长、潜在维度d_m（默认32）、卷积层数E（默认3）、卷积核大小k（默认3）、膨胀率δ=2^{ℓ-1}、损失权重λ1=0.1, λ2=1.0。复杂度：在序列长度L、变量数N、patch数上均为线性O(L)。局限性：尺度数和损失权重需根据数据集调参；跨尺度映射增加了可学习参数；对于极长序列（>1000步），CNN感受野可能不如Transformer或SSM灵活。
