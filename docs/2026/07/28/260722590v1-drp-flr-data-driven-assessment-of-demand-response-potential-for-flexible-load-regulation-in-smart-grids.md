# DRP-FLR: Data-Driven Assessment of Demand Response Potential for Flexible Load Regulation in Smart Grids

- 区域：速读区
- 排名：12
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Yunhao Yao, Siyu Jing, Yang Yang, Qiang Xu, Changqi Weng, Xiang-Yang Li
- 机构：University of Science and Technology of China, Anhui Zhongxin Jiyuan Information Technology Co., Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22590v1) · [PDF](https://arxiv.org/pdf/2607.22590v1)

## TLDR
DRP-FLR is a data-driven framework that accurately forecasts loads by embedding exogenous knowledge, estimates demand response potential through consumption pattern clustering, and optimizes flexible load regulation via mixed-integer linear programming to significantly reduce regulation deviation and improve participant economic benefits.

## Abstract
The rapid growth of AI workloads and renewable energy resources exacerbates supply-demand imbalance in power systems, making traditional load regulation designed for efficient allocation inadequate and motivating demand response (DR) mechanisms to enable load controllability in smart grids. However, existing DR-oriented approaches either focus on optimizing electricity cost or occupant comfort with limited benefit to system-level balance. Others overlook the diverse and dynamic consumption patterns of heterogeneous energy entities, leading to significant over- or under-regulation. Therefore, we propose DRP-FLR. First, DRP-FLR achieves accurate short-term load forecasting by embedding exogenous knowledge (e.g., entity information, prediction time) into historical load representations. Next, it constructs entity-specific load-pattern profiles by clustering historical load curves, and estimates DR potential by matching forecasted loads with pattern profiles. Finally, DRP-FLR formulates flexible load regulation as a mixed-integer optimization problem and solves it with an MILP solver to jointly optimize DR utilization, participant economic benefit, and renewable accommodation, while enforcing supply-demand balance and economic feasibility. Experiments on a regional grid and a campus microgrid show that DRP-FLR reduces regulation deviation by 36.63%-91.87% and improves participant benefit by 44.66% on average.
