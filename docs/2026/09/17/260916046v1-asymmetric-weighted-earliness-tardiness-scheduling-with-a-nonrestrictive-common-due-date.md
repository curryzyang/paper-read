# Asymmetric Weighted Earliness-Tardiness: Scheduling with a Nonrestrictive Common Due Date

- 区域：速读区
- 排名：10
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Nicholas G. Hall, Hans Kellerer, Miao Song
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16046v1) · [PDF](https://arxiv.org/pdf/2609.16046v1)

## TLDR
This paper studies single-machine asymmetric weighted earliness–tardiness scheduling with a nonrestrictive common due date, establishing strong NP-completeness, a polynomial-time constant-factor approximation, weak NP-completeness with an exact pseudopolynomial algorithm for reversed ratio orders, and an FPTAS for separable ratio-order refinements, thereby showing that the complexity hinges on how the two Smith-ratio orders interact.

## Abstract
Single-machine asymmetric weighted earliness--tardiness (AWET) scheduling asks how to sequence jobs around a common synchronization date when early and late completion incur unrelated job-dependent penalties. At the boundary nonrestrictive date $d=\sum_jp_j$, a compact V-shaped schedule reduces the continuous-time problem to a quadratic choice of a nonempty early set. We establish four complementary results for this model. First, the positive-integer problem is strongly NP-complete by a unary-polynomial reduction from Restricted Exact Cover by 3-Sets. Second, unrestricted AWET admits a polynomial-time $(3+2\sqrt2+\varepsilon)$-approximation based on an anchored semidefinite relaxation and deterministic marginal thresholding. Third, when the earliness and tardiness ratio orders are strict reversals, the problem is weakly NP-complete but has an exact two-resource pseudopolynomial dynamic program. Fourth, for fixed total refinements whose ratio permutation is separable, an exact separating-tree recurrence and coordinated geometric trimming yield an FPTAS. The proofs use different manifestations of the same canonical objective: scale-separated prefix penalties, positive-semidefinite minimum-kernel covariance, a dominant completed load square, and a bounded four-coordinate decomposition interface. Together, the results show that the decisive issue is not merely whether the two ratio orders agree, but whether their interaction can be controlled by a global certificate or compressed into a bounded constructive interface.
