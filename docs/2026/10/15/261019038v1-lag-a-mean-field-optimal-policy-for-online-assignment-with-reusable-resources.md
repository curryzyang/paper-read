# Lag: A Mean-Field Optimal Policy for Online Assignment with Reusable Resources

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Keerthana Gurushankar
- 机构：Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19038v1) · [PDF](https://arxiv.org/pdf/2610.19038v1)

## TLDR
The paper introduces **Lag**, a closed-form Lagrangian index policy derived from an occupancy-measure LP for online task assignment with reusable resources, proves its asymptotic optimality in a mean-field scaling regime, and shows it outperforms greedy assignment on peer review and call center routing tasks.

## Abstract
We study online task assignment with reusable resources. This problem arises in peer reviewer assignment, skill-based call routing, rideshare matching, emergency dispatch, and crowdsourcing: Tasks arrive according to a geometric process and must be immediately assigned to servers that become temporarily busy, yielding rewards that depend on the task-server pair. The goal is to maximize long-run average reward.
  We cast the problem as a contextual restless multi-armed bandit (CRMAB). We derive an occupancy-measure LP (OCC-LP) that upper-bounds the reward of any work-conserving policy. From its dual we obtain Lag, a closed-form index policy. We introduce a scaling regime in which the number of copies of each server and the number of arrivals per step grow together. This regime yields the first deterministic fluid limit for a contextual bandit. In it, Lag is asymptotically optimal.
  Finally, we evaluate our algorithms on peer review datasets and call center routing. The Lagrangian index achieves 83-99% of the LP upper bound across all load levels. Moreover, the Lagrangian index policy significantly outperforms the natural greedy assignment scheme, improving reward by up to 12.3% on journal data and 36% on structured synthetic instances.
