# Compact Slack-Free Penalty Functions for Inequality Constraints in Higher-Order Unconstrained Binary Optimization

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Naoaki Mochida, Shoya Yasuda
- 机构：Quantum Fabric Inc., Institute of Science Tokyo, Vignette & Clarity, Inc., St. Mary's International School
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25102v1) · [PDF](https://arxiv.org/pdf/2611.25102v1)

## TLDR
The paper proposes compact, slack-free, exact hierarchical penalty functions for inequality constraints in HUBO that are constructed recursively from threshold bits, reduce worst-case product-term count from linear to logarithmic, lower polynomial degree, and compose via addition or multiplication for interval and exclusion constraints.

## Abstract
Inequality constraints in higher-order unconstrained binary optimization (HUBO) are commonly handled using slack variables or by enumerating infeasible assignments, which respectively enlarge the search space or produce penalties whose size grows with the number of forbidden values. We construct exact slack-free penalty functions for upper- and lower-bound constraints on binary-encoded integers. Each function is constructed hierarchically from the threshold bits through a recursive addition-and-multiplication rule, and its correctness for arbitrary bit widths and representable thresholds is proved by mathematical induction. Equivalent explicit finite sum-product representations are also derived, enabling direct analysis of product-term count and polynomial degree. Interval constraints are obtained by adding the lower- and upper-bound penalties, while exclusion constraints are obtained by multiplying them. Compared with the trivial enumerative construction, the proposed method reduces the worst-case product-term count from linear to logarithmic in the representable range. Except at one non-vacuous boundary threshold for each bound, it also reduces both product-term count and degree. The resulting single-bound penalties have minimum positive value 1 and maximum value at most the bit width, which may simplify penalty-weight selection. The same construction also extends exactly to fixed-scale fractional variables through appropriate scaling of the integer thresholds.
