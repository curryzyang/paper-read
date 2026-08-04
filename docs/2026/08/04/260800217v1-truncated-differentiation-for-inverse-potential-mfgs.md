# Truncated Differentiation for Inverse Potential MFGs

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Siting Liu, Yat Tin Chow, Samy Wu Fung
- 机构：Colorado School of Mines, University of California, Riverside
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00217v1) · [PDF](https://arxiv.org/pdf/2608.00217v1)

## TLDR
This paper introduces JFB-r, a truncated, Jacobian-free backpropagation method that differentiates only the final r iterations of a preconditioned PDHG solver for inverse potential mean-field games, and shows—via a metric-resolvent analysis of the PDHG map—that it recovers full-unrolling accuracy at a fraction of the memory and runtime.

## Abstract
We study inverse potential mean-field games (MFGs), in which an unknown spatial inverse-cost (mobility) map is inferred from observed population densities. We solve the forward MFG with a preconditioned primal-dual hybrid gradient (PDHG) method and develop Jacobian-free backpropagation (JFB-$r$), which records only the final $r$ iterations from a detached warm start while retaining the full forward solve. To analyze this truncated differentiation method, we show that the exact-proximal dual-extrapolated PDHG map is a metric resolvent of the maximal monotone KKT operator. This resolvent view shows that JFB-$r$ exactly differentiates a finite-trajectory surrogate and, under a locally fixed active set at an exact equilibrium detach point, converges to the implicit gradient as the tracked depth increases. Across several inverse-MFG settings, numerical experiments show that JFB-r at moderate tracked depths can achieve recovery accuracy comparable to full unrolling while reducing memory and runtime.


## 精读解读（中文）
### 一、研究动机
反演势能平均场博弈中的未知空间逆成本（迁移率）图通常需要对均衡解映射求导。现有方法如伴随灵敏度需要额外大规模线性求解，嵌入KKT会扩大优化系统，完全展开前向求解器反向传播则需存储完整轨迹，内存和计算开销大。因此需要一种既能保留完整前向求解精度又能降低反向存储与运行时的可微求解方案。

### 二、技术方案（Method）
将前向势能MFG离散为凸规划：以密度ρ和通量m为原始变量，加上连续性约束、非负约束及KL终端项，构造拉格朗日鞍点问题。使用带精确Schur预条件子的G-prox预条件原始对偶混合梯度（PDHG）迭代求解，预条件子W=KK^T通过对空间DCT和小时间块特征分解求逆，每格邻近算子用12步阻尼牛顿迭代。在反问题中，用可微参数θ参数化c_θ(s)，以观测密度与模拟密度的平方误差为损失。为求梯度，采用JFB-r：前向仍运行N_itr步PDHG，但在第N_itr-r步分离计算图，只记录并反向传播最后r步迭代，从而得到近似的隐式梯度；理论上该操作等价于对有限轨迹替代目标精确求导。

### 三、结果（Result）
在多个反演势能MFG数值实验中，JFB-r在适中跟踪深度下能达到与完全展开相当的恢复精度，同时显著降低内存和运行时间。具体地，在含噪声且仅部分时间观测密度的情形下，JFB-25相比完全展开将峰值内存降低约3.9倍，运行时间减少约一半，而恢复误差在三种随机种子变化范围内与完全展开持平。

### 四、结论（Conclusion）
截断微分方法JFB-r为反演势能MFG提供了一种高效且可证明的求导方式：它不需要收缩性假设，而是通过将精确邻近PDHG映射视为极大单调KKT算子的度量预解式，说明在局部固定活动集和精确均衡分离点条件下，随跟踪深度增加会趋于隐式梯度。数值上以更小内存和更快速度恢复与完全展开相当的成本图，适合大规模反演问题。

### 五、方法论与关键技术细节
关键点包括：精确邻近双外推PDHG映射T_θ是单位参数度量预解式，因此无需压缩映射条件；JFB-r精确微分有限轨迹替代目标，并在局部固定活动集与精确均衡分离点下与隐式梯度一致；反向存储和计算成本随r而非N_itr增长，但需保留完整前向求解；实现中邻近算子采用12步阻尼牛顿近似；理论结果依赖固定网格上的局部正则性、密度内点假设和活动集局部固定，未声称网格一致或离散到连续极限；参数化为非线性时外目标非凸，灵敏度是局部分支意义上的。
