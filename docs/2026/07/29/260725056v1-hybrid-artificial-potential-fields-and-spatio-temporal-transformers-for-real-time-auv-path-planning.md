# Hybrid Artificial Potential Fields and Spatio-Temporal Transformers for Real-Time AUV Path Planning

- 区域：速读区
- 排名：2
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Khadija Rais, Abdelmadjid Benmachiche, Imene Soualmia
- 机构：Chadli Bendjedid University, Echahid Cheikh Larbi Tebessi University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.25056v1) · [PDF](https://arxiv.org/pdf/2607.25056v1)

## TLDR
The paper proposes and evaluates a hybrid Artificial Potential Field and Spatio-Temporal Transformer path planning framework for AUVs, which balances reactive obstacle avoidance and global path optimality to achieve superior performance in real-time underwater navigation.

## Abstract
Autonomous Underwater Vehicles (AUVs) operate in complex, unstructured environments where efficient and safe path planning is critical for mission success and energy conservation. This paper presents a comprehensive comparative evaluation of thirteen path planning algorithms, ranging from classical graph-search methods (A*, Dijkstra) and sampling-based approaches (RRT*) to metaheuristics (PSO, GA, ACO, BCO) and learning-based architectures. Special emphasis is placed on a proposed hybrid approach combining Artificial Potential Fields (APF) with a Spatio-Temporal (ST) Transformer. Evaluated across five navigation scenarios on high-resolution underwater terrain maps, all algorithms achieved 100\% task completion; however, significant trade-offs emerged in path optimality, collision avoidance, and computational load. The Hybrid APF + ST-Transformer demonstrated superior balanced performance, achieving the shortest average path length (943.15 units), a low collision rate (0.031), and efficient computation time (0.96 s), outperforming standalone learning models, which required fallback mechanisms and classical methods that incurred higher latency. While classical algorithms guaranteed collision-free paths, their excessive path lengths and processing times render them less suitable for dynamic underwater operations. Conversely, metaheuristic approaches introduced trajectory complexity unsuitable for strict energy constraints. Based on these findings, the Hybrid APF + ST framework is recommended as a principal approach for real-time AUV navigation, offering a robust solution that harmonizes reactive obstacle avoidance with global path optimality in resource-constrained underwater systems.
