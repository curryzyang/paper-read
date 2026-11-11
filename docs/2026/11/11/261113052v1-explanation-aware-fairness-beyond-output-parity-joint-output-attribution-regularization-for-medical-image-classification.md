# Explanation-Aware Fairness Beyond Output Parity: Joint Output-Attribution Regularization for Medical Image Classification

- 区域：速读区
- 排名：15
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Gökhan Özbulak, Oscar Jimenez-del-Toro, Lilian Berton, André Anjos
- 机构：Universidade Federal de São Paulo, Idiap Research Institute, École Polytechnique Fédérale de Lausanne
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13052v1) · [PDF](https://arxiv.org/pdf/2611.13052v1)

## TLDR
Adding an attribution-disparity penalty to output-level equalized-odds fairness regularization improves utility–fairness trade-offs and reduces hidden attribution disparities/cancellation in medical image classifiers, validated across 960 DINOv2-LoRA models on HAM10000 and Harvard-GF.

## Abstract
Output-level fairness does not constrain whether demographic groups rely on similar predictive contributions in representation space. For a nonlinear encoder with a linear head, we show that outcome-conditioned output score disparity equals the signed sum of feature attribution differences across subgroups by allowing small prediction gaps to arise through cancellation effect. We test whether an attribution disparity penalty complements output-level equalized odds based fairness surrogates. Across 960 DINOv2-LoRA models on HAM10000 and Harvard-GF datasets for gender and race fairness, attribution augmentation increases utility-fairness trade-off performance for hypervolume in six different settings with paired 95% confidence intervals and relative gains of 1.49-10.57%. Under a predefined utility constraint, augmented model families also achieve 9.0-38.7% lower equalized odds difference, lower attribution disparity, and reduced cancellation ratio while preserving predictive utility. These results support attribution fairness as a complementary explanation-aware constraint on output fairness.
