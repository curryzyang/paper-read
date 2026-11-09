# FasterRW: An Efficient Prior-Assisted Random Walk Solver for Thermal Analysis

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Zixiao Wang, Tianshu Hou, Chenghan Wang, Zhen Zhuang, Leilei Jin, Tsung-Yi Ho, Farzan Farnia, Bei Yu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08490v1) · [PDF](https://arxiv.org/pdf/2611.08490v1)

## TLDR
FasterRW accelerates Feynman–Kac thermal random-walk simulation by using a stopping-time residual identity and a cheap prior-corrected estimator—plus kriging for multi-point queries—to achieve up to 28× speedup while maintaining accuracy.

## Abstract
Thermal simulation is becoming increasingly critical in modern IC design and manufacturing. Feynman--Kac random walk methods can estimate localized temperatures without solving the global field, but in practical settings without Dirichlet boundaries they require very long paths to control the truncation residual. This paper presents FasterRW, a continuation-value framework for accelerating Feynman--Kac thermal random walks. We prove a stopping-time residual identity showing that the expected tail after truncation equals the current attenuation weight multiplied by the temperature at the stopping location. This identity enables a prior-corrected single-point estimator: a cheap, noisy prior replaces the unknown continuation value, making the truncation bias scale with prior error rather than absolute temperature and yielding an error-controlled threshold-selection rule. For multi-point queries, FasterRW further converts cross-query pass-through tails into pseudo-samples and refines the resulting observations in prior-error coordinates through kriging. Compared with prior state-of-the-art methods, FasterRW achieves up to $28\times$ acceleration while maintaining accuracy. Our code is open-sourced at https://github.com/ShiningSord/FastRW.
