# CacheScope: Exact-Compute Allocation for Training-Free Diffusion Acceleration

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Qinhan Lyu, Jusheng Zhang, Zhixing Zhang, Hao Liu, Zijie Liang, Jin Jiang, Keze Wang
- 机构：Sun Yat-sen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12530v1) · [PDF](https://arxiv.org/pdf/2610.12530v1)

## TLDR
CacheScope is a training-free diffusion acceleration scheduler that normalizes shallow-probe output variation by input-trajectory displacement to identify high-risk cache-reuse steps online and selectively fall back to exact denoising, achieving up to 3.57× speedup and up to 70.1% lower median LPIPS across image and video diffusion transformers.

## Abstract
Training-free feature reuse accelerates diffusion transformer inference by replacing full denoising computation at selected steps with cached approximations. Existing methods mainly improve the reconstruction of skipped features, but we find that once a stable first-order reconstructor is used, increasing reconstruction complexity brings limited gains, whereas the placement of exact-computation steps has a much larger effect on fidelity. More importantly, absolute shallow-probe variation is jointly affected by input-trajectory displacement and network response strength, and therefore does not directly reflect cache risk. We address this confounding by normalizing probe-output variation with the corresponding input displacement, yielding a directional gain per unit trajectory movement. Based on this signal, we propose CacheScope, which identifies high-risk reuse steps online and selectively falls back to full denoising computation while leaving the underlying cache reconstructor unchanged. CacheScope requires no additional training, gradients, auxiliary networks, or prompt-specific offline schedule optimization. Across FLUX.1-dev, Wan2.1-T2V-1.3B, and Open-Sora 1.2, CacheScope achieves up to 3.57x acceleration and reduces median LPIPS by up to 70.1% over the strongest probe-based baseline.
