# TS2TabPFN: Time Series Classification and Extrinsic Regression through Feature Extraction and a Tabular Foundation Model

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Gabriel da Costa Merlin, Diego Furtado Silva
- 机构：University of São Paulo (USP)
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04174v1) · [PDF](https://arxiv.org/pdf/2608.04174v1)

## TLDR
TS2TabPFN bridges feature engineering and foundation models by extracting time series features (tsfresh, catch22, ROCKET) and feeding them into the tabular foundation model TabPFN, achieving state-of-the-art time series extrinsic regression and competitive classification performance.

## Abstract
Time series data are ubiquitous in practical applications, where classification (TSC) and extrinsic regression (TSER) have emerged as essential tasks for obtaining value from temporal sequences. While the literature has seen significant progress through feature-based and deep learning models, existing methods often focus either on the quality of feature extraction or on the intrinsic predictive power of complex architectures applied to raw data. This division creates a gap between the control offered by feature engineering and the automated performance of end-to-end models. This paper proposes TS2TabPFN, a framework that bridges this gap by integrating explicit feature extraction with TabPFN 2.5, a cutting-edge foundation model for tabular data, to leverage its predictive capabilities. Our extensive experimental evaluation demonstrates that TS2TabPFN significantly outperforms state-of-the-art models in TSER tasks with statistical significance, providing a robust and efficient alternative for TSC and surpassing most of the currently best-performing algorithms. These results suggest that combining foundation models with structured features overcomes single-paradigm limitations, establishing a new time series state-of-the-art.
