# On-Policy Residual Learning for Diffusion Language Models

- 区域：精读区
- 排名：3
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Yifan Yu, Yuqing Jian, Jisen Li, Yuezhou Hu, Tianyi Zhang, Xiaoxia Wu, Rui-Jie Zhu, Junxiong Wang, Zhongzhu Zhou, Fan Lai, James Zou, Chenfeng Xu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20687v1) · [PDF](https://arxiv.org/pdf/2610.20687v1)

## TLDR
The paper introduces ORL, an on-policy residual learning framework for diffusion language models that learns from model-induced residual trajectories via an entropy-contraction objective and systems co-design, enabling up to 6.9x higher end-to-end throughput at comparable or better quality.

## Abstract
Residual context is key to unlocking the speed-quality Pareto frontier of diffusion language models (DLMs) by carrying forward predictive distributions across denoising steps. Yet turning this seemingly simple mechanism into an effective learning paradigm is far from simple: there is no clear recipe for how residual context should be learned. We introduce ORL, a framework for on-policy residual learning in DLMs. Algorithmically, we identify that residual learning is inherently on-policy. ORL learns from model-induced residual trajectories on the fly and introduces an entropy-contraction objective that sharpens predictions as the model revisits its own predictions. System-wise, exact residual supervision requires capturing, retaining, and reprocessing many trajectory-dependent states. ORL co-designs the algorithm with asynchronous residual capture and transport, specialized block-diffusion attention, and packed compute-balanced training, making it practical at scale. On a 4B DLM converted from Qwen3-4B, ORL improves tokens per forward (TPF) by up to 6.2x and, with our dlmrt engine, end-to-end throughput by approximately 6.9x at comparable or better quality. In single-request serving on one H100, this mode achieves a stronger speed-quality Pareto frontier than autoregressive models with EAGLE3 and DFlash speculative decoding under both strict and relaxed verification, running 1.74x faster than DFlash at matched accuracy. ORL also transfers to existing DLMs: on LLaDA-2.1-mini, 36 H100-hours and 4.2M self-generated tokens, about 10x less data than prior LLaDA recipes, yield up to 1.5x higher TPF and up to 3x higher throughput at comparable quality, and on DiffusionGemma, ORL raises TPF by 1.1-1.2x. With dlmrt and NVFP4 quantization, ORL models decode a single request at up to 5,046 tokens/s on one B200, 7,708 on eight B200s, and 2,788 on a consumer RTX 5090, with comparable quality.


## 精读解读（中文）
### 一、研究动机
残差上下文是解锁扩散语言模型速度-质量帕累托前沿的关键，因为它能在去噪步之间携带预测分布；然而如何有效学习残差上下文尚无明确配方，现有机制难以直接转化为可扩展的学习范式。ORL 旨在回答扩散语言模型中残差学习应如何建模与训练，并解决其在大规模系统实现上的瓶颈。

### 二、技术方案（Method）
ORL 以扩散语言模型为基座，将前序去噪步的预测分布作为 residual context 在步间传递，并把残差学习形式化为 on-policy 问题：训练数据并非固定离线轨迹，而是由当前模型在线诱导的 residual 轨迹构成。算法上引入熵收缩目标，让模型在重访自身预测时逐步锐化预测分布；系统上协同设计异步残差捕获与传输、面向块扩散的专用注意力以及打包计算均衡训练，以支持对轨迹相关状态的精确残差监督。推理阶段通过 dlmrt 引擎执行块扩散解码，可结合 NVFP4 量化部署。

### 三、结果（Result）
在由 Qwen3-4B 转换得到的 4B DLM 上，ORL 将 tokens per forward（TPF）最高提升 6.2 倍，配合 dlmrt 引擎端到端吞吐最高提升约 6.9 倍，质量相当或更好。单请求 H100 服务下，其速度-质量帕累托前沿优于带 EAGLE3 与 DFlash 投机解码的自回归模型，在严格与宽松验证下均成立，匹配精度时比 DFlash 快 1.74 倍。迁移到 LLaDA-2.1-mini 时，仅用 36 H100 小时和 4.2M 自生成 token（约为此前 LLaDA 配方数据的十分之一）即获得最高 1.5 倍 TPF 与最高 3 倍吞吐提升，质量相当；在 DiffusionGemma 上 TPF 提升 1.1-1.2 倍。结合 dlmrt 与 NVFP4 量化，ORL 模型单请求解码在单张 B200 上最高 5,046 tokens/s，八张 B200 上 7,708 tokens/s，消费级 RTX 5090 上 2,788 tokens/s，质量相当。

### 四、结论（Conclusion）
ORL 表明残差学习本质上是 on-policy 的，并通过熵收缩目标与系统级协同设计把这一范式做到可扩展、可部署。它显著推进了扩散语言模型的速度-质量前沿，并能在不同 DLM 与硬件/量化设置下迁移，说明该方法对实际服务具有通用价值。

### 五、方法论与关键技术细节
关键实现包括：以模型自身在线生成的 residual 轨迹进行训练，避免离线残差监督的分布偏移；采用熵收缩目标在重访自身预测时锐化分布；系统上使用异步残差捕获与传输、块扩散专用注意力和 packed compute-balanced 训练来处理大量轨迹相关状态。评测模型涵盖 Qwen3-4B 转换的 4B DLM、LLaDA-2.1-mini 与 DiffusionGemma，指标为 TPF、端到端吞吐、严格/宽松验证下的速度-质量帕累托前沿；训练数据方面 LLaDA-2.1-mini 仅用 4.2M 自生成 token 与 36 H100 小时，约为此前配方十分之一。部署涉及 dlmrt 引擎与 NVFP4 量化，硬件包括 H100、B200 和 RTX 5090；主要代价或约束在于精确残差监督需捕获、保留并重处理轨迹相关状态，且收益依赖系统协同与量化部署。
