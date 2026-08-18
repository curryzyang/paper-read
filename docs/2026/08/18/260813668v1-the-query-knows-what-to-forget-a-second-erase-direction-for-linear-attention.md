# The Query Knows What to Forget: A Second Erase Direction for Linear Attention

- 区域：速读区
- 排名：12
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Dhruman Gupta, Aritra Das, Debayan Gupta
- 机构：Truth Audit Labs
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13668v1) · [PDF](https://arxiv.org/pdf/2608.13668v1)

## TLDR
QED adds a query-derived, key-orthogonal second erase direction to GDN-2 linear attention, improving long-context retrieval and roughly doubling usable context length on S-NIAH-1.

## Abstract
Linear attention keeps a state of fixed size. At long context, many stored items share this state, and interference between them degrades retrieval. Gated DeltaNet-2 (GDN-2), like every delta-rule model before it, derives its erase vector from the key of the current token. However, the interference in its reads is measured through the query, and the erase step cannot reach it. We introduce the Query-derived Erase Direction (QED). QED adds a second erase direction derived from the query and orthogonal to the key. In the fast-weight view, a key-directed delta edit cannot change the key-orthogonal part of a read. It uses the editable part to cancel old-state content measured along the query. It also improves retrieval at every length past the training window, and it about doubles the usable context length on S-NIAH-1.
