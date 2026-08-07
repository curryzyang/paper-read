# Rectifying Geometric Misalignment: Online Source-Free Adaptation for Class-Imbalanced EEG

- 区域：速读区
- 排名：9
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Shiwen Chu, Shanglin Li, Motoaki Kawanabe, Reinmar Kobler
- 机构：BIFOLD – Berlin Institute for the Foundations of Learning and Data, Nara Institute of Science and Technology, Advanced Telecommunications Research Institute International
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05315v1) · [PDF](https://arxiv.org/pdf/2608.05315v1)

## TLDR
OSPDIM is an online source-free unsupervised domain adaptation framework that introduces a manifold-constrained bias parameter optimized via information maximization to correct geometric misalignment caused by label shifts in class-imbalanced EEG-based BCIs.

## Abstract
Electroencephalography (EEG) based Brain-Computer Interfaces (BCIs) often require unsupervised domain adaptation (UDA) to generalize across subjects and sessions. While Riemannian alignment methods like the Riemannian Centering Transformation (RCT) are effective for handling covariate shifts, they implicitly assume balanced class priors. However, in realistic online BCI scenarios, the label distributions vary dynamically (label shift), causing standard alignment techniques to geometrically misalign the target data distributions. In this work, we propose OSPDIM (Online SPD manifold information maximization), a source-free online UDA framework designed to address label shifts on the Riemannian manifold. OSPDIM introduces a manifold-constrained bias parameter into the tangent space mapping, which is optimized via information maximization to correct the geometric skew caused by imbalanced data streams. Unlike offline methods relying on global batch statistics, OSPDIM estimates and corrects geometric bias on-the-fly. Simulations on 2D SPD matrices visually demonstrate that OSPDIM successfully rectifies the misalignment where standard centering fails. Extensive experiments on multiple motor imagery datasets show that OSPDIM significantly outperforms standard Riemannian baselines, particularly in challenging online adaptation scenarios with severe class imbalance, offering a robust solution for practical, plug-and-play BCI systems.
