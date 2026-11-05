# Tight Lower Bounds under Matched High-Order Hölder Smoothness and Uniform Convexity

- 区域：速读区
- 排名：8
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Cedar Site Bai
- 机构：Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05527v1) · [PDF](https://arxiv.org/pdf/2611.05527v1)

## TLDR
This paper proves a tight lower bound showing that minimizing functions with matched high-order Hölder smoothness and uniform convexity, where \(q=p+\nu\), requires \(\Omega((H/\sigma)^{2/(3(p+\nu)-2)}\log(\Delta_0/\epsilon))\) deterministic oracle calls, matching the known upper bound and resolving the previously open matched case.

## Abstract
In this paper, we provide tight lower bounds for minimizing high-order Hölder-smooth and uniformly convex functions when their orders match. Specifically, we consider functions whose $p^{th}$-order derivatives are Hölder continuous with degree $ν$ and parameter $H$, and that are uniformly convex with degree $q$ and parameter $σ$. When these orders match, namely, $q = p + ν$, we show that any deterministic algorithm with access to derivatives up to order $p$ requires $Ω\left(\left(\frac{H}σ\right)^{\frac{2}{3(p+ν)-2}}\log\frac{Δ_0}ε\right)$ oracle calls to reduce an initial optimality gap of $Δ_0$ to $ε$. This matches the corresponding upper bound and establishes a higher-order uniformly convex counterpart to Nesterov's classical first-order lower bound for strongly convex functions. Rather than directly generalizing Nesterov's classical quadratic-chain construction, we develop a multiscale phase-wise construction that preserves previous oracle responses while maintaining global Hölder smoothness and uniform convexity. Our result resolves the matched case left open by existing lower bounds for the two asymmetric regimes.
