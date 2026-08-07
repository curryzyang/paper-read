# Evaluating Machine Learning Models for Post-Wildfire Debris-Flow Prediction

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Quinn Ledingham, Zhengsen Xu, Yimin Zhu, Zack Dewis, Mabel Heffring, Saeid Taleghanidoozdoozan, Motasem Alkayid, Megan Greenwood, Lincoln Linlin Xu
- 机构：University of Calgary
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05265v1) · [PDF](https://arxiv.org/pdf/2608.05265v1)

## TLDR
This paper systematically evaluates 15 machine learning models for post-wildfire debris-flow prediction, finding TabPFN achieves the highest performance, using SHAP to identify key rainfall features, and showing that synthetic data augmentation improves most models under data-scarce, class-imbalanced conditions.

## Abstract
Prediction of post-wildfire debris flows is critical for mitigating hazards to communities, infrastructure, and resources during intense rainfall in recently burned areas. However, identifying reliable machine learning models is complicated by overlapping debris-flow and non-debris-flow events in feature space, the need for model interpretability, and limited training data. This paper addresses these challenges through a systematic evaluation of machine learning models in terms of predictive performance, feature importance, and synthetic data augmentation. Using basin-scale observations of post-wildfire debris-flow events across the western United States, we compare 15 models, including the Tabular Prior-Data Fitted Network (TabPFN). Repeated stratified cross-validation shows that TabPFN achieves the highest unaugmented performance with a threat score of 0.637, closely followed by the best tree-based models. SHapley Additive exPlanations (SHAP) are used to identify the features driving predictions, revealing that short-duration rainfall intensity and storm accumulation consistently rank highest, while burn severity and terrain features contribute less. We further evaluate synthetic data augmentation using TabPFN-generated samples to address the scarcity of debris-flow observations. Synthetic augmentation improves the performance of all models except CNN, with the largest mean threat score increase of +0.041 among the deep learning models. By combining rigorous model benchmarking, interpretable feature analysis, and synthetic data augmentation, this work provides a comprehensive framework for improving post-wildfire debris-flow prediction.
