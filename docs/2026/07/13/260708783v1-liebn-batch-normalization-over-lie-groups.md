# LieBN: Batch Normalization over Lie Groups

- 区域：速读区
- 排名：8
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Ziheng Chen, Yue Song, Rui Wang, Xiao-Jun Wu, Nicu Sebe
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08783v1) · [PDF](https://arxiv.org/pdf/2607.08783v1)

## TLDR
LieBN introduces a general Riemannian batch normalization framework for Lie groups that leverages invariant metrics to effectively normalize manifold-valued data across diverse geometries.

## Abstract
Manifold-valued measurements are prevalent in various machine learning tasks. Recent advances have extended Deep Neural Networks (DNNs) to operate on manifolds, accompanied by normalization techniques tailored to different geometries, collectively referred to as Riemannian normalization. However, most existing Riemannian normalization methods are either designed for specific manifolds or fail to effectively normalize manifold-valued sample distributions. To address these limitations, we propose LieBN, a framework for Riemannian Batch Normalization (RBN) over Lie groups. Our approach leverages the theoretically convenient left- and right-invariant metrics, which naturally exist in every Lie group, and provides theoretical guarantees for controlling the Riemannian mean and variance. We instantiate LieBN across nine distinct geometries: four on the Symmetric Positive Definite (SPD) manifold, one on the group of rotation matrices, and four on the manifold of full-rank correlation matrices. Notably, among the SPD metrics, we introduce a novel right-invariant metric and extend three existing Lie group structures via matrix power deformation. Extensive experiments on different manifolds validate the effectiveness of our framework. The code is available at https://github.com/GitZH-Chen/LieBN.git.
