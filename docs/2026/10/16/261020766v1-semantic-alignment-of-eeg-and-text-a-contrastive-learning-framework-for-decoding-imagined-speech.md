# Semantic Alignment of EEG and Text: A Contrastive Learning Framework for Decoding Imagined Speech

- 区域：速读区
- 排名：12
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Shahryar G. Namdari, Francesco Iacomi, Riccardo Barbieri, Luca Mainardi
- 机构：Politecnico di Milano
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20766v1) · [PDF](https://arxiv.org/pdf/2610.20766v1)

## TLDR
This paper proposes a contrastive EEG–language alignment framework that maps imagined-speech EEG into a frozen pretrained text encoder’s embedding space using semantically reweighted EEG–sentence alignment and text-prototype class discrimination, achieving decoding performance comparable to a closed-set classifier on the Chisco 39-category dataset while supporting similarity-based retrieval, intrinsic reliability ranking, and broader semantic probing.

## Abstract
Imagined speech decoding from EEG offers a promising route toward naturalistic brain-computer interfaces. Traditional closed-set classifiers treat semantic categories as independent labels and do not explicitly exploit relationships among linguistic intents, limiting output flexibility. We adapt a multimodal contrastive learning framework to imagined speech, aligning EEG trials with language representations in the embedding space of a frozen pretrained text encoder. An EEG encoder is trained with a composite objective combining semantically reweighted EEG-sentence alignment and text-prototype-based class discrimination, encouraging semantic structure while preserving separability among 39 intent categories. We evaluate the approach on the Chisco imagined speech dataset across five subjects, reporting Top-k accuracy, macro-F1, and balanced pairwise matching accuracy (2v2). We also investigate maximum EEG-text cosine similarity (MaxCosine) as an intrinsic indicator of decoding reliability and probe semantic structure beyond category labels using five evaluation-time semantic axes and a qualitative Semantic Gallery Probe (SGP) with previously unseen candidate sentences. The contrastive framework achieved decoding performance comparable to a task-optimized closed-set classifier while mapping EEG into a frozen language embedding space. MaxCosine identified subsets of held-out trials with higher Top-1 and Top-5 accuracy across subjects. Evaluation-time semantic axes showed mean agreement above the 50% chance reference across all five dimensions, and the SGP qualitatively illustrated direct comparison with unseen candidate sentences. Together, these findings suggest that EEG-language alignment can retain comparable fixed-intent decoding while supporting similarity-based retrieval, intrinsic reliability ranking, and evaluation of broader semantic structure.
