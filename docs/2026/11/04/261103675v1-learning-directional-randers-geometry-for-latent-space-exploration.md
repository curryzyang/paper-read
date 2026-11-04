# Learning Directional Randers Geometry for Latent-Space Exploration

- 区域：精读区
- 排名：3
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Théau Blanchard, Stéphanie Allassonnière
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03675v1) · [PDF](https://arxiv.org/pdf/2611.03675v1)

## TLDR
The paper introduces a Finsler–Randers metric learning framework that equips latent spaces with direction-dependent asymmetric distances, enabling interpolation and extrapolation along monotonic trajectories that respect irreversible real-world processes such as disease progression.

## Abstract
Deep neural networks extract powerful latent representations from images, enabling fast and efficient downstream analysis. However, these latent spaces lack explicit geometric structure, leading to possibly poor interpolation fidelity and misleading extrapolation. Latent interpolation techniques assume symmetric transition costs which are often not the case for real world data. Their symmetric nature cannot capture directional processes, such as disease progression, where certain transitions are impossible (e.g. tumor growth dynamics or cognitive improvement in Alzheimer's disease). Although Riemannian metrics extend Euclidean geometry by incorporating curvature, they remain symmetric. We show that understanding asymmetry and not curvature alone directly addresses these problems. To do so we propose a new Finsler-Randers metric learning framework. It incorporates direction-dependent distances, thus enabling the computation of trajectories respecting monotonic sequential constraints. We demonstrate its potential for interpolation and extrapolation on controlled cross-sectional datasets.


## 精读解读（中文）
### 一、研究动机
深度网络从图像中提取的潜表示虽便于下游分析，但潜空间缺乏显式几何结构，常导致插值保真度差和外推误导。现有潜空间插值多假设对称转移代价，难以刻画真实数据中的方向性过程，例如疾病进展中肿瘤增长或阿尔茨海默病认知改善等不可逆或单向约束。因此需要一种能显式建模非对称方向距离的潜空间几何框架。

### 二、技术方案（Method）
论文提出 Finsler-Randers 度量学习框架：先将图像编码到潜空间，在该空间中参数化具有方向依赖性的 Randers 度量，使距离不再对称；再利用受控横截面数据中的单调顺序约束学习度量参数，并基于学习到的非对称几何计算插值与外推轨迹。关键模块包括潜空间编码、Randers 度量参数化、方向约束训练以及非对称测地线/轨迹求解，推理时沿满足顺序约束的路径生成中间或外推样本。

### 三、结果（Result）
在受控横截面数据集上，该框架能够计算方向依赖距离并生成尊重单调顺序约束的插值和外推轨迹，验证了非对称几何用于潜空间探索的可行性。核心发现是：仅靠黎曼曲率仍受对称性限制，而显式建模非对称性才能直接处理不可逆方向过程，避免反向或错误过渡。

### 四、结论（Conclusion）
Finsler-Randers 几何为潜空间探索提供了一种可表达方向依赖距离的原则性方法，特别适合疾病进展等具有单调性和不可逆转移的过程。该工作表明非对称性而非单纯曲率是解决此类插值/外推问题的关键，但当前验证仍限于受控横截面数据，真实纵向与临床场景的泛化需进一步检验。

### 五、方法论与关键技术细节
数据为受控横截面数据集；核心先验是序贯过程具有单调性且部分反向转移不可行；实现上需在潜空间参数化 Randers 度量的黎曼部分与方向线性项，并以有序约束驱动度量学习。摘要未披露具体损失权重、正则形式和超参，计算约束主要来自非对称测地线/轨迹求解；局限性是验证规模和真实纵向数据覆盖有限。
