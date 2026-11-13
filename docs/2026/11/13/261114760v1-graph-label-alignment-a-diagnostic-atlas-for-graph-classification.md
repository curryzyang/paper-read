# Graph Label Alignment: A Diagnostic Atlas for Graph Classification

- 区域：速读区
- 排名：13
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Neelam Akula, Varun Shiralkar, Murat Kantarcioglu, Baris Coskunuzer
- 机构：Virginia Tech, University of Texas at Dallas
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14760v1) · [PDF](https://arxiv.org/pdf/2611.14760v1)

## TLDR
The paper introduces graph label alignment—a lightweight diagnostic using structural (SLA) and feature-only (FLA) label-predictability probes—and shows that the resulting SLA–FLA plane explains when graph classification benchmarks are easy for pooled models versus when success depends on interaction-dependent structure–feature reasoning.

## Abstract
Graph classification benchmarks vary widely in difficulty: some are solved by simple pooled baselines, while others remain challenging for GNNs and graph transformers. We take a data-centric view and ask whether benchmark success is driven by genuine structure--feature reasoning or by label signal already accessible from restricted marginal views. We introduce graph label alignment, a lightweight diagnostic that measures label accessibility through two supervised probes computed without training a graph encoder: structural label alignment (SLA), based on permutation-invariant topological and spectral summaries, and feature label alignment (FLA), based on pooled node features with edges removed. Across real graph classification benchmarks and multiple pooled backbones, the resulting SLA--FLA plane strongly organizes test accuracy, with low-alignment datasets forming a consistent regime where standard pooled pipelines struggle. To probe what lies beyond marginal accessibility, we introduce controlled interaction-dominated stress tests, including heterophilic ego-graphs and synthetic Twins tasks whose structural and feature marginals are matched across classes but whose role--feature couplings differ. These results show that high alignment explains much of easy benchmark performance, while low alignment reveals regimes where success requires preserving structure--feature correspondence beyond standard pooled representations.
