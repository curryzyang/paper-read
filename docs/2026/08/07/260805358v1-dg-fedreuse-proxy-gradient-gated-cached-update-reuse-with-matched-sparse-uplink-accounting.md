# DG-FedReuse: Proxy-Gradient-Gated Cached-Update Reuse with Matched Sparse Uplink Accounting

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Rahil Aftab, Vineet Kumar Rakesh, Soumya Mazumdar, Tapas Samanta
- 机构：Jamia Hamdard, Variable Energy Cyclotron Centre, Gargi Memorial Institute of Technology, Homi Bhabha National Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05358v1) · [PDF](https://arxiv.org/pdf/2608.05358v1)

## TLDR
DG-FedReuse is a federated learning mechanism that lets selected clients reuse age-decayed cached updates when a stochastic head-gradient proxy stays below a round-dependent threshold, using sparse Top-K fresh updates and safeguard quotas to achieve substantial modeled uplink savings with only small accuracy trade-offs.

## Abstract
Federated learning repeatedly incurs local optimization and model-update transmission. We study DG-FedReuse, a simulator-level mechanism that allows selected clients to contribute age-decayed cached updates when a stochastic head-gradient discrepancy proxy remains below a round-dependent threshold. A hard cache-age limit and minimum fresh-client quota constrain reuse, while fresh updates use an adaptive per-tensor Top-K numerical-field representation. Experiments cover six image-classification datasets, 50 virtual clients, Dirichlet label heterogeneity (α=0.5), and three seeds. At a common 90-round budget, DG-FedReuse yields 83.36-85.42% modeled update-data-field uplink saving, compared with 76.88% for matched Top-K FedAvg; the seed-aligned accuracy differences range from -5.29 to -0.14 percentage points. Best-observed test accuracies obtained under test-controlled checkpointing are retained only as exploratory archival evidence and range from -2.38 to +0.45 percentage points relative to matched FedAvg. A symmetric dense-model-downlink sensitivity reduces the headline saving to 41.68-F42.71% and the incremental gain over Top-K FedAvg to 3.24-4.27 percentage points, demonstrating the dependence of communication conclusions on the accounting boundary. The study characterizes the proposed reuse rule in the implemented simulator; it does not establish unbiased generalization, end-to-end bandwidth reduction, runtime or energy savings, faster convergence, or superiority over existing stale-update and lazy-aggregation methods.
