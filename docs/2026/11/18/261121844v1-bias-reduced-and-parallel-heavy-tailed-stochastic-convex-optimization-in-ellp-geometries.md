# Bias-Reduced and Parallel Heavy-Tailed Stochastic Convex Optimization in $\ell_p$ Geometries

- 区域：精读区
- 排名：6
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Zhengyun Nie, Anant Shyam, Brian Bullins
- 机构：Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21844v1) · [PDF](https://arxiv.org/pdf/2611.21844v1)

## TLDR
The paper develops bias-reduced \(\ell_p\) optimal-distance-convergence algorithms and a new \(\ell_p\)-generalized Gaussian gradient estimator to improve parallel query-depth guarantees for heavy-tailed stochastic convex optimization in \(\ell_p\) geometries, along with new dimension-dependent lower bounds.

## Abstract
We consider the fundamental problem of parallel stochastic convex optimization (SCO), whose aim is to approximately minimize a convex objective when given the ability to query a moment-bounded stochastic gradient oracle multiple times in parallel per round. Whereas most previous results have focused on the variance-bounded Euclidean ($\ell_2$-norm) setting, meaning the objective is Lipschitz with respect to the $\ell_2$-norm over an $\ell_2$-bounded feasible set in $\mathbb{R}^d$, in this work we study parallel SCO in $\ell_p$ settings for $2 \le p < \infty$ under a heavy-tailed noise model. We begin by introducing a new class of $\ell_p$-optimal-distance-convergence (ODC$_p$) algorithms, drawing on prior stochastic bias-reduced techniques [ACJ+21], which combine with multilevel Monte Carlo methods to efficiently estimate the optimum of uniformly convex objectives. As a consequence of our ODC$_p$ algorithms, we first establish rates for projection-efficient $\ell_p$-Lipschitz optimization, composite convex minimization, and efficient $\ell_p$-proximal point estimation. Combining our ODC$_p$ algorithms with a new $\ell_p$-generalized Gaussian-based stochastic gradient estimator ($p$-GREG), we provide two efficient $\ell_p$ parallel algorithms, EpochDA and $\ell_p$-AC-SA, which achieve optimization error $ε> 0$ with at most $\tilde{O}(d^{\frac{p}{2p + 2}} ε^{-\frac{p}{p + 1}})$ query depth, improving upon the sequential heavy-tailed stochastic query depth of $O(ε^{-p})$ for $ε\leq \tilde{O}(d^{-1/(2p)})$. We also establish dimension-dependent lower bounds of $Ω\bigl(\min\{ε^{-p},d^{p/(3p-2)}\}\bigr)$ adaptive rounds for nonsmooth convex optimization over a subset of the unit $\ell_p$ ball. Our results improve upon the $Ω(\min\{ε^{-p},ε^{2/3}d^{1/3}\})$ bounds of [DG19], when adapted to the same feasible set.


## 精读解读（中文）
### 一、研究动机
现有并行随机凸优化研究多集中在ℓ2方差有界设定，ℓp几何下重尾噪声的并行SCO仍缺乏系统结果；本文旨在降低ℓp-Lipschitz凸优化在矩有界随机梯度下的查询深度，并给出相应下界。

### 二、技术方案（Method）
提出ODC_p算法：把随机偏差缩减思想推广到ℓp-Moreau包络，直接用多层蒙特卡洛估计Moreau梯度以回避p>2时近端点映射非线性带来的困难；构造p-GREG的ℓp广义高斯重加权梯度估计器，再与ℓp球oracle加速结合，形成EpochDA和ℓp-AC-SA两个并行算法；同时导出投影高效ℓp优化、复合凸最小化和ℓp近端点估计流程。

### 三、结果（Result）
在2≤p<∞、q=p/(p-1)矩有界重尾噪声下，两个并行算法达到误差ε的查询深度至多tilde O(d^{p/(2p+2)} ε^{-p/(p+1)})，在ε≤tilde O(d^{-1/(2p)})时优于顺序重尾的O(ε^{-p})；并证明单位ℓp球子集上非光滑凸优化的自适应轮数下界Ω(min{ε^{-p}, d^{p/(3p-2)}})，在相同可行域下改进已有Ω(min{ε^{-p}, ε^{2/3}d^{1/3}})界；还给出投影高效优化、复合最小化和近端点估计的复杂度结论。

### 四、结论（Conclusion）
论文表明偏差缩减、MLMC与ℓp广义高斯平滑可在重尾噪声和非欧几何中协同降低并行查询深度，并建立维度相关下界，使ℓp并行SCO的上界与下界更接近；其意义在于把并行重尾优化从ℓ2推广到ℓp并改进特定域限制下的复杂度。

### 五、方法论与关键技术细节
关键设定是每轮可并行多次查询、复杂度以查询深度计，随机次梯度仅假设q阶矩有界；ODC_p通过MLMC控制偏差与对偶ℓq矩，EpochDA采用几何增长epoch、递减步长和epoch末平均，ℓp-AC-SA用自适应prox正则与加速权重；分析依赖ℓp-Moreau包络光滑性、p次幂正则和球oracle加速，常数/对数因子与维度相关，结果主要覆盖p≥2、重尾矩模型及特定ℓp可行域，下界针对非光滑凸优化子集。
