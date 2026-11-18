# The Impact of Scenario Representation in Scenario-based Optimization Certification

- 区域：速读区
- 排名：14
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Stephen Crawford, Nora Ayanian
- 机构：Brown University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21795v1) · [PDF](https://arxiv.org/pdf/2611.21795v1)

## TLDR
Lossless regrouping of scenarios can change scenario-based optimization certification outcomes—yielding a distortion factor \(k^2(1-\epsilon)^{k-1}\) and apparent sample-efficiency gains—even when the underlying sampled information, feasible region, optimizer, and violation probability are unchanged.

## Abstract
Scenario-based optimization provides finite-sample guarantees for decisions constructed from sampled uncertainty, but its certification procedures can be sensitive to how those samples are represented. We investigate this sensitivity under lossless scenario regrouping, which preserves the sampled information, feasible region, optimizer, and primitive violation probability. For an equal-allocation support-subsample certificate, we derive the distortion factor \(k^2(1-ε)^{k-1}\), establish certification reversals between equivalent representations, and provide sufficient conditions for acceptance dominance under nested coarsening. We further apply nondegeneracy-free Wait-and-Judge theory to coordinatewise scenario envelopes, enabling stronger certification directly from the primitive observations. In paired scenario-MPC experiments, exact regrouping increases certification availability from 318 to 471 of 480 attempts without changing the samples, numerical proposals, or requiring any reduction in witness cardinality. Primitive Wait-and-Judge certification accepts the same 471 attempts without regrouping. These results demonstrate that apparent scenario sample-efficiency gains can arise from certificate accounting rather than additional information or reduced decision risk.
