# TD-DPO: Difference-Aware Preference Optimization for Mitigating Sycophancy in Clinical Autism Intervention Dialogue

- 区域：速读区
- 排名：13
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Shuzhong Lai, Junhong Lai, Chenxi Li, Qing Zhou, Haifeng Li, Gang Pan, Lin Yao, Yueming Wang
- 机构：Zhejiang University School of Medicine, Children's Hospital Zhejiang University School of Medicine, Zhejiang University, State Key Laboratory of Brain-Machine Intelligence, Nanhu Brain-Computer Interface Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18304v1) · [PDF](https://arxiv.org/pdf/2607.18304v1)

## TLDR
TD-DPO introduces a token-level difference-aware preference optimization method with minimal-edit data augmentation to reduce sycophancy in large language models for autism intervention dialogues while preserving intervention capabilities.

## Abstract
The sycophancy of large language models can increase the safety risk in intervention dialogue for autistic children. Supervised fine-tuning can somewhat reduce sycophancy, but relying solely on positive examples is often insufficient to identify and correct failure patterns. We observe that sycophancy behaviors can often be localized to a limited span within the model response. In this regime, sequence-level preference optimization can over-update preference-irrelevant tokens and degrade intervention ability. To address this, we propose the \textbf{M}inimal \textbf{E}dit \textbf{D}ata \textbf{A}ugmentation (MEDA) strategy to construct controlled, stable, minimal edit preference pairs and \textbf{T}oken-level \textbf{D}ifference \textbf{D}irect \textbf{P}reference \textbf{O}ptimization (TD-DPO), which upweights difference tokens between chosen and rejected responses while downweighting shared tokens to suppress background drift. Extensive experiments across multiple backbones and evaluators show that TD-DPO achieves a better trade-off between sycophancy mitigation and intervention ability retention in our offline settings, highlighting its potential as a practical alignment approach for autism intervention.
