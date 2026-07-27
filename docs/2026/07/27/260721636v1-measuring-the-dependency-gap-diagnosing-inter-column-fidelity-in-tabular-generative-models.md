# Measuring the Dependency Gap: Diagnosing Inter-Column Fidelity in Tabular Generative Models

- 区域：速读区
- 排名：14
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Jie Zhang
- 机构：Accenture Japan
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21636v1) · [PDF](https://arxiv.org/pdf/2607.21636v1)

## TLDR
This paper introduces a dependency-aware fidelity diagnostic that reveals a real and stubborn inter-column dependency gap in tabular generative models—missed by standard metrics and resistant to capacity scaling, architectural fixes, and post-hoc correction—highlighting the need for direct dependency supervision.

## Abstract
Synthetic tabular data is valued for preserving not only each column's marginal distribution but the dependencies between columns -- structure that carries much of the discriminative signal for minority classes in imbalanced domains such as fraud and clinical risk. Yet the metrics most commonly used to certify synthetic tabular data are, we show, largely blind to inter-column dependency: a baseline that models every column independently (and therefore destroys all dependency) is judged indistinguishable from real data by the logistic-regression C2ST, and the pairwise Trend score is only partially sensitive. We introduce a dependency-aware fidelity diagnostic that decomposes a strong classifier two-sample test (XGB-C2ST) into marginal, dependency, and numerical-categorical cross components, anchored between a worst-case fully-factorized reference (all dependency destroyed) and a best-case real-data oracle. Applying it to a state-of-the-art flow-matching generator (TabbyFlow/EF-VFM), we find a real dependency gap that standard metrics miss; destroying dependency outright collapses minority-class utility, and the generator's residual gap carries a smaller, consistent utility cost. We then ask whether this gap reflects a structural limitation of mean-field generative objectives. It does not: consistent with recent recovery results for variational flow matching, the objective is asymptotically exact. Yet the gap is stubborn -- a 16x increase in model capacity does not close it -- pointing to the absence of direct dependency supervision rather than a capacity or structural limit. Consistent with this, and because the residual gap is higher-order, no cheap intervention closes it: not an in-model dependency mechanism, not post-hoc copula correction, and not the 16x capacity increase -- a caution for a field that assumes such fixes help.
