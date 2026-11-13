# CAFIN: CUDA-accelerated Adaptive Fisher Information Matrix Network Optimization via GPU-Native Kernel Fusion

- 区域：速读区
- 排名：3
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Maryam Arshad, Muhammad Khuram Shahzad
- 机构：National University of Sciences and Technology (NUST)
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14589v1) · [PDF](https://arxiv.org/pdf/2611.14589v1)

## TLDR
CAFIN is a GPU-native CUDA kernel-fusion framework that accelerates AdaFisher second-order optimization by fusing preconditioner construction, EMA updates, gradient preconditioning, momentum, weight decay, and parameter updates into integrated kernels, reducing latency and intermediate GPU memory while preserving numerical consistency and convergence.

## Abstract
Second-order optimizers improve deep neural network training using curvature information, but their practical efficiency is limited by GPU execution overhead. AdaFisher reduces Fisher Information Matrix (FIM) approximation costs through diagonal Kronecker structures and exponential moving averages, yet its PyTorch implementation requires sequential CUDA kernel launches, intermediate tensor allocations, and repeated memory accesses. We introduce CAFIN, a GPU-native CUDA kernel fusion framework that improves AdaFisher execution efficiency without changing its optimization formulation. The proposed approach progressively integrates FIM preconditioner construction, exponential moving average updates, gradient preconditioning, momentum accumulation, weight decay, and parameter updates into fused CUDA kernels. Shared-memory reuse, register-resident computation, and in-place operations further reduce memory traffic and intermediate allocations. Experiments using ResNet-18 on CIFAR-10, CIFAR-100, and Tiny ImageNet across NVIDIA GTX 1660 Ti and RTX 3060 Laptop GPUs demonstrate up to 78.4% lower isolated FIM construction latency and 2.1-26.9% lower optimizer-step latency. The implementation also eliminates approximately 18.91 MB of intermediate GPU memory allocations per optimizer step. Numerical validation confirms consistency within the predefined FP32 tolerance, while convergence accuracy remains comparable across evaluated datasets and random seeds. These findings demonstrate that CUDA kernel fusion can substantially accelerate second-order optimization while preserving AdaFisher's underlying mathematical formulation and learning behavior.
