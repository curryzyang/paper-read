# Graph-Regularized Deep Learning for EEG-Based Emotion Recognition with Psychologically-Grounded Label Structure

- 区域：速读区
- 排名：6
- 匹配度：2.0/10
- 来源：arxiv
- 作者：Dongyang Kuang, Zizheng Ma, Yushan Zhang, Xiaocong Zeng
- 机构：Sun Yat-sen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07773v1) · [PDF](https://arxiv.org/pdf/2607.07773v1)

## TLDR
This paper introduces a graph-regularized deep learning framework for EEG-based emotion recognition that models emotions according to psychological theory, achieving consistent accuracy improvements and fewer psychologically implausible misclassifications across multiple architectures.

## Abstract
EEG-based emotion recognition is critical for mental health monitoring and affective brain-computer interfaces, yet existing deep learning approaches often treat emotion classes as isolated labels, ignoring their psychological interdependencies. We propose a graph-regularized learning framework that conceptualizes emotions as nodes in a graph where edges encode proximity based on dimensional emotion theories. We adapt three complementary regularization strategies--Graph Label Smoothing (intuitive soft labeling), Commuting distance on graph via Graph Laplacian (spectral graph theory), and Sliced Wasserstein Distance (optimal transport on graph)--ordered by increasing computational complexity. These strategies penalize model predictions that deviate from the established emotion topology. Our framework is evaluated across three representative backbone architectures: AudioTransformer (pure transformer), Conformer (CNN-transformer hybrid), and DCGNN (causal graph neural network), demonstrating architecture-agnostic benefits. Experiments on SEED-IV (4 classes) and SEED-V (5 classes) datasets show consistent improvements: best case up to +5.42% accuracy and 39% reduction in psychologically implausible misclassifications. Ultimately, our framework help raise the upper bound of performance achievable with standard approaches. Code will be released.
