# Physics-Informed Dynamic State Estimation for Current Transformers Using Graph Neural Networks

- 区域：精读区
- 排名：2
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Michael A. Boateng, Gabriel Gauderman, Nathalie Uwamahoro
- 机构：Syracuse University, Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02679v1) · [PDF](https://arxiv.org/pdf/2607.02679v1)

## TLDR
This paper proposes a physics-informed graph neural network warm-start strategy for current transformer dynamic state estimation that improves robustness under noisy conditions by generating informed initial state estimates from the Jacobian sparsity pattern, achieving average gains of 25% in initialization distance and 38% in weighted objective value.

## Abstract
Current transformers are fundamental to power system protection and measurement, yet transient core saturation can severely distort the secondary current and degrade measurement accuracy. Existing dynamic state estimation methods rely mainly on numerical discretisation and iterative solvers, but their initialisation is not informed by the physical dependency structure of the estimation problem, which limits robustness under noisy conditions. This paper presents a physics-informed enhancement for current transformer dynamic state estimation using COMTRADE measurements generated in WinIGS-T. A structured benchmark of four discretisation schemes and three iterative solvers identifies Gauss-Newton with Quadratic discretisation as the strongest baseline. To address the limitation of conventional cold-start initialisation, a graph neural network is constructed from the Jacobian sparsity pattern to generate physics-informed initial state estimates. The proposed warm-start strategy improves estimator conditioning and achieves average gains of 25% in initialisation distance and 38% in initial weighted objective value across all tested SNR levels. The results demonstrate that embedding physical structure into the initialisation stage improves the robustness of CT saturation correction and supports more reliable measurement and protection performance in modern power grids.
