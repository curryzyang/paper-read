# The geometry of AI validation: Exact certification limits for iid best-of-N search

- 区域：速读区
- 排名：8
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Ricardo Fitas
- 机构：Technical University of Darmstadt
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21496v1) · [PDF](https://arxiv.org/pdf/2608.21496v1)

## TLDR
This paper formalizes AI validation as a target-relative inverse problem using kernel span geometry, derives exact certification limits for iid best-of-N search—where auditing best-of-m reliability leaves an ambiguity governed by m²/N—and proposes a two-gate audit rule combining structural coverage with independent task precision.

## Abstract
AI systems increasingly generate alternatives, inspect evidence, and deploy a selected output. Validation is therefore target-relative: evidence certifies deployment only in directions resolved by the interventions that produced it. We represent validation and deployment rules as kernels over a reliability surface. Their span geometry separates replication, which reduces sampling noise, from new intervention directions, which reduce structural blindness. We make this principle exact for iid best-of-$N$ search. Under scalar ranking, randomized ties, maximum selection, bounded binary truth, and a stable rank-truth relation, knowing best-of-$n$ reliability through $n=m$ leaves exact ambiguity width $B_{m,N}=1+2\sum_{r=1}^{m}(-1)^r\cos^{2N}{rπ/[2(m+1)]}$. Explicit bounded worlds attain the entire interval, and the complete prefix is information-maximal among reliability-mean audits confined to $n\le m$. The governing scale is $m^2/N$: when $m$ is proportional to $\sqrt{N}$, ambiguity remains about 0.83, while width $\varepsilon$ requires $m$ of order $\sqrt{N\log(1/\varepsilon)}$. Monotonicity gives an exact uniform-approximation frontier; a Lipschitz bound gives an exact capped-tail dual and order-sharp $L/m^2$ ambiguity. These results yield a two-gate audit rule: establish structural coverage, then add independent tasks for precision. Retrospective studies of mathematical reasoning and code selection construct compatible deployment values with wide separation and show that a score-tail audit rule frozen on 82 discovery tasks substantially reduces held-out error. Beyond iid search, the geometry applies only to known or independently estimated kernels; the empirical analyses are illustrative rather than prospective interventions.
