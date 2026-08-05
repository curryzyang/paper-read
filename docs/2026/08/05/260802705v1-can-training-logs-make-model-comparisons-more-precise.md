# Can Training Logs Make Model Comparisons More Precise?

- 区域：速读区
- 排名：7
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Wei-Jung Huang
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02705v1) · [PDF](https://arxiv.org/pdf/2608.02705v1)

## TLDR
Training logs can make model comparisons more precise through arm-specific covariate adjustment, but only when the adjustment statistic is chosen carefully to avoid the noise introduced by broad covariate selection.

## Abstract
Comparing stochastically trained models requires estimating both a performance difference and its uncertainty from repeated runs. We study whether training logs from those same runs can make such comparisons more precise. Because training-log covariates are produced during training rather than measured before it, we use arm-specific covariate adjustment: each model is adjusted only with statistics from its own runs, and the raw mean difference remains the reported effect. In a vision study spanning three architectures and three datasets, simple adjustments based on early training logs often reduce uncertainty in model comparisons. The main limitation is covariate selection. Broadly searching the log pool for the most correlated statistic often adds more noise than it removes, even when useful statistics exist in hindsight. Training logs therefore appear useful for more precise model comparisons, but only when the adjustment avoids large selection noise.
