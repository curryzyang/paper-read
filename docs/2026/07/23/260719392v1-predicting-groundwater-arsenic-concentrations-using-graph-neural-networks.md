# Predicting Groundwater Arsenic Concentrations Using Graph Neural Networks

- 区域：速读区
- 排名：11
- 匹配度：3.2/10
- 来源：arxiv
- 作者：William Xing, Stephanie Yang, Aarush Bandemegal, Anushree Misra, Ananya Kalapatapu, Brennan Lagasse, Kevin Zhu
- 机构：Algoverse AI Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19392v1) · [PDF](https://arxiv.org/pdf/2607.19392v1)

## TLDR
This study demonstrates that graph neural networks, by capturing spatial dependence, can match or outperform gradient-boosted trees in predicting groundwater arsenic concentrations across the contiguous United States using a novel, spatially integrated dataset of over 74,000 samples.

## Abstract
Arsenic contamination in groundwater presents a longstanding public health crisis in the United States, especially for households depending on private wells. Accurate and spatially informed prediction of arsenic concentration is vital to identify high-risk areas and focus mitigation efforts. However, there is a lack of generalizable models for representing continuous variation in arsenic concentrations across regions. In this work, we pose arsenic prediction as a regression task and construct a spatially integrated dataset to aggregate over 74,000 arsenic samples from the Water Quality Portal (WQP), Mineral Resources Data System (MRDS), and Gridded National Soil Survey Geographic Database (gNATSGO). Specifically, we use a variety of techniques including kNearest Neighbors (k-NN) and Geographic Information Systems (GIS) to join arsenic measurement points from across the United States by location. Building on this dataset, we evaluate a diverse suite of machine learning models, including tree-based ensemble approaches, multilayer perceptrons, and spatially aware graph neural networks (GNN). Our findings show that while gradient-boosted trees are still considered state-of-the-art in the field of tabular data, GNNs are able to further account for spatial dependence to match or outperform the results of gradient-boosted trees. These results demonstrate that graph-based and spatially informed learning can enhance environmental prediction and provide a foundation for improved groundwater risk mapping and monitoring.
