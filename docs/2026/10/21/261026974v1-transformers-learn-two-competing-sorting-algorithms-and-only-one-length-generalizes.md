# Transformers Learn Two Competing Sorting Algorithms, and Only One Length-Generalizes

- 区域：速读区
- 排名：9
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Khashayar Gatmiry, Nathan W. Henry, Chloe H. Su, Emmanuel Abbe, Samy Bengio, Melanie Weber, Jonathan A. Kelner, Peter L. Bartlett
- 机构：Google DeepMind, UC Berkeley, EPFL, MIT, Harvard University, Apple
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26974v1) · [PDF](https://arxiv.org/pdf/2610.26974v1)

## TLDR
Two-layer transformers trained on fixed-length sorting converge—depending on initialization—to either a single-stage solution that fails to length-generalize or a two-stage solution that uses both attention layers to length-generalize perfectly, with the latter’s advantage explained by layer-wise specialization on rare small-gap sequences and cross-layer “hinting” that narrows the second layer’s search space.

## Abstract
We show that two-layer transformers trained to near-zero loss on a sorting task converge to one of two mechanistically distinct solution classes depending on their initialization. One solution class consists of solutions that do not use the second attention layer to sort, but also fail to length-generalize. The other, which uses both attention layers, length-generalizes perfectly, despite only being trained to sort sequences of a fixed length. By carefully choosing the weight initialization, we demonstrate that we can steer the model toward learning one solution or the other. We identify input types that are rare at the training length but increasingly common at longer sequence lengths as a source of this disparity in length-generalization, and find that layer-wise specialization of the second class of solutions allows them to handle these rare sequences more accurately. In the second class, we discover a mechanism by which the second layer attention can use the contextual information gathered by the first layer attention to reduce its search space. On the related task of finding the minimum of a sequence, we find a similar two solution-type phenomenon, but with the opposite generalization pattern, where a different form of layer-wise specialization causes the two-layer solution to length-generalize worse than the single-attention solution.
