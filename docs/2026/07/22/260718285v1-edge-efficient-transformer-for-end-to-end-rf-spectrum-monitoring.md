# Edge-Efficient Transformer for End-to-End RF Spectrum Monitoring

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Zhifan Song, Haralampos-G. Stratigopoulos, Hassan Aboushady
- 机构：Sorbonne Université
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18285v1) · [PDF](https://arxiv.org/pdf/2607.18285v1)

## TLDR
E-SpecFormer, an edge-efficient Transformer family with a novel Softmax- and LayerNorm-free linear attention mechanism (LiTAN), achieves state-of-the-art accuracy for end-to-end automatic modulation and covert channel recognition on RF spectrum monitoring with minimal parameters and low latency on FPGA/CPU, enabling real-time IoT deployment.

## Abstract
We present E-SpecFormer (Edge Spectrum monitoring Transformer) for end-to-end automatic modulation and covert channel (CC) recognition. We introduce LiTAN (Linear Tanh Attention Network), a Softmax- and LayerNorm-free attention mechanism that reduces complexity while increasing accuracy in RF tasks. E-SpecFormer is parameterized in four scalable variants (Nano, Small, Medium, Large) to accommodate diverse hardware constraints. Using the RadioML2018 dataset for modulation recognition, the Nano variant achieves 86.5% average accuracy for Signal-to-Noise Ratios (SNRs)>0 dB, and on the hardware Trojan (HT)-based CC dataset it reaches 94.2% accuracy, both with fewer than 10k parameters and up to speed of 92 μs per frame on FPGA/CPU co-execution, surpassing state-of-the-art edge models at a fraction of their cost. These results establish E-SpecFormer as an edge-efficient solution for real-time spectrum intelligence on Internet of Things (IoT) devices. GitHub link to the repository: https://github.com/zsniko/E-SpecFormer.
