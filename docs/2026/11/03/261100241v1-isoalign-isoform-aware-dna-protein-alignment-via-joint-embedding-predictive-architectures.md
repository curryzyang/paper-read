# IsoAlign: Isoform-Aware DNA-Protein Alignment via Joint-Embedding Predictive Architectures

- 区域：速读区
- 排名：15
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Niousha Sadjadi, Arman Seyed-Ahmadi, Tony Tu, Micaela Elisa Consens, Kerr Ding, Alif Munim, Lila Kari, Zehui Li, Barry B. Rubin, Bo Wang, Vallijah Subasri
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00241v1) · [PDF](https://arxiv.org/pdf/2611.00241v1)

## TLDR
IsoAlign introduces an isoform-aware DNA–protein alignment framework using Joint-Embedding Predictive Architectures to improve genomic foundation model representations and downstream functional prediction.

## Abstract
Genomic foundation models (GFMs) have emerged as a powerful paradigm for learning DNA sequence representations, yet existing self-supervised pretraining strategies overlook alternative splicing and underperform compared to specialized models. To address this gap, we introduce IsoAlign, a multimodal framework that grounds genomic pretraining in isoform-aware DNA-protein alignment to learn biologically meaningful representations. IsoAlign aligns transcripts to their corresponding protein isoforms, capturing both coding sequences and broader regulatory contexts, using two Joint-Embedding Predictive Architectures (JEPA): DNA-Protein JEPA (DP-JEPA), which predicts protein representations from DNA using contrastive alignment, and Isoform-Masked JEPA (IM-JEPA), which models relationships among alternative isoforms of the same gene through masked protein prediction. We evaluate the learned DNA representations of these architectures across a multi-metric evaluation suite spanning tasks, including the prediction of pathogenicity, fitness, gene expression, and TF binding. Our results demonstrate that isoform-aware cross-modal alignment using JEPA significantly improves functional representations and downstream performance, establishing a promising direction for GFM pretraining.
