# Voltage-Feedback Backoff and Restoration for Priority-Based EV Charging Control

- 区域：速读区
- 排名：2
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Eyad Alsulayhim, Ning Lu
- 机构：North Carolina State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33300v1) · [PDF](https://arxiv.org/pdf/2611.33300v1)

## TLDR
The paper proposes a voltage-feedback backoff and restoration (VFBR) framework that separates the number of allowed concurrent EV chargers from EV selection—adjusting charging based on monitored critical-bus voltages without forecasts or optimization—and uses an urgency-plus-voltage-sensitivity priority score to mitigate undervoltage while improving charging service and fairness.

## Abstract
Uncoordinated residential electric vehicle (EV) charging can cause sustained undervoltage in distribution networks. This paper proposes a centralized voltage-feedback backoff and restoration (VFBR) framework that separates concurrent charging-count control from EV selection. The controller adjusts the allowable charging count using monitored critical-bus voltages, without load forecasts, online power-flow calculations, or optimization. Initial charging suspension relieves undervoltage, followed by group-wise restoration and backoff as voltage conditions permit. A complementary priority score combines charging urgency with voltage sensitivity precomputed offline to balance time-critical requests against their location-dependent voltage impacts. One-week simulations on the unbalanced IEEE 123-bus feeder with 500 EVs show that VFBR reduces the proportion of charging-period bus-time samples below 0.95 p.u. from 15% to less than 1%. Among the evaluated strategies, combined allocation with urgency and sensitivity weights of 0.75 and 0.25 delivers 25% more energy than random allocation and achieves the highest mean departure state of charge and fairness. These results demonstrate that simple voltage-feedback control, coupled with urgency- and sensitivity-based allocation, effectively mitigates undervoltage while improving charging service.
