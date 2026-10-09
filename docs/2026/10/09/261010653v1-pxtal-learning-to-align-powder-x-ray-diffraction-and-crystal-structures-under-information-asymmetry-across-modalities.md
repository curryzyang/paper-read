# PXtal: Learning to Align Powder X-Ray Diffraction and Crystal Structures under Information Asymmetry across Modalities

- 区域：速读区
- 排名：6
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Zhuoran Yang, Christopher M. Collins, Bei Peng, Luke M. Daniels, Matthew J. Rosseinsky, Vladimir V. Gusev
- 机构：University of Liverpool, University of Sheffield
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10653v1) · [PDF](https://arxiv.org/pdf/2610.10653v1)

## TLDR
PXtal is an unbalanced optimal transport-based framework that aligns powder X-ray diffraction and crystal structure representations under physically imposed information asymmetry, improving PXRD-to-crystal retrieval and downstream transfer over contrastive baselines.

## Abstract
Scientific multimodal learning commonly assumes that paired views are comparably informative. Powder X-ray diffraction (PXRD) makes this mismatch explicit: compressing a three-dimensional crystal structure into a one-dimensional diffraction pattern loses information and makes the pattern harder to connect to the crystal structure that produced it. We introduce PXtal, a framework for learning aligned PXRD and crystal representations under this physically imposed information asymmetry. PXtal uses Unbalanced Optimal Transport (UOT) to adapt the cross-modal coupling and coupling-level generalized Kullback-Leibler (GKL) divergence to supervise the full transport plan. Across six test sets, including four zero-shot transfer sets, PXtal consistently outperforms the baseline models in PXRD-to-crystal candidate retrieval, with the largest gains when PXRD patterns have close but crystallographically distinct nonpaired neighbors, meaning similar input patterns associated with different crystals. The resulting crystal and PXRD encoders transfer more effectively to downstream materials and crystallographic tasks. These results identify information asymmetry as a general design problem in scientific multimodal learning: alignment objectives should reflect what each modality preserves.
