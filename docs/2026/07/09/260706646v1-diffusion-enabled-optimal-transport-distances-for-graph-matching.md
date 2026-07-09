# Diffusion enabled Optimal Transport distances for graph matching

- 区域：速读区
- 排名：12
- 匹配度：2.0/10
- 来源：arxiv
- 作者：Iman Seyedi, Francesco Archetti
- 机构：University of Milano-Bicocca
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06646v1) · [PDF](https://arxiv.org/pdf/2607.06646v1)

## TLDR
DsrFGW integrates diffusion processes into semi-relaxed fused Gromov-Wasserstein optimal transport to robustly align graphs under noise and sparsity, outperforming existing methods on synthetic tasks.

## Abstract
This paper introduces Diffusion Semi-Relaxed Fused Gromov-Wasserstein (DsrFGW), a novel method for graph comparison that unifies node features and structural connectivity through optimal transport. While traditional Gromov-Wasserstein and semi-relaxed variants (srGW, srFGW) capture graph structure, they often struggle with sparse, noisy, or partially observed graphs. Inspired by Graph Diffusion Distance, which posits graphs are similar if they enable similar information transmission patterns, DsrFGW incorporates diffusion processes allowing information propagation across nodes, capturing local and global structural patterns while reducing sensitivity to noise or missing edges. An extensive evaluation on 36 synthetic pairwise graph matching tasks (easy, medium, hard) demonstrates consistent superiority over srFGW, achieving accuracy improvements of 0-20 percentage points and dramatic Adjusted Rand Index (ARI) gains: in medium-difficulty scenarios, srFGW often achieves negative ARI (worse than random) while DsrFGW offers better performance in terms of both internal and external clustering quality measures (i.e., Adjusted Rank Index and Accuracy with respect to the true underlying clusters, respectively). Even under severe noise, DsrFGW improves clustering quality in 92% of the synthetic tasks with optimal diffusion scales adapting to problem difficulty, establishing DsrFGW as a robust framework for graph comparison under structural uncertainty.
