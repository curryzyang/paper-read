# An Input-Dependent Readout Phase for Resonant Sequence Models

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Shivesh Rane
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12496v1) · [PDF](https://arxiv.org/pdf/2610.12496v1)

## TLDR
Making ResonatorLM’s fixed readout phase input-dependent adds content-dependent memory reading at negligible parameter cost, matches the original at training length, and removes its long-context failure (e.g., WikiText-2 character perplexity from 12.81 to 3.76 when trained on 256 tokens and tested on 1024), even though the learned phase tracks the current token rather than elapsed time.

## Abstract
Sequence models with a fixed-size state avoid the quadratic cost of attention, but face a design choice. An input-dependent state transition gives content-dependent memory at the cost of FFT-based training, while a fixed transition keeps the O(T log T) convolutional path but reads memory the same way for every input. ResonatorLM, a recent model of the second kind, reads a bank of damped complex oscillators through a fixed learned phase per head. We make that readout phase a function of the current token, which adds input dependence to the read only, keeps the convolution exact, and costs 0.2 percent more parameters. An analysis of the untrained bank shows that phase does encode elapsed time, but an ordinary token falls below the background within 2-8 steps and no choice of damping extends linear reconstruction beyond about 16 tokens. In 6M-parameter character-level models on WikiText-2, the input-dependent phase matches the original at the training length and removes its failure beyond it: trained on 256 tokens and tested on 1024, perplexity falls from 12.81 to 3.76. We trace the failure to long-memory heads that accumulate more history than training exposed them to. The learned phase tracks the current character rather than distance and does not improve retrieval.
