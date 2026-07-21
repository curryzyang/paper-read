# Benchmarking Machine Learning Models for Multi-Omics-Based Breast Cancer Prediction

- 区域：速读区
- 排名：15
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Priyanka Paudel, Madan Baduwal
- 机构：Mississippi State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16250v1) · [PDF](https://arxiv.org/pdf/2607.16250v1)

## TLDR
This study benchmarks classical machine learning models for breast cancer ER status prediction using multi-omics data, finding that Random Forest with integrated transcriptomic, genomic, and proteomic data achieves the best performance (balanced accuracy 90.3%, ROC-AUC 97.1%) and that RNA expression provides the strongest predictive signal.

## Abstract
Estrogen Receptor (ER) status is a critical biomarker in breast cancer diagnosis, prognosis, and treatment selection. Recent advances in high-throughput sequencing technologies have enabled the generation of multi-omics datasets that provide complementary molecular information for computational prediction tasks. This study presents a systematic benchmarking analysis of classical machine learning models for ER status prediction using transcriptomic (RNA expression), genomic (copy number variation; CNV), and proteomic (RPPA) data from the TCGA-BRCA cohort. A rigorous experimental framework incorporating stratified train-test splitting, stratified five-fold cross-validation, class imbalance handling, and fold-specific feature selection was employed to ensure reliable evaluation and prevent data leakage. Random Forest, XGBoost, LightGBM, CatBoost, Support Vector Machines (SVM), and Logistic Regression were evaluated across single-omic and multi-omic settings. Results demonstrated that RNA expression provided the strongest predictive signal, while multi-omic integration yielded modest but consistent improvements over individual modalities. Among all evaluated approaches, Random Forest achieved the best overall performance in the integrated multi-omic setting, obtaining a balanced accuracy of 90.3\% and an ROC-AUC of 97.1\%. Furthermore, recurrent selection of biologically relevant genes, including \textit{ESR1}, \textit{PGR}, \textit{FOXA1}, and \textit{GATA3}, supported the biological validity of the learned models. These findings indicate that carefully regularized classical machine learning methods remain highly effective for small, high-dimensional genomic datasets and that multi-omic integration provides complementary information for breast cancer ER status prediction.
