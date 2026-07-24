# SOAP, Muon, and Beyond: Pushing LLM Pretraining Scales

- 区域：精读区
- 排名：10
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Mikail Khona, Aditya Vavre, Boxiang Wang, Deyu Fu, Hao Wu, Mike Chrzanowski, Bryan Catanzaro, Dheevatsa Mudigere, Jeff Pool, Michael Lightstone, Mohammad Shoeybi, Mostofa Patwary, Nima Tajbakhsh, Tijmen Blankevoort
- 机构：NVIDIA
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20548v1) · [PDF](https://arxiv.org/pdf/2607.20548v1)

## TLDR
This paper adapts and scales higher-order optimizers SOAP and Muon for LLM pretraining by fixing instabilities with per-step QR orthogonalization and improved preconditioning, demonstrating their consistent performance advantage over AdamW at up to 100M-token batch sizes, and introduces a scalable layer-wise distributed optimizer implementation.

## Abstract
Higher-order optimizers such as Muon and SOAP offer faster convergence than AdamW, but their computational cost and numerical stability challenges have limited adoption at scale. In this work, we adapt and enhance preconditioned gradient methods to overcome the practical challenges of large-scale LLM pretraining. We first identify instabilities in SOAP at large batch sizes and propose algorithmic modifications including per-step QR orthogonalization and improved preconditioning strategies that eliminate loss spikes and enable stable training in these regimes. We then present a unified empirical study of SOAP, Muon, and AdamW using update-RMS matching to ensure fair learning rate transfer across optimizers. As part of this analysis, we empirically evaluate the orthogonalization quality of Muon. Our experiments on multi-billion-parameter models trained on trillions of tokens reveal that SOAP and Muon consistently outperform AdamW at the scales we tested. Notably, at batch sizes of up to 100M tokens for next-token prediction, these optimizers maintain training stability and quality while AdamW degrades. To enable efficient training at large scale, we introduce a layer-wise distributed optimizer compatible with Megatron-LM. Our implementation balances memory and hides communication while avoiding approximations to the optimizer computations, thus retaining their convergence benefits. Additionally, we identify and build specific system-level improvements to further accelerate our layer-wise implementation. To support the research community, we release a codebase that contains emerging algorithms for optimization: https://github.com/NVIDIA-NeMo/Emerging-Optimizers


## 精读解读（中文）
### 一、研究动机
高阶优化器如Muon和SOAP在收敛速度上优于AdamW，但其计算成本和数值不稳定性限制了大规模LLM预训练中的实际应用。本文旨在通过改进预条件梯度方法，克服这些挑战，实现稳定且高效的大规模训练。

### 二、技术方案（Method）
首先，识别SOAP在大批量训练中的不稳定性，通过每步QR正交化和改进的预条件策略消除损失尖峰。采用更新均方根匹配框架实现AdamW、Muon和SOAP之间的公平学习率迁移。针对多亿参数模型（8B密集GPT、3B/30B MoE、8B/72B混合Mamba-Transformer MoE）在数万亿token上实验。引入与Megatron-LM兼容的逐层分布式优化器，平衡内存并隐藏通信，同时避免近似计算以保留收敛优势。系统层面进一步加速实现。

### 三、结果（Result）
在多亿参数模型上，SOAP和Muon在所有测试规模下均持续优于AdamW。当全局批量达到100M tokens时，SOAP和Muon保持训练稳定性和质量，而AdamW性能显著下降。KL-SOAP略优于Muon。

### 四、结论（Conclusion）
通过算法改进和系统优化，SOAP和Muon能够在大规模LLM预训练中稳定超越AdamW，尤其在大批量场景下。逐层分布式优化器使得这些高阶优化器在现实生产规模中可行。

### 五、方法论与关键技术细节
SOAP的数值不稳定性源于预条件器与梯度统计之间的滞后，在批量≥100M时尤其明显，通过每步QR正交化和KL散度协方差估计解决。Muon使用Newton-Schulz迭代（迭代次数影响计算成本）近似极分解，不维护二阶矩。层式分布式优化器将不同层的参数分布到不同数据并行节点，避免切分矩阵，但需额外通信进行全参数收集。学习率按平方根规则缩放批量大小。MoE模型中，专家参数有效批量较低，压力集中在密集组件。局限包括对大模型高计算开销和超参数敏感性。
