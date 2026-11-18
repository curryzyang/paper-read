# Primal--Dual Kullback--Leibler Mirror-Prox for Dynamic Mean Field Games

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Erhan Bayraktar, Ibrahim Ekren, Lu Vy, Ziqing Zhang
- 机构：Princeton University, University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21837v1) · [PDF](https://arxiv.org/pdf/2611.21837v1)

## TLDR
The paper proposes a primal–dual Kullback–Leibler Mirror-Prox algorithm for finite-horizon dynamic mean field games that alternates exponential tilting of occupation measures with linear PDE dual corrections—avoiding nonlinear Hamilton–Jacobi–Bellman solves—and proves convergence rates plus discretization and approximation guarantees.

## Abstract
We compute finite-horizon dynamic mean field equilibria using a primal--dual Kullback--Leibler Mirror-Prox algorithm. Each iteration updates occupation measures by exponential tilting and computes the dual correction by solving a linear PDE, without solving a nonlinear Hamilton--Jacobi--Bellman equation or a best-response control problem. Under assumptions and Lasry--Lions monotonicity, we prove an $O(K^{-1})$ ergodic Minty bound after $K$ iterations and an $O(K^{-1/2})$ approximate-equilibrium bound for the corrected average. We obtain convergence rates for the population flow under strong monotonicity, and for smooth diffusions with uniformly convex control costs under ordinary monotonicity. We also prove convergence of continuous-time Markov chain approximations to diffusion equilibria and, under additional smoothness and convexity assumptions, bound the error in terms of the spatial mesh size and the number of iterations. Galerkin approximations preserve the $O(K^{-1})$ estimates under suitable bounds on the correction errors. Numerical experiments illustrate the method and its convergence.


## 精读解读（中文）
### 一、研究动机
动态平均场博弈（MFG）的均衡计算通常需要求解耦合的非线性 Hamilton–Jacobi–Bellman（HJB）方程与 Fokker–Planck 方程，或通过反向动态规划反复求解最佳响应控制问题，计算代价高且对连续状态空间不友好。本文希望借助占据测度线性规划与原始–对偶变分不等式表述，设计一种每次迭代只需指数倾斜和线性 PDE 求解的算法，从而避免处理 HJB 非线性，并适用于无势结构的 Lasry–Lions 单调博弈。

### 二、技术方案（Method）
将有限时域动态 MFE 写成乘积空间 Π×H^1(0,T;H) 上的原始–对偶变分不等式：原始变量为占据测度 π=(ν,(π_t))，经边缘映射 M 得到种群流 μ_t；对偶变量为代表 agent 的候选值函数 u，算子 F(π,u)=(C_{Mπ}-A^*u, Aπ-ρ)，其中第一块为终端与运行 HJB 残差，第二块为前向 Fokker–Planck 方程的弱形式残差。算法采用 KL Mirror-Prox：每个原始半步按当前 HJB 残差对 ν 和每个 π_t 做指数倾斜（相对熵近端步）；每个对偶半步加上 -τR(Aπ-ρ)，R 为 H^1(0,T;H) 的 Riesz 映射，该修正等价于求解以前向方程残差为源、以初末失配为边界数据的线性两点边值问题，并有显式公式（时间积分加一次 H 的 Riesz 映射）。实现上给出两种路线：在空间网格上用连续时间 Markov 链替换扩散，或在连续状态空间直接使用扩散生成元并用函数基/Galerkin 或二次能量最小化近似对偶修正；积分用求积或 Monte Carlo 计算。

### 三、结果（Result）
在给定假设与 Lasry–Lions 单调性下，证明 K 次迭代后遍历 Minty 界为 O(K^{-1})，对可行比较点给出 O(K^{-1}) 的前向方程残差界，对校正后的平均占据测度给出 O(K^{-1/2}) 的近似均衡界；强单调性下得到平均种群流以 L^2-in-time Wasserstein 距离 O(K^{-1/2}) 收敛到唯一均衡流；在普通单调性加光滑扩散与一致凸控制代价假设下得到 Wasserstein 收敛速率。还证明连续时间 Markov 链近似收敛到扩散均衡，并在额外光滑与凸性假设下给出以空间网格 h=1/N 和迭代数 K 表示的误差界：取 K≥N 时种群与占据测度误差为 O(h^{1/6})=O(N^{-1/6})；Galerkin 近似在修正误差可控时保持 O(K^{-1}) 估计。数值实验显示有限状态拥堵博弈中前向残差、修正误差与 Stampacchia 间隙均以约 K^{-1} 衰减，网格扩散实验步长与网格无关。

### 四、结论（Conclusion）
该工作给出了一种无需在每次迭代中求解非线性 HJB 方程或最佳响应控制问题的动态 MFE 原始–对偶 KL Mirror-Prox 算法，将均衡计算化为指数倾斜与线性边值问题求解的交替，并在 Lasry–Lions 单调框架下建立了遍历 Minty 界、前向残差界、近似均衡保证及种群流收敛速率；网格与 Galerkin 实现的理论与数值结果支持该方法的可扩展性，使其适用于无势结构的一般单调平均场博弈。

### 五、方法论与关键技术细节
原始–对偶结构依赖占据测度约束 Aπ=ρ 与 HJB 残差 C_{Mπ}-A^*u；对偶空间选为 H^1(0,T;H)，对偶步的 Riesz 映射在有限状态空间为恒等、环面 Sobolev 空间为 (I-Δ)^{-m}、RKHS 中为对核积分。步长 τ 与相对熵强凸常数 λ 出现在 Minty 比较项 (D(π'||π_0)/λ+||u'-u_0||^2/(2τ))/K 中。关键实现约束是遍历平均未必可行，需用校正映射 proj_ρ 将其分解为流与松弛反馈并求解前向方程恢复可行性；若修正大小被前向残差常数倍控制且可行集有统一熵界，则校正平均的 Minty 间隙为 O(K^{-1})、Stampacchia 间隙为 O(K^{-1/2})。对偶可达性要求最优乘子属于 H^1(0,T;H)，强于可测对偶可达性；扩散结果依赖各定理附带的正则性与近似假设，网格误差界需 H^3 型 Sobolev 假设与凸控制代价，且可求和的对偶修正误差才能保持 O(K^{-1}) 遍历估计。
