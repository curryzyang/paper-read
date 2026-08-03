# Guarantees on Dynamical System Distinguishability for LLM Token Generation

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Mohamed Akrout, Dan Wilson
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28667v1) · [PDF](https://arxiv.org/pdf/2607.28667v1)

## TLDR
This paper provides theoretical guarantees for classifying large language models by modeling their token embeddings as stochastic linear dynamical systems, showing that misclassification probability decays exponentially with sequence length and characterizing when such classification transfers across embedding models.

## Abstract
Recent work has shown that classifying large language models (LLMs)' responses can be distinguished by modeling token embeddings as trajectories of a black-box dynamical system (DS) and comparing prediction residuals of two DSs. Despite the empirical success of this dynamical approach, a theoretical understanding of why it works, how well it scales as a function of the token sequence, and when it transfers across embedding models remains lacking. We address these questions by formalizing the classification task as a binary hypothesis test between two stochastic linear DSs. We show that the total variation distance between the stationary marginal distributions of the two DSs can be arbitrarily small even when the dynamics differ substantially, which provides a fundamental accuracy floor for any classifier that ignores token dynamics. We then show that the misclassification probability of DS-based classification decays exponentially in the sequence length $L$, with the decay governed by a dynamical discriminability quantity $δ^2$ that captures the spectral distance between the two DSs. We also characterize cross-embedding generalization by introducing an approximate intertwining condition between embedding models and establishing a lower bound on the transferable discriminability in terms of the intertwining map's smallest singular value. Together, these results explain the empirical performance of DS-based classification and motivate further investigation into using DS theory to analyze AI systems, in contrast to the more common approach of using AI to model dynamical systems.
