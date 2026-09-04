# No-Regret Bayesian Optimization with Finite-Library Input-Warped Kernels

- 区域：速读区
- 排名：2
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Edvin Ketabati Augustinsson, Robert A. Bridges
- 机构：AI Sweden
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.02993v1) · [PDF](https://arxiv.org/pdf/2609.02993v1)

## TLDR
TLDR: The paper proposes FLIWBO, a Bayesian optimization method that adaptively selects input warps from a finite library to improve sample efficiency under misspecified geometries, while proving the first high-probability sublinear cumulative-regret guarantee for GP-UCB with history-dependent kernel adaptation.

## Abstract
Gaussian-process Bayesian optimization (GP-BO) excels at black-box optimization of costly functions, e.g., hyperparameter optimization (HPO) and multi-agent system (MAS) design. Convergence-rate guarantees exist for select methods, notably GP upper confidence bound (GP-UCB), but require a fixed kernel. Critically, the kernel encodes how input proximity affects objective value similarity. When raw coordinates poorly match this geometry - as with log-scaled hyperparameters or localized peaks - input warping can greatly improve sample efficiency, yet known GP-UCB proofs require a fixed kernel. We propose Finite-Library Input-Warped Bayesian Optimization (FLIWBO), which selects warps from a finite library of smooth input maps by any history-dependent rule. It adapts the input geometry to accelerate learning while retaining high-probability convergence guarantees under mild hypotheses, with an explicit $\sqrt(N_\varepsilon)$ library-size cost. Controlled diagnostics show that finite-library warping repairs planted geometry mismatches and identify FLIWBO failure cases. Across four repeated benchmarks - warped synthetic objectives, a confidence-fence trap, and Fashion-MNIST HPO - FLIWBO-UCB beats raw-coordinate GP-UCB under misspecified geometry, escapes traps that defeat even oracle-warp expected improvement, and recovers much of the gain from manual log scaling, while leading the tested methods that admit a matching regret guarantee. A 20-dimensional MAS design study further shows feasibility under costly noisy evaluations. Code for experiments is available: https://github.com/edvin-ketabati/bogp-paper-experiments.
