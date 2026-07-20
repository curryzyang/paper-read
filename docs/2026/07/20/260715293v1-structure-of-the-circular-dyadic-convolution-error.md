# Structure of the Circular-Dyadic Convolution Error

- 区域：速读区
- 排名：7
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Ben Fauber, Alireza Moradzadeh
- 机构：NVIDIA
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15293v1) · [PDF](https://arxiv.org/pdf/2607.15293v1)

## TLDR
The paper characterizes the substitution error when using the Hadamard transform in place of the FFT for convolution, showing that the error is structured, predictable, and governed by alignment, with universal zero-error positions and a nearly full-rank error operator.

## Abstract
Dyadic and circular convolution can both be computed in $O(N\log N)$ time using the Hadamard transform and the FFT-computed discrete Fourier transform (DFT), respectively. The Hadamard transform is preferable for its real-valued sign flips, yet its substitution for the DFT introduces algebraic error. We present three complementary results that characterize this error. First, we identify exact error cancellation: two input and two output positions are universally error-free, and no reordering of the output can eliminate this error. Second, the error operator is nearly full rank, while its null space has only logarithmic dimension. Third, the expected error is governed by a single alignment scalar, with a closed-form expression obtained by averaging over random filters. In general, the substitution error asymptotically doubles the output energy, except for filters in the universal zero-error subspace, which incur no error. Collectively, these results show that the substitution error is structured, predictable, and governed by alignment.
