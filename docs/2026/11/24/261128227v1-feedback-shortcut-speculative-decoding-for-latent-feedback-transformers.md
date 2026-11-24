# Feedback Shortcut: Speculative Decoding for Latent Feedback Transformers

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Benhao Huang, Xuezhe Ma, Hector Liu
- 机构：Institute of Foundation Models, USC
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28227v1) · [PDF](https://arxiv.org/pdf/2611.28227v1)

## TLDR
**Feedback Shortcut enables speculative decoding for latent feedback Transformers by aligning lightweight projections from multi-token-prediction head states to approximate missing feedback and pipelining draft correction with predecessors’ newly computed states, achieving near-exact decoding quality with 2.4–2.8× speedup at only ~2% extra training compute.**

## Abstract
Feeding each position's top-layer hidden state back into the next position's input improves Transformer performance. However, this feedback breaks speculative decoding, since verifying a drafted token requires the top-layer state from its preceding position, which forces the draft to rely on an approximate stand-in. Training the model to adapt to this stand-in can lower the exact-decoding performance ceiling, while using it at inference time further introduces approximation error. We propose Feedback Shortcut to address both bottlenecks. First, state alignment trains a lightweight projection from multi-token prediction head states to stand-ins, leaving base model training untouched. Second, pipelined correction re-evaluates each draft using its predecessor's newly computed state, a much closer proxy to true feedback. Running this correction inside the verification pass of subsequent drafts improves accuracy with zero extra calls. Across 135M and 780M scales, Feedback Shortcut stays within $10^{-4}$ bits per byte of the exact-decoding ceiling on Paloma and accelerates decoding by 2.4-2.8x with about 2% more training compute than the latent feedback Transformer. At large batch sizes, skipping correction still preserves Transformer speed and over 80% of latent feedback's gains.
