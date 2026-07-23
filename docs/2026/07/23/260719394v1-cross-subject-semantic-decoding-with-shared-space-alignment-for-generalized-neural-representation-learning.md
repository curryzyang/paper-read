# Cross-Subject Semantic Decoding with Shared-Space Alignment for Generalized Neural Representation Learning

- 区域：速读区
- 排名：4
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Ji-Hoon Heo, Aleksandra Joanna Wisniewska, Seo-Hyun Lee, Seong-Whan Lee
- 机构：Korea University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19394v1) · [PDF](https://arxiv.org/pdf/2607.19394v1)

## TLDR
This paper proposes a cross-subject semantic decoding framework that aligns neural responses from multiple subjects into a shared latent space via the Shared Response Model and decodes contextual semantic embeddings, achieving improved generalization to held-out subjects without retraining.

## Abstract
Generalizing across subjects remains challenging in invasive neural recordings because electrode configurations, anatomical structures, and neural signal patterns vary substantially across individuals. To investigate such inter-subject variability, we propose a cross-subject semantic decoding framework that aligns neural responses to speech perception from multiple subjects into a shared latent space and learns a mapping from the aligned neural representations to contextual embeddings. More specifically, using electrocorticography data collected during natural language comprehension, we estimate the shared space using the shared response model and train a decoder to predict contextual semantic embeddings from projected neural responses. For a held-out subject, we estimate a subject-specific projection into the predefined shared space, and directly apply the pretrained decoder without any retraining. Experimental results demonstrate that the proposed framework consistently outperforms baseline methods across evaluation settings and exhibits a reduced performance drop from source subject to held-out subject testing, indicating improved cross-subject generalization. These results suggest that aligning neural activity into a shared latent space, while decoding in a semantic embedding space, provides an effective strategy for improving cross-subject generalization by reducing subject-specific differences in neural responses while effectively capturing shared stimulus-related representations.
