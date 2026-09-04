# Evaluating Graph Neural Networks for Change-Criticality Classification in Maritime Navigation Charts

- 区域：速读区
- 排名：10
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Abhishek Potnis, Jacob Arndt
- 机构：Oak Ridge National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.02996v1) · [PDF](https://arxiv.org/pdf/2609.02996v1)

## TLDR
A systematic benchmark of graph neural network architectures on graph-pair representations of electronic navigational chart updates shows that GNNs—especially GraphSAGE—outperform an MLP baseline in classifying change criticality for navigational safety, demonstrating a scalable approach to automating ENC maintenance.

## Abstract
Graph neural networks (GNNs) are a class of neural networks suitable for learning on graph-structured data. Their application to spatial data is a natural extension, however its relatively unclear which message-passing operations, architectural configurations, and graph representation is best suited for classifying changes to objects in electronic navigational charts (ENCs)--geospatial vector datasets used for marine navigation. Maintaining these datasets is a challenge, and categorizing changes to objects in the ENC based on their significance to navigational safety is of particular importance. Here, we propose to represent these vector navigation datasets as a graph structure where the spatial objects serve as nodes and their spatial and semantic relationships form edges. We encode both the old ENC dataset and new ENC dataset into a pair of graphs and frame the task as a graph-pair classification problem. Building on this representation, we investigate the use of GNN architectures to classify whether the encoded graphs constitutes a critical or non-critical risk to navigational safety. We train and evaluate several GNN architectures and model configurations on ENC changes reviewed by maritime experts. Our results demonstrate that graph-based representations improve the classification of ENC updates, providing a scalable approach for automating or improving ENC maintenance workflows.
