# Sparse plus low-rank matrix embedding with applications in cancer radiotherapy optimization

- 区域：速读区
- 排名：6
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Mojtaba Tefagh, Gourav Jhanwar, Masoud Zarepisheh
- 机构：Memorial Sloan Kettering Cancer Center, University of Edinburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05695v1) · [PDF](https://arxiv.org/pdf/2609.05695v1)

## TLDR
TLDR: This paper introduces sparse-plus-low-rank matrix embedding (SLME) and a trust-region algorithm (R3-Trust) to efficiently approximate large dense matrices—motivated by radiotherapy dose optimization—by trading off approximation error against computational cost, outperforming recovery-oriented decompositions on clinical and synthetic benchmarks.

## Abstract
Decomposing a matrix into sparse and low-rank components is central to robust principal component analysis and has broad applications in machine learning, signal processing, and computer vision. Classical formulations seek to recover the underlying sparse and low-rank structure. We instead introduce \emph{sparse-plus-low-rank matrix embedding} (SLME), whose goal is to construct a computationally efficient surrogate for a large dense matrix, without requiring its components to be interpretable. Given $A\in\mathbb{R}^{m\times n}$, SLME approximates $A \approx S+HW$, where $S$ is sparse, $H\in\mathbb{R}^{m\times r}$, $W\in\mathbb{R}^{r\times n}$, and $r\ll \min\{m,n\}$. The resulting matrix-vector product can be evaluated as $Sx+H(Wx)$ in $\mathrm{nnz}(S)+r(m+n)$ operations, rather than the $mn$ operations required by $Ax$. Our primary motivation arises from optimization problems in cancer radiotherapy treatment planning, where a large dense \emph{dose-influence matrix} is a major computational bottleneck.
  We formulate SLME as a bi-objective nonconvex optimization problem that balances approximation error against the computational cost of the downstream tasks. We then develop \emph{R3-Trust}, an efficient trust-region algorithm that approximates the Pareto frontier in a single parameter-free run. Each point on the resulting frontier provides a sparse-plus-low-rank representation with a different balance between accuracy and downstream computational cost. Experiments on clinical radiotherapy matrices show that decompositions obtained from existing recovery-oriented formulations can be suboptimal for the embedding objective. Conversely, experiments on synthetic instances demonstrate that SLME and R3-Trust can also be applied to sparse-plus-low-rank recovery, where they compare favorably with state-of-the-art recovery methods in both reconstruction accuracy and computational time.
