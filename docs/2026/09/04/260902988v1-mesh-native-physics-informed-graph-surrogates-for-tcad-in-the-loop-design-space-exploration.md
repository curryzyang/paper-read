# Mesh-Native Physics-Informed Graph Surrogates for TCAD-in-the-Loop Design Space Exploration

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Leonid Popryho, Ayoub Sadeghi, Inna Partin-Vaisband
- 机构：University of Illinois Chicago
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.02988v1) · [PDF](https://arxiv.org/pdf/2609.02988v1)

## TLDR
The paper proposes a mesh-native, physics-informed graph attention surrogate that directly predicts drift-diffusion fields on tetrahedral TCAD meshes, enabling size-transferable and orders-of-magnitude faster design space exploration via active learning.

## Abstract
High-fidelity TCAD simulation of drift-diffusion transport remains the workhorse of emerging FinFET device design, but it is computationally expensive, especially for 3D structures where runtime escalates steeply with mesh complexity. This sharply limits multi-objective design space exploration. Existing machine-learning surrogates map a fixed set of design parameters to a few scalar device metrics, discarding the underlying physics and losing transferability across device geometries and families. A physics-informed graph attention network (GAT) surrogate is proposed. It operates directly on the tetrahedral TCAD mesh and predicts, at every mesh node, the electrostatic potential together with the electron and hole quasi-Fermi levels, the fundamental unknowns of the drift-diffusion system. Training combines a data loss with finite-volume current-continuity residuals, embedding carrier-transport physics into the objective. Operating on the mesh as a graph, the surrogate inherits size generalization: a model trained on few-fin meshes applies unchanged to substantially larger arrays, bounded at inference only by GPU memory. Per-node uncertainty from a deep ensemble drives an active-learning loop that screens large candidate pools in seconds and forwards only the most informative designs for full simulation. Benchmarked against Sentaurus Device on multi-fin tri-gate FinFETs, the surrogate reproduces the three drift-diffusion fields with sub-volt per-field RMSE and reaches a per-design throughput orders of magnitude higher than the full simulator. The advantage grows with device size: on large multi-fin arrays that are prohibitively slow to simulate directly, inference still completes in under a second per device, enabling Pareto-front exploration across device scales infeasible for direct TCAD sweeps.


## 精读解读（中文）
### 一、研究动机
暂无可提取到的动机信息。

### 二、技术方案（Method）
暂无可提取到的方法信息。

### 三、结果（Result）
暂无可提取到的结果信息。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
暂无可提取到的关键方法论细节。
