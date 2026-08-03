# Flow Matching with Missing Data

- 区域：速读区
- 排名：2
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Fairoz Nower Khan, Nabuat Zaman Nahim, Peizhong Ju
- 机构：University of Kentucky
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28698v1) · [PDF](https://arxiv.org/pdf/2607.28698v1)

## TLDR
Missing-Data Flow Matching trains flow matching on incomplete data by treating missing coordinates as latent variables resampled from their conditional distribution, proving exact equivalence to complete-data training under MCAR and showing that a single oracle completion is optimal.

## Abstract
Flow matching assumes fully observed training data, which many real-world applications rarely provide. We propose Missing-Data Flow Matching, which treats the missing coordinates of training samples as latent variables and averages the flow matching loss over the values they could take. We first prove the correction is exact rather than approximate. Under missing completely at random with true completions, the incomplete-data objective equals the complete-data objective, so missingness changes nothing about what flow matching learns and the entire difficulty relocates to the completion model. Our finite-sample analysis then answers design questions that the algorithm leaves open, and the answers are not the ones intuition suggests. Missingness transfers estimator variance rather than adding it, one completion per example already matches complete-data variance exactly, and under a fixed evaluation budget one completion is optimal. A learned completion model contributes a single irreducible bias, which we bound by its expected conditional Wasserstein distance to the true completion law. Experiments numerically validate the theoretical predictions, show that deterministic rather than frozen imputation is what collapses the generated distribution, and place our method alongside strong classical and deep imputation baselines on real tabular data.
