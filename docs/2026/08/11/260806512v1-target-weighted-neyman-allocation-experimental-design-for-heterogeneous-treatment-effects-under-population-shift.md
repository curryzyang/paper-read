# Target-Weighted Neyman Allocation: Experimental Design for Heterogeneous Treatment Effects under Population Shift

- 区域：速读区
- 排名：12
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Hoang Dang, Luan Pham, Minh Nguyen
- 机构：Independent Researcher, University of New South Wales, Florida Atlantic University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06512v1) · [PDF](https://arxiv.org/pdf/2608.06512v1)

## TLDR
TWNA is a two-stage stratified experimental design that uses pilot variance estimates to allocate sample sizes and treatment probabilities, balancing deployment-group importance with measurement difficulty to minimize target-weighted error in estimating heterogeneous treatment effects under population shift.

## Abstract
Randomized experiments are often run in one population to guide decisions in another. Allocating by experimental proportions wastes budget on groups that rarely appear in deployment, whereas allocating by deployment proportions under-samples groups that are hard to measure precisely. We propose \textbf{TWNA} (Target-Weighted Neyman Allocation), a two-stage stratified design that uses pilot estimates of group--arm outcome variances to allocate final-stage sample sizes and treatment probabilities for target-weighted group average treatment effect (GATE) precision. The oracle rule has a closed form and balances deployment importance with statistical difficulty; the plug-in rule recovers it as pilot variance estimates stabilize. We also extend TWNA to handle uncertainty about deployment composition, remaining robust whether the target mix is roughly known or entirely unknown. Finally, we distinguish this weight robustness from a pilot-robust variant for skewed, rare-event, or contaminated outcomes. Simulations and real-covariate benchmarks show the largest gains when groups are both deployment-important and difficult to measure.
