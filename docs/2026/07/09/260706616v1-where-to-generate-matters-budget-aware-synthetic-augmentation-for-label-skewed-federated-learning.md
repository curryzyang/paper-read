# WHERE to Generate Matters: Budget-Aware Synthetic Augmentation for Label Skewed Federated Learning

- 区域：速读区
- 排名：6
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Sangwoo Lee, Sunghwan Park, Jaewoo Lee
- 机构：Chung-Ang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06616v1) · [PDF](https://arxiv.org/pdf/2607.06616v1)

## TLDR
FedEAS, an entropy-adaptive per-class generation budget policy for label-skewed federated learning, recovers most accuracy gains of full class balancing while reducing the generation budget by 94.1%.

## Abstract
Label skew in federated learning (FL) causes client drift and degrades global accuracy. Synthetic data augmentation can reduce this imbalance; however, full class balancing requires substantial computation cost. We propose FedEAS, a policy that assigns each client an entropy-adaptive per-class generation budget computed from its local label distribution. The budget jointly decides \emph{how much} each client generates and \emph{WHERE} the samples go. Accordingly, the total generation budget follows from the per-client budgets rather than being fixed in advance. FedEAS recovers most of the accuracy gain of full class balancing while reducing the generation budget by 94.1\%. At the same total generation budget, it outperforms Uniform allocation by up to 18.82\% across CIFAR-10 and CIFAR-100.
