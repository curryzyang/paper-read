# KernelMosaic: An Open Dataset and Agentic Framework for CUDA Kernel Generation

- 区域：速读区
- 排名：2
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Ningyuan Xi, Yuhang Lai, Ning Miao
- 机构：City University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14604v1) · [PDF](https://arxiv.org/pdf/2611.14604v1)

## TLDR
KernelMosaic is an open dataset and agentic framework that pairs diverse CUDA tasks with verified solutions and iterative development trajectories, enabling supervised fine-tuning of a small open-source LLM to substantially improve CUDA kernel correctness and performance on KernelBench.

## Abstract
Training large language models to generate efficient CUDA kernels requires supervision spanning diverse computational requirements and iterative code optimization. Constructing this supervision is challenging because of heterogeneous specifications, and useful implementations emerge through iterative complicated testing and refinement. We introduce KernelMosaic, an open dataset pairing diverse CUDA tasks with verified solutions and trajectories. Human-guided review and diversity-aware selection curate tasks expressed as natural-language descriptions, reference programs, mathematical specifications, and their intersections. To build the solutions and trajectories, our agentic framework guides a strong LLM through implementation, correctness repair, and performance optimization with reusable CUDA guidance and execution feedback. Supervised fine-tuning of a small open-source model on KernelMosaic raises correctness from 4%, 0%, and 0% to 88%, 82%, and 16% on KernelBench L1, L2, and L3, respectively, while increasing the fraction of tasks with kernels faster than PyTorch eager at every level. Further training experiments show that supervision from the curated trajectories substantially outperforms direct responses and promotes sustained testing and revision. These results demonstrate that KernelMosaic enables a general-purpose model to achieve substantial gains in CUDA kernel generation.
