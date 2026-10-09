# Masked Generative Motion Planning with Geometry-Guided Token Search

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Lipeng Zhuang, Yingdong Ru, Shiyu Fan, Edmond S. L. Ho, Gerardo Aragon Camarasa, Paul Henderson
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10646v1) · [PDF](https://arxiv.org/pdf/2610.10646v1)

## TLDR
MGMP combines a masked generative transformer that generates discrete trajectory candidates in parallel with Geometry-Guided Token Search to enable efficient, geometry-aware route-level repair of motion plans, achieving strong planning and repair success and generalizing across layouts, obstacles, single- and dual-arm planning, and real-world tasks.

## Abstract
Generative motion planners typically use learned trajectory priors for initial generation, while leaving test-time repair to local continuous refinement. We introduce Masked Generative Motion Planning (MGMP), which extends the learned prior from efficient parallel generation to structural repair. A masked generative transformer generates discrete trajectory candidates in parallel, and Geometry-Guided Token Search (GGTS) uses scene geometry to target where to edit and which prior-supported alternatives to evaluate. This turns refinement into an efficient search over discrete motion alternatives, enabling route-level restructuring beyond local trajectory deformation. MGMP achieves 96% success on Ring Maze and 82% repair success on Controlled Route Invalidation on Kuka, exceeding the strongest external baselines by 23 and 25 percentage points, respectively. It further generalizes to unseen layouts, additional obstacles, unseen geometries, single- and dual-arm planning, and real-world Baxter tasks.
