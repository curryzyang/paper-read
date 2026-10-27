# Inference-Time Prior Adaptation for Imbalanced Data Streams under Concept Drift

- 区域：速读区
- 排名：2
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Tobias Callies, Eirini Ntoutsi, Arthur Zimek
- 机构：University of Southern Denmark, University of the Bundeswehr Munich
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33126v1) · [PDF](https://arxiv.org/pdf/2610.33126v1)

## TLDR
PAI-KNN is a sliding-window k-NN stream classifier that adapts to concept drift and class imbalance by adjusting class priors at inference time rather than modifying memory, achieving competitive minority-class performance.

## Abstract
Data stream classification under concept drift and class imbalance requires models to adapt continuously while maintaining strong minority-class performance. Many existing approaches rely on active memory management, in- cluding instance removal, memory restructuring, resampling, and synthetic data generation. We present PAI-KNN, a k-nearest neighbor classifier that adapts via inference-time prior adjustment rather than memory modification. PAI-KNN main- tains a simple sliding-window buffer and dynamically adjusts its decision rule using class prior estimates derived from recent observations. Evaluated on a mul- titude of synthetic data streams covering various imbalance and drift scenarios, PAI-KNN achieves competitive performance with state-of-the-art methods, per- forming particularly well under scenarios involving dynamic class imbalance and concept drift. These findings highlight the potential of inference-time adaptation in challenging non-stationary environments and suggest that adaptation in memory- based stream classifiers need not rely exclusively on memory modification.
