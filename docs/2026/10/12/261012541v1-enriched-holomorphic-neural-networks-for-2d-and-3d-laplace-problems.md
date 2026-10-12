# Enriched Holomorphic Neural Networks for 2D and 3D Laplace Problems

- 区域：精读区
- 排名：2
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Kalp Shah, Andrei Vlad Nicula, Mihnea Andrei Bârsan, Robert-Stefan Sofroni, Agneya Bhardwaj, Jan Jelínek, Alejandro Valverde Mahou
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12541v1) · [PDF](https://arxiv.org/pdf/2610.12541v1)

## TLDR
The paper introduces enriched holomorphic neural networks that combine harmonic-by-construction networks with trainable, geometry-derived singular functions to solve 2D and 3D Laplace boundary-value problems from boundary data alone, achieving state-of-the-art accuracy especially for domains with corners, edges, and junctions.

## Abstract
Boundary-value problems for the Laplace equation develop singular behaviour near corners, edges and junctions that smooth approximators resolve poorly. We combine holomorphic neural networks with singular functions derived from the local geometry and boundary conditions. The representation is harmonic by construction, so no interior residual is needed: the network fits the smooth remainder from boundary data alone, and the enrichment terms capture the singular behaviour. Singular exponents are trainable, so the construction also applies when the local expansion is not known in advance. We extend the approach to three dimensions using independent networks evaluated along complex null directions. The enriched model is the most accurate tested method on every problem. Its margin is several orders of magnitude where the enrichment captures the singularity exactly, and a factor of about 1.7-2.1 over the next-best method on a CdZnTe radiation detector with many singular sites, in both two and three dimensions.


## 精读解读（中文）
### 一、研究动机
拉普拉斯方程的边值问题在角点、棱边与交接处会产生奇异行为，光滑近似器（如常规物理信息神经网络）在这些位置收敛差、精度低。作者希望在保持神经网络无网格、易实现优势的同时，把由局部几何与边界条件决定的奇异结构显式纳入表示，从根本上提升对奇异解的逼近能力。

### 二、技术方案（Method）
方法为富集全纯神经网络（Enriched PIHNN）：用复值多层感知机构造满足柯西–黎曼条件的全纯函数，其实部/虚部天然调和，因此不需要任何内点 PDE 残差，损失只由边界数据拟合光滑余项；同时按每个奇异位点的局部几何与边界条件构造幂律型奇异基函数作富集项，其奇异指数作为可训练参数与网络权重联合优化，从而在局部展开未知时也适用；三维情形则沿复零（null）方向对若干独立网络求值，把二维全纯构造推广到 3D，并保持按构造成立的调和性。

### 三、结果（Result）
富集模型在所有测试问题上都是精度最高的方法：当富集项恰好捕捉到真实奇异形式时，误差比次优方法低数个数量级；在含大量奇异位点的 CdZnTe 辐射探测器算例上，二维与三维均比次优方法好约 1.7–2.1 倍，且该优势在 2D 与 3D 中一致成立。

### 四、结论（Conclusion）
将解析奇异先验与保调和的神经网络表示相结合，可在不引入内点残差、不增加配点训练的代价下大幅提升奇异边值问题的求解精度；可训练奇异指数进一步使该方法在局部展开未知的实际几何中依然可用，三维扩展也验证了其可推广性。

### 五、方法论与关键技术细节
实现要点：损失仅在边界上评估，表示按构造调和，故无内点配点与 PDE 残差项；富集项来自局部几何与边界条件推导的奇异函数，奇异指数可训练，需要注意初值与优化稳定性；3D 依赖沿复零方向的独立网络求值，奇异位点多时带来额外的网络与参数开销；评测覆盖角点、棱边、交接等 2D/3D 基准及 CdZnTe 探测器多奇异位算例；局限性在于需要先验知道奇异位置与奇异形式（否则只能靠可训练指数近似）、指数优化可能非凸、奇异位点众多时计算与调参成本上升。
