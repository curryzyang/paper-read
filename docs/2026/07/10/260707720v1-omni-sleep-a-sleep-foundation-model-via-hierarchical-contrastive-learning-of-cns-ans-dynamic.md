# Omni-Sleep: A Sleep Foundation Model via Hierarchical Contrastive Learning of CNS--ANS Dynamic

- 区域：速读区
- 排名：3
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Zhoujie Hou, Song Wang, Kexin Lou, Mo Wang, Chen Wei, Quanying Liu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07720v1) · [PDF](https://arxiv.org/pdf/2607.07720v1)

## TLDR
Omni-Sleep introduces a sleep foundation model that leverages a physiological CNS–ANS hierarchy via hierarchical contrastive learning, achieving superior sleep staging and multi-disease classification with improved robustness and label efficiency across large-scale multimodal polysomnography data.

## Abstract
Sleep physiology arises from the coordinated dynamics of the central nervous system (CNS) and autonomic nervous system (ANS), as reflected by multimodal polysomnography signals including EEG, EOG, EMG, ECG, and respiration. However, existing sleep foundation models often fuse heterogeneous biosignals in a topology-agnostic manner, overlooking their physiological organization. We introduce Omni-Sleep, a sleep foundation model that uses the CNS/ANS partition as a physiological prior for topology-constrained representation learning. Omni-Sleep learns structured representations through three objectives: intra-system consistency, which captures shared subsystem-level factors within neural and cardio-respiratory signals; inter-system synchronization, which aligns subsystem trajectories to model brain--body dynamics; and latent-space masked temporal modeling, which captures long-horizon sleep dynamics. Pre-trained on over 100,000 hours of multi-center multimodal PSG data, Omni-Sleep is evaluated on sleep staging and multi-disease classification. Across datasets and modality-ablation settings, Omni-Sleep outperforms strong foundation-model baselines, showing improved label efficiency, cross-dataset generalization, and robustness to missing modalities. These results highlight the value of physiological hierarchy for generalizable sleep representation learning. Code is available at https://github.com/AutoBrain-sleep/OmniSleep.
