# FedImp: Enhancing Federated Learning Convergence with Impurity-Based Weighting

- 区域：速读区
- 排名：4
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Hai Anh Tran, Cuong Ta, Truong X. Tran
- 机构：The Pennsylvania State University, Hanoi University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14654v1) · [PDF](https://arxiv.org/pdf/2608.14654v1)

## TLDR
FedImp improves federated learning convergence under non-IID data by assigning aggregation weights based on the entropy-based impurity (informational content) of each client's local dataset, reducing communication rounds by up to 66.7% and achieving higher accuracy than FedAvg, FedProx, and FedAdp.

## Abstract
Federated Learning (FL) is a collaborative paradigm that enables multiple devices to train a global model while preserving local data privacy. A major challenge in FL is the non-Independent and Identically Distributed (non-IID) nature of data across devices, which hinders training efficiency and slows convergence. To tackle this, we propose Federated Impurity Weighting (FedImp), a novel algorithm that quantifies each device contribution based on the informational content of its local data. These contributions are normalized to compute distinct aggregation weights for the global model update. Extensive experiments on EMNIST and CIFAR-10 datasets show that FedImp significantly improves convergence speed, reducing communication rounds by up to 64.4%, 27.8%, and 66.7% on EMNIST, and 44.2%, 44%, and 25.6% on CIFAR-10 compared to FedAvg, FedProx, and FedAdp, respectively. Under highly imbalanced data distributions, FedImp outperforms all baselines and achieves the highest accuracy. Overall, FedImp offers an effective solution to enhance FL efficiency in non-IID settings.
