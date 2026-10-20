# Announced Breaks Separate Conformal Reliability from Frequency Calibration

- 区域：速读区
- 排名：11
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Karl Li
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23917v1) · [PDF](https://arxiv.org/pdf/2610.23917v1)

## TLDR
The paper shows that resetting conformal prediction at announced breakpoints separates per-time conformal reliability from frequency calibration, achieving minimax per-time coverage and strong frequency-calibration guarantees with empirical improvements over adaptive conformal methods after synthetic and real-world breaks.

## Abstract
An announced boundary reveals the partition before the first affected outcome, and a reset there serves one of two audits. The per-time audit reads conformal reliability, the expected distance of the threshold's coverage from nominal at miscoverage 0.1. The frequency audit reads frequency calibration, whether a closed window's error rate matched it. The reset rule, the post-boundary empirical quantile, attains the minimax per-time rate for independent scores. On bounded scores a recursion reset at the boundary attains a frequency gap of order one over the count when its floor adds a bounded total. At the 50th forecast after a large synthetic break, the reset rule's per-time gap stands below that of five adaptive methods, four from their authors' code, with every paired band below zero. After an electricity market reform, on 68 unseen scores, the band stands below zero against two, includes zero against two, adaptive conformal inference among them, and is a point at zero against one. After monetary policy decisions its pointwise band stands above zero against all five on 10 of the first 34 days. Of 9 announced boundaries one clears the smallest coverage difference its window detects, where every method's per-time gap at the 50th forecast exceeds the nominal miscoverage. Over the first 50 forecasts the reset recursion leads the frequency audit after every synthetic break.
