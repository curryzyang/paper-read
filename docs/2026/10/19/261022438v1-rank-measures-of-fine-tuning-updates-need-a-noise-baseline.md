# Rank Measures of Fine-Tuning Updates Need a Noise Baseline

- 区域：速读区
- 排名：15
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Muhammad Usman Altaf
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22438v1) · [PDF](https://arxiv.org/pdf/2610.22438v1)

## TLDR
The paper argues that rank measures of fine-tuning weight updates require a random-noise baseline and alignment-free controls, since the apparent low-rank structure is not specific to alignment data and can mislead claims about post-training.

## Abstract
Studies of what fine-tuning does to a language model often summarise the weight update $ΔW$ by its rank. We compare the rank measures used for this against the same measures on a random matrix of the same shape, and against two harder references: the pretrained weights, and matched fine-tunes without alignment content. Measures that count directions put our fine-tuning updates only a little below noise; stable rank, computed from the same singular values, puts them far below. Both are right: an update has a few strong directions on top of a long tail. The pattern holds for thirteen released pairs up to 8B parameters, and it is not a mark of alignment: with training held fixed, instruction data does not stand out from Wikipedia or code, DPO gives the same update whether its preference labels are real or half swapped at random (one model, modest preference strength), and scrambled text gives the most concentrated update of all. Applied to a recent claim that post-training is superficial because the effective rank of the weights barely changes, the baselines show that a random update of the same size leaves that rank almost unchanged while wrecking the model, and that an edit built on the effective rank of the update has no measurable effect in our tests. Rank measures of weight updates need a noise baseline, and claims about alignment need a control without alignment content.
