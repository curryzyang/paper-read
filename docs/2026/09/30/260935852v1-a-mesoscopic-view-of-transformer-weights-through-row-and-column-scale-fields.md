# A Mesoscopic View of Transformer Weights Through Row and Column Scale Fields

- 区域：速读区
- 排名：7
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Tiexin Ding
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35852v1) · [PDF](https://arxiv.org/pdf/2609.35852v1)

## TLDR
This paper introduces row and column scale fields—median-centered log-RMS profiles of Transformer weight matrices—as a mesoscopic representation that, together with global scale and a balanced core, reveals stable core magnitude profiles, functional channel and RoPE-related alignment, training dynamics, analogous structure in AdamW’s second moment, and a loss-sensitive relative channel gain separable from invariant reciprocal balancing.

## Abstract
Pooled statistics of Transformer weights obscure how magnitude is distributed across functional channels, while individual weights are too numerous to compare directly. We study the mesoscopic level between them: row and column scale fields, the median-centred log-RMS profiles of a weight matrix over its channels, which together with a global scale and a full balanced core represent the matrix exactly. Across public Pythia checkpoints at four sizes and controlled runs from three initialization families, balancing reveals similar measured core magnitude profiles. A mixture bridge, with its form fixed before the analysis and its coefficients fitted, predicts the pooled-shape departure from field width on held-out runs and data arms of the controlled grid. The indexed fields retain further structure: they align across projections that share a functional channel, and query/key profiles follow reassigned RoPE frequencies rather than fixed matrix coordinates. Training trajectories show early field formation followed by component-dependent broadening or recession. Extending the channel-based analysis to AdamW's second moment reveals related functional organization in its log-space row and column factors. Finally, edits of a frozen checkpoint separate reciprocal scale balance, which preserves the forward computation, from relative channel gain: flattening the gain increases in-distribution loss while preserving matrix norms and the balanced core. Row and column scale fields thus connect pooled magnitude statistics to channel organization and provide coordinates for tracking and testing trained weight structure.
