# What a Weight Update Buys: Leverage Across Training Stages

- 区域：速读区
- 排名：2
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Shikhar Shiromani
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37719v1) · [PDF](https://arxiv.org/pdf/2610.37719v1)

## TLDR
The paper introduces **leverage**—the behavioral effect of a weight update measured by its Fisher quadratic form relative to random updates of the same size—and uses it to show that tiny post-training deltas (SFT/RL/DPO) buy far more behavioral change than large pretraining updates, while also revealing bf16-without-fp32-master distortions and predicting DARE-style delta-reuse damage.

## Abstract
Post-training moves a language model's weights by about a thousandth of their norm and changes its behavior sharply; pretraining moves them by a third and buys a slow drift. We introduce leverage, an exact measure of what a unit of weight change buys: the Fisher quadratic form of an update, computed with one forward-mode pass per direction, divided by the same form for random directions of the same size at the same checkpoint. Leverage orders released Olmo-3, Tülu-3, Zephyr, and OLMo-2 checkpoints over four orders of magnitude: pretraining windows sit at the random level on prose, SFT five times above it, RL-Zero and RLVR at 400-1,500, and DPO at 400-23,000. With this instrument we find that pretraining accumulates into noise: windows of 30k to 1M steps are no more consequential on prose than random directions of their size, as a noisy quadratic model of SGD predicts. We find that training precision changes what an update looks like: training bf16 parameters without an fp32 master copy freezes 36-99% of coordinates, lowers leverage up to sevenfold, and creates an alignment between update magnitudes and the diagonal Fisher that fp32 training does not show. We derive and verify a law for reuse: the sign-flip null predicts the relative damage of random drop-and-rescale (DARE) at keep rate $p$ as $(1-p)/(p\,ρ_{\mathrm{sign}})$, within a factor of two of measurement wherever DARE succeeds. Two controls make these readings reliable: every controlled SFT and DPO trajectory with fp32 master weights loses leverage as it moves, and two re-runs of a released DPO stage from its anchor with its published recipe land within 1% of the released displacement and 4% of its leverage, where a plain recipe reads five to six times lower; leaving one component out traces the level to the length-normalized loss and its batch size of 128 together.
