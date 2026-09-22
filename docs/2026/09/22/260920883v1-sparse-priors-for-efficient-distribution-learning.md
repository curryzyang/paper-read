# Sparse Priors for Efficient Distribution Learning

- 区域：速读区
- 排名：1
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Saumya Goyal, Barnabás Póczos
- 机构：Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20883v1) · [PDF](https://arxiv.org/pdf/2609.20883v1)

## TLDR
This paper introduces sparse priors and a “sparse dimension” to show that Bayesian distribution learning and learning to sample under a \(k\)-sparse prior achieve risk bounds of order \(\sqrt{k/n}\), overcoming the curse of dimensionality and better aligning theory with practical generative AI performance.

## Abstract
Despite the widespread use and success of generative AI techniques today, theoretical guarantees on learning a distribution supported in $d$ dimensions from $n$ samples degrade as $O(n^{-1/Θ(d)})$, though shown to be minimax optimal. We hypothesize that present bounds are too pessimistic because smoothness assumptions are not enough to capture the structure of distributions that often appear in real applications. Consequently, we introduce the class of sparse priors and define the "Sparse Dimension" as a measure of sparsity of a prior over the space of all distributions. We show that distribution learning under a $k$-sparse prior achieves a Bayesian risk lower bound of $Ω(\sqrt{k/n})$ under common distance metrics, and show a matching (up to logarithmic terms asymptotically in $n,k$) upper bound for the TV distance under mild additional assumptions. We show the statistical equivalence of distribution learning and learning to sample in the Bayesian setting so that our results apply to learning to sample as well. While $k$ can still depend on the dimension $d$, or a notion of intrinsic dimension, our results show that learning under an appropriate prior overcomes the curse of dimensionality with respect to the dependence on $n$.
