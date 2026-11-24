# Scalable Beckmann Maps Improve One-step Generation

- 区域：速读区
- 排名：1
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Ulrik Unneberg, Shiyi Wang, Lee Cheuk-Kit, Felix Berg, Boris Kozinsky, Yilun Du, Michael S. Albergo, Eric Vanden-Eijnden
- 机构：Harvard University, Capital Fund Management, Imperial College London, New York University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28286v1) · [PDF](https://arxiv.org/pdf/2611.28286v1)

## TLDR
Scalable Beckmann Maps (SBM) add classifier-free guidance and a scalable training recipe to one-step Beckmann Transport Models, enabling high-quality single-network-evaluation generation without a teacher or distillation and achieving strong image, text-to-image, and world-model results.

## Abstract
Beckmann Transport Models (BTM) learn one-step generative maps end-to-end from data, without a teacher, a distillation stage, or pretrained features. We introduce Scalable Beckmann Maps (SBM), which bring to BTM the two ingredients behind the quality of modern multistep generators: classifier-free guidance (CFG) and a training recipe that scales, while keeping sampling at a single network evaluation. CFG combines conditional and unconditional velocity or score predictions, which a Beckmann map does not have. Our guidance rests on one observation: the BTM current is a positive multiple of an autonomous denoising field, to which CFG applies as it does to a velocity. With exact denoisers this gives guided BTM. In practice we substitute the map's own conditional and null predictions for the denoisers, which requires no additional network and introduces a bias that we characterize. We show that the guided update is consistent with a guided conservation equation, and that guidance can move the boundaries between basins, sending more noise to the modes a condition favors. Trained from scratch in the latent of a representation autoencoder, SBM reaches a one-step FID of 1.6 on ImageNet 256x256 without a teacher or a feature loss, outperforming the Improved-MeanFlow baseline with 3.2x fewer FLOPs. In text-to-image generation it reaches a GenEval score of 0.86 with one network evaluation. As a world model, where we train without guidance, the recipe alone outperforms DriftWorld on all five metrics of two robot-manipulation benchmarks, with 1.9-2.8x less training compute and no pretrained auxiliary feature encoder.
