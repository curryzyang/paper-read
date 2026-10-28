# DuplexTune: Coupled-State Replay for Memory-Efficient Mixture-of-Experts Adaptation

- 区域：速读区
- 排名：4
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Paul Raj, Simon Caldwell, Daniel Whitmore, Mutlu Mete
- 机构：Michigan State University, Texas A&M University-Commerce
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.36009v1) · [PDF](https://arxiv.org/pdf/2610.36009v1)

## TLDR
DuplexTune enables memory-efficient Mixture-of-Experts language model adaptation by replaying coupled hidden states through frozen-router pretrained attention and expert modules using trainable width bridges and bridge warm-up, achieving lower peak memory and higher throughput than checkpointed supervised fine-tuning on Qwen1.5-MoE-A2.7B while trading off some multilingual performance.

## Abstract
Sparse expert execution does not remove the stored states needed to adapt a mixture-of-experts language model. We present DuplexTune, a framework for replaying coupled hidden states through pretrained attention and expert modules. Trainable width bridges connect two residual streams to the backbone. Bridge warm-up precedes backbone adaptation, with router weights kept frozen. We analyze the implicit state-recovery equation and identify the convergence and replay conditions needed for reconstruction. On Qwen1.5-MoE-A2.7B, the single-H800 evaluation reports 38.8 GB peak memory, versus 64.8 GB for supervised fine-tuning with checkpointing, and throughput of 25.1 versus 19.9 samples/s. DuplexTune achieves 67.2% MMLU, 75.6% GSM8K, and 7.69 MT-Bench, with a weaker multilingual score than the checkpointed baseline. The results characterize a configuration-dependent tradeoff among state storage, throughput, and adaptation quality.
