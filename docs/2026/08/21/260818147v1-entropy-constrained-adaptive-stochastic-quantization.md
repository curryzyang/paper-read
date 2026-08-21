# Entropy-Constrained Adaptive Stochastic Quantization

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Ran Ben Basat, Yaniv Ben-Itzhak, Michael Mitzenmacher, Shay Vargaftik
- 机构：VMware Research by Broadcom, University College London, Harvard University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18147v1) · [PDF](https://arxiv.org/pdf/2608.18147v1)

## TLDR
This paper introduces the Entropy-Constrained Adaptive Stochastic Quantization (ECASQ) problem, which jointly optimizes adaptive stochastic quantization to minimize mean squared error under an entropy budget and unbiasedness constraint, and provides an optimal dynamic program alongside a faster GPU-friendly approximate algorithm with near-optimal performance.

## Abstract
Adaptive stochastic quantization (ASQ) is a recently introduced quantization approach that optimizes the Mean Squared Error (MSE) for a given input while preserving unbiasedness. It is designed to alleviate the communication and memory bottlenecks of modern data and machine learning workloads, including model, gradient, and KV-cache compression and nearest-neighbor search. Further, practical systems can then compress quantized data with a lossless entropy encoder. However, existing unbiased methods, including ASQ, choose their quantization values without considering this later encoding stage, leaving accuracy on the table.
  We formulate the Entropy Constrained Adaptive Stochastic Quantization (ECASQ) problem, which jointly selects adaptive quantization values to minimize MSE under an entropy budget and an unbiasedness constraint. We give an optimal dynamic program with $O(sd^2)$ time and $O(d^2)$ space for a length-d vector and at most s quantization values, and a GPU-friendly approximate dynamic program with $O(sd^2)$ time and $O(d)$ space. The approximation guarantees that the solution has an MSE no larger than the optimal solution that uses one fewer bit of entropy per entry. We also provide an iterative refinement procedure for the approximation solution that, in our experiments, yields near-optimal results while retaining a substantial speed advantage over our solver for the optimal solution.
