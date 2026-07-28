# Learning to Optimize at Scale: A Benders Decomposition-TransfORmers Framework for Stochastic Combinatorial Optimization

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Seung Jin Choi, Kimiya Jozani, Josh Cooper, Esra Buyuktahtakin Toy
- 机构：Virginia Tech
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22550v1) · [PDF](https://arxiv.org/pdf/2607.22550v1)

## TLDR
This paper introduces a Transformer-accelerated Benders decomposition framework that efficiently solves large-scale two-stage stochastic capacitated lot-sizing problems by generating high-quality approximate subproblem solutions and enabling zero-infeasibility scalability to previously intractable horizons.

## Abstract
We propose a learning-augmented Benders decomposition framework to solve large-scale two-stage stochastic mixed-integer programs. We focus on the two-stage stochastic capacitated lot-sizing problem (TSSCLSP) under demand uncertainty. Our method accelerates the convergence of the decomposition by using a pre-trained TransfORmer model to rapidly generate high-quality approximate solutions for the scenario subproblems. This hybrid strategy uses the TransfORmer predictions to generate strong optimality and feasibility cuts, effectively guiding the Benders master problem. Our framework includes a novel expandable generation mechanism, allowing a model trained on a fixed horizon to solve instances of arbitrary length. For the test set considered, our method solves instances up to T = 270, a scale previously intractable for this approach, while maintaining zero infeasibility in the generated subproblem solutions. This demonstrates the potential of TransfORmers as powerful surrogate solvers embedded within classical decomposition algorithms.
