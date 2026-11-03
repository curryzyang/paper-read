# Porteous Meets Walsh: Counting Critical Points for $\mathcal{H}_2$-Norm Model Order Reduction Using Algebraic Geometry Behind Multiparameter Eigenvalue Problems

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Sibren Lagauw, Leonie Kayser, Bart De Moor
- 机构：Max Planck Institute for Mathematics in the Sciences, KU Leuven
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00258v1) · [PDF](https://arxiv.org/pdf/2611.00258v1)

## TLDR
The paper leverages multiparameter eigenvalue problem reformulations and the Thom–Porteous formula to prove finiteness and derive an exact formula for the number of complex critical points in single-input single-output \(\mathcal{H}_2\)-norm model order reduction.

## Abstract
Several polynomial systems arising in systems and control have been shown to exhibit a partially linear structure, which allows them to be reformulated as a multiparameter eigenvalue problem (MEP). In this work, we show how such MEP formulations can be leveraged to obtain refined information about the solution set of the polynomial system. We demonstrate, in the setting of single-input single-output $\mathcal{H}_2$-norm model order reduction, how the Thom--Porteous formula can be used to derive an exact count of the complex solutions of the critical equations derived from Walsh's theorem. We prove, under suitable genericity assumptions, that their set of complex solutions is finite and that all solutions occur without multiplicity. Moreover, we derive an explicit formula for the total number of complex solutions as a function of the model orders. Throughout, we provide a self-contained and application-oriented exposition of the algebro-geometric tools required for our analysis, with the aim of making them accessible to the broader engineering community.


## 精读解读（中文）
### 一、研究动机
系统与控制中的若干多项式系统具有部分线性结构，可重写为多参数特征值问题（MEP），但通常只有 Bézout 型粗上界，缺乏对解集规模的精确先验信息。单输入单输出 H2 范数模型降阶是非凸优化问题，可能有多局部最优，其临界方程来自 Walsh 定理；任意问题规模下临界点精确计数此前未知，因此需要更精细的代数几何工具来判定有限性、重数和总数。

### 二、技术方案（Method）
针对连续时间、严格因果、稳定 SISO LTI 模型，将 H2 模型降阶的一阶最优性条件写成 Walsh 临界方程，并利用其部分线性结构重排为矩形 MEP，关联到相应的行列式簇。先借助纤维维数定理，在给定模型仅有单极点及适当生成性假设下证明复临界点集有限；再对 MEP 关联的行列式簇应用 Thom--Porteous 公式，推导复解的精确计数，并将结果写成全阶 N 与降阶 n 的显式函数。文中还给出面向工程读者的代数几何自包含介绍，并讨论多重极点情形的上界及离散时间推广。

### 三、结果（Result）
在生成性的 McMillan 度 N 高阶模型和 1≤n<N 的降阶问题下，临界方程复解总数由 ∑_{j=0}^n binom(N-n-1+j,j) 2^j 给出；若高阶模型仅有单极点，临界点集有限，且生成性条件下所有解均无重数。该计数适用于复临界点全体，实临界点只是其子集；对含多重极点的模型，该结果可导出临界点数的上界，离散时间情形也可类似推广。

### 四、结论（Conclusion）
论文给出了 SISO H2 模型降阶临界点的一个精确先验计数，并证明在适当假设下解集有限且无重数，从而可用于评估计算成本、验证数值枚举是否完整以及辅助全局最优性认证。其核心贡献不止于该降阶问题，还表明 MEP 重写结合纤维维数定理与 Thom--Porteous 公式，可为其他具有部分线性结构的工程多项式系统提供解集规模的结构性信息。

### 五、方法论与关键技术细节
关键假设包括实系数、连续时间、严格因果、稳定、互素且 Hurwitz 的分母多项式，降阶模型取 McMillan 度恰为 n；分析在复化临界方程上进行。方法核心是 MEP 的行列式簇、纤维维数定理判有限性、Thom--Porteous 公式计无重数复解，计数公式依赖 N 和 n。局限性在于完整数值枚举仍只适合较小规模，实际大规模方法如 IRKA 通常只收敛到单个局部最优；多重极点时一般只能由上界处理，生成性与单极点假设是精确计数和无重数结论的重要条件。
