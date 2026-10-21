# HierDTA: Hierarchical Structure-Aware Representation Learning for Drug--Target Affinity Prediction

- 区域：速读区
- 排名：15
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Huangchao Xu, Baohua Zhang, Qian Liu, Zhong Jin, Yi Du
- 机构：University of Chinese Academy of Sciences, Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.27001v1) · [PDF](https://arxiv.org/pdf/2610.27001v1)

## TLDR
HierDTA is a hierarchical structure-aware framework for drug–target affinity prediction that combines atom–motif drug graphs with motif-to-atom semantic augmentation, kinase-domain residue interaction graphs, atom–residue cross-attention, and global fingerprint/ESM-2 features to achieve state-of-the-art accuracy and strong cold-start generalization.

## Abstract
Drug--target affinity (DTA) prediction plays an important role in computer-aided drug discovery, where reliable computational models can help prioritize compound--protein pairs before experimental validation. A key challenge in DTA prediction is to effectively mine multi-level molecular information from drug structures while accurately modeling the binding-site environment of target proteins. To address these issues, we introduce HierDTA, a hierarchical structure-aware framework for DTA prediction. \textcolor{black}{HierDTA represents each drug as an atom--motif heterogeneous graph and introduces an augmentation module that propagates functional-motif semantics to the corresponding atoms. For proteins, kinase-domain structures are converted into residue interaction graphs. The resulting atom and residue representations are integrated using cross-attention to capture pair-specific relationships, while molecule fingerprints and pretrained ESM-2 embeddings provide complementary global information. Compared with state-of-the-art methods, HierDTA achieves superior performance on the Davis dataset across all metrics and attains the highest \(r_m^2\) of 0.791 on KIBA. It also exhibits strong generalization under cold-start settings, particularly on KIBA, where MSE is reduced by 21.7\% in the unseen-protein scenario. Ablation study and interpretability analysis supported the contributions of the hierarchical augmentation and interaction components.} Case studies further showed that HierDTA provided early enrichment of candidate bioactive compounds. These results indicate that HierDTA is an effective framework for affinity prediction and target-specific virtual screening.
