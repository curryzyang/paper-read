# Can Acceleration in Gradient-Norm Minimization Be Anytime? Sharp Last-Iterate Limits in Smooth Convex Optimization

- 区域：速读区
- 排名：2
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Pierre Vernimmen, François Glineur
- 机构：UCLouvain
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05710v1) · [PDF](https://arxiv.org/pdf/2609.05710v1)

## TLDR
This paper characterizes the limits of anytime acceleration for gradient-norm minimization in smooth convex optimization, showing that horizon-independent linear-span methods cannot beat a sharp \( \limsup_N N\mathcal G_N \ge 1/2 \) barrier, although they can achieve near-\(N^{-2}\) last-iterate rates on a density-one set of horizons, a strict dichotomy with uniform \(O(N^{-2})\) best-so-far guarantees.

## Abstract
In smooth convex optimization, the gradient norm is a directly observable measure of stationarity. Accelerating a first-order method that minimizes the gradient norm is known to be more delicate than accelerating the minimization of function values. Optimal accelerated methods such as OGM-G (Kim & Fessler, 2021) are known to exist for any prescribed finite horizon, but their coefficients depend explicitly on the length of that horizon, i.e. the number of iterations.
  We ask what kind of acceleration is feasible when the stopping horizon is unknown to the method, i.e. for horizon-independent methods. Diakonikolas & Wang (2022) conjectured that an $Ω(N^{-1})$ lower bound on the squared gradient norm holds at every horizon $N$ for any nonadaptive, horizon-independent linear-span first-order method. We disprove this pointwise conjecture by exhibiting a method that achieves near-$N^{-2}$ last-iterate guarantees on a density-one set of horizons. We show instead that an $Ω(N^{-1})$ lower bound must hold for infinitely many horizons. More precisely, if $\mathcal G_N(\mathcal A)$ denotes the bound on the squared gradient norm after $N$ iterations for a method $\mathcal A$, we prove that $\limsup_{N\to\infty}N \mathcal G_N(\mathcal A) \ge 1/2$ for any method $\mathcal A$. This bound is sharp: the constant $1/2$ is exactly attained by the horizon-independent gradient-descent schedule of Rotaru et al. (2026).
  In addition, we show that the above two extreme behaviors cannot be achieved by the same method: any method $\mathcal A$ with an $o(N^{-1})$ guarantee on a subsequence of iterates must satisfy $\limsup_N N \mathcal G_N(\mathcal A)=\infty$. In contrast, best-so-far output admits a uniform $O(N^{-2})$ guarantee.
