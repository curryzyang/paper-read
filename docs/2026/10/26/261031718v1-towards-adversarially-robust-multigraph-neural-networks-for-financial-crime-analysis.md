# Towards Adversarially Robust Multigraph Neural Networks for Financial Crime Analysis

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Dennis Heijmans, H. Çağrı Bilgi, Rui Wang, Kubilay Atasu
- 机构：Delft University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31718v1) · [PDF](https://arxiv.org/pdf/2610.31718v1)

## TLDR
The paper introduces the first scalable framework for learned structural attacks and adversarial training on multigraph neural networks using node–edge incidence matrices and a cycle-based plausibility regularizer, showing that these models are vulnerable to such attacks but can be made more robust through adversarial training.

## Abstract
Financial transaction networks are naturally represented as multigraphs, where repeated transactions between the same pair of accounts are modeled as distinct edges. Recently proposed multigraph neural network architectures leverage this structure explicitly to achieve a strong performance on anti-money laundering (AML) tasks. However, their robustness to adversaries that manipulate transaction structures to evade detection remains largely unexplored. We present the first scalable framework for structural attacks and adversarial training of multigraph neural networks using node-edge incidence matrices, adapting projected gradient descent and projected randomized block coordinate descent methods to optimize structural perturbations over such matrices. We further introduce a cycle-based regularizer that penalizes changes in the global counts of directed 2- and 3-cycles, providing a structural measure of attack plausibility. Experiments on synthetic pattern-detection and realistic AML datasets show that our learned attacks substantially outperform non-learnable perturbation baselines in reducing detection performance (PR-AUC), while adversarial training consistently improves robustness against these attacks. These results demonstrate that multigraph neural networks are vulnerable to learned structural attacks and that adversarial training provides an effective defense. Our code is available at https://github.com/denheijmans/robust_multignn.
