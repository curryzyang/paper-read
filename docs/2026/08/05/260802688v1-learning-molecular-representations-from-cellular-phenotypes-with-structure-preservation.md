# Learning Molecular Representations from Cellular Phenotypes with Structure Preservation

- 区域：速读区
- 排名：13
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Xuan Lin, Jingyu Sheng, Tengfei Ma, Li Sun, Dapeng Xiong
- 机构：Hunan University, Xiangtan University, Southeast University, Beijing University of Posts and Telecommunications
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02688v1) · [PDF](https://arxiv.org/pdf/2608.02688v1)

## TLDR
PhenMol is a structure-preserving multimodal framework that learns phenotype-aware molecular representations by disentangling shared cellular signals from private chemical structure, preventing molecular embedding collapse and improving bioactivity prediction, retrieval, and clinical outcome prediction.

## Abstract
Phenotypic drug discovery enables the discovery of functional relationships between molecular structures and cellular responses. However, existing multimodal representation learning methods often optimize cross-modal alignment without considering the intrinsic organization of chemical space, resulting in distorted molecular representations and loss of structural information. We propose \textbf{PhenMol}, a structure-preserving framework for phenotype-aware molecular representation learning. PhenMol disentangles molecular and cellular representations into shared and private components, enabling phenotype-guided alignment while preserving chemical structures through a dedicated molecular branch. This design integrates cellular phenotype information without disrupting molecular neighborhood organization. Experiments on approximately $3.04 \times 10^{4}$ molecule--cell morphology pairs demonstrate that PhenMol improves molecular property prediction across 270 bioactivity tasks, molecule--phenotype retrieval, and clinical trial outcome prediction. Moreover, ECFP4-based structural analysis shows that PhenMol better preserves molecular neighborhoods and reduces embedding distortion compared with existing multimodal alignment methods. These results highlight the importance of structure-aware constraints in multimodal molecular representation learning and provide an effective approach for integrating cellular phenotypes with chemical knowledge for drug discovery.
