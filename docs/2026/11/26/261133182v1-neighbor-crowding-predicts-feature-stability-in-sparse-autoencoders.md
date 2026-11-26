# Neighbor Crowding Predicts Feature Stability in Sparse Autoencoders

- 区域：速读区
- 排名：3
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Denis Federico Lim, Naveen Dasari, George Flint, Kevin Zhu
- 机构：University of Cambridge, Korea Advanced Institute of Science and Technology (KAIST), University of Pennsylvania, University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33182v1) · [PDF](https://arxiv.org/pdf/2611.33182v1)

## TLDR
In TopK sparse autoencoders, cross-seed feature stability can be predicted cheaply from a single training run, with neighbor crowding—how densely a feature sits among nearby decoder directions—being the strongest single predictor.

## Abstract
Sparse Autoencoders (SAEs) offer an approach to identify language model representations by breaking apart polysemantic features into more sparse, interpretable ones. Yet, it is challenging to identify which of the learned features are actually stable, rather than artifacts of initialization. One approach is to train multiple SAE seeds, and compare the learned features across seeds by cosine similarity, but this is notably costly. This raises the question of whether stable features can be identified without the computational expense of training multiple seeds. In this work, we examine cross-seed feature stability across differing levels of training tokens, and demonstrate that in TopK SAEs, it is highly predictable using six computationally cheap statistics derived from a single training run. Neighbor crowding, a geometric property of the dictionary, is the strongest single predictor, with features that sit in dense regions of the unit sphere more likely to be stable than isolated ones.
