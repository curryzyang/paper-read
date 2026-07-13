# HERO: A Heterogeneity-Aware Benchmark Library for Federated Continual Learning

- 区域：速读区
- 排名：2
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Thinh T. H. Nguyen, Le-Tuan Nguyen, Minh-Duong Nguyen, Nhi Trinh, Anh Tran Nam Nguyet, Dung D. Le, Kok-Seng Wong
- 机构：VinUniversity
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08784v1) · [PDF](https://arxiv.org/pdf/2607.08784v1)

## TLDR
HERO is a heterogeneity-aware benchmark library for Federated Continual Learning that decouples task split, client data split, and client task sequence to enable controlled, reproducible, and setting-aware evaluation, as demonstrated on image-based FCIL and graph-based Domain-IL benchmarks.

## Abstract
Federated continual learning (FCL) evaluates how distributed clients learn from changing data streams while retaining previously learned knowledge. Existing evaluations are difficult to compare because they often change datasets, task splits, client data splits, task orders, backbones, memory assumptions, and reporting rules simultaneously. We introduce \textbf{HERO}, a heterogeneity-aware benchmark library for FCL. HERO builds benchmark streams by separating three choices that are often coupled, namely the task split, the client data split, and the client task sequence. In HERO-Core, the main comparable benchmark, $α$ controls client data skew and $ρ$ controls task-order mismatch. We evaluate representative FCL methods on CIFAR-100 and TinyImageNet using final average accuracy, average forgetting, and bottom-10\% client accuracy. We also include a graph-based Domain-IL portability case study on OGB-MolPCBA, where scaffold-domain granularity changes the input distribution while the prediction task remains fixed. Our results show that method behavior changes across easy and heterogeneous settings, that average accuracy can hide weak bottom-client performance, that task-order mismatch favors different strategies from synchronized evaluation, and that the same HERO interface can expose domain-shift difficulty beyond image-based FCIL. HERO releases benchmark streams, configurations, method implementations, and reporting scripts to support reproducible and setting-aware FCL evaluation.
