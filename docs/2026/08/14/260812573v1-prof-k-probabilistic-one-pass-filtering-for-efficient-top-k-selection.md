# Prof-K: Probabilistic One-Pass Filtering for Efficient Top-k Selection

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Tadeusz Dziarmaga, Witold Sikora, Łukasz Struski, Jacek Tabor, Marcin Mazur
- 机构：Jagiellonian University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12573v1) · [PDF](https://arxiv.org/pdf/2608.12573v1)

## TLDR
Prof-K is a fast, distribution-agnostic top-k selection algorithm that uses a small random sample to estimate an adaptive threshold, filters the input in a single pass into a compact buffer, and then runs exact top-k refinement, providing probabilistic correctness guarantees and 1.5–10x speedups over existing methods.

## Abstract
Top-k selection is a fundamental computational primitive with applications spanning databases, information retrieval, signal processing, and modern machine learning workloads, including sparse activations and attention pruning. As data sizes grow, existing approaches become inefficient: exact methods incur high memory and compute overhead, while approximate methods often rely on brittle heuristics that degrade under adversarial or heavy-tailed inputs. In this paper, we introduce Prof-K, a fast, scalable, and distribution-agnostic top-k algorithm with probabilistic correctness guarantees. Prof-K performs a single-pass filtering procedure: a small random sample estimates an adaptive threshold, the N input elements are streamed once into a compact buffer, and an exact top-k routine on this buffer recovers the true top-k elements with probability at least 1 - $ε$, where $ε$ > 0 is user specified. We derive high-probability guarantees for correctness and buffer size, together with an approximately optimal sample size that minimizes overhead as a function of N and k. Empirically, Prof-K achieves 1.5x-10x speedups over the highly optimized PyTorch topk and recent RadiK implementations, with the largest gains in the large-scale, small-to-moderate-k regime where prior methods struggle most. Unlike previous approaches, these guarantees hold independently of the input distribution, ensuring robustness to adversarial settings. By relaxing the recall target (e.g., recovering 95% of the true top-k values), Prof-K additionally provides a principled accuracy-speed trade-off. We further demonstrate its impact on training BatchTopK Sparse Autoencoders (SAEs), where top-k selection constitutes a significant portion of the training cost.
