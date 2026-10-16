# Expanding Attention: A Taylor-Series Route to Linear-Time Transformers with a Fixed Number of Recurrent States

- 区域：速读区
- 排名：4
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Zicong Huang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20637v1) · [PDF](https://arxiv.org/pdf/2610.20637v1)

## TLDR
Expanding attention’s exponential kernel as a truncated Taylor series and factorizing each term into tensor-power inner products turns softmax attention into a lossless linear-time recurrence with exactly \(n\) fixed-size states (optimally \(n=3\)), provided queries and keys are normalized, eliminating context-length-dependent memory and decoding cost.

## Abstract
We expand the exponential kernel of attention into a truncated Taylor series of $n$ terms and factorize each term into a tensor-power inner product, which collapses the causal history into exactly $n$ recurrent states, each updated by one rank-one outer product per token and independent of context length $N$. The recursion is lossless with respect to the truncated kernel ($2.2 \times 10^{-16}$ in float64), and the states are additive across chunks ($5.7 \times 10^{-14}$), so prefill admits a parallel scan. Measured exponents are $t \propto N^{2.28}$ for softmax against $N^{0.91}$ for states, with a crossover at $N \approx 728$ and $20.8\times$ at $N = 8192$; per-token decoding latency is constant at $7.3\,μ$s against $N^{1.04}$ for softmax, giving $76.0\times$ at $N = 65536$. Accuracy improves exponentially in $n$ while cost grows combinatorially, since the $m$-th state is $\binom{d+m-1}{m}$ wide---a bound confirmed by SVD---so the optimum is second order, $n = 3$, at $6.5 \times 10^{-4}$ error and $9{,}945$ elements per head. Query and key normalization is a prerequisite: without it the argument exceeds the convergence radius and adding terms stops helping.
