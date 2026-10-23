# Automated screening of privacy risks in medical AI

- 区域：速读区
- 排名：15
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Konstantinos Vrettos, Eleftherios Tzanis, Haridimos Kondylakis, Evangelia E. Vassalou, Florence X. Doo, Michail E. Klontzas
- 机构：FORTH, University of Maryland, University Hospital of Heraklion, University of Crete, Karolinska Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30229v1) · [PDF](https://arxiv.org/pdf/2610.30229v1)

## TLDR
A large-scale audit of 7,789 medical AI models shows that membership-inference privacy risk is concentrated in specific patients and remains predictable across training choices, enabling a lightweight screening tool to flag at-risk patients before production-model training.

## Abstract
Medical artificial intelligence (AI) models are often shared without their training data, assuming this protects the patients who contributed them. However, a model can reveal whether a patient's records were used in training, a privacy breach known as a membership inference attack. This risk is usually reported as a cohort average, which can appear negligible while individual patients are almost certainly exposed. Identifying potentially vulnerable records before developing a production model could make privacy assessment more practical. We measured each patient's vulnerability to membership inference attack, across 7,789 models trained on six clinical datasets in four modalities, including two adapted pretrained medical models. Training choices changed how many patients had high attack scores, but the patients who ranked highest by risk largely stayed the same across the configurations we tested. Stronger weight decay reduced the exposed cohort up to threefold, yet largely the same patients remained most at risk across training recipes, architectures and initializations, including foundation models. Therefore, we developed a lightweight screening tool that uses four small models to identify patients with high risk of exposure before production-model training. We also assessed if flagged patients could be protected without removing their data. Privacy screening should become incorporated into data preparation for clinical AI.
