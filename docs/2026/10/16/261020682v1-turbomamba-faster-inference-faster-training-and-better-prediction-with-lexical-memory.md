# TurboMamba: Faster Inference, Faster Training, and Better Prediction with Lexical Memory

- 区域：速读区
- 排名：7
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Hanxin Zhang
- 机构：University of Pittsburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20682v1) · [PDF](https://arxiv.org/pdf/2610.20682v1)

## TLDR
TurboMamba is a blockwise language-model architecture that combines a global Mamba-3 model over token blocks with a small local Transformer and lightweight lexical-memory enhancements to achieve lower test NLL and substantially faster training and inference than Transformer, Mamba-3, Jamba, and Zamba baselines.

## Abstract
We introduce TurboMamba, a language-model architecture for faster inference, faster training, and better token prediction. A global Mamba-3 model runs once per completed token block. A small Transformer uses this global context and earlier tokens within the block to predict the next token. Three lightweight additions improve local predictions: direct access to the previous block's last token, a small correction to next-token scores, and a learned mixture with recent-token frequencies. We compare twelve small-scale implementations on public FineWeb-Edu, with comparable parameter counts and shared training-budget caps. The baselines include Transformer, Mamba-3, Jamba, and Zamba. The Jamba and Zamba versions use Mamba-3 in place of their original Mamba modules. TurboMamba achieves the lowest mean test prediction loss (negative log-likelihood, NLL) among all twelve models. Its mean NLL is 9.4% lower than that of Mamba-3, 7.3% lower than that of the Jamba version, and 18.3% lower than that of the Zamba version. End-to-end training throughput is 2.60x that of Mamba-3, 2.81x that of the Jamba version, and 4.82x that of the Zamba version. We measure end-to-end batch latency for a batch of 32 sequences, each with a 256-token prompt and 128 generated tokens. On this workload, TurboMamba achieves a 3.12x speedup over Mamba-3, a 3.53x speedup over the Jamba version, and a 6.21x speedup over the Zamba version.
