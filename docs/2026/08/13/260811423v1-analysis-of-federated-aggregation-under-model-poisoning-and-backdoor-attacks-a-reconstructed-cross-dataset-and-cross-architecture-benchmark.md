# Analysis of Federated Aggregation under Model Poisoning and Backdoor Attacks: A Reconstructed Cross-Dataset and Cross-Architecture Benchmark

- 区域：速读区
- 排名：10
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Soumya Mazumdar, Vineet Kumar Rakesh, Tapas Samanta
- 机构：Gargi Memorial Institute of Technology, Variable Energy Cyclotron Centre, Homi Bhabha National Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11423v1) · [PDF](https://arxiv.org/pdf/2608.11423v1)

## TLDR
A reconstructed 500-cell benchmark of five federated aggregation methods under clean, sign-flipping, Gaussian, and BadNets conditions finds Trimmed Mean best on clean accuracy and Krum best under attacks, while provenance and code audits reveal metric-semantics and update-correspondence caveats that limit claims to descriptive comparisons.

## Abstract
Robust comparisons of federated aggregation methods require joint consideration of predictive performance, threat definitions, metric semantics, and execution provenance. A 500-cell seed-1 evaluation matrix was reconstructed across five aggregation methods, five datasets, five architectures, and four recorded conditions: clean, sign-flipping, Gaussian, and BadNets. Successful execution logs were identified for 454 original runs and 36 repaired or rerun executions, whereas 10 clean SVHN cells were supported by summary-only provenance. Trimmed Mean achieved the highest clean macro-mean accuracy (76.02%) and the lowest mean within-task rank (1.70). Krum attained the highest recorded accuracy under both sign-flipping and Gaussian configurations. These relative rankings remained unchanged when analysis was restricted to 21 task pairs for which original successful logs were available for every method-condition combination. Audit of the supplied BadNets metric implementation established that every test input is triggered prior to target-label counting; consequently, the retained metric represents Triggered Target-Label Rate (TTLR) rather than a conventional target-excluding attack success rate. An audit of the supplied FedPARETO scaffold further identified a pathway in which predictive summaries may characterize an uncorrupted local model while the aggregation weight is applied to a separately corrupted update, introducing a potential discrepancy between reported predictive outcomes and the updates used for aggregation. The canonical matrix contains a single identified seed for each cell, and exact attack and configuration lineage is incomplete. Accordingly, the findings should be interpreted as descriptive comparisons within the recorded configurations and not as statistical estimates or universal claims regarding robustness.
