# Fresh Enough to Decide: Age of Intelligence for Cost-Aware Model Synchronization in Dynamic IoT Systems

- 区域：速读区
- 排名：9
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Hui Wang, Seyyedali Hosseinalipour, Jacob Chakareski, Ming Shi
- 机构：University at Buffalo, New Jersey Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.09935v1) · [PDF](https://arxiv.org/pdf/2611.09935v1)

## TLDR
The paper introduces **Age of Intelligence (AoInt)**—a decision-utility-based, client-specific model staleness metric—and develops **KL-AoIntSync** and lightweight **Param-AoIntSync** policies to balance stale-decision regret against refresh cost in dynamic IoT model synchronization, with guarantees and a calibrated Param-AoIntSync achieving a **6.15% joint-cost reduction** over an Instant-Parameters baseline while matching KL-AoIntSync performance.

## Abstract
Resource-constrained IoT devices cache learned models for real-time decisions, but frequent updates incur substantial bandwidth, energy, and service overhead. Because decision-relevant model differences need not grow with elapsed time, we define Age of Intelligence (AoInt) as a model-version-relative, client-specific, and action utility distortion, and formulate synchronization as a tradeoff between stale-decision regret and refresh cost. Furthermore, we develop Kullback-Leibler-aware AoInt Synchronization (KL-AoIntSync), which accumulates output-distribution changes using client-specific unlabeled probes, whereas Parameter-aware AoInt Synchronization (Param-AoIntSync) uses a server-broadcast scalar parameter change. Then, we establish pathwise guarantees with fixed client distributions, action sets, and utilities. The numerical results show that calibrated Param-AoIntSync reduces joint synchronization cost by 6.15% relative to an Instant-Parameters policy while performing comparably to KL-AoIntSync.
