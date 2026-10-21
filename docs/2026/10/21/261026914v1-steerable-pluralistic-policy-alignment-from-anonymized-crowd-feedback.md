# Steerable Pluralistic Policy Alignment from Anonymized Crowd Feedback

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Akansha Kalra, Ellen R. Novoseller, Vernon J. Lawhern, Daniel S. Brown
- 机构：U.S. Army DEVCOM Army Research Laboratory, University of Utah
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26914v1) · [PDF](https://arxiv.org/pdf/2610.26914v1)

## TLDR
P3L learns a shared PCA-based preference basis from anonymized, heterogeneous crowd feedback—without annotator identities—to enable rapid test-time personalized reward learning and steerable policy alignment for new users.

## Abstract
Pluralistic alignment requires AI systems to learn from diverse populations whose preferences may reflect heterogeneous or even conflicting objectives, and to personalize their behavior to individual users. Existing approaches in pluralistic alignment often assume access to annotator identities and rely on powerful pretrained representations to model individual preference variations. We propose Preference-PCA Pluralistic Learning (P3L), a novel framework for pluralistic alignment that jointly learns trajectory embeddings and the shared basis of preference directions via PCA decomposition from heterogeneous crowd feedback without requiring annotator identities. At test time, our approach enables rapid and accurate personalized reward learning and downstream policy optimization. Experiments across multiple embodied control tasks demonstrate that P3L enables steerable personal alignment that generalizes beyond the offline dataset to out-of-distribution new users and attains competitive RL and test performance, while substantially reducing computational cost and supporting variable adaptation query budgets.
