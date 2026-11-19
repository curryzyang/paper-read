# Adaptive Line Switching for Cascade Mitigation in Power Systems via Graph Reinforcement Learning

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Naeem Md Sami, Soumav Biswas, Mia Naeini
- 机构：University of South Florida
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23423v1) · [PDF](https://arxiv.org/pdf/2611.23423v1)

## TLDR
This paper develops graph-aware deep reinforcement learning frameworks (Graph-DQN, Graph-A2C, and Graph-PPO) for adaptive transmission line switching to mitigate cascading failures in power systems, showing that incorporating network topology reduces cascade size, load loss, and network clustering across IEEE 39-, 57-, and 118-bus systems.

## Abstract
Although cascading failures are relatively rare events in power systems, they pose significant risks and can lead to severe economic and societal consequences within a short period. Therefore, developing effective mitigation strategies to prevent cascade propagation and to minimize their impacts is essential. This paper presents a deep reinforcement learning (DRL)-based framework for adaptive transmission line switching to mitigate cascading failures. Given the important role of network topology and component interactions in cascading failure propagation in power systems, graph-based DRL approaches, including Graph-DQN, Graph-A2C, and Graph-PPO frameworks, are developed to capture and utilize the topological information of power systems. The proposed frameworks are evaluated on the IEEE 39, 57, and 118 bus systems and benchmarked against the unmitigated case, random and heuristic-based switching strategies as baselines, as well as their corresponding graph-agnostic DRL counterparts. The results demonstrate the importance of incorporating graph information into these mitigation frameworks, leading to reduced cascade size, load loss, and network clustering.
