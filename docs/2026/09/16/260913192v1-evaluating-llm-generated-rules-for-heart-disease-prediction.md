# Evaluating LLM-Generated Rules for Heart Disease Prediction

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Feisal Alaswad, Batoul Aljaddouh, Maher Alrahhal, Wafaa Al Nassan, Talal Bonn
- 机构：University of Sharjah, Amity University Dubai, SRM Institute of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13192v1) · [PDF](https://arxiv.org/pdf/2609.13192v1)

## TLDR
Traditional machine learning models, especially Random Forest with 90.2% accuracy, outperformed GPT-4o- and Claude Sonnet 4.6-generated IF-THEN rule-based systems for heart disease prediction on the UCI dataset, though the LLM-generated rules provided greater interpretability.

## Abstract
This study compares traditional machine learning models and Large Language Model (LLM)-generated rule-based systems for heart disease prediction using the UCI Heart Disease dataset. Several classifiers, including Logistic Regression, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Naive Bayes, Decision Tree, and Random Forest, were evaluated alongside rule-based systems generated using GPT-4o and Claude Sonnet 4.6. Model performance was assessed using accuracy, precision, recall, and F1-score metrics. Experimental results show that traditional machine learning models consistently outperform LLM-generated rule-based systems in predictive performance. Random Forest achieved the best overall performance with 90.2% accuracy, a precision of 0.829, perfect recall of 1.0, and an F1-score of 0.906. Naive Bayes followed closely with 88.5% accuracy and an F1-score of 0.881. In contrast, the LLM-generated rule models achieved lower performance, with Claude Sonnet 4.6 reaching 80.3% accuracy (F1-score: 0.833) and GPT-4o obtaining 70.5% accuracy (F1-score: 0.690). Despite the performance gap, the LLM-generated rules provide interpretable IF-THEN diagnostic logic that enhances explainability and transparency in clinical decision-making. These findings highlight the trade-off between predictive performance and interpretability in medical artificial intelligence systems. The complete implementation of all experiments, including machine learning models and LLM-derived rule classifiers, is publicly available in the GitHub repository at https://github.com/FeisalAlaswad/LLM-Rule-ML-Heart-Disease-Prediction .
