# Does Joint-Embedding Predictive Architecture Pretraining Help Time Series Forecasting?

- 区域：速读区
- 排名：2
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yutong Feng, Bowen Liao, See Kiong Ng, Yuxuan Liang
- 机构：National University of Singapore, Hong Kong University of Science and Technology (Guangzhou), South China University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31680v1) · [PDF](https://arxiv.org/pdf/2609.31680v1)

## TLDR
A large-scale cross-architecture evaluation shows that JEPA pretraining for time series forecasting is not universally beneficial, producing consistent gains for some backbones but consistent degradation for others across both temporal and spatio-temporal tasks.

## Abstract
Joint-embedding predictive architectures (JEPA) have emerged as a promising self-supervised pretraining paradigm for time series, learning representations by predicting target embeddings in latent space rather than reconstructing raw signals. Yet evidence on their benefits remains mixed, and most studies test only a single backbone or a narrow set of architectures, leaving unclear whether JEPA pretraining is a reliable improvement or one that depends heavily on the downstream model. We address this gap through a large scale evaluation of one JEPA instantiation across nine backbones and eleven benchmarks spanning temporal and spatio-temporal forecasting, the most extensive cross architecture assessment of JEPA for time series to date. We find that the benefit of this instantiation varies sharply across backbones, producing consistent gains for some architectures and consistent degradation for others, even on the same dataset. This pattern holds across both task families, indicating the variability is a general property of this instantiation rather than a dataset specific artifact worth accounting for when choosing a backbone in practice.
