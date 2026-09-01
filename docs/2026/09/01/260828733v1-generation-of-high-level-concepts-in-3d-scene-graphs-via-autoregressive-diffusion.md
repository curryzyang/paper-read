# Generation of High-Level Concepts in 3D Scene Graphs via Autoregressive Diffusion

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Jose Andres Millan-Romera, Samuel Cognolato, Holger Voos, Jose Luis Sanchez-Lopez, Luciano Serafini
- 机构：Fondazione Bruno Kessler, University of Padova, University of Luxembourg
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28733v1) · [PDF](https://arxiv.org/pdf/2608.28733v1)

## TLDR
The paper proposes a unified autoregressive diffusion-based graph generative model that jointly learns structure and features to construct complete multi-level 3D scene graphs bottom-up from observed planes, and introduces a Fused Gromov–Wasserstein distance for principled evaluation.

## Abstract
Indoor 3D Scene Graphs (3DSGs) represent environments as multi-layer hierarchies that connect observed geometric primitives (e.g., planes) to higher-level metric-semantic concepts (e.g., rooms, floors, buildings), enabling incremental spatial reasoning for robotic perception and SLAM. However, classical high-level concept generation approaches rely on hand-crafted rules for specific concept classes, while learning-based methods require separate models for graph structure and spatial node features (e.g., centroids), which limits scalability to novel classes and more complex hierarchies. We propose a unified autoregressive diffusion-based graph generative model that jointly learns structure and features, constructing complete 3DSGs bottom-up from observed vertical planes across arbitrary hierarchy depths. Our method consistently surpasses all learning-based and random baselines across 3DSG datasets spanning synthetic scenes, real architectural floor plans, and robotic sensor data, with varying layout complexity and hierarchy depth, and surpasses a one-shot model with oracle access to the target graph size on the largest hierarchy and on real single-floor data. Finally, we propose an adaptation of the Fused Gromov--Wasserstein distance for principled graph-level evaluation of generated 3DSGs against ground truth.
