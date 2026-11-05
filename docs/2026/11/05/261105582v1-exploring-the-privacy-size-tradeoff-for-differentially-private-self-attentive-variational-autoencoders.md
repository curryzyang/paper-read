# Exploring the Privacy--Size Tradeoff for Differentially Private Self-Attentive Variational Autoencoders

- 区域：速读区
- 排名：13
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Rohit Sadavarte, Dhruvi Kothari, Sparsh Gupta, Eric Van Oeveren
- 机构：Intuit
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05582v1) · [PDF](https://arxiv.org/pdf/2611.05582v1)

## TLDR
The paper introduces SAVANT, a differentially private self-attentive variational autoencoder for tabular data, and jointly evaluates privacy budget versus dataset size to show that more data generally improves utility under a fixed DP guarantee, with marginal mechanisms absorbing strict-budget costs better than DP-SGD, while membership-inference audits find no aggregate privacy leakage signal.

## Abstract
Data tends to be most useful when it is shared, and the data most worth sharing is often the data that privacy obligations restrict. Synthetic data from a generator trained under differential privacy (DP) is one way to reconcile the two, but its utility depends on the privacy budget $\varepsilon$ and on how much data the generator sees - a parameter that most data sharing applications of synthetic data control. We present SAVANT, a self-attentive variational autoencoder for tabular data trained with DP-SGD that, to our knowledge, is the first to combine attention, a VAE, and DP in one tabular model. We evaluate it against two marginal mechanisms, PrivBayes and MST, jointly over the privacy budget and the dataset size on two public datasets, measuring the utility a downstream classifier loses by training on synthetic rather than real data. We find that, under the same DP guarantee, more data generally means more utility. For the marginal mechanisms it absorbs most of what a strict budget costs, and a noise-scaling argument suggests DP-SGD exchanges data fo budget at a worse rate. Two independent membership-inference attacks, judged against a measured null, found no aggregate membership signal.
