# Unsupervised Latent Space Alignment with Hyperspherical Geodesic Matching

- 区域：速读区
- 排名：14
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Cameron Ryan, Vivek Sivaraman Narayanaswamy, Kowshik Thopalli, Shusen Liu
- 机构：Northeastern University, Lawrence Livermore National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28840v1) · [PDF](https://arxiv.org/pdf/2608.28840v1)

## TLDR
This paper introduces HGA (Hyperspherical Geodesic Alignment), a method that aligns latent spaces by optimizing an orthogonal transformation to maximize a geodesic-based Gaussian affinity between normalized point clouds, achieving supervised-level performance on model stitching and multilingual embedding alignment with minimal or no supervision.

## Abstract
Independently trained neural networks tend to encode the same data with similar latent geometries. These latent geometries are not directly compatible, yet they can be nearly the same up to some class of transformations. While there exists many methods for alignment between different latent spaces, it is typically done using a set of shared sample correspondences, known as anchors. This leaves a fundamental question: are the geometric signatures of different latent spaces representing similar data sufficient to recover an alignment between them? To that end, we introduce HGA (Hyperspherical Gaussian Alignment), a method that directly optimizes a transformation between two latent spaces by maximizing a geometric measure of "fit" between them. Since it is driven by the geometry of the latent spaces rather than paired data, HGA can operate in both an unsupervised and weakly supervised regime. On tasks such as model stitching or multilingual word embedding correspondence recovery, HGA manages to match supervised results with minimal or no supervision.
