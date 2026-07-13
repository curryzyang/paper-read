# Pattern-Aware Graph Neural Networks for Handling Missing Data

- 区域：速读区
- 排名：14
- 匹配度：1.4/10
- 来源：arxiv
- 作者：Minett Tran, Taehee Jeong
- 机构：San Jose State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08915v1) · [PDF](https://arxiv.org/pdf/2607.08915v1)

## TLDR
Pattern-aware graph neural networks that explicitly encode missingness patterns achieve substantial improvements over traditional methods (17% balanced accuracy, 22% F1-macro) across diverse datasets, with simple random embeddings performing nearly as well as learned ones, indicating that distinguishing patterns matters more than task-specific optimization.

## Abstract
Missing data is ubiquitous in real-world datasets. Traditional methods either discard incomplete samples or apply imputation techniques that ignore potentially informative missingness patterns, implicitly assuming that missingness occurs randomly. However, missingness patterns might provide additional information. We propose pattern-aware graph neural networks that explicitly encode which features are missing alongside observed values. We used four encoding strategies -- learned embeddings, frozen random embeddings, statistical features, and hierarchical representations -- across seven UCI datasets with naturally occurring missingness. Our Pattern-aware methods achieve substantial improvements over baselines, with an average improvement of 17\% in balanced accuracy and 22\% in F1-macro across all datasets. The benefits vary significantly by dataset: annealing shows dramatic improvement (+80\% balanced accuracy), while hepatitis and soybean show minimal gains (+4--5\%). Notably, even simple random pattern embeddings perform comparably to learned embeddings (0.650 vs 0.663 balanced accuracy), suggesting that distinguishing between patterns may be more important than task-specific optimization. Our ablation study reveals that attention mechanisms, while helpful, are not critical when pattern information is available -- simple mean aggregation with pattern awareness achieves 0.640 balanced accuracy compared to 0.645 for attention-based variants.
