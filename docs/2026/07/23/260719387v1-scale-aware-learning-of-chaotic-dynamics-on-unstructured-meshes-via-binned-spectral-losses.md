# Scale-Aware Learning of Chaotic Dynamics on Unstructured Meshes via Binned Spectral Losses

- 区域：精读区
- 排名：4
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Kanad Sen, Romit Maulik
- 机构：Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19387v1) · [PDF](https://arxiv.org/pdf/2607.19387v1)

## TLDR
This paper extends binned spectral power losses to unstructured meshes by replacing Fourier bands with graph-Laplacian frequency bands and introduces scalable Chebyshev and multilevel approximations to improve long-horizon rollout fidelity for surrogate modeling of chaotic dynamical systems.

## Abstract
Surrogate modeling for high-dimensional nonlinear dynamical systems that exhibit chaos requires mechanisms that preserve not only pointwise accuracy but also the scale-dependent structure of physical fields. Bandwise spectral power losses, such as the binned spectral loss function, provide such supervision on structured grids, where Fourier modes define a standard frequency decomposition. On irregular meshes, however, no canonical Fourier basis exists, and spectral representations must be constructed from graph operators induced by mesh connectivity and geometry. In this study, we extend the binned spectral power loss for application to unstructured-mesh surrogate modeling of nonlinear dynamical systems. This is obtained by replacing Fourier bands with graph-Laplacian frequency bands, and we provide scalable Chebyshev and multilevel approximations for improving long-horizon rollout fidelity. In its full-spectrum form, our approach uses graph Laplacian eigenspaces to provide a graph analogue of Fourier band-power matching, but incurs the high cost of spectral decomposition. As a scalable approximation, we replace exact band projectors with sparse Chebyshev polynomial graph filters, avoiding explicit eigendecomposition. When utilizing multilevel graph architectures, we introduce Graph Laplacian Energy Alignment for Meshes (GLEAM), which applies retained-subspace scale-aware supervision across graph hierarchies so that coarse and fine representations are regularized during autoregressive rollout. Our results show that the proposed spectral losses improve long-horizon rollout fidelity and preserve statistical invariants for the forecasting of turbulent flows on unstructured meshes, compared to deterministic baselines.


## 精读解读（中文）
### 一、研究动机
针对非结构化网格上混沌动力系统代理建模，传统点对点损失不足以保持尺度依赖的结构，而现有的傅里叶带谱损失仅适用于结构化网格，需将其扩展到非结构化网格。

### 二、技术方案（Method）
将非结构化网格构建为加权图，定义对称归一化图拉普拉斯算子，利用其特征分解得到图傅里叶基，用于定义图模拟的频率带和能量。提出精确图BSP损失作为全谱参考，但计算成本高；为此设计Chebyshev BSP，用稀疏Chebyshev多项式图滤波器近似频带投影器，避免显式特征分解；并引入GLEAM，在多层级图架构中通过保留子空间进行尺度感知监督，在训练时对粗细表示进行正则化。

### 三、结果（Result）
在非结构化网格湍流预测中，所提出的图谱损失相比确定性基线改善了长时程滚动保真度，并更好地保持了统计不变量，如能量谱分布和相干结构。

### 四、结论（Conclusion）
图带谱能量对齐作为一种模块化监督目标，能有效提升非结构化网格上混沌动力学的代理模型长期预测能力，并保持多尺度物理结构。

### 五、方法论与关键技术细节
关键细节包括：数据来自非结构化网格湍流模拟；先验利用了图拉普拉斯的平滑性编码几何连接；损失函数为频带能量匹配；超参数包括频带数、Chebyshev多项式阶数、GLEAM层级数；精确BSP需要特征分解，计算复杂度高，但Chebyshev和GLEAM提供了高效近似；局限性可能依赖于图构建方式和基函数选取的鲁棒性。
