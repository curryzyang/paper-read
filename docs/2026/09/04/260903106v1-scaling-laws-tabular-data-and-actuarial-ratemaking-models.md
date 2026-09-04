# Scaling Laws, Tabular Data and Actuarial Ratemaking Models

- 区域：速读区
- 排名：11
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Ronald Richman
- 机构：Bayes Business School, insureai
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03106v1) · [PDF](https://arxiv.org/pdf/2609.03106v1)

## TLDR
Scaling-law-style power-law improvements with training data also emerge in actuarial ratemaking, but the gains differ strongly by architecture—TabM models scale far better than transformers or MLPs, while simply increasing transformer size yields little benefit without added inductive biases.

## Abstract
Scaling laws in modern deep learning describe how held-out loss improves as model capacity, training data, and compute increase, often following power-law trends. We investigate whether analogous scaling regularities arise in actuarial ratemaking, where data are tabular, heterogeneous, and noisy, and where classical models such as GLMs remain strong baselines. Using a real-world motor insurance portfolio, we train models from different families across increasing fractions of the training data and multiple random seeds, evaluating out-of-sample Poisson deviance, a likelihood-based loss for Poisson count predictions in which lower values indicate better held-out fit. We find that all model families improve with additional data, but scaling exponents differ substantially: TabM exhibits markedly stronger data scaling than purely supervised tabular Transformers and standard MLP baselines. Transformer variants show weak parameter scaling unless augmented with additional inductive biases (TabM-style adaptation or self-supervision). These results provide quantitative guidance on model selection by data regime and suggest that effective scaling on actuarial tabular tasks depends on architecture and loss function objective design, with simple increases in Transformer size providing limited gains.
