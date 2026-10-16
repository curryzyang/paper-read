# Sliced Wasserstein Sketches with Error Certificates

- 区域：速读区
- 排名：2
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Elaheh Akbari, James Liu, Keaton Hamm, Soheil Kolouri
- 机构：Vanderbilt University, University of Texas at Arlington
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20788v1) · [PDF](https://arxiv.org/pdf/2610.20788v1)

## TLDR
This paper introduces sliced Wasserstein sketches that compress probability distributions using optimal one-dimensional M-atom quantizations along shared projections, provides exact computable error certificates for their pairwise distances, and shows they drastically reduce storage while preserving classification performance.

## Abstract
Compact representations that support geometrically meaningful comparisons are valuable for learning from probability distributions. We study optimal, free-weight $M$-atom quantization of one-dimensional probability measures in quadratic Wasserstein distance and extend it to higher dimensions via slicing. Using $L$ shared projections yields a sketch with $O(LM)$ comparison time. Our main result is an exact decomposition of squared distance error into residual and partition-mismatch terms, yielding computable certificates for arbitrary centroid sketches. For optimal sketches, a finite $(2+δ)$ moment for some $δ>0$ guarantees $O(M^{-1})$ error in the finite-direction sliced distance, while equal-mass sketches can converge more slowly. Each slice preserves its mean, while storing residual energies enables covariance recovery from sufficiently many generic directions. Experiments on document, point-cloud, and flow-cytometry benchmarks show that optimal sketches substantially reduce storage while preserving the classification performance of uncompressed sliced distances. They also improve generalization from few labelled subjects and support end-to-end learning as compact pooling layers.
