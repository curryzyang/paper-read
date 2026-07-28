# Threshold-indexability of restless bandits with real interval state spaces: a performance-metric verification framework and long-run average analysis

- 区域：速读区
- 排名：11
- 匹配度：3.7/10
- 来源：arxiv
- 作者：José Niño-Mora
- 机构：Universidad Carlos III de Madrid
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22557v1) · [PDF](https://arxiv.org/pdf/2607.22557v1)

## TLDR
The paper develops a performance-metric verification framework for proving threshold-indexability and computing Whittle indices in restless bandits with real interval state spaces, extending discounted partial conservation law methods to a criterion-agnostic setting and specializing to long-run average analysis.

## Abstract
Restless multiarmed bandits are Markov decision process models for allocating a scarce resource among projects whose states evolve under active or passive actions. Whittle's index policy is widely used for such problems, but its application to a given model requires both a proof of indexability and a means of computing the index, two analytically challenging tasks. This paper develops a performance-metric framework for proving threshold-indexability and computing Whittle indices for binary-action projects with real interval state spaces. The framework extends discounted partial conservation law \textup{(PCL)} methods to a criterion-agnostic setting and works directly with reward and resource metrics of threshold policies, rather than first proving threshold optimality and then monotonicity of optimal thresholds in the resource price. The main theorem is a verification and characterization result: under marginal-resource positivity and a marginal integration-by-parts identity, threshold-indexability is equivalent to monotonicity and continuity of the marginal productivity (MP) index, which then equals the Whittle index. The framework is specialized to the discrete-time long-run average criterion by a vanishing-discount transfer of discounted threshold metrics and includes exceptional states where the MP marginal-resource denominator vanishes, handled by continuous extension or vanishing-discount limits. Applications to web crawling and noisy-channel transmission recover known long-run average Whittle indices. For scalar Kalman-filter bandits, it proves a regular-part average-cost result and reduces the remaining indexability question to explicit exceptional-state metric-limit conjectures.
