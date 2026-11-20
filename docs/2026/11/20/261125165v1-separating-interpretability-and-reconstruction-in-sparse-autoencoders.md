# Separating Interpretability and Reconstruction in Sparse Autoencoders

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Anh Tien Nguyen, Dimitris Samaras, Mahdi S. Hosseini
- 机构：Mila--Quebec AI Institute, Concordia University, Stony Brook University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25165v1) · [PDF](https://arxiv.org/pdf/2611.25165v1)

## TLDR
DualSAE separates sparse interpretable semantic features from non-semantic residual information by augmenting standard sparse autoencoders with a plug-in Residual Branch, a decorrelation loss, and two-stage training, thereby improving both reconstruction fidelity and interpretability.

## Abstract
Sparse Autoencoders (SAEs) are effective tools for mechanistic interpretability by decomposing neural representations into sparse and interpretable features. However, a single sparse representation in traditional SAEs is responsible for both reconstruction fidelity and interpretability, which are not guaranteed to align. To separate these objectives, we propose DualSAE, a modular framework that augments standard SAEs with a plug-in Residual Branch. A standard SAE serves as the Sparse Branch, learning a sparse code that contains the dominant semantics of the input. The added Residual Branch models the non-semantic information omitted by the Sparse Branch. We ensure that the contributions of the two branches towards the overall reconstruction have minimal overlap through a decorrelation loss. We also adopt a two-stage training strategy that first stabilizes sparse representation learning before coupling with the Residual Branch. Across diverse encoder-SAE configurations on two vision datasets and two language corpora, DualSAE achieves mean relative improvements of approximately 29% in reconstruction fidelity and 34% in interpretability (measured by monosemanticity score). Moreover, with more interpretable representations, DualSAE yields consistent performance gains in the downstream applications of topic modeling, hypothesis generation, and LLM steering. Qualitative analysis further suggests that the Sparse Branch indeed preserves dominant semantic content, whereas the Residual Branch captures non-semantic information to improve reconstruction fidelity.
