# Adaptive Margin Ordinal Loss: Penalizing Center-Class Hedging in Ordinal Classification

- 区域：速读区
- 排名：12
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Manisha Kandel
- 机构：University of Delaware
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10752v1) · [PDF](https://arxiv.org/pdf/2609.10752v1)

## TLDR
The paper proposes the Adaptive Margin Ordinal Loss (AMOL), a multiplicative per-class weighting scheme that penalizes center-adjacent predictions when the true ordinal label is extreme, thereby suppressing center-class hedging and improving Quadratic Weighted Kappa across ordinal classification benchmarks, with an asymmetric variant eliminating the Center-Hedging Rate on Abalone.

## Abstract
Standard cross-entropy loss causes neural networks trained on ordinal classification tasks to hedge predictions toward center classes, a failure mode we term \emph{center-class hedging}. This occurs because predicting the middle class minimizes expected symmetric loss, making it the path of least resistance regardless of the true label. Existing ordinal losses address related problems such as large-error penalization and rank consistency, but none directly suppresses center-class hedging as a function of where the true label lies relative to the ordinal center. We propose the Adaptive Margin Ordinal Loss (AMOL), a multiplicative weight applied to per-class loss terms of the form $m(k,y) = 1 + α\cdot (1 - |k-c|/c) \cdot (|y-c|/c)$, where $c$ is the center class, $k$ is the candidate class, and $y$ is the true label. The weight encodes a joint condition: it is large only when the candidate class is near center and the true label is far from center, collapsing to standard behavior otherwise. We further introduce the Center-Hedging Rate (CHR) as a diagnostic metric that directly quantifies this failure mode. Across four ordinal classification benchmarks and five random seeds, AMOL achieves the best or tied-best Quadratic Weighted Kappa (QWK) on all four datasets compared to cross-entropy, OLL, and SORD baselines. An asymmetric variant (AMOL-asym) eliminates center-class hedging entirely on the Abalone dataset ($\text{CHR} = 0.000 \pm 0.000$ across all five seeds, $n \approx 266$ extreme-class test samples per run), compared to $0.074 \pm 0.005$ for standard cross-entropy.
