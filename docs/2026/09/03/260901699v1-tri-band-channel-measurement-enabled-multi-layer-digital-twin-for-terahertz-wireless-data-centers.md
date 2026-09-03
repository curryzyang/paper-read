# Tri-Band Channel Measurement-Enabled Multi-Layer Digital Twin for Terahertz Wireless Data Centers

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Mingjie Zhu, Ziming Yu, Guangjian Wang, Chong Han
- 机构：Shanghai Jiao Tong University, Huawei Technologies Company Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01699v1) · [PDF](https://arxiv.org/pdf/2609.01699v1)

## TLDR
This paper proposes a measurement-driven, four-layer digital twin framework for terahertz wireless data centers, using 140/220/300 GHz channel measurements to calibrate a physical twin and a LoS-aware AI neural channel twin that enables real-time reconstruction, system-level coverage/interference evaluation, and deployment planning, achieving over 90% coverage for ceiling-mounted APs at a 10 dB SINR threshold.

## Abstract
The rapid growth of AI computing has driven increasing demands for flexible and high-capacity data-center interconnections. Owing to its ultra-wide bandwidth and high spatial reuse capability, terahertz (THz) communication has emerged as a promising solution for future wireless data centers, while digital twins (DTs) enable efficient wireless planning and real-time optimization. In this work, a measurement-driven multi-layer DT framework is proposed for THz wireless data centers, where the physical, channel, evaluation, and manipulation layers are progressively constructed from bottom to top. First, extensive channel measurements are conducted at 140, 220, and 300 GHz to characterize frequency-dependent propagation behaviors. Based on the tri-band measurements, a measurement-calibrated physical twin is established by jointly optimizing the geometry, material, antenna, and hybrid propagation models. On top of the physical twin, a line-of-sight (LoS)-aware implicit neural field is developed to construct an AI channel twin for efficient channel reconstruction. The proposed AI twin learns location-dependent channel statistics from the calibrated twin, enabling real-time prediction of received power and LoS probability. Building upon the reconstructed channel field, a system-level evaluation layer is derived to analyze coverage and interference for both AP-to-rack and rack-to-rack communications. Experimental results show that the proposed AI twin achieves lower power reconstruction error than existing neural-field baselines while maintaining real-time inference capability. Moreover, the ceiling-mounted AP deployment achieves over 90% coverage under a 10 dB signal-to-interference-plus-noise ratio (SINR) threshold, demonstrating the effectiveness of the proposed DT framework for THz wireless data-center planning and optimization.
