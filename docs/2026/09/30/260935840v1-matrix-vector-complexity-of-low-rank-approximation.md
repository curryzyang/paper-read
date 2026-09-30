# Matrix-Vector Complexity of Low-Rank Approximation

- 区域：速读区
- 排名：9
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Haihan Zhang, Wendao Wu, Chenheng Zhang, Yanyi Li, Chunyuan Zheng, Cong Fang, Haoxuan Li, Zhouchen Lin
- 机构：Peking University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35840v1) · [PDF](https://arxiv.org/pdf/2609.35840v1)

## TLDR
This paper proves matching matrix-vector query bounds for relative-error rank-\(k\) low-rank approximation, showing that the optimal query complexity scales as \(\widetilde{\Theta}(\min\{N, k\min\{p^{1/6}\varepsilon^{-1/3}, \varepsilon^{-1/2}\}\})\) for \(2\le p<\infty\) and \(\widetilde{\Theta}(\min\{N, k\varepsilon^{-1/2}\})\) for \(p=\infty\), thereby recovering the multiplicative rank dependence and identifying the transition at \(p\varepsilon \asymp 1\).

## Abstract
We establish matching polynomial query bounds for low-rank approximation from exact matrix--vector products. Given an unknown matrix $A\in\mathbb{R}^{m\times n}$, at each step a randomized algorithm chooses either $v\in\mathbb{R}^n$ and receives $Av$, or $u\in\mathbb{R}^m$ and receives $A^\top u$. The choice may depend measurably on all previous queries and replies and on the algorithm's private randomness; each vector product costs one query. The output is a rank-$k$ right projector with Schatten-$p$ residual at most $1+\varepsilon$ times optimal. Write $N=\min\{m,n\}$ and let $Q_p^*$ denote the worst-case query budget for success probability $2/3$ on every input. For every $1\le k<N$ and sufficiently small $\varepsilon$, our lower bounds, combined with existing Krylov upper bounds, give $Q_p^*=\widetildeΘ\!\left(\min\{N,k\min\{p^{1/6}\varepsilon^{-1/3},\varepsilon^{-1/2}\}\}\right)$ $(2\le p<\infty)$, $Q_\infty^*=\widetildeΘ\!\left(\min\{N,k\varepsilon^{-1/2}\}\right)$. These bounds have universal constants and allow $p$ to vary with the problem parameters, identifying the transition at $p\varepsilon\asymp1$. A complementary result for each fixed $1\le p<2$ gives $\widetildeΘ_p(\min\{N,k\varepsilon^{-1/3}\})$, with constants and an accuracy threshold that may depend on $p$. Together, the results recover this fixed-norm rate for every fixed finite $p$, supplying the multiplicative rank dependence missing from previous lower bounds. Tildes suppress logarithmic factors. The proof extends adaptive Wishart deferred decisions to a rectangular factor with a $k$-dimensional nullspace. Posterior overlap gives a short fixed-norm argument, while persistence of small compression eigenvalues controls growing $p$ and the spectral endpoint. Exact range recovery handles target costs of order $k$; the Wishart family covers the remaining regimes.
