# SPERA: Spherical Prior EEG Foundation Model with Geometry- and Frequency-Aware Latent Prediction

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Minsu Kim, Ye-Sung Kim, Hyeseong Jeon, Wooseok Hyung, Joshua Lee, Chang-Hwan Im
- 机构：Hanyang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10571v1) · [PDF](https://arxiv.org/pdf/2610.10571v1)

## TLDR
SPERA is an EEG foundation model that combines JEPA-based latent prediction with a Legendre-polynomial spherical electrode prior, factorized spatiotemporal attention with periodic full-attention blocks, and a relational spectral regularizer, achieving state-of-the-art average balanced accuracy across nine downstream clinical, cognitive, and BCI tasks after pretraining on ~80,000 hours of EEG.

## Abstract
Electroencephalography (EEG) provides a non-invasive measure of ongoing neural activity, but building general-purpose EEG models remains challenging due to the heterogeneity of subjects, devices, and electrode montages. Existing EEG foundation models predominantly rely on reconstruction-based objectives defined on the observed signal, which contains both neural and non-neural components. We introduce SPERA (Spherical Prior EEG Representation Architecture), an EEG foundation model that adopts the joint-embedding predictive architecture (JEPA) to predict in latent space. SPERA introduces a Legendre-polynomial spatial prior, incorporated into attention to encode varying scalp electrode geometries. Two further components adapt the model to EEG: factorized temporal and spatial attention interleaved with periodic full-attention blocks, and a relational spectral regularizer aligning latent similarity structure with spectral views. Pretrained on approximately 80,000 hours of EEG from 29,048 subjects across 106 datasets, SPERA achieves the highest average balanced accuracy across nine downstream tasks spanning clinical, cognitive, and BCI applications. SPERA further exhibits strong parameter efficiency under linear probing and robustness across varying recording conditions, suggesting its potential as a general-purpose backbone for diverse EEG analyses.
