# Support Discovery With Iteratively Reweighted Least Squares for Fixed-Charge Network Flow

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Sindura Saraswathi, Christian Kümmerle
- 机构：University of Central Florida
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09295v1) · [PDF](https://arxiv.org/pdf/2609.09295v1)

## TLDR
This paper proposes a scalable iteratively reweighted least-squares algorithm using a smooth Lasry–Lions surrogate and support-improvement search to find high-quality feasible solutions for large-scale fixed-charge network flow problems.

## Abstract
The fixed-charge network flow problem (FCNFP) couples continuous flow allocation with discrete arc-activation decisions, making it a canonical but computationally challenging model for a variety of network design and resource allocation problems. Exact mixed-integer linear programming formulations capture the fixed-charge structure faithfully, but often become difficult to solve on large networks. We propose a scalable continuous-optimization algorithm for large-scale single-commodity FCNFP based on an iteratively reweighted least-squares (IRLS) framework. The method replaces the discontinuous fixed-charge and linear arc cost objective with a smooth nonconvex Lasry--Lions surrogate and solves a sequence of weighted quadratic flow subproblems. Each subproblem is solved by a warm-started dual semismooth Newton method whose Newton systems have weighted graph-Laplacian structure, enabling the use of modern Laplacian solvers. To further improve the discovered arc supports of the challenging underlying combinatorial problem, we also develop an algorithmic variant that incorporates objective-driven perturbation restarts and an anchor-union restricted search that jointly leverages supports discovered by IRLS and by complementary FCNFP heuristics. Computational experiments on 410 benchmark, synthetic, and large-scale instances show that our method obtains the best objective quality among the evaluated scalable FCNFP algorithms, with a mean gap of $1.316\%$ to a time-limited MILP reference and a win-or-tie rate of $90.0\%$ among the non-MILP methods. The results indicate that combining smooth continuous optimization with support-level search is an effective strategy for producing high-quality feasible solutions to large-scale FCNFP.


## 精读解读（中文）
### 一、研究动机
固定费用网络流（FCNFP）同时耦合连续流量分配与离散弧激活决策，是网络设计与资源配置的经典模型，但因固定费用项非连续、问题NP难，精确MILP在大网络上往往难以求解甚至无法证明最优。作者希望在不显式求解混合整数搜索的前提下，利用连续优化和网络流结构为大规模单商品FCNFP生成高质量可行解。

### 二、技术方案（Method）
输入为有向网络 G=(V,E)、每条弧的容量 c_e、比例成本 r_e、固定成本 b_e 以及节点需求 d，用关联矩阵 C 建模为 min Σ(r_e f_e + b_e 1{|f_e|>0}) s.t. Cf=d, 0≤f_e≤c_e。方法用 Lasry-Lions 双包络光滑非凸代理替代不连续的固定加线性成本，代理分近零二次区、过渡区与活动区三段，由 λ>μ>0 控制，α=λ/(λ+sλ0) 且 s=10^-2，过渡点 x1、x2 保证连续可微。在 IRLS 框架中，每轮根据当前流量按代理曲率计算边权 W_k，把问题化为加权二次流子问题 min 1/2 f^T W_k f s.t. Cf=d, 0≤f≤c；小流量获得大权重以促其消失，大流量权重较小以集中支持。每个子问题用热启动对偶半光滑牛顿法求解，其牛顿系统具有加权图拉普拉斯结构，可借助现代拉普拉斯求解器；改进版还加入目标驱动扰动重启和 anchor-union 限制搜索，联合 IRLS 与外部 FCNFP 启发式发现的支持并在受限子图上重跑 IRLS。

### 三、结果（Result）
在410个基准、合成与大规模实例上，该方法在所评估的可扩展FCNFP算法中取得最佳目标质量，相对时间受限MILP参考的平均gap为1.316%，在非MILP方法中的胜或平率为90.0%。作为对比，时间受限的OR-Tools MILP基线能求解60节点/400弧实例，但在120节点/1500弧处开始无法证明最优，并在所有1000节点/20000弧实例上均无法证明最优。

### 四、结论（Conclusion）
结果表明，将光滑连续优化与支持级组合搜索结合，是生成大规模FCNFP高质量可行解的有效策略，尤其适用于精确MILP过慢或只能给出次优可行流的场景。该方法本质上是一种原始启发式算法，不尝试证明全局最优性。

### 五、方法论与关键技术细节
关键实现点包括：Lasry-Lions代理的三段权重 w_e 分别为 1/(λ-μ)、(T_e-|f_e|)/(μ|f_e|) 与 r_e/|f_e|+α b_e/|f_e|^2，其中 T_e=λ r_e+sqrt(2λ b_e)，x2 由 S_e=T_e-μ r_e 确定；λ随迭代减小以逐步增强非凸性并逼近原目标，μ受逐边上界约束以保证过渡点实且有序。理论上在受限参数域和精确解析权重下，IRLS更新构成对固定参数代理的majorization-minimization；数值实现会裁剪权重并非精确求解二次规划，因此直接验证代理下降。子问题规模与图拉普拉斯系统相关，借助近线性拉普拉斯求解器提升可扩展性；局限在于非凸性导致无全局最优保证，性能依赖平滑调度、扰动重启质量以及外部启发式提供锚支持的好坏。
