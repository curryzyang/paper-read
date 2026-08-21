# Online Bipartite Matching with Reusable Capacity under Non-Stationary Rewards

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Xi Chen, Shixin Wang, Bingkun Zhou, Yuan Zhou
- 机构：Beijing Institute of Mathematical Sciences and Applications, Georgia Institute of Technology, Tsinghua University, New York University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18130v1) · [PDF](https://arxiv.org/pdf/2608.18130v1)

## TLDR
TLDR: This paper introduces BALANCE-type online algorithms for bipartite matching with reusable server capacity under non-stationary rewards, achieving an asymptotically optimal competitive ratio of ln(δD) under a locally bounded reward condition.

## Abstract
We study online bipartite matching with reusable server capacity and non-stationary rewards. Jobs arrive sequentially, reveal compatible servers, reward rates, and processing durations, and must be accepted or rejected irrevocably. An accepted job occupies one unit of server capacity only during its processing interval, so an assignment may displace an unknown sequence of future jobs. Existing guarantees are typically calibrated by a global reward range, which can become arbitrarily large when rewards drift over a long horizon. We instead impose a locally bounded reward condition: reward rates of jobs that can compete for the same server within a relevant time window differ by at most a factor $δ$. Under this condition, we develop two BALANCE-type algorithms with time-aware opportunity-cost losses. TS-BAL maximizes cumulative blocking losses over feasible reuse schedules and achieves a competitive ratio of $2\ln(δD)+\mathcal O(\ln\ln(δ\vee D))$. GR-BAL uses a greedy relaxation of this loss and achieves $\ln(δD)+\mathcal O(\ln\ln(δ\vee D))$, matching a lower bound of $\ln(δD)$ in the leading term. Numerical experiments demonstrate robust performance under substantial global reward drift and favorable finite-capacity performance.
