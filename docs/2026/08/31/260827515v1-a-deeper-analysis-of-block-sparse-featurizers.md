# A Deeper Analysis of Block-Sparse Featurizers

- 区域：速读区
- 排名：12
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Alexandru-Iulius Jerpelea, Amith Ananthram
- 机构：Columbia University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27515v1) · [PDF](https://arxiv.org/pdf/2608.27515v1)

## TLDR
This paper analyzes block-sparse featurizers (BSFs), shows they still suffer from SAE-style failure modes such as feature splitting and composition, and proposes architectural improvements—including a Tournament Top-K selection rule that substantially reduces splitting—while extending the block paradigm to crosscoders.

## Abstract
The recently introduced block-sparse featurizer (BSF; Fel et al., 2026) is similar to a sparse autoencoder (SAE), but its atomic unit is a small subspace (a block of directions) rather than a single direction. It is designed for features that live on low-dimensional manifolds, which are especially frequent in vision. This work studies the BSF's strengths and weaknesses, finding how it still somewhat suffers from classic SAE failure modes, like feature splitting and composition. We propose several architectural changes to the BSF, including a Tournament Top-K selection rule that significantly reduces feature splitting, and we also extend the block paradigm to the crosscoder.
