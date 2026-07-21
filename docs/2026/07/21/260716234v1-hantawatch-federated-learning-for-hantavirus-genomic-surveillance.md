# HantaWatch: Federated Learning for Hantavirus Genomic Surveillance

- 区域：速读区
- 排名：9
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Shanika Iroshi Nanayakkara, Shiva Raj Pokhrel
- 机构：Deakin University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16234v1) · [PDF](https://arxiv.org/pdf/2607.16234v1)

## TLDR
HantaWatch introduces a federated learning framework for decentralized hantavirus genomic surveillance that enables collaborative sequence-based model training without sharing raw data, using adaptive DU-FedProx optimization to handle non-IID heterogeneity, and outputs risk scores, confidence estimates, and ranked expert-review priorities for efficient decision support.

## Abstract
Hantavirus genomic surveillance is limited by the distribution of sequence data, non-IID source heterogeneity, and constrained expert-review capacity. We propose HantaWatch, a federated learning framework that enables laboratories and surveillance sites to collaboratively train sequence-based models without sharing raw data. HantaWatch integrates k-mer feature extraction, source-aware federated client construction, adaptive DU-FedProx optimization, surveillance-specific model selection, and prediction-only triage. Experiments on binary and multi-class tasks show that HantaWatch supports high-risk screening, outbreak-associated prediction, clade classification, and clinical-syndrome categorization while balancing predictive performance, false-negative risk, and update stability. The framework converts model output into risk scores, confidence estimates, uncertainty flags, and ranked expert-review priorities. HantaWatch therefore provides a practical federated decision-support layer for decentralized Hantavirus surveillance, supporting expert prioritization without replacing laboratory or public-health interpretation.
