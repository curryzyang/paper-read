# CLOE: Christoffel Loss Autoencoder for Anomaly Detection

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Léa Billet, Louise Travé-Massuyès, Elodie Chanthery, Alexandre Gaffet
- 机构：SCHAEFFLER, Université de Toulouse
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20530v1) · [PDF](https://arxiv.org/pdf/2607.20530v1)

## TLDR
CLOE combines an autoencoder with a Christoffel Function-based detector through a novel differentiable loss that guides representation learning, achieving superior anomaly detection on high-dimensional tabular data while maintaining simplicity and minimal hyperparameter tuning.

## Abstract
Semi-supervised anomaly detection plays a key role in diverse fields such as process monitoring, healthcare, and finance. However, lightweight methods often struggle with high-dimensional data and typically require careful tuning of multiple hyperparameters. Among existing approaches, Christoffel Function--based methods are attractive due to their simplicity, requiring at most a single hyperparameter. They also benefit from a well-established theoretical foundation that yields several interesting results for data science. However, their main limitation is poor scalability to high-dimensional settings. In this paper, we introduce CLOE, a new method that combines an autoencoder for dimensionality reduction with a Christoffel Function--based detector applied in the latent space. To better align representation learning with anomaly detection, we design a novel loss function that leverages the Christoffel Function to guide the autoencoder toward representations that better capture the support of the normal data distribution. We further propose a principled procedure to set the detection threshold and an efficient strategy to tune the single remaining hyperparameter. Experiments on multiple high-dimensional tabular anomaly detection benchmarks demonstrate that CLOE achieves superior performance compared to existing methods, while preserving the lightweight and low-tuning advantages of Christoffel Function--based approaches.
