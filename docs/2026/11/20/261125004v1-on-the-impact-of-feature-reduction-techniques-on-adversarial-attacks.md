# On the Impact of Feature Reduction Techniques on Adversarial Attacks

- 区域：速读区
- 排名：13
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Mohammad Meymani, Roozbeh Razavi-Far
- 机构：University of New Brunswick
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25004v1) · [PDF](https://arxiv.org/pdf/2611.25004v1)

## TLDR
This paper evaluates four feature-reduction techniques across five machine learning classifiers under poisoning, backdoor, and universal adversarial perturbation attacks on the APT dataset, finding that permutation importance ranking and univariate mutual information generally provide the most consistent adversarial-robustness improvements while other methods vary by classifier and attack scenario.

## Abstract
Adversarial attacks have posed significant threats to machine learning models by exploiting their inherent vulnerabilities. Researchers have established an interdisciplinary field called adversarial machine learning to explore these vulnerabilities and develop corresponding defense strategies. Feature reduction strategies are used to decrease the dimensionality of the data in order to reduce training time, avoid the curse of dimensionality, prevent overfitting, and mitigate redundant features. However, their effect on adversarial robustness across different classifiers and attack scenarios remains insufficiently explored. This study aims to analyze the effect of feature reduction techniques on the adversarial robustness of a diverse set of machine learning models under poisoning, backdoor, and universal adversarial perturbation attacks on the APT dataset. These models include support vector machine, decision tree, random forest, multi-layer perceptron, and k-nearest neighbors. The attained results are compared with scenarios where different feature reduction techniques are applied, including principal component analysis, permutation importance ranking, recursive feature elimination, and univariate mutual information. Metrics such as accuracy, F1-score, and mitigation score are employed to evaluate the effect of these techniques on adversarial robustness. The results demonstrate that permutation importance ranking and univariate mutual information generally provide the most consistent robustness improvements, while other methods exhibit more variable effects depending on the classifier and attack scenario.
