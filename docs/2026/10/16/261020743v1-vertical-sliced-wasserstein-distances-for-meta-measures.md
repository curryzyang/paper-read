# Vertical Sliced Wasserstein Distances for Meta-Measures

- 区域：精读区
- 排名：7
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Elaheh Akbari, Ahmadreza Moradipari, Kyungtae Han, Hamed Pirsiavash, Yikun Bai, Rocio Diaz Martin, Soheil Kolouri
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20743v1) · [PDF](https://arxiv.org/pdf/2610.20743v1)

## TLDR
The paper introduces the vertical sliced Wasserstein (VSW) distance, a scalable metric for distributions of probability measures that projects inner measures via continuous test functions and compares their one-dimensional Wasserstein distances, with proofs of metric and weak-convergence properties, dimension-independent statistical guarantees, and a particle gradient for efficient meta-measure comparison and optimization.

## Abstract
Many modern learning problems require comparing probability distributions whose individual observations are themselves probability measures, naturally giving rise to meta-measures in $\mathcal{P}(\mathcal{P}(Ω))$. However, optimal transport distances on this space can be prohibitively expensive to evaluate. We introduce the vertical sliced Wasserstein ($\mathrm{VSW}$) distance, a scalable metric on $\mathcal{P}(\mathcal{P}(Ω))$. Rather than slicing along the transport geometry of $\mathcal{P}(Ω)$, $\mathrm{VSW}$ projects each inner measure using continuous test functions and compares the resulting one-dimensional distributions with one-dimensional Wasserstein distance. We prove that $\mathrm{VSW}$ is a valid metric on $\mathcal{P}(\mathcal{P}(Ω))$, metrizes weak convergence, and admits dimension-independent statistical convergence guarantees. Empirically, $\mathrm{VSW}$ provides high accuracy and efficiency compared with existing distances for meta-measures. We further derive a practical particle gradient for the empirical $\mathrm{VSW}_2^2$ objective and demonstrate its use for gradient-based transport of meta-measures. $\mathrm{VSW}$ provides a simple and scalable alternative for comparing and optimizing distributions of distributions.


## 精读解读（中文）
### 一、研究动机
现代学习任务常需比较以概率测度为观测对象的概率分布，即 meta-measures（P(P(Ω)) 上的测度）；然而直接在这些空间上使用最优传输距离代价过高，难以扩展。因此需要一种既能保持几何/统计性质、又可高效计算和优化的分布之分布距离。

### 二、技术方案（Method）
论文提出 vertical sliced Wasserstein (VSW)：不沿 P(Ω) 的传输几何切片，而是用连续测试函数 f:Ω→R 将每个内层测度 m∈P(Ω) 推前为一维分布 f_#m，并用一维 Wasserstein 距离比较这些投影分布；再在 meta-measure 层面通过切片积分或最优传输耦合聚合内层一维代价，实际以有限测试函数或随机采样近似积分。对经验 meta-measures（有限个内层测度/粒子），推导 VSW_2^2 目标关于粒子的实用梯度，从而支持基于梯度的 meta-measure 传输。该方案把昂贵的内层最优传输替换为可闭式计算的一维排序/分位数计算。

### 三、结果（Result）
理论结果证明 VSW 是 P(P(Ω)) 上的有效度量，能度量弱收敛，并具有与维数无关的统计收敛保证。实验表明，与已有 meta-measure 距离相比，VSW 在准确性和效率上均有优势；同时利用所推导的经验 VSW_2^2 粒子梯度，可成功进行基于梯度的 meta-measure 传输。这些结果支持其作为可扩展的分布之分布比较与优化工具。

### 四、结论（Conclusion）
VSW 为比较和优化分布之分布提供了一种简单、可扩展的替代方案，在保持度量与收敛性质的同时显著降低计算复杂度，适用于需要 meta-measure 距离的现代学习问题。

### 五、方法论与关键技术细节
关键实现点包括：输入为 P(P(Ω)) 中的 meta-measures 或其经验粒子表示；用连续测试函数族对每个内层测度做一维推前，并以一维 Wasserstein 距离作为内层代价；通过切片积分或最优传输耦合聚合，实际用有限测试函数/随机采样近似。理论分析覆盖度量性、弱收敛度量和维数无关统计率；经验目标 VSW_2^2 的粒子梯度依赖内层一维分位数/排序计算。局限可能在于测试函数族的选择与采样近似质量、对经验样本数的依赖，以及推导和优化所依赖的正则性/可积性假设。
