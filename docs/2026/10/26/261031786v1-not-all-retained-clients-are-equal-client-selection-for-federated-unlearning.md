# Not All Retained Clients Are Equal: Client Selection for Federated Unlearning

- 区域：速读区
- 排名：6
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Thanh Linh Nguyen, Quoc-Viet Pham
- 机构：Trinity College Dublin
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31786v1) · [PDF](https://arxiv.org/pdf/2610.31786v1)

## TLDR
TLDR: The paper proposes PDF, a path-dependent client-selection framework for federated unlearning that uses lightweight CLP-weighted training histories to rank and retrain with only the top-k retained clients that are globally informative yet weakly coupled to the target client, achieving effective forgetting with strong retained utility and substantially lower communication and computation than full retraining.

## Abstract
Federated unlearning (FU) aims to remove a designated target client's influence from a trained model without the prohibitive cost of retraining from scratch. Existing methods largely treat unlearning as a post-hoc, stateless operation, overlooking that client influence is path-dependent: contributions made during training, particularly during critical learning periods (CLPs), can have disproportionate and persistent effects. Moreover, knowledge overlap and intermittent client availability make relying on all retained clients inefficient and impractical. We introduce PDF, a path-dependent client-selection framework based on the insight that retained clients are not equally valuable for unlearning. During training, PDF maintains lightweight, target-agnostic, CLP-weighted histories summarizing each client's accumulated update direction and global-model alignment. Upon an unlearning request, these histories identify and rank retained clients that are globally informative yet weakly coupled to the target, enabling retraining-based unlearning with only the top-$k$ clients over a small number of rounds. Experiments on FMNIST, CIFAR-10, and CIFAR-100 under IID and non-IID settings show that PDF achieves effective forgetting and strong retained utility with substantially fewer retained clients. In particular, PDF achieves $0\%$ forgetting accuracy with retraining-like MIA AUC on non-IID CIFAR-10, improves retained accuracy by up to $6.91$ percentage points over the strongest competing FU baseline on CIFAR-100, and reduces communication by approximately $69\%$ and computation by $57$--$61\%$ relative to Retrain.
