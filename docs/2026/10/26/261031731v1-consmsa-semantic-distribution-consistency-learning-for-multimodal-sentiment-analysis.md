# ConsMSA: Semantic Distribution Consistency Learning for Multimodal Sentiment Analysis

- 区域：速读区
- 排名：13
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Pan Wang, Lipeng Ke, Huajun Ying, Pritish Mohapatra, Rohan Sarkar, Suresh Lakhani, Sankar Venkataraman, Jingtong Hu
- 机构：University of Pittsburgh, Amazon
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31731v1) · [PDF](https://arxiv.org/pdf/2610.31731v1)

## TLDR
ConsMSA enhances multimodal sentiment analysis by measuring intra- and inter-modality semantic distribution consistency in a shared sentiment space and coupling it with predictive relevance to regularize learning, reweight tokens, and prune redundant or conflicting tokens, achieving state-of-the-art accuracy while retaining comparable performance with only 10% of tokens.

## Abstract
Multimodal sentiment analysis (MSA) aims to predict human sentiments by integrating signals from different modalities such as text, video, and audio. However, raw multimodal sequences often suffer from semantic inconsistency--exhibiting redundancy or conflicts within and across modalities--which hinders robust understanding and increases computational cost. To this end, we introduce ConsMSA, which explicitly formalizes semantic distribution consistency across both $\textit{intra}$- and $\textit{inter}$-modality, providing a consistency-aware mechanism for robust and efficient multimodal sentiment prediction. Specifically, ConsMSA projects multimodal token features into a shared sentiment space to compute an Intra- and Inter-modality Consistency Score ($I^2CS$). By coupling this score with predictive relevance, we formulate consistency-aware importance signals that are utilized: (i) as a consistency regularizer to align latent distributions during training, (ii) to derive semantic-aware weights for adaptive multimodal token reweighting, and (iii) as a practical criterion to prune redundant or conflicting tokens. Extensive experiments on CMU-MOSI, CMU-MOSEI, and CH-SIMS demonstrate that ConsMSA achieves state-of-the-art performance while remaining robust under aggressive token compression--retaining only 10% of tokens yields comparable accuracy. These results establish semantic distribution consistency as a promising foundation for synergizing predictive robustness with computational efficiency.
