# ED-CSP: Crystal Structure Prediction from Electron Diffraction

- 区域：速读区
- 排名：7
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Germain Poloudenny, Yaël Frégier, Arnaud Demortière
- 机构：CNRS, UPJV, Université d'Artois
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06448v1) · [PDF](https://arxiv.org/pdf/2608.06448v1)

## TLDR
ED-CSP introduces a machine learning framework that generates crystal structures from sparse multi-view electron diffraction patterns via a relational encoder and periodic flow generator, and with the new ED-CS dataset it outperforms PXRDGen on CHILI-100K while demonstrating genuine generative capability beyond composition-only retrieval.

## Abstract
Recovering a periodic 3D crystal structure from sparse, unindexed electron diffraction (ED) observations is a challenging generative inverse problem. Existing ED-based learning methods mainly predict crystallographic labels, reconstruct structures from indexed reflections, or retrieve candidates from finite structure libraries. Here, we introduce ED-CSP, a machine learning framework that predicts crystal structures from chemical composition, atom count, and multiple detector-plane ED spot sets. ED-CSP combines a relational set encoder, permutation-invariant multi-view aggregation, and a periodic flow generator to jointly predict lattice parameters and fractional atomic coordinates.
  To train the model, we construct ED-CS, a dataset of 4.85 million simulated multi-view ED crystal structures, deduplicated across seven materials repositories and filtered to exclude CHILI-100K overlaps. On 2,075 held-out CHILI-100K materials, ED-CSP trained only on CHILI achieves a structural match rate of 57.49% MR@5, outperforming PXRDGen (52.92%), a state-of-the-art crystal structure prediction model conditioned on powder X-ray diffraction. Scaling training data further improves performance: initializing from a one-million-structure precursor raises MR@5 to 66.27%. On 1,024 compositions absent from the training retrieval library, the model still achieves 53.52% MR@5, demonstrating true generative capability beyond exact-formula retrieval. Replacing target ED observations with diffraction from non-isomorphic structures of identical composition decreases MR@5 by 22.09 percentage points, confirming that predictions depend on the input diffraction patterns rather than composition alone. ED-CSP and ED-CS establish a benchmark for generative crystal structure prediction from sparse ED observations and provide a foundation for future transfer to experimental data.
