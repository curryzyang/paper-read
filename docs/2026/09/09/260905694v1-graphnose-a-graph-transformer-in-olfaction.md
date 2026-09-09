# GraphNOSE: A Graph Transformer in Olfaction

- 区域：速读区
- 排名：14
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Mrityunjay Sharma, Sarabeshwar Balaji, Valentina Parma, Ritesh Kumar
- 机构：CSIR- Central Scientific Instruments Organisation, Indian Institute of Science Education and Research Bhopal(IISERB), University of Pennsylvania, Monell Chemical Senses Center, Academy of Scientific and Innovative Research (AcSIR), Department of Higher Education, Himachal Pradesh
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05694v1) · [PDF](https://arxiv.org/pdf/2609.05694v1)

## TLDR
GraphNOSE introduces an open-source graph transformer with positional and structural encodings that predicts odor descriptors for single molecules and binary mixtures, outperforming linear models, fingerprints, language model embeddings, and baseline GNNs—including on out-of-distribution compounds—while using fewer parameters and offering interpretable insights.

## Abstract
Predicting olfactory qualities from molecular structure is an open problem in chemoinformatics. Although linear models can link molecular features to odor descriptors, they often fail when extrapolating to novel chemical scaffolds, extreme molecular weights, or complex odor mixtures. To address this, we introduce GraphNOSE, an open-source graph transformer framework that predicts multi-label odor descriptors from simplified molecular-input line-entry system (SMILES) strings for single molecules and binary mixtures. By integrating positional and structural encodings within a transformer-based graph architecture, GraphNOSE achieves strong performance with six times fewer parameters than standard graph neural network (GNN) baseline while consistently outperforming linear models, molecular language model embeddings, molecular fingerprints, and baseline GNNs by an average area under the ROC curve (AUROC) margin of 4.52% (p < 0.01). GraphNOSE achieves an AUROC of 84% on out-of-distribution compounds (OODs). This exceeds the current state-of-the-art GNN for OOD in olfaction (Open-POM: 81%, p < 0.001), and identifies conditions under which linear models empirically fail. Finally, we apply XAI (explainable AI) methods to identify which substructures and molecular features drive odor predictions, yielding insights consistent with chemical intuition and grounded in the model's learned representations. Together, these results establish GraphNOSE as a scalable and interpretable architecture for olfactory prediction that generalizes to structurally distinct compounds underrepresented in current perceptual databases.
