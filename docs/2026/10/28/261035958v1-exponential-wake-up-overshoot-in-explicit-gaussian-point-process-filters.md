# Exponential Wake-Up Overshoot in Explicit Gaussian Point-Process Filters

- 区域：速读区
- 排名：12
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Hanwu Qin, Dianhai Wang
- 机构：Zhejiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35958v1) · [PDF](https://arxiv.org/pdf/2610.35958v1)

## TLDR
The paper shows that explicit Gaussian point-process filters can exponentially overshoot on the first event after a long silence, derives the exact wake-up update distribution and a computable crossing index, and contrasts this with the implicit filter’s logarithmic risk and lack of a uniform bin-width/silence-duration bound, confirmed experimentally.

## Abstract
When events resume after a long silence, explicit Gaussian point-process filters amplify the first update exponentially in the silence duration. We give the exact distribution of this update and a computable index that predicts when it overshoots. For the explicit (single-scoring-step) filter and its implicit posterior-mode counterpart, we derive second-order silence expansions of the state variance with opposite-sign logarithmic corrections. The crossing index determines when the post-wake prediction exceeds the resumed rate, separating the bin width at which the amplification exponent reaches one from the larger width at which the true rate is overshot. At fixed bin width, the implicit filter's expected loss grows logarithmically with silence duration, whereas a continuous-time counterexample rules out a bound uniform in bin width and silence duration. Experimental evaluation confirms these predictions in all 73 crossing cells and on exchange trade data, while variance caps reduce explicit overshoot but mostly hurt the implicit filter.
