# Parallel versions of the mesh adaptive direct search algorithm

- 区域：速读区
- 排名：7
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Sébastien Le Digabel, Antoine Lesage-Landry, Samuel Mendoza, Christophe Tribes
- 机构：Group for Research in Decision Analysis (GERAD), Polytechnique Montréal
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08872v1) · [PDF](https://arxiv.org/pdf/2607.08872v1)

## TLDR
This paper surveys parallel variants of the mesh adaptive direct search (MADS) algorithm for constrained blackbox optimization, detailing their implementations, computational performance, and trade-offs to guide users in selecting the appropriate parallelization strategy.

## Abstract
This work surveys the different parallel variants of the mesh adaptive direct search (MADS) algorithm for constrained blackbox optimization. These problems can inherently imply high computational costs due to the possible large number of variables and multi-modality of the search space. In addition, the potential time-intensive nature and time heterogeneity of the blackboxes defining the problem prompts the need for efficient implementations. Parallelism emerges as an actionable solution to mitigate computation time, as modern computer systems rely on multi-core architecture. The reviewed methods employ diverse levels of parallelism and distinct parallel strategies to effectively tackle each aspect outlined above. The manuscript details the practical implementations, provides computational results, and offers insights into the advantages and limitations of each MADS parallel method.
