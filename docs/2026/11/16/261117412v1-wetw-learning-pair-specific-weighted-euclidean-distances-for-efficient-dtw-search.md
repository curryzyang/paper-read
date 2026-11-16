# WETW: Learning Pair-Specific Weighted Euclidean Distances for Efficient DTW Search

- 区域：速读区
- 排名：13
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Christos Panourgias, Qitong Wang, George Tzagkarakis, Themis Palpanas
- 机构：FORTH-ICS, Harvard University, Université Paris Cité
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17412v1) · [PDF](https://arxiv.org/pdf/2611.17412v1)

## TLDR
The paper proposes WETW, a learned pair-specific weighted Euclidean distance over fixed-length series embeddings that approximates DTW without computing alignments, and combines it with a filter-and-verify pipeline (WETW-FV) that uses WETW for shortlisting and exact DTW for verification, achieving up to 11.4× faster search (40× on long series) at high recall.

## Abstract
Dynamic Time Warping (DTW) is the standard distance for similarity search over time series that are misaligned in time, but its cost is quadratic in the series length and lower bounds often prune few candidates, so search over large collections of long series is slow. Learned approximations embed the series to make comparisons cheap, yet compare every pair with the same fixed rule, usually the Euclidean distance, although DTW aligns each pair differently. We observe that, once a pair is aligned, DTW is a Euclidean distance over coordinates selected for that pair. Building on this view, we propose Weighted Euclidean Time Warping (WETW), a learned distance that adapts the comparison of fixed-length embeddings to each pair. A small symmetric network predicts one weight per embedding di- mension and pair without computing an alignment, which halves the error of the best static distance on the same embeddings. The embeddings come from the Weighted Euclidean SEries Encoder (WESEE), whose multi-scale Temporal Feature Extractor keeps the timing information that global pooling removes and raises recall@1 from 0.90 to 0.95, although WETW works with any encoder. We also show that fitting DTW distances is not enough for search, as regression alone misorders the closest neighbours, and that ranking regularization raises recall@1 from 0.79 to 0.95. Our filter-and-verify pipeline, WETW-FV, uses WETW to build a shortlist and exact DTW to check it, so the search is approximate but every returned distance is exact. Over eight datasets, WETW-FV is 11.4x faster than the fastest exact method among the UCR Suite, lower bounds and MESSI-DTW, at a mean recall@10 of 0.93, while the best learned baseline reaches 0.59 at the same speed. On 48K-point series, WETW- FV remains 40x faster than the UCR Suite at a recall@10 of 0.91.
