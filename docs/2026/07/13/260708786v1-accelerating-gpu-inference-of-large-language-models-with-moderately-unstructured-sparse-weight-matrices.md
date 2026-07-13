# Accelerating GPU Inference of Large Language Models with Moderately Unstructured Sparse Weight Matrices

- 区域：速读区
- 排名：11
- 匹配度：2.0/10
- 来源：arxiv
- 作者：Tao Lu, Haoyu Wang, Zonghui Wang, Keshen Xiang, Jiaheng Zhang, Wenzhi Chen
- 机构：Zhejiang University, National University of Singapore
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08786v1) · [PDF](https://arxiv.org/pdf/2607.08786v1)

## TLDR
The paper proposes a three-layer storage format and a hybrid SpMM kernel leveraging sparse tensor cores and CUDA cores to achieve, for the first time, faster-than-dense GPU inference for large language models with moderate unstructured sparsity.

## Abstract
With the growing deployment of large language models (LLMs), LLM inference cost has become a key challenge. Pruning techniques that introduce sparsity into weight matrices can accelerate inference. However, maintaining model quality typically limits pruning to moderate unstructured sparsity (around 50\%). At these sparsity levels, none of the existing GPU kernels for sparse matrix multiplication (SpMM) can outperform their dense counterparts. This paper proposes an efficient GPU inference method for LLMs with moderate sparsity. We propose a three-layer matrix storage format comprising: (i) a Sparse-TC layer enabling sparse tensor cores to accelerate SpMM; (ii) a Slot-Filling layer using parallel differential distance for matrix compression while supporting low-cost on-chip decoding; (iii) a lightweight Residual Layer ensuring correct SpMM computation. Building on this format, we design a SpMM kernel that jointly utilizes sparse tensor cores and CUDA cores. This design enables an efficient execution pipeline and overlaps on-chip computation with memory access. Evaluations show that our work is the first to outperform dense matrix multiplication on modern GPUs equipped with high-bandwidth memory (HBM). It achieves up to 1.64x kernel-level speedup over SpInfer (EuroSys'25, Best paper) and up to 1.41x end-to-end speedups over FlashLLM (VLDB'24). Our source code: https://github.com/moui0/cudac.
