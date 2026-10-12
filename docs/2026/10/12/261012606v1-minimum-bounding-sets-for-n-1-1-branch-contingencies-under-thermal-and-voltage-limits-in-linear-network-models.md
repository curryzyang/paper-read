# Minimum Bounding Sets for N-1-1 Branch Contingencies Under Thermal and Voltage Limits in Linear Network Models

- 区域：速读区
- 排名：9
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Timothy N. Thacker
- 机构：The University of Tennessee, Knoxville, CURENT
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12606v1) · [PDF](https://arxiv.org/pdf/2610.12606v1)

## TLDR
The paper derives exact minimum bounding sets for N-1-1 branch contingencies in linear network models by using cycle-space cosine bounds on outage-pair interactions—extended to low-rank positive semidefinite updates—to build a best-first search that reproduces brute-force worst-case thermal and voltage violations with orders-of-magnitude fewer pair evaluations.

## Abstract
N-1-1 contingency analysis studies the loss of one element followed by system adjustments and the loss of a second. The number of contingency pairs increases quadratically with the number of applicable elements, and traditional ranking-based screening methods cannot guarantee that omitted pairs are bounded. This paper determines the minimum bounding set of two-branch-outage pairs: the smallest set that can reproduce the worst value of every violated thermal and voltage limit of a linear network model. In the DC model, effects of an outage pair can be quantified by the extent of the coupling between the outages. The paper measures this by the cosine between the two outages in the network's cycle space, with a bound that splits into one term per outage and is within a near-ideal factor of $\sqrt{1+\varepsilon}$. This argument extends to every linear model in which an outage subtracts a positive semi-definite low-rank term from a symmetric positive definite matrix, with a tight bound and a collapse test. A model with voltage magnitudes is extracted by performing one Newton step on the energy function of the lossless network in rectangular coordinates. A best-first search built on these bounds reproduced brute force on public systems of up to 2{,}869 buses with 130 to 3{,}800 times fewer pair evaluations for flows and 170 to 23{,}700 times fewer for voltages. Gaps in translation to nonlinear models are explored on the IEEE 118-bus system.
