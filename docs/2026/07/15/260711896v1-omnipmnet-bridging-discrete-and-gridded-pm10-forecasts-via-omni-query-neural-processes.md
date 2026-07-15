# OmniPMNet: Bridging discrete and gridded PM10 forecasts via omni-query neural processes

- 区域：速读区
- 排名：4
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Shuangshuang He, Shuo Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11896v1) · [PDF](https://arxiv.org/pdf/2607.11896v1)

## TLDR
OmniPM-Net is a neural process fusion model that combines discrete GNN station forecasts with gridded CAMS forecasts into a shared spatial representation, achieving consistent and accurate PM10 predictions at both station and grid levels while reducing CAMS mean absolute error by 30% and improving performance during dust storms.

## Abstract
Forecasting particulate matter (PM10) requires both station-scale accuracy and continuous spatial fields, especially during severe dust storms. Chemical transport models (CTMs) provide gridded forecasts but retain local biases, whereas graph neural networks (GNNs) track monitoring sites well at short lead times but do not produce gridded outputs. Here we present OmniPM-Net, a Convolutional Conditional Neural Process (ConvCNP)-based fusion model that reconciles these two forecast types within a shared spatial representation. A terrain-aware Gaussian set convolution lifts irregular GNN station forecasts onto a regular grid, where a multi-scale Spatial Source Attention (SSA) module blends them with Copernicus Atmosphere Monitoring Service (CAMS) forecasts; a shared omni-query readout then decodes this representation into consistent PM10 predictions at either stations or grid cells over a 108 h horizon. Evaluated across 1,618 air-quality monitoring stations throughout China over the full year of 2024, OmniPM-Net matches the station-level accuracy of the stronger GNN baseline (mean absolute error 21.14 versus 22.00 ug/m3) and reduces the CAMS mean absolute error by 30%, while simultaneously delivering the gridded fields that the discrete GNN cannot. Its clearest gains are in the high-concentration tail, where the 90th-percentile MAE falls by 9% relative to the GNN and 25% relative to CAMS, and during dust episodes, where it improves categorical detection skill while tracking the evolving spatial trajectory.
