# Radio-Frequency Convolutional Neural Networks

- 区域：速读区
- 排名：8
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Zhihui Gao, Shi-Yuan Ma, Yiran Chen, Dirk Englund, Tingjun Chen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19279v1) · [PDF](https://arxiv.org/pdf/2609.19279v1)

## TLDR
The paper introduces radio-frequency convolutional neural networks (RF-CNNs) that repurpose existing wireless radio mixers to perform CNN inference via frequency-domain convolution, enabling deep-model accuracy and down to 0.72 fJ per multiply-accumulate by sharing analog hardware with communication.

## Abstract
Running artificial intelligence (AI) models directly on edge devices such as smartphones, wearables, and drones offers low latency, pervasive scalability, and data privacy, but these devices rarely carry the computing capability that modern neural networks demand. Edge accelerators have been developed in response, yet each adds computing hardware to devices already constrained in size, weight, power, and cost (SWaP-C). An alternative lies in what these devices already carry: the frequency mixer in every wireless radio multiplies signals in time, natively performing convolution in the frequency domain. Here we introduce radio-frequency convolutional neural networks (RF-CNNs), which repurpose existing communication hardware for CNN inference. Multi-channel convolutions are mapped onto frequency tones for a passive mixer to execute in a single pass. We experimentally demonstrate that RF-CNN runs deep CNNs up to 26.4 million parameters and nine layers from classification of wireless signals and images to controllable image generation, close to full-precision performance. Because the weights arrive over the air and the analog hardware is shared with communication, the edge device spends energy only on data preparation and readout-down to 0.72 femtojoules per multiply-accumulate, two orders of magnitude less than it would cost on an added digital processor. These results suggest that deployed wireless infrastructure can bring efficient, state-of-the-art AI inference to the billions of devices it already connects.
