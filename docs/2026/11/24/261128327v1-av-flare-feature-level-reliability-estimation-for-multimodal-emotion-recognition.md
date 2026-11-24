# AV-FLARE: Feature-Level Reliability Estimation for Multimodal Emotion Recognition

- 区域：速读区
- 排名：11
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Ines Jemmali, Alaa Nfissi, Wassim Bouachir, Nizar Bouguila
- 机构：Concordia University, Université TÉLUQ
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28327v1) · [PDF](https://arxiv.org/pdf/2611.28327v1)

## TLDR
AV-FLARE explicitly estimates fine-grained audio-visual feature reliability using a supervised network and an unsupervised Gaussian Mixture Model to modulate features before temporal modeling, then fuses modalities via text-guided hierarchical cross-modal attention, improving multimodal emotion recognition robustness and performance.

## Abstract
Multimodal emotion recognition (MMER) systems typically rely on learned feature representations and attention mechanisms that implicitly weight information across time and modalities. However, these mechanisms do not explicitly incorporate input reliability, despite the presence of noise in audio, occlusions in visual data, and the sparse and event-driven nature of affective cues. We propose AV-FLARE, a framework that explicitly estimates fine-grained reliability scores across both temporal and feature dimensions prior to temporal modeling and uses them to modulate feature representations. Reliability is computed using two complementary components: (i) a supervised network trained jointly with the classification objective, and (ii) an unsupervised Gaussian Mixture Model that models global feature distributions. These signals are combined to provide both task-driven and distribution-aware reliability estimates. To integrate modalities, we introduce a hierarchical cross-modal attention mechanism in which textual features are used to guide audio-visual fusion as a semantic reference modality. Experiments on the IEMOCAP dataset show that AV-FLARE improves over a no-reliability baseline, achieving 90.81\% accuracy and 81.69\% F1-score, corresponding to gains of +4.41% and +8.56%, respectively. These results suggest that incorporating explicit input reliability estimation may improve robustness in multimodal emotion recognition under the evaluated setting.
