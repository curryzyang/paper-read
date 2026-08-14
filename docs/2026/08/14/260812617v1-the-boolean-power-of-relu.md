# The Boolean Power of ReLU

- 区域：速读区
- 排名：10
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Pablo Barceló, Floris Geerts, Matthias Lanzinger, Klara Pakhomenko, Jan Van den Bussche
- 机构：University of Antwerp, Universiteit Hasselt, TU Wien, Pontifical Catholic University, IMFD & CENIA
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12617v1) · [PDF](https://arxiv.org/pdf/2608.12617v1)

## TLDR
ReLU-based message-passing GNNs are strictly more expressive than GNNs using any eventually constant activation functions (such as truncated ReLU) for Boolean queries on Boolean-featured graphs, resolving an open problem in GNN expressivity.

## Abstract
We prove that, on finite simple undirected graphs equipped with a single Boolean node feature, the Boolean queries expressible in $Σ$-MPLang, for any collection $Σ$ of eventually constant activation functions and with arbitrary real coefficients, form a strict subclass of the Boolean queries expressible in ReLU-MPLang. We thereby settle a recently posed open problem: whether ReLU-MPLang is more powerful than trReLU-MPLang when it comes to Boolean queries. In particular, this implies that ReLU-GNNs are strictly more expressive than {TrReLU,id}-GNNs with respect to Boolean queries on Boolean-featured graphs.
