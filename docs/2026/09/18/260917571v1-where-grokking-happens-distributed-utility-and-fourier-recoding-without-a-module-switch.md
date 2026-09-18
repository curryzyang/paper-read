# Where Grokking Happens: Distributed Utility and Fourier Recoding Without a Module Switch

- 区域：速读区
- 排名：6
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Dekun Yang
- 机构：Zhejiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17571v1) · [PDF](https://arxiv.org/pdf/2609.17571v1)

## TLDR
Using behavior-aligned exact activation games with paired controls, the paper shows that grokking in Transformers arises from distributed utility gains and Fourier spectral recoding of an existing circuit—centered on early attention and block-1 MLP pathways—rather than a module switch from MLP memorization to attention generalization.

## Abstract
Where in a Transformer is the change from memorization to generalization functionally expressed? We introduce Transition Games--behavior-aligned exact activation games with paired non-generalizing controls--and find distributed utility gain with a prospective block-0 attention bias; selected degree-two modes account for 67--92% of its addition contrast across replacement games, and a disjoint exact path study confirms that block-1 MLP mediates more of their effect than all other tested downstream paths in 12/12 pairs. The sharper "MLP memorizes, attention generalizes" prediction instead reverses (-.331 bits/example at the memory anchor; 0/12 in the predicted direction), while routing onset, global rank collapse, and a prime-invariant architecture ridge also fail, identifying grokking here as spectral recoding of an existing distributed circuit rather than a module switch.
