# Similarity-Aware Machine Unlearning

- 区域：速读区
- 排名：10
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Madhavan Citalamangalam Kumaran, Midhun Parakkal Unni, Vicky Kouni, Haripriya Harikumar
- 机构：University of Sheffield, University of Manchester, Paris Dauphine - PSL University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00246v1) · [PDF](https://arxiv.org/pdf/2608.00246v1)

## TLDR
This paper proposes a retain-aware localization method for machine unlearning that selects parameters based on importance to both forgotten and retained data, reducing collateral damage to semantically similar retained examples.

## Abstract
Machine unlearning removes the influence of user-specified training examples from a trained model, avoiding the need to retrain it from scratch. Localization-based methods improve unlearning efficiency by identifying a subset of influential model parameters. However, existing approaches select parameters based solely on forget-set importance, neglecting their role in retained dataset and often causing collateral damage to semantically similar retained examples. We address this limitation with a retain-aware localization method that considers parameter importance to both forgotten and retained data. We also introduce a retain-similar evaluation set, constructed using cosine similarity in the model embedding space, to directly measure collateral damage. Across eleven experimental settings on CIFAR-10 dataset and ResNet18 model, our method consistently reduces collateral damage while improving standard unlearning metrics, demonstrating the effectiveness of retain-aware localization for similarity-aware machine unlearning.
