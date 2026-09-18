# Randomized SVD Approximations for Spectral Co-Clustering of Word-Document Matrices

- 区域：速读区
- 排名：14
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Fateme Mazdarani, Carlos Toxtli
- 机构：Clemson University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19243v1) · [PDF](https://arxiv.org/pdf/2609.19243v1)

## TLDR
This paper presents two randomized SVD approximations for normalized spectral co-clustering of word-document matrices, showing that both reduce runtime versus full SVD while random projection is generally more reliable and sampling-based approximation mainly helps on denser matrices.

## Abstract
Spectral co-clustering is a useful tool for discovering latent structure in word-document matrices, but its reliance on singular value decomposition (SVD) can make standard formulations expensive on high-dimensional data. This paper presents two randomized approximations for normalized spectral co-clustering of bipartite text data when the numbers of document and word clusters may differ. The first method uses randomized SVD through random projection, while the second combines partial SVD with element-wise random sampling. Across real-world and synthetic datasets, both methods reduce runtime relative to the full-SVD baseline, but their behavior depends on matrix sparsity. The random projection method is the more reliable approximation across the tested settings, whereas the sampling-based method is most useful on denser matrices and provides limited benefit on already sparse text data. These results show that randomized approximations for spectral co-clustering should be selected according to the underlying structure of the data.
