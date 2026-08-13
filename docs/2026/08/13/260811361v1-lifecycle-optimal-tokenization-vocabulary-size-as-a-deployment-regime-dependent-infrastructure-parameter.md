# Lifecycle-Optimal Tokenization: Vocabulary Size as a Deployment-Regime-Dependent Infrastructure Parameter

- 区域：速读区
- 排名：12
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Rima Mittal, Ankit Gubrani, Satyanarayana Kakollu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11361v1) · [PDF](https://arxiv.org/pdf/2608.11361v1)

## TLDR
The optimal tokenizer vocabulary size for LLMs is not a fixed constant but a deployment-dependent infrastructure parameter that should shift by up to 16× based on serving batch size and inference volume—from ~32k for on-device serving to 131k–262k for datacenter serving—with no significant quality penalty.

## Abstract
Tokenizer vocabulary size is a foundational design choice in large language model (LLM) infrastructure, yet it is typically fixed at training time based on convention rather than deployment analysis. We show that the cost-optimal vocabulary is not a constant but a function of the serving regime. We formalize total deployment cost as $C_{lifecycle}(V) = C_{train}(V) + λ\cdot C_{infer}(V, B)$, where $λ$ is inference volume and $B$ is the serving batch size. Through controlled experiments on two GPU families spanning the memory-bound to compute-bound regimes (A10G, ridge $\approx$ 117 FLOP/byte; A100, ridge $\approx$ 183 FLOP/byte), we demonstrate: (1) the inference-optimal vocabulary shifts 16x with serving batch, from 32k at $B=1$ to 524k at $B=64+$, driven by amortization of the $V \times d$ unembedding matrix read; (2) at 1.3-2.3B model scale, quality (bits per byte, BPB) is optimized at $V=65$k, confirming scale-dependent vocabulary preference; (3) the lifecycle-optimal vocabulary diverges from training-optimal by up to 16x for production deployments. Quality is approximately invariant across the optimal range ($<$2% BPB spread), making vocabulary a pure systems optimization with no quality penalty in the measured range. Our results provide actionable capacity planning guidance: on-device deployments ($B=1$) should use $V \approx 32$k; datacenter serving ($B \geq 64$, $λ\geq 10$) should use $V \approx 131$-262k.
