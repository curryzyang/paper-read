# More Data Cannot Break a Symmetry: Identifiability by Design

- 区域：速读区
- 排名：15
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Jing Xu, Christopher Kanan
- 机构：University of Rochester
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27651v1) · [PDF](https://arxiv.org/pdf/2608.27651v1)

## TLDR
Symmetries in stimulus geometry make unsupervised representational alignment unidentifiable regardless of data size, so the authors propose a design-time "catastrophic cost" diagnostic that lets experimenters choose asymmetric stimulus sets—reducing alignment failures from 75% to 2% without changing models or data.

## Abstract
Unsupervised representational alignment recovers a stimulus-by-stimulus correspondence from geometry alone, but the automorphism group of the stimulus geometry bounds what any such alignment can identify, before data exist. The obvious diagnostic for this degeneracy, the cheapest non-identity relabelling, ranks two published designs in the wrong order, because dense sampling creates near-duplicates whose transposition is nearly free. We turn this known invariance (Demetci et al., 2024) into a design-time diagnostic and intervention. In colour, where candidate geometries have closed form, we show that the failure is structural: sixty-four times the restart budget leaves a symmetric design unmoved while an asymmetric set at the same N recovers every time. Discriminating representational models and recovering a correspondence are essentially uncorrelated objectives (r = -0.02 over 3,000 subsets). Choosing nine colours by this diagnostic alone, without consulting any learned representation, moves all 93 model representations away from the degenerate point and cuts catastrophic alignment failures from 75% to 2% with the models, the layers, N and the solver all held fixed. The same risk arises wherever a regular design meets its candidate geometry's isometry group, including evenly spaced orientations, tones, or motion directions, and the check costs one function call before data collection.
