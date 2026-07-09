# Creating Power Distribution Network Layouts Using Generative Adversarial Networks and Image-Based Representations

- 区域：速读区
- 排名：3
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Juan Manuel Garcia-Perez, Carlos Mateo
- 机构：Comillas Pontifical University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06622v1) · [PDF](https://arxiv.org/pdf/2607.06622v1)

## TLDR
This paper proposes a generative framework based on Generative Adversarial Networks (GANs) that uses image-based representations to create power distribution network layouts, learning patterns from rasterized GIS data and enabling both unconditional and conditional generation, though with limitations in training stability and electrical constraints.

## Abstract
Utilities increasingly rely on planning and operational tools to cope with the increased penetrations of distributed energy resources, yet the lack of realistic, openly available datasets remains a major barrier for benchmarking and comparison. Traditional test feeders, and recently proposed large-scale synthetic networks alleviate this issue but are typically based on heuristic rules and do not learn directly from data. This paper proposes a generative framework based on Generative Adversarial Networks (GANs) to create power distribution network layouts using image-based representations. The model is trained on rasterised views of distribution systems and can operate in two modes: an unconditional configuration that learns layout patterns from the training dataset, and conditional configurations that incorporate geographical context such as street maps and the spatial distribution of consumers. The methodology includes dataset preparation from Geographic Information System (GIS) sources, GAN architecture design, and the analysis of training stability and image resolution. Results from three representative cases show that the proposed approach can reproduce the topologies of low (LV), medium (MV) and high voltage (HV) feeders and align generated layouts with underlying geographical structures. At the same time, the study reveals limitations related to training stability, resolution-dependent artefacts and limits, and the absence of explicit electrical constraints. The proposed framework constitutes a data-driven complement to existing synthetic network generation methods, and could be applied to propose distribution network layouts for the electrification of new areas. This would require future extensions towards power flow, electrically validated models.
