# Near-Quadratic Sample Compression for All VC Classes

- 区域：速读区
- 排名：11
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Yang Cai, Vineet Gupta, Yanchen Jiang, Christopher Liaw, Aranyak Mehta, Shay Moran, Grigoris Velegkas, Di Wang, Manfred K. Warmuth
- 机构：Technion, Google, Yale University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25011v1) · [PDF](https://arxiv.org/pdf/2611.25011v1)

## TLDR
The paper proves the polynomial sample-compression conjecture for all binary VC classes by constructing, for any class of VC dimension \(d\), a labeled sample compression scheme using \(O(d^2\log^2 d)\) examples and \(O(d\log^2 d)\) side-information bits—the first polynomial and near-quadratic improvement over the previous exponential-in-\(d\) bound.

## Abstract
The sample compression conjecture is a longstanding open problem in learning theory, originating in the work of Littlestone and Warmuth in the 1980s. At its heart is a connection between simplification and generalization: if a predictor consistent with a training sample is defined using only a small part of that sample, then it is likely to generalize. Sample compression schemes formalize this idea, and many natural learning algorithms can be analyzed this way.
  The sample compression conjecture of Floyd and Warmuth (1995) asserts that every binary concept class of VC dimension $d$ admits a sample compression scheme of size $O(d)$; a weaker conjecture asks only for size polynomial in $d$. Both have remained open: the first bound depending only on $d$, due to Moran and Yehudayoff (2016), is exponential in $d$. We prove the weaker conjecture by constructing a sample compression scheme of size $O(d^2 \log^2 d)$.
