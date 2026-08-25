# Bankruptcy Prediction via Hybrid Resampling and Stacking Ensemble Techniques with Explainable Artificial Intelligence (XAI)-Driven Analysis

- 区域：速读区
- 排名：12
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Obu-Amoah Ampomah, Edmund Fosu Agyemang, Kofi Acheampong, Louis Agyekum, Enock Adu Bonsu, Eric Nyarko
- 机构：Western Michigan University, Tulane University, University of Ottawa, University of Ghana, University of Arizona
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20343v1) · [PDF](https://arxiv.org/pdf/2608.20343v1)

## TLDR
This study develops a bankruptcy prediction framework that integrates consensus-based feature selection, hybrid resampling (SVM-SMOTE, SMOTE-Tomek, SMOTE-ENN), stacking ensembles of machine learning and deep learning models, and SHAP-based explainable AI, demonstrating that SMOTE-ENN with a GRU or an LSTM-stacked ensemble yields the best balance of minority-class recall and overall predictive performance on severely imbalanced Taiwanese financial data.

## Abstract
This study develops and evaluates a bankruptcy prediction framework that integrates consensus-based feature selection, hybrid resampling, stacking ensembles, and explainable artificial intelligence to improve minority-class detection in severely imbalanced financial data. Using the Taiwanese Bankruptcy Prediction dataset from the UCI Machine Learning Repository, five feature-selection algorithms were first applied, and a consensus retention rule reduced the input space to 23 robust variables. The balanced training data were then generated using SVM-SMOTE, SMOTE-Tomek, and SMOTE-ENN. Five ensemble machine learning classifiers, namely gradient boosting, extreme gradient boosting, histogram-based gradient boosting, LightGBM, and AdaBoost, were compared with five deep learning models, including RNN, LSTM, GRU, DNN, and MLP. In addition, hybrid stacking ensembles combined the five machine learning classifiers as base learners with each deep learning model as a meta-learner. Model performance was assessed using accuracy, recall, specificity, G-mean, and ROC-AUC, while SHAP was used to explain feature contributions. The results show that resampling strategy materially shaped model behavior. SVM-SMOTE and SMOTE-Tomek favored accuracy and specificity, whereas SMOTE-ENN delivered stronger minority-class detection. Among standalone models, the GRU with SMOTE-ENN achieved the best overall predictive balance, with recall of 0.8627, G-mean of 0.8517, and ROC-AUC of 0.9431. Among stacking ensembles, SMOTE-ENN with (GB+XGB+HGB+LGBM+AB)+LSTM provided the strongest compromise between sensitivity and specificity. SHAP analysis identified leverage, profitability, solvency, and operational efficiency indicators as the most influential predictors of bankruptcy risk. These findings support more reliable and interpretable early warning systems for financially distressed firms.
