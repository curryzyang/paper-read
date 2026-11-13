# Beyond Row-Level Prediction: Evaluating and Learning Composition for Reusable Table Representations

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Ali Younes, Saeed Ghoorchian, Maximilian Schambach, Georgia Chalvatzaki, Johannes Höhne
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14697v1) · [PDF](https://arxiv.org/pdf/2611.14697v1)

## TLDR
The paper introduces a table-level embedding benchmark and shows that the compositional rule used to aggregate local cell/schema states—learned via self-supervised support-conditioned distribution matching (SCDM)—is critical for reusable table representations, substantially improving partial-view consistency, clustering, and retrieval over strong row-level models and simple fingerprints.

## Abstract
Tables are compositional, with content spread across a schema, cell values, rows, and columns. Large-scale operations such as retrieval, overlap estimation, deduplication, and data curation need these local signals composed into one reusable embedding vector per table. Table representation methods, however, are mostly evaluated through row-level prediction or supervised downstream tasks, which do not measure table-level embedding quality directly. We introduce a benchmark that evaluates table-level embeddings through four desiderata: consistency under partial views, discriminability across label granularities, robustness to benign perturbations, and efficiency. Across twelve methods on synthetic and real corpora, lightweight schema- and text-based fingerprints are among the strongest. The sharpest contrast comes from two tabular foundation models, TabPFN and ConTextTab: although both are strong row-level predictors, their states, composed by mean, max, or three further parameter-free pooling rules, trail the strongest fingerprints. We therefore ask whether the gap lies in the encoder or in the compositional rule. Keeping ConTextTab frozen, we learn only the compositional rule over its cell states, using support-conditioned distribution matching (SCDM), a self-supervised loss we propose that matches the distribution of embedding similarities to the distribution of partition overlaps within and across tables. Across all fifteen head configurations, the learned rule raises the Spearman correlation between embedding similarity and partial-view overlap from 0.04 to 0.43-0.50 on synthetic data and improves triplet ranking, clustering, and retrieval, with smaller but systematic gains on real data. A downstream parent-table retrieval task confirms these findings. How local states are composed, and with what objective, substantially affects the quality of table-level embeddings.
