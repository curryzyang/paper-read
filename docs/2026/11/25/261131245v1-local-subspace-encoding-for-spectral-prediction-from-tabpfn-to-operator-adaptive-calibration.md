# Local subspace encoding for spectral prediction: from TabPFN to operator-adaptive calibration

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Gregory Beurier, Robin Reiter, Denis Cornet, Lauriane Rouan
- 机构：UMR AGAP Institut, CIRAD
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31245v1) · [PDF](https://arxiv.org/pdf/2611.31245v1)

## TLDR
LVSE local subspace encoding improves spectral prediction with TabPFN and classical calibrators (PLS/Ridge) on many NIR-style datasets, though gains are not universal and a raw-vs-LVSE selector is not guaranteed to help every task.

## Abstract
TabPFN has already shown useful predictive performance on near-infrared spectra. RamanPFN subsequently proposed two spectral representations for tabular inference: Global Compositional Unmixing (GCU) and Local Vibrational Subspace Encoding (LVSE). We assess whether these representations also help on datasets assembled through the nirs4all ecosystem, and whether their value extends to classical calibration. We reanalyse completed experiments from a public spectral dataset catalogue. On a post-hoc subset of 61 matched numerical prediction tasks, after excluding ten class-code, metadata or semantically ambiguous targets, LVSE reduces RMSE relative to raw-spectrum TabPFN by 10.22%, 12.80% and 14.52% on average for checkpoints 2.5, 3 and 3.5, respectively, with median reductions of 4.99%, 4.74% and 7.82%. Across 76 classification datasets, weighted F1 increases by 2.22, 2.56 and 3.81 percentage points. The 2.5 classification procedure uses output coding on 15 datasets exceeding the checkpoint's native class limit. GCU alone is less reliable in this implementation. LVSE also improves PLS and Ridge in many cases, with median RMSE reductions of 4.75% and 1.89%. Adding LVSE candidates to an operator-adaptive model is feasible, but a separate 35-task panel derived from the public AOM benchmark shows only small median gains. These results motivate evaluating LVSE alongside existing representation choices. They do not establish that a selector choosing between raw and LVSE inputs will improve every task.
