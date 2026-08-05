# Output-Aware Rotation for INT2 KV-Cache Quantization

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Vincent-Daniel Yun, Woosang Lim, Minsoo Cheong, Sunwoo Lee, Murali Annavaram, Sai Praneeth Karimireddy, Sungjoo Yoo
- 机构：Seoul National University, University of Southern California, Inha University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02691v1) · [PDF](https://arxiv.org/pdf/2608.02691v1)

## TLDR
OptR is an output-aware rotation method for INT2 KV-cache quantization that learns per-head orthogonal corrections to minimize post-attention-output projection error, consistently improving existing rotation-based pipelines like QuaRot and OSCAR across reasoning and coding benchmarks.

## Abstract
The key-value (KV) cache has become a major memory and bandwidth bottleneck in long-context large language model inference, making ultra-low-bit quantization increasingly important. However, existing rotation-based INT2 methods optimize cache statistics or proxy errors before the complete attention readout, even though the model is ultimately affected by the error propagated through attention and the output projection $W_O$. To address this mismatch, we propose \textit{OptR}, an output-aware rotation method that minimizes post-$W_O$ attention-output error. OptR decomposes the post-$W_O$ attention-output error into key- and value-induced terms and learns per-head orthogonal corrections through the full INT2 quantization and attention path. OptR further applies an attention-equivalent key reparameterization to reduce large channel-wise offsets without changing the softmax distribution. Across three models and five reasoning and coding benchmarks, OptR consistently improves both QuaRot and OSCAR and strengthens long-context retrieval, while preserving the paged KV-cache format with negligible inference overhead.
