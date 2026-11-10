# Quantum Natural Muon: Spectral-Natural Optimization for Variational Quantum Circuits

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Duong The Do, Duong Tung Nguyen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10105v1) · [PDF](https://arxiv.org/pdf/2611.10105v1)

## TLDR
The paper introduces Quantum Natural Muon (QNM), an order-sensitive spectral natural-gradient optimizer for variational quantum circuits that combines damped quantum Fisher preconditioning with blockwise polar normalization, and shows theoretical guarantees and empirical gains—especially when spectral blocks match circuit structure—for its distance-aware variant.

## Abstract
Training parameterized quantum circuits requires optimization methods that account for two distinct structures: the information geometry of quantum states and the matrix or tensor structure induced by circuit parameterization. We introduce Quantum Natural Muon (QNM), a spectral natural-gradient framework that applies polar normalization to circuit-semantic parameter blocks after damped quantum Fisher preconditioning. This ordering is essential: quantum Fisher preconditioning and blockwise polar normalization do not commute in general, so QNM is not an order-free composition of quantum natural gradient (QNG) and Muon. We show that Frobenius-matched polar mixing preserves active singular subspaces while raising a spectral floor and improving active conditioning, and that the resulting direction remains a controlled perturbation of QNG. For its distance-aware realization (DA-QNM), we further establish alignment, descent, and nonconvex stationarity guarantees for the normalized update, together with perturbation bounds under gradient and QFIM estimation error. Experiments on variational quantum eigensolving, weighted QAOA-MaxCut, and supervised quantum classification isolate the roles of quantum geometry, circuit-semantic spectral structure, and radius control. The strongest gains arise when the spectral blocks match the circuit structure, supporting the central principle that quantum-state and structured spectral geometries provide complementary information for variational quantum optimization.
