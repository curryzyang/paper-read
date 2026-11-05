# Constraint-Preserving Flow Matching for Spectral Graph Generation

- 区域：速读区
- 排名：11
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Anita Yang, Ken-ichi Kawarabayashi, Yohan Jung
- 机构：The University of Tokyo, National Institute of Informatics, Jeonbuk National University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05436v1) · [PDF](https://arxiv.org/pdf/2611.05436v1)

## TLDR
The paper introduces Laplacian-Constrained Stiefel Flow Matching (LaSFM), a flow-matching method for spectral graph generation that preserves eigenvector orthonormality, the Laplacian nullspace constraint, and positive eigenvalues—and extends to property-guided generation—thereby improving spectral/graph-level fidelity and target-property alignment.

## Abstract
Spectral graph generation models graphs through the eigenvalues and eigenvectors of their Laplacians, providing a compact and continuous alternative to direct graph construction. However, these eigensystems must retain the structural properties of graph Laplacians. Existing approaches preserve eigenvector orthonormality but do not enforce the Laplacian nullspace constraint, potentially producing eigensystems inconsistent with Laplacian structure. To address this, we introduce Laplacian-Constrained Stiefel Flow Matching (LaSFM), which preserves the nullspace condition alongside eigenvector orthonormality and positive eigenvalues during generation. We characterize the underlying constrained Stiefel manifold and formulate flow matching on it. We further extend LaSFM to property-guided generation, steering samples toward desired graph properties while maintaining these constraints. Experiments demonstrate improved performance on both spectral and graph-level metrics, along with better alignment with target properties.
