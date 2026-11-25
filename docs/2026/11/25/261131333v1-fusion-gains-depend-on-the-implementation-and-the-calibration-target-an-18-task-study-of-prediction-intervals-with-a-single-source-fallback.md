# Fusion Gains Depend on the Implementation and the Calibration Target: An 18-Task Study of Prediction Intervals with a Single-Source Fallback

- 区域：速读区
- 排名：9
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Liwei Deng, Lu Wang
- 机构：Hunan Mechanical & Electrical Polytechnic, Central South University of Forestry and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31333v1) · [PDF](https://arxiv.org/pdf/2611.31333v1)

## TLDR
In an 18-task study of prediction intervals, fusion gains varied substantially by implementation and calibration target, but a development-set selector with a matched single-source fallback consistently improved average scores while sometimes losing to the single source, so fusion should be evaluated against matched candidates on held-out data with both average gain and loss frequency reported.

## Abstract
A fused model can benefit from an extra learning stage as well as from a second data source. We compare four fusion implementations with matched single-source learners on 18 regression tasks with prediction intervals. Across ten refits under group-wise calibration, linear stacking improved the interval score by 6.0% against a source model without a second stage and by 0.1% against its matched single source. The four implementations agreed on 3 of 18 tasks and gave opposite clear verdicts on 12, including 8 of the 10 tasks with naturally distinct sources. With pointwise calibration, they agreed on 5 tasks and gave opposite clear verdicts on 9. A development-set selector with a matched single-source fallback improved ten-refit task-averaged scores by 2.2--6.3% in every implementation under both calibrations. Adding fused arms to the pool of single-source candidates improved the mean relative score by about 5 percentage points. Under group-wise calibration, the gradient-boosted selector met the criterion frozen before evaluation on eight held-out tasks. In post-opening refits, selectors lost to the matched single source in 4.4--6.1% of task-level runs under group-wise calibration. Under signed pointwise calibration, three implementations lost in 19--23% of runs. Fusion evaluations should compare matched candidates on held-out data and report how often the selector loses alongside its average gain.
