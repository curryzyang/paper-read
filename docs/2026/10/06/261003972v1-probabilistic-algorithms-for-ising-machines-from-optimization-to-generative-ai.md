# Probabilistic Algorithms for Ising Machines from Optimization to Generative AI

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Corentin Delacour, Xiuqi Zhang, Abdelrahman S. Abdelrahman, Saleh Bunaiyan, Kyle Lee, Shuvro Chowdhury, Kerem Y. Camsari
- 机构：King Fahd University of Petroleum & Minerals, University of California, Santa Barbara
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03972v1) · [PDF](https://arxiv.org/pdf/2610.03972v1)

## TLDR
This review surveys probabilistic algorithms for diverse Ising machine platforms through an algorithm-hardware co-design lens, covering methods from annealing and parallel tempering to variational samplers, PAOA, and generative-AI synergies to guide next-generation Ising computing.

## Abstract
Ising machines have emerged as promising hardware accelerators for intractable optimization and sampling problems, yet their practical impact increasingly hinges on the co-design of algorithms and hardware, where algorithmic demands shape new architectures and new hardware capabilities inspire entirely new algorithms. In this Review, we survey probabilistic algorithms designed for portability across diverse Ising platforms, advocating a top-down perspective that prioritizes principled methods with provable guarantees. We cover foundational methods such as simulated annealing and parallel tempering, including two-dimensional extensions that natively encode hard constraints, and examine approaches that expand the scale of solvable problems from cluster mean-field methods to variational samplers. We highlight the Probabilistic Approximate Optimization Algorithm (PAOA), a classical analog of QAOA that emerged directly from probabilistic hardware development, and explore how generative AI and Ising machines might reinforce each other: learned models propose global moves to accelerate optimization, while probabilistic techniques improve inference in large language models. Much as quantum computing has seen algorithms co-evolve with hardware, probabilistic and Ising computing stand at a similar inflection point. We outline a co-design framework for accelerating the capabilities and adoption of next-generation Ising machines.
