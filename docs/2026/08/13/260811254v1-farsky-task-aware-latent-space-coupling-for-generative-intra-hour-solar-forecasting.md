# FarSky: Task-Aware Latent-Space Coupling for Generative Intra-Hour Solar Forecasting

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Yann Fabel, Bijan Nouri, Milon Miah, Niklas Blum, Luis F. Zarzalejo, Julia Kowalski, Robert Pitz-Paal
- 机构：CIEMAT, RWTH Aachen University, DLR
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11254v1) · [PDF](https://arxiv.org/pdf/2608.11254v1)

## TLDR
FarSky is a generative intra-hour solar forecasting framework that uses task-aware latent-space coupling—a multi-task autoencoder combined with a latent diffusion model—to produce realistic future sky images and accurate probabilistic irradiance forecasts, outperforming existing methods in forecast skill (up to 11 percentage points) and ramp event detection.

## Abstract
Accurate solar irradiance forecasting is essential for the reliable integration of photovoltaic power into modern electricity grids. All-sky imagers (ASI) provide high-resolution observations of clouds, making them well suited for intra-hour forecasting. Recent deep learning approaches have substantially improved forecast accuracy but are often limited by deterministic predictions and a reduced capability to anticipate ramp events. This work proposes FarSky, a generative forecasting framework that leverages latent-space coupling to learn task-aware representations of sky images. A multi-task autoencoder first learns a shared latent representation for image reconstruction and irradiance estimation. A latent diffusion model then generates future latent states conditioned on recent observations, from which irradiance forecasts are directly decoded. Probabilistic forecasts are inherently obtained through stochastic sampling. The framework is developed using a multi-year ASI dataset acquired at the Plataforma Solar de Almería, Spain, and evaluated on two independent test datasets against persistence, state-of-the-art end-to-end, and generative forecasting approaches. FarSky achieves the best overall deterministic and probabilistic forecasting performance, improving forecast skill by up to 11 percentage points. Furthermore, it substantially improves ramp event detection over existing methods, achieving F1-scores above 60%. These results demonstrate the potential of combining generative models with task-aware latent-space coupling for solar forecasting.
