# Stable FP4 Training via Transposition-Invariant Block Quantization

- 区域：速读区
- 排名：4
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Mehdi Rahimifar, Amin Darabi, Mehran Taghian Jazi, Xing Huang, Yao Wang, Zhijun Tu, Yufei Cui, Yunke Peng, Hongliang Li
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24953v1) · [PDF](https://arxiv.org/pdf/2607.24953v1)

## TLDR
This paper identifies transposition-induced scale inconsistency in 1D microscaling as a key cause of FP4 training instability and proposes a 2D block quantization framework that enforces forward-backward consistency, enabling stable end-to-end FP4 training with less than 1.3% degradation compared to BF16 across models up to 30B parameters.

## Abstract
Reducing training precision is a key lever for improving the e ciency of large language model (LLM) training, but pushing beyond FP8 to 4-bit oating point (FP4) remains challenging due to instability during optimization. We identify a fundamental source of this instability in existing microscaling approaches: scale inconsistency induced by tensor transposition. In conventional 1D block quantization, forward and backward passes assign di erent scaling factors to the same values after transposition, leading to biased and unstable gradient updates. To address this issue, we propose a low-precision training framework based on 2D block FP4 quantization, which enforces transposition-invariant scaling and preserves consistency between forward and backward computations. We further combine this with truncation-free scaling and stochastic rounding to control quantization error and maintain unbiased gradients. To handle the sensitivity of attention mechanisms, we adopt MXFP8 quantization for query and key projections, yielding a practical mixed-precision design. We evaluate our method on dense LLMs up to 7B parameters and a 30B Mixture-of-Experts model, trained on up to 100B tokens. Across all settings, our approach achieves stable end-to-end FP4 training and closely matches BF16 performance, with less than 1.3% degradation in perplexity and downstream accuracy. These results demonstrate that enforcing forwardbackward scaling consistency is su cient to enable practical FP4 training at scale, providing a simple and e ective pathway toward more e cient LLM training.
