# Typical Angina, Reversed: A Long-Standing Documentation Error in the UCI Heart Disease Data

- 区域：速读区
- 排名：15
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Tejas Tovinkere Pattabhi
- 机构：University of the Cumberlands
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33248v1) · [PDF](https://arxiv.org/pdf/2611.33248v1)

## TLDR
The UCI Heart Disease dataset’s chest-pain variable is stored in reverse of its documentation—code 4 labeled “asymptomatic” actually denotes typical angina and code 1 labeled “typical angina” denotes asymptomatic/no chest pain—a long-standing error that barely affects conventional model accuracy but reverses clinical interpretations and misleads label-reading models, so the paper provides the corrected mapping, evidence, and code.

## Abstract
The UCI Heart Disease data are a widely used machine-learning benchmark. We show that their chest-pain variable is stored in reverse of its documentation. At all four sites, the code documented as "asymptomatic" (4) marks patients with typical angina, and the code documented as "typical angina" (1) marks patients with almost none of the classical angina features (at Cleveland, no chest pain).
  Two complementary checks establish this: (i) the chest-pain table and regression coefficients of the original 1986 Cleveland study are reproduced only under the corrected reading; (ii) in the Budapest, Switzerland and Long Beach files, 93-96% of patients coded 4 have all three classical angina features. A 1990 word-labeled Cleveland file already uses the documented labels, and Statlog (Heart), a Cleveland subset, stores the same codes. OpenML, PMLB and two highly voted Kaggle copies that name the categories use the same documented labels (about 400,000 downloads combined).
  We audited a seeded random sample of 150 records from a pre-specified Scholar query for SHAP studies of these data mentioning asymptomatic chest pain (124 readable). Of 32 papers that state a direction for a named category, 25 (78%; 95% CI 61-89%) state one inconsistent with the corrected category identities; 22 (69%; 51-82%; post hoc) are attributable to the documentation error, and nine of these explain it clinically. None of the 124 readable papers identifies the reversal.
  Conventional models are essentially unaffected, one reason the error went unnoticed. Interpretations that attach the documented names to model effects are reversed, and zero-shot language-model classifiers that read the labels are misled: with the documented labels, three open-weight models lose 0.12-0.33 in area under the receiver operating characteristic curve (AUC) given age, sex and chest-pain type. We give the corrected mapping, evidence and code.
