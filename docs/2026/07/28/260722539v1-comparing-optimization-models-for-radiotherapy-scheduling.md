# Comparing Optimization Models for Radiotherapy Scheduling

- 区域：速读区
- 排名：15
- 匹配度：3.0/10
- 来源：arxiv
- 作者：C. C. Rambaldi Migliore, D. Stanicel, N. Musliu, G. Iacca, M. Roveri
- 机构：Technische Universität Wien, University of Trento, University of Pisa
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22539v1) · [PDF](https://arxiv.org/pdf/2607.22539v1)

## TLDR
This paper introduces two novel greedy heuristics for radiotherapy scheduling and integrates them with simulated annealing to achieve near-optimal solutions with dramatically lower runtime and memory usage compared to exact integer linear programming solvers.

## Abstract
The Radiotherapy Scheduling Problem (RTSP) involves determining an optimal schedule for patients undergoing radiation treatments, a task that has a massive impact on clinical outcomes given the central role of radiotherapy in cancer care. The daily batch approach--which consists of scheduling all the newly arrived patients together at the end of each day--modelled with Integer Linear Programming, is currently one of the most effective methods for the RTSP. However, this kind of formulation requires substantial computational resources in terms of time and memory. Here, we address these limitations by developing two novel greedy heuristics (named RTSP First Fit and RTSP Best Fit) and use them as constructive heuristics for a Simulated Annealing (SA) approach to optimize the scheduling. The proposed methods--the heuristics alone and their combination with SA--are evaluated on a publicly available dataset against an integer linear program formulation solved with two different state-of-the-art exact solvers. Evaluation metrics include six scheduling objectives capturing patient waiting times, preference satisfaction, and changes in linear accelerator assignment (aggregated in four different weight configurations), solving time, and memory consumption. The results show that the novel heuristics achieve solutions close to those of exact methods, while dramatically reducing runtime and memory usage; furthermore, when combined with SA, they further improve the solution quality while maintaining low runtime and memory usage.
