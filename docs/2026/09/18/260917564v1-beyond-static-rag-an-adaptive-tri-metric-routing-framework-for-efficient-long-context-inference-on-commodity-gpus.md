# Beyond Static RAG: An Adaptive, Tri-Metric Routing Framework for Efficient Long-Context Inference on Commodity GPUs

- 区域：速读区
- 排名：11
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Saipraveen Vabbilisetty, Ajay Kumar Boddepalli, Deep Narayan Mishra, Shashank Kapadia, Haoan Wang, Anupriya Sharma
- 机构：Walmart Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17564v1) · [PDF](https://arxiv.org/pdf/2609.17564v1)

## TLDR
The paper introduces a training-free Tri-Metric Router that uses hardware-physical signals to adaptively choose among raw, neural, and lexical compression for long-context RAG on commodity GPUs, eliminating OOM failures and improving efficiency and F1 without extra VRAM or training cost.

## Abstract
Deploying retrieval-augmented generation (RAG) on commodity GPUs such as the NVIDIA T4 (16 GB VRAM) exposes a practical failure mode we call the Compression Paradox: neural prompt compression can add key-value (KV) cache contention and preprocessing latency that outweigh generation-time savings, while skipping compression can cause out-of-memory (OOM) failures on long contexts. We identify two distinct failure mechanisms when a vLLM-served LLM and a PyTorch-based compressor are co-deployed under tight memory budgets, and introduce the Tri-Metric Router, a deterministic, training-free policy that selects among Raw, Neural (LLMLingua-2), and Lexical (BM25) pipelines. The router uses three CPU-side signals: spatial complexity ($L$), syntactic density ($ρ_{key}$), and type-token ratio (TTR). Unlike prior semantic-only adaptation, our dispatch signal is hardware-physical, based on VRAM headroom and a latency crossover point. Thresholds are calibrated from profiling on LongBench qasper, yielding an operating crossover near 4,332 words on T4; our contribution is this calibration methodology rather than a hardware-specific constant. On out-of-distribution holdouts, the method achieves 0% OOM failures, 88.5 $\pm$ 4.4% oracle alignment, and 49.3% Combined F1, improving over always-on lexical compression by 5.2 points without additional VRAM or training cost.
