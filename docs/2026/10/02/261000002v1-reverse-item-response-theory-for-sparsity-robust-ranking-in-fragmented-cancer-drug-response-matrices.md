# Reverse Item Response Theory for Sparsity-Robust Ranking in Fragmented Cancer Drug-Response Matrices

- 区域：速读区
- 排名：15
- 匹配度：2.1/10
- 来源：arxiv
- 作者：Jung Min Kang
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00002v1) · [PDF](https://arxiv.org/pdf/2610.00002v1)

## TLDR
By inverting Item Response Theory so cancer types act as latent “subjects” with resistance ability and drugs as “items” with evasion difficulty, this paper shows that reverse IRT provides sparsity-robust ranking recovery and better held-out prediction than averaging in fragmented cancer drug-response matrices, though cross-platform replication indicates the contribution is methodological rather than a universal clinical resistance ranking.

## Abstract
We introduce reverse Item Response Theory (IRT) to pharmacogenomic drug-response analysis by treating cancer types as latent "subjects" with resistance ability and drugs as "items" with evasion difficulty. Applied to 242,036 drug sensitivity measurements from the Genomics of Drug Sensitivity in Cancer (GDSC2) database, the model estimates cancer-type-level in-vitro resistance and drug-level broad activity on a shared latent scale. Validation across four missingness regimes demonstrates that reverse IRT better recovers the full-data latent ranking than simple averaging, with advantages of Delta-rho = +0.089 to +0.095 at 60% missingness under MCAR, cancer-biased, and drug-biased sparsity. Held-out prediction confirms IRT achieves the best Brier score among five evaluated methods. Bootstrap confidence intervals show 19 of 28 cancer types have stable resistant/sensitive classifications. Cross-platform PRISM replication shows 82% directional agreement but weak rank-order correlation (rho = 0.25), indicating the contribution is methodological robustness under fragmented evaluation, not a universal clinical resistance leaderboard.
