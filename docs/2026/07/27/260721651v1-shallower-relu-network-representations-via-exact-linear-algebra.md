# Shallower ReLU Network Representations via Exact Linear Algebra

- 区域：精读区
- 排名：10
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Kilian Rueß, Gennadiy Averkov, Florestan Brunck, Moritz Grillo, Christoph Hertrich, Georg Loho, Jack Stade, Moritz Stargalla, Matthew Sun, Martin Winter
- 机构：University of Technology Nuremberg, Max Planck Institute for Mathematics in the Sciences, Freie Universität Berlin, University of Copenhagen, Brandenburg University of Technology Cottbus--Senftenberg
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21651v1) · [PDF](https://arxiv.org/pdf/2607.21651v1)

## TLDR
This paper proves that the maximum of up to ten numbers can be exactly represented by a ReLU network with just two hidden layers, leading to improved depth bounds for larger maxima and for all continuous piecewise-linear functions.

## Abstract
We prove that the maximum of $n$ real numbers is exactly representable by a ReLU network with two hidden layers for every $n\le 10$. The constructions are obtained by reducing the problem to exact rational linear algebra: after a symmetry reduction, the necessary cancellations are encoded in finite linear systems over $\mathbb{Q}$, which we solve and verify computationally. The representation of $\max_{10}$ has a structured first hidden layer consisting only of pairwise maxima, a feature that allows it to be recursively substituted into larger networks. We use this to show that for every $n>10$, the maximum $\max_{n}$ can be exactly represented with $\lceil{\log_5 (n / 2)\rceil}+1 < \log_5(n) +1.5694$ hidden layers. Via the generalized hinging-hyperplane representation [Wang, Sun, IEEE Trans. Inf. Theory 2005], the same depth bound holds for all continuous piecewise-linear functions on $\mathbb{R}^d$, with $d+1$ in place of $n$. In particular, every continuous piecewise-linear function on $\mathbb{R}^d$ for $d\le 9$ admits a two-hidden-layer ReLU representation. Our results improve on [Bakaev, Brunck, Hertrich, Stade, Yehudayoff, STOC'26]. In that work, the authors established a two-hidden-layer representation for $\max_{5}$ and an upper bound of $\lceil{\log_3 (n-2)\rceil}+1$ hidden layers for $\max_{n}$.


## 精读解读（中文）
### 一、研究动机
已有工作证明了最大值函数max_5可用两层ReLU网络精确表示，并给出了基于log_3的深度上界；本文旨在进一步扩展这一结果，证明max_10也可用两层表示，并基于此改进一般n下的深度上界。

### 二、技术方案（Method）
通过对称性约化将问题归结于有序锥上的有理线性系统，将表示max_n的系数求解转化为有限线性系统并在有理数域精确求解；利用max_10表示中第一层仅含成对最大值这一结构特性，通过递归替换构建更大n的表示，每次递归增加一层隐藏层并将输入变量数乘以5；结合Wang-Sun表示，将结论推广至任意连续分段线性函数。

### 三、结果（Result）
证明了对于n≤10，max_n可用两层隐藏层精确表示，且max_10的表示第一层仅含成对最大值；基于此，对于所有n>10，max_n可用至多ceil(log_5(n/2))+1层隐藏层表示；对于d维连续分段线性函数，深度上界为ceil(log_5((d+1)/2))+1，特别地当d≤9时两层即可，这改进了此前log_3的上界。

### 四、结论（Conclusion）
通过精确线性代数方法，本文给出了ReLU网络表示最大值函数所需深度的更优上界，证实了更浅网络表示的可能性，并推进了关于连续分段线性函数深度复杂度的理解。

### 五、方法论与关键技术细节
方法依赖于对称性约化到有序锥上的线性系统，且系统在有理数域上有解确保精确性；max_10表示的第一层结构允许递归替换，每次替换使深度加一、输入数乘五；该构造未涉及下界证明，是否最优仍开放；使用支持函数与多面体视角，但最终构造未显式依赖几何直观。
