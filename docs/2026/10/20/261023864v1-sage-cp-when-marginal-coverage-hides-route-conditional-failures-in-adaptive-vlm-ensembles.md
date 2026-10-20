# SAGE-CP: When Marginal Coverage Hides Route-Conditional Failures in Adaptive VLM Ensembles

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Mushir Akhtar, M. Tanveer
- 机构：Indian Institute of Technology Indore
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23864v1) · [PDF](https://arxiv.org/pdf/2610.23864v1)

## TLDR
SAGE-CP shows that marginal conformal coverage can mask severe route-specific failures in adaptive VLM ensembles, and fixes this by freezing the router and applying Mondrian split conformal calibration separately to each computational route, achieving stronger route-conditional coverage with modest set-size cost while retaining large latency and energy savings.

## Abstract
Adaptive VLM ensembles save computation by stopping early on easy images and escalating harder ones. Although a single conformal threshold can make the final predictor marginally valid, it can still fail severely along individual computational routes. We characterize this failure precisely: if a route has prevalence pi, marginal 1-alpha coverage allows its conditional coverage to fall to max{0, 1-alpha/pi}. To address this mismatch, we learn the router on development data, freeze all routing choices, and calibrate the returned score separately for early exits and escalated inputs. We call this pipeline SAGE-CP. Its calibration step applies Mondrian split conformal prediction to the operational groups created by the router. Under exchangeability, the resulting prediction sets achieve finite-sample coverage within each route. Across 10 benchmarks, 4 frozen VLMs, and 5 aligned splits, both global calibration and SAGE-CP achieve 0.900 marginal coverage at a 0.90 target, but their route behavior differs substantially. SAGE-CP raises mean worst-route coverage from 0.623 to 0.887 and reduces the mean route-coverage gap from 0.324 to 0.025, using the same routed scores and 1.177 source calls per image. The stronger guarantee increases the mean prediction-set size from 1.893 to 2.212; nevertheless, the sets remain smaller than those of the full ensemble (2.486) while requiring 70.6 percent fewer source calls. The route-level reliability persists across 6 fixed query fractions, while finer exit-depth groups demonstrate the need for additional calibration data on rare routes. Across 5 datasets, SAGE-CP also reduces measured batch-one latency by 58.8 to 63.4 percent and gross GPU energy by 55.7 to 57.5 percent relative to full inference. Thus, routing provides computational savings, while route-stratified calibration attaches coverage guarantees to the operational paths created by the router.
