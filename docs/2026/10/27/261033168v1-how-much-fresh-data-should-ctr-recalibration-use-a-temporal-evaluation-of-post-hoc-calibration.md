# How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration

- 区域：速读区
- 排名：7
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Rui Liu
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33168v1) · [PDF](https://arxiv.org/pdf/2610.33168v1)

## TLDR
On Avazu, random splits overstate CTR calibration relative to temporal evaluation, calibration error is not monotone with test-day distance, and post-hoc recalibration is safer and more effective when fitted on a roughly 12-hour span than on only the freshest few hours, with slice time span mattering more than impression count and only small simulated-auction profit effects.

## Abstract
Offline evaluation of click-through rate (CTR) models still defaults to random splits, although deployed models score future traffic and downstream systems consume calibrated probabilities. On Avazu (40.4M impressions) we train logistic regression (LR), DeepFM, and DCN-v2 under two rolling temporal origins and a random split, three seeds per arm, and recalibrate each test day with Platt scaling and isotonic regression fitted on the preceding hours. At origin 1's nearest test day, random splits report LR's expected calibration error (ECE) at 55-62% of the temporal value in every seed (the deep models' ratio is seed-unstable), and no model's ECE is monotone in temporal distance. With a 6-hour fitting slice, recalibration removes up to 61% of ECE in badly miscalibrated cells but increases it in about a third of applications (14-17 of 48 across seeds). On fixed evaluation sets, a 12-hour slice cuts harm from 13-17 to 3-5 of 36 applications, and 24 hours raises it again. The 12-hour slice subsampled to the 1-hour slice's size (5% of the impressions; 20-25x faster to fit) recovers 88% of the full slice's gain, so impression count alone does not explain it. A slice-ECE gate shows no benefit out-of-origin, and in a simulated auction recalibration moves profit by only about -0.21% to +0.26%. Offline protocols should measure calibration temporally, over multiple origins and seeds; in this data, recalibration fitted on a wide time span beat the freshest few hours, which other logs must confirm.
