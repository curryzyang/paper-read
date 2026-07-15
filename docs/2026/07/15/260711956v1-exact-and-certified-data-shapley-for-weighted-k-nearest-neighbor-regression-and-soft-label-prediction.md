# Exact and Certified Data Shapley for Weighted k-Nearest-Neighbor Regression and Soft-Label Prediction

- 区域：速读区
- 排名：7
- 匹配度：2.1/10
- 来源：arxiv
- 作者：Zongye Lyu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11956v1) · [PDF](https://arxiv.org/pdf/2607.11956v1)

## TLDR
This paper presents the first exact pseudo-polynomial algorithm and a certified approximation scheme for weighted KNN-regression and soft-label Data Shapley, resolving the open problem of handling the coalition-dependent normalization denominator, along with complexity results and an open-source library.

## Abstract
Data Shapley is the standard principled answer to which training points are worth what, and its k-nearest-neighbor (KNN) specialization is the version deployed in practice: the exact estimator shipped by toolkits such as pyDVL and OpenDataVal. Exact algorithms are known for unweighted KNN and for weighted KNN classification, but weighted KNN regression and soft-label prediction have resisted: the only exact method is an O(N^K) brute force, exponential in neighborhood size K. The obstruction: the weighted regression prediction is a ratio of two coalition-dependent sums, whose normalization denominator breaks the additive, threshold, and duplication structures the prior polynomial algorithms rely on. We close this gap. We give (i) the first pseudo-polynomial-time exact algorithm (polynomial in N and K at fixed lattice precision) for weighted KNN-regression Data Shapley, a counting dynamic program over the joint integer state (sum of w, sum of w*y), verified against exhaustive enumeration with zero mismatch on 12,716 adversarial instances; (ii) a certified FPTAS for continuous weights and targets, with a machine-checkable per-value error certificate never violated across 86,400 checks; (iii) a complexity landscape, including an unconditional Omega(D_w) output-size lower bound and access-model hardness results; and (iv) a weighted soft-label multi-class extension. We release an open-source, CPU-only library and the first exact weighted-regression Data Shapley ground truth. On downstream mislabel detection our exact values are statistically equivalent to Monte-Carlo Data Shapley (dataset-level TOST, n=8, p<10^-4), the pre-registered outcome; the value of exactness is instead determinism, a certified error bound, and an exact reference for auditing estimators: Monte-Carlo did not reproduce the exact top-10% ranking at any budget tested, up to 3,000 permutations (~1.28e6 utility evaluations).
