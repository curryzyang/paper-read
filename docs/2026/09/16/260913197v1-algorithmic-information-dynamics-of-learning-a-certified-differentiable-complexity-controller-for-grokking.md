# Algorithmic Information Dynamics of Learning: A Certified, Differentiable Complexity Controller for Grokking

- 区域：速读区
- 排名：1
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Luan Ozelim, Hector Zenil
- 机构：Oxford Immune Algorithmics, King's College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13197v1) · [PDF](https://arxiv.org/pdf/2609.13197v1)

## TLDR
By replacing the usual piecewise-constant complexity estimator with a certified, differentiable one, the paper turns algorithmic complexity from a passive monitor into a transient controller and timing gate that accelerates grokking, rescues failing seeds, and operates within a data-dependent Occam boundary—its key contribution being when to intervene, not attribution.

## Abstract
Algorithmic Information Dynamics (AID) studies systems by perturbing them and measuring changes in algorithmic complexity, but its usual estimator, the Block Decomposition Method, is piecewise constant, restricting the calculus to finite differences. We use $K^{\mathrm{CDM}}_{\mathrm{s}F}$, a certified, differentiable estimator, to bring the calculus into learning dynamics: grokking, where a complexity order parameter is known but has not been made to act. A\empts a transient loss kick, the estimator becomes a controller that accelerates grokking in Levin's description-length--versus-time sense, within a data-dependent Occam boundary whose finite-size trend, $f_c\sim\ln p/p$, is consistent with a coupon-collector interpretation. Ablations show that a complexity gate matches a train-loss gate in rescuing failing seeds with $27\%$ less intervention; among the tested signals, only map complexity marks the transition's completion; the certified prior and the per-parameter $\nabla K$ attribution are both fungible (a uniform-prior sensor makes bit-identical gate decisions, and random supports match $\nabla K$-selected ones above a sparsity threshold); and direct field perturbation shows a nucleation-like response to the Occam field (no linear regime is resolved over the probed amplitudes, so these measurements do not justify a fluctuation--dissipation surrogate), with a finite-field response growing by orders of magnitude toward the transition. These measurements account for the empirically tuned staircase: bang--bang pulses, stall-fired and released on yield, whose iteration plausibly builds the response it exploits. The kick transfers to sparse parity and to a transformer; a sustained weight-space loss fails. The algorithmic estimator's distinct contribution is timing (when to fire and when to release), not attribution.
