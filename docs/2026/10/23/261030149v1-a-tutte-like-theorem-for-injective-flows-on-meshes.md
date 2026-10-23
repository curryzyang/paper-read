# A Tutte-Like Theorem for Injective Flows on Meshes

- 区域：速读区
- 排名：1
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Darsh Kaushik, Noam Aigerman
- 机构：Université de Montréal, Mila - Quebec Artificial Intelligence Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30149v1) · [PDF](https://arxiv.org/pdf/2610.30149v1)

## TLDR
The paper proves a Tutte-like theorem showing that the 90°-rotated gradient of a discrete harmonic function on a spherical triangle mesh defines an injective flow computable via a sparse linear system and differentiably optimizable through Laplacian weights.

## Abstract
This work proves a theorem regarding injectivity of continuous flows that are defined via discrete vector fields on triangle meshes. In similar fashion to Tutte's embedding, the theorem shows a connection between harmonicity and injectivity. Specifically, a discrete harmonic function is computed over a spherical mesh, and its $90^\circ$-rotated gradients are taken as the vector field. We show that this leads to an injective flow over the mesh, i.e., when two points are advected along the vector field, their trajectories are guaranteed to not intersect. The core insight behind this theorem is that the characterization of the Poincaré-Hopf indices of discrete harmonic 1-forms is paralleled in the combinatorial rules for injective vector fields. Similarly to Tutte's embedding, the injective vector field can be computed by simply solving a sparse linear system. Furthermore, it is differentiably dependent on the entries of the Laplacian, enabling unconstrained gradient-based optimization of the vector field while preserving injectivity. The advection itself can be computed by a quick and accurate algorithm. We experimentally validate the injectivity of the results, as well as show examples of differentiable optimization, such as computing an injective approximation to a given non-injective vector field, and fitting an injective vector field to satisfy constraints.
