# Regularizing modality contribution drift in multimodal continual learning

- 区域：速读区
- 排名：2
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Zhen Zhang, Jielei Chu, Bin Liu, Tianrui Li
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27260v1) · [PDF](https://arxiv.org/pdf/2607.27260v1)

## TLDR
TLDR: The paper identifies modality contribution drift (MCD) as an overlooked cause of forgetting in multimodal continual learning and proposes CMCDR, a replay-based and replay-free regularization method that preserves modality-specific and interaction contribution structures across incremental tasks.

## Abstract
Multimodal continual learning (MMCL) aims to learn emerging knowledge from multimodal data while preserving knowledge. To mitigate forgetting, current MMCL methods usually focus on cross-modal representation alignment or semantic similarity, but they overlook whether the relative contributions of individual modalities and their interactions remain stable across incremental tasks. We term this decision-level shift Modality Contribution Drift (MCD) and quantify it with the MCD score, which combines contribution-strength and relative-reliance changes under controlled interventions on modality subsets. Theoretical and empirical analyses further explain why current MMCL methods cannot reliably mitigate this drift. To this end, we propose Continual Modality Contribution Drift Regularization (CMCDR), which preserves the modality contribution structure of previously learned tasks. Since MMCL settings differ in whether old exemplars are available, CMCDR includes both replay-based and replay-free versions. The replay-based version uses modality-subset interventions as diagnostic probes on stored old samples, compares their contribution profiles between the current model and a frozen previous model, and constrains changes in old-sample modality-specific and interaction contributions. The replay-free version uses current-task samples as probes and distills the frozen model's old-task contribution responses, thereby regularizing the observed contribution profile without exemplars. Experiments on multimodal class-incremental learning and continual visual question answering validate the generality and effectiveness of CMCDR.
