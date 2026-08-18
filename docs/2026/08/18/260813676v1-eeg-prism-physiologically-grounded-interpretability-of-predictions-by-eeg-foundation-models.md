# EEG-PRISM: Physiologically-Grounded Interpretability of Predictions by EEG Foundation Models

- 区域：速读区
- 排名：4
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Deeksha M Shama, Punnisa Amornsirikul, Archana Venkataraman
- 机构：Boston University, Johns Hopkins University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13676v1) · [PDF](https://arxiv.org/pdf/2608.13676v1)

## TLDR
EEG-PRISM is a post-hoc, model-agnostic framework that maps time-channel attributions from EEG foundation models into clinically meaningful spectral and source domains via linear transformations, enabling accurate seizure localization and biomarker discovery without retraining the underlying model.

## Abstract
Objective: Foundation models represent the next advancement in AI for EEG analysis; however current explainable AI techniques provide attribution scores in the time-channel input space, which is mismatched to clinical intuition about EEG. Thus, there is a critical need for a universal method that can extend the interpretability of any foundation model to alternative and physiologically relevant domains without modifying or retraining the underlying model. Methods: EEG-PRISM leverages linear transformations and established backpropagation rules to map time-channel attribution scores into alternative domains. We derive mappings to the frequency domain via an invertible DFT and to the source domain via an approximately invertible EEG generative model. We evaluate EEG-PRISM in simulated and real data, assessing recovery of ground-truth phenomena across domains with five foundation models and four AI explainers. Results: In simulation, EEG-PRISM achieves near-perfect spectral recovery and 69.2% spatial accuracy. In epilepsy, EEG-PRISM correctly determines that delta-theta activity is most salient and correctly localizes the seizure onset region with 50% accuracy. In autism, EEG-PRISM localizes the predictive delta-alpha biomarkers to frontal and temporal regions, consistent with prior work. Conclusion: EEG-PRISM is a theoretically-grounded post-hoc attribution method with accurate mapping into the spectral and spatial domains. It supports window-level analysis of transient events (e.g., seizures) and group-level identification of clinically relevant biomarkers (e.g., autism), thus advancing interpretable EEG foundation models. Significance: This work enables physiologically-grounded interpretation of EEG foundation models and supports clinically relevant insights such as event localization and biomarker identification.
