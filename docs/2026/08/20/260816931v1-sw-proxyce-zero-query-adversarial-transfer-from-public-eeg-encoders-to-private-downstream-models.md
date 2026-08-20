# SW-ProxyCE: Zero-Query Adversarial Transfer from Public EEG Encoders to Private Downstream Models

- 区域：速读区
- 排名：8
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Linhua Cong, Dingkun Liu, Dongrui Wu
- 机构：Huazhong University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16931v1) · [PDF](https://arxiv.org/pdf/2608.16931v1)

## TLDR
This paper proposes SW-ProxyCE, a zero-query adversarial transfer attack that exploits publicly released EEG foundation encoders to generate transferable adversarial examples against private downstream models using only a small labeled reference set, revealing that strong encoder transferability introduces a security risk.

## Abstract
Electroencephalography (EEG) foundation models have recently emerged as a promising paradigm for EEG decoding by learning reusable representations from large-scale heterogeneous neural recordings. However, the open release of EEG foundation encoders, while facilitating downstream developments, also introduces a previously unexplored security risk: publicly available representations may make private downstream models vulnerable. This paper investigates adversarial transfer attacks in EEG foundation model deployment in a public-encoder and private-downstream setting, where attackers have white-box access to a released encoder and a small task-matched labeled reference set, but no access or query to victim parameters, outputs, or gradients. We propose Shrinkage-Whitened Proxy Cross-Entropy (SW-ProxyCE), a query-free task-aware attack framework that recovers task-level decision geometry from a small labeled reference set through shrinkage-whitened class prototypes, enabling transferable adversarial generation without training an additional surrogate classifier. We evaluated SW-ProxyCE across three EEG tasks using three general-purpose foundation encoders and a paradigm-specific pre-trained encoder, covering both linear-probing and full-fine-tuning downstream models in cross-subject and within-subject scenarios. Results demonstrated that adversarial examples generated from the public encoder and limited labeled references can effectively transfer to inaccessible downstream models. SW-ProxyCE consistently outperformed task-agnostic representation-shift attacks, revealing that the strong transferability of EEG foundation models does not necessarily lead to adversarial robustness. Our code will be available on GitHub.
