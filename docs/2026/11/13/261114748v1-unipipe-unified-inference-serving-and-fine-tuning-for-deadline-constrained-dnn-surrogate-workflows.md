# UniPipe: Unified Inference Serving and Fine-Tuning for Deadline-Constrained DNN Surrogate Workflows

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Jaiaid Mobin, Avinash Maurya, M. Mustafa Rafique, Bogdan Nicolae
- 机构：Rochester Institute of Technology, Argonne National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14748v1) · [PDF](https://arxiv.org/pdf/2611.14748v1)

## TLDR
**TLDR:** UniPipe is a single-context edge-GPU system that unifies DNN surrogate inference and fine-tuning by fusing serving and training data in one forward pass and using a deadline-aware scheduler, thereby improving accuracy and throughput while reducing latency variance and deadline misses in high-rate scientific workflows such as ptychographic imaging.

## Abstract
DNN surrogates are increasingly used to accelerate scientific workflows that must process high-rate sensor streams in near real time, exemplified by Ptychographic imaging at next-generation X-ray light sources. Such surrogates deliver 100-1000x higher throughput than iterative solvers, enabling faster steering of experiments. To preserve surrogate accuracy during an experiment, as the input distribution evolves, state-of-the-art deployments freeze the pretrained surrogate or run a separate CUDA context that fine-tunes concurrently with serving. However, multi-context concurrency causes significant contention on the GPU, inflating both the mean and the variance of inference latency, triggering deadline misses in workflows where sensor data has to be processed within a hard per-unit deadline. To address this challenge, we propose UniPipe, a single-context system that unifies inference serving and fine-tuning of a DNN surrogate on a single edge GPU. UniPipe is driven by three key insights: both serving and fine-tuning require a forward pass and can be fused into one; the per-sample latency of modern GPUs is non-linear in batch size; and the workload is repetitive across intervals, enabling offline scheduling. Specifically, UniPipe fuses training and inference data in a single forward pass with a selective backward pass on the training subset, and uses a polynomial-time scheduler that exploits the latency curve to compute the batch composition. We evaluate UniPipe on a real-world Ptychographic reconstruction workflow with sensor rates up to 5000 patterns/sec.; UniPipe lowers reconstruction MSE by up to 30% and inference MSE by up to 50% over a pretrained baseline, and reduces the deadline-miss rate by 13%-22% over a multi-context baseline. UniPipe's unified deployment reduces the latency spread from 106% to 57% of the mean, and increases total throughput compared to multi-context baseline.
