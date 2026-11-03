# KINDER: Kernel-based Independence for Fair Representation Learning via Prototype-space Erasure

- 区域：速读区
- 排名：10
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Abtin Mogharabin, Alp Toykan Kaplan, Jiaee Cheong, Sinan Kalkan
- 机构：Zuse School ELIZA, MIT, University of Tübingen, Harvard University, Middle East Technical University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00264v1) · [PDF](https://arxiv.org/pdf/2611.00264v1)

## TLDR
KINDER is a model-agnostic fair representation learning method that directly erases sensitive-attribute information by estimating a protected-group subspace from prototypes in a random Fourier feature space and projecting intermediate representations onto its orthogonal complement, enabling decoder-independent concept erasure across tasks and data modalities.

## Abstract
Concept erasure is a prominent approach to achieving fairness in machine learning through the removal of sensitive attributes from learned representations. Prior concept erasure methods typically define debiasing indirectly through the failure of a chosen adversary, probe, or fairness penalty, which makes the target of erasure dependent on a particular decoder family or optimization setup. We introduce KINDER, which directly removes sensitive-attribute information from intermediate representations with respect to a chosen family of prototype functionals, and is compatible with any deep model containing an intermediate feature space, independent of the architecture, task type, or training paradigm. KINDER operates in a random Fourier feature space, where it estimates a sensitive subspace from protected group prototypes and projects representations onto its orthogonal complement. Thus, it forms an explicit representation cleaning mechanism distinct from prior fairness control studies. We conduct extensive experiments across diverse settings and show the effectiveness of KINDER on (i) supervised and self-supervised settings, (ii) classification, regression, and image segmentation tasks, and (iii) diverse data modalities, including visual, textual, and tabular data. Code and trained models are available at: https://github.com/abtinmU/KINDER
