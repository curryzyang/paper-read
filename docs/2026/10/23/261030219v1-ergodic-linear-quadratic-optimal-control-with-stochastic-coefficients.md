# Ergodic Linear-Quadratic Optimal Control with Stochastic Coefficients

- 区域：精读区
- 排名：2
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Xuyang Lin, Nizar Touzi
- 机构：New York University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30219v1) · [PDF](https://arxiv.org/pdf/2610.30219v1)

## TLDR
The paper introduces a stochastic ergodic Hamilton–Jacobi–Bellman framework for linear–quadratic optimal control with stochastic coefficients, in which a random process replaces the classical ergodic constant and characterizes optimal ergodic costs across general averaging kernels, including random-periodic and perturbed settings.

## Abstract
We investigate ergodic linear-quadratic optimal control problems with stochastic coefficients and introduce the associated stochastic ergodic Hamilton-Jacobi-Bellman (HJB) equation, in which the classical ergodic constant is replaced by a random process $λ$. We establish well-posedness of the equation and show that $λ$ characterizes the optimal ergodic costs for a general class of averaging kernels, including those corresponding to normalized finite-horizon and discounted costs. For random-periodic coefficients, we construct a random-periodic solution and show that the optimal ergodic costs associated with all admissible averaging kernels coincide. We also establish stability of the optimal ergodic costs under perturbations of the coefficients.


## 精读解读（中文）
### 一、研究动机
随机系数线性二次控制是经典且可处理的控制问题，但无限时域与遍历准则在系数随机时缺乏统一刻画，已有工作常限制漂移项或只能处理先折扣后取极限的次序。本文旨在为一般随机系数、含非零漂移项的遍历LQ问题建立随机遍历HJB方程，并用随机过程替代经典常数遍历成本，以统一覆盖归一化有限时域与折扣型平均核。

### 二、技术方案（Method）
考虑带随机有界系数A、B、C、D、f、g和半正定状态成本S的受控线性随机微分方程，控制属于H^2_∞，运行成本为S_t x·x+|u|^2；引入随机遍历HJB方程λ_t=inf_u{ℓ_t(x,u)+L_t^u V_t(x)}，其中V为半鞅随机场、λ为实值随机过程。技术路线是研究无限时域后向随机Riccati方程及对偶BSDE，在已有Riccati存在性基础上把对偶方程存在性推广到有界f、g，并证明唯一性与一致估计；引入 uniformly local conditional 空间L^p_unif及范数sup_t ||E[∫_t^{t+1}|Y_s|^p ds|F_t]||_∞^{1/p}，证明Riccati解Q、k属于L^2_unif、λ属于L^1_unif。随后通过验证定理处理一般平均核K_ρ(t)=ρK(ρt)，其中K非负、非增、右连左极且积分为1，并构造最优仿射反馈控制；对随机周期系数构造随机周期解，并分析系数扰动下的稳定性。

### 三、结果（Result）
建立了随机遍历HJB方程的适定性和验证定理，并证明λ刻画了一般平均核下的最优遍历成本：liminf_{ρ↓0} inf_ν J^{K_ρ}=inf_ν liminf_{ρ↓0} J^{K_ρ}=liminf_{ρ↓0} E∫_0^∞ K_ρ(t)λ_t dt，limsup情形亦有对应等式。该框架统一覆盖K=1_[0,1)的归一化有限时域平均和K=e^{-t}的折扣成本，并在折扣情形下得到inf与liminf可交换的等式。对于随机周期系数，构造随机周期解并证明所有容许平均核对应的最优遍历成本相同；同时给出Riccati解、对偶解及最优遍历成本在系数扰动下的稳定性。

### 四、结论（Conclusion）
本文把经典遍历HJB中的常数λ推广为随机过程，为随机系数遍历LQ控制提供了统一的理论框架，涵盖一般平均核、验证原理、最优仿射反馈、随机周期情形和系数扰动稳定性。结果弥补了以往在对偶方程存在性、非零g以及inf与liminf次序等方面的限制。论文属于理论分析工作，未报告数值实验或实际数据应用。

### 五、方法论与关键技术细节
关键假设包括系数A、B、C、D、f、g和S有界，S取值于半正定矩阵锥，控制成本对u为|u|^2；平均核K需非负、非增、右连左极且∫K=1，K_ρ(t)=ρK(ρt)。方法核心是无限时域后向随机Riccati方程与对偶BSDE、Itô-Wentzell算子、L^p_unif一致局部条件空间、唯一性和一致估计，以及验证与局部化论证；得到Q、k∈L^2_unif和λ∈L^1_unif。局限在于结果依赖有界系数与二次LQ结构，稳定性主要为理论刻画，未给出数值算例或定量收敛率。
