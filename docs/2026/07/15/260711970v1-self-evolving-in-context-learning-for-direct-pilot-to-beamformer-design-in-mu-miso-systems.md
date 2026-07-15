# Self-Evolving In-Context Learning for Direct Pilot-to-Beamformer Design in MU-MISO Systems

- 区域：速读区
- 排名：3
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Yubo Zhang, Xiaodong Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11970v1) · [PDF](https://arxiv.org/pdf/2607.11970v1)

## TLDR
The paper proposes a self-evolving in-context learning framework with curriculum training and dynamic context expansion to enable direct, gradient-free pilot-to-beamformer design in MU-MISO systems that adapts to multiple channel models and outperforms existing beamforming schemes.

## Abstract
We develop an enhanced in-context learning (ICL) framework to improve the performance of pilot-based beamforming in multi-user multiple-input single-output (MU-MISO) systems. The proposed scheme integrates the ICL-Transformer backbone with the pilot encoder-decoder network (EDN) and the beamformer EDN. A crucial feature of our ICL network is that it can handle multiple channel models without retraining, enabled by the construction of model-specific context datasets. To improve convergence and robustness, we introduce three key innovations: (a) a curriculum learning (CL) strategy that smoothly transitions from supervised LMMSE-labeled imitation to unsupervised sum-rate maximization, (b) a self-evolving mechanism that dynamically expands and refines the context datasets for all channel models during CL-based training, and (c) a mismatch-aware extension that incorporates several mismatches into the general ICL framework and bypasses explicit channel calibrations. Ablation studies validate the effectiveness of the in-context architecture and enhanced training strategies. Simulation results over diverse communication environments show that the proposed scheme is able to rapidly adapt to both seen and unseen channel models without gradient-based parameter updates, and can mitigate the mismatch issues via intelligent context constructions. Furthermore, our scheme consistently outperforms the existing beamforming schemes under pilot-based settings, including the WMMSE benchmark and the recent Transformer-based methods.
