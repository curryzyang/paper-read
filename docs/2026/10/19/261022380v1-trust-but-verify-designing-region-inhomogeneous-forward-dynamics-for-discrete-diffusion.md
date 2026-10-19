# Trust but Verify: Designing Region-Inhomogeneous Forward Dynamics for Discrete Diffusion

- 区域：速读区
- 排名：11
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Gunmay Jhingran
- 机构：Delhi Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22380v1) · [PDF](https://arxiv.org/pdf/2610.22380v1)

## TLDR
The paper proposes region-inhomogeneous forward dynamics for discrete diffusion—lightly corrupting conditioning context during training and using a detect–remask–refill sampler at inference—so a pretrained masked diffusion model can verify and repair corrupted context, improving infilling without regressing on clean conditioning.

## Abstract
Continuous diffusion treats the forward process as a design space; discrete language diffusion often uses absorbing corruption, leaving context fully trusted throughout generation. This makes trust binary: corrupted context is copied as ground truth, propagating errors into generated spans. We reopen this design space by combining absorbing and uniform-mixing kernels with region-dependent rates. Missing positions follow absorbing dynamics, while context undergoes low-rate random substitution, exposing the model to observed but uncertain tokens during training. At inference, a heuristic sampler re-injects noise into suspicious context under an annealed intensity and freezes context updates late in the trajectory. An 8,000-step finetune of a pretrained 170M-parameter masked diffusion model takes under five hours on a 6 GB laptop GPU. The base model assigns roughly 50% probability to observed tokens even when they are uniform-random garbage. For uniform-random corruption, finetuning detects corrupted context with 0.96 recall and 0.91 precision, improves infill token-F1 by 3.8 points at 10% corruption and 6.4 points at 20%, and removes the accuracy dip next to corruptions. Clean conditioning shows no measurable regression, with a false-edit rate below 0.4%. Gains for plausible corruptions are weaker: about 0.5 F1 points at 10% corruption, without statistical significance. Our results suggest that detectability and damage depend jointly on departure from the data conditional: nearby noise is hard to detect and semantically mild, while distant noise is conspicuous and destructive. We interpret absorbing diffusion as the infinite-contrast limit of a trust axis, analogous to the signal-to-noise gap between known and unknown regions in diffusion inpainting. In our setting of a 170M model and a single text domain, intermediate trust is reached by changing forward dynamics rather than architecture.
