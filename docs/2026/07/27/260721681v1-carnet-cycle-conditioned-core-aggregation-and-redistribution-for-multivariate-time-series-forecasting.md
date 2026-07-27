# CARNet Cycle-Conditioned Core Aggregation and Redistribution for Multivariate Time Series Forecasting

- 区域：速读区
- 排名：9
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Awsaf Tausif Adib, Md. Shahria Sarker Shuvo, Md. Estehaar Ahmed Emon, Mustafa Kamal, Fuad Rahman, Shafin Rahman, Nabeel Mohammed
- 机构：North South University, Apurba Technologies
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21681v1) · [PDF](https://arxiv.org/pdf/2607.21681v1)

## TLDR
CARNet proposes a cycle-conditioned core aggregation and redistribution framework that integrates global periodic patterns into linear-complexity cross-variate dependency modeling, consistently outperforming transformer and non-attention baselines on multivariate forecasting benchmarks.

## Abstract
Accurately modeling cross-variate dependencies remains a key challenge in multivariate time series forecasting, particularly in the presence of strong periodic patterns. Many existing approaches rely on attention-based mechanisms that incur quadratic complexity and scale poorly with increasing numbers of variates. Recent attention-free aggregation models address this issue through linear-complexity core-based interactions, but they do not explicitly leverage the global periodic structure present in the data. To overcome this limitation, we propose CARNet, a Cycle-Conditioned Core Aggregation and Redistribution framework that integrates global recurrent cycle information into efficient core based interaction modeling via Multihead Core Aggregation. Extensive experiments on multiple real-world multivariate forecasting benchmarks demonstrate that CARNet consistently outperforms strong transformer and non-attention baselines across diverse prediction horizons while preserving linear-complexity modeling of cross-variate dependencies.
