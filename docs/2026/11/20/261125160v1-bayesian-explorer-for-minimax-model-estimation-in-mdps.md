# Bayesian $κ$-Explorer for Minimax Model Estimation in MDPs

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Xihe Gu, Urbashi Mitra, Tara Javidi
- 机构：University of Southern California, University of California, San Diego
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25160v1) · [PDF](https://arxiv.org/pdf/2611.25160v1)

## TLDR
**TLDR:** The paper introduces Bayesian κ-Explorer, a simplified posterior-variance-driven active exploration algorithm for minimax transition estimation in MDPs that uses Dirichlet priors and posterior-mean planning to eliminate confidence-set optimization while retaining the frequentist κ-Explorer’s convergence rate and improving worst-case estimation error.

## Abstract
We study active exploration for minimax transition estimation in unknown Markov decision processes (MDPs). Frequentist $κ$-Explorer~\citep{gu2026kappa} addresses this problem through a parameterized family of exploration objectives, but requires confidence-bound constructions and joint optimization over plausible transition kernels and occupancy measures, introducing a computational burden that limits its practical applicability. We develop Bayesian $κ$-Explorer, which simplifies this procedure by placing Dirichlet priors on the transition distributions. Under the posterior mean estimator, the posterior expected squared $\ell_2$ error equals the total posterior variance, providing a closed-form exploration signal. The algorithm plans under the posterior mean model, eliminating confidence-set optimization. Under the stated assumptions, this simpler planning procedure retains the $\widetilde{O}(T^{-1/3})$ surrogate convergence rate of frequentist $κ$-Explorer. We further bound the maximum posterior variance relative to the optimal asymptotic minimax allocation benchmark. Experiments on Pendulum, Mountain Car, and Taxi demonstrate lower worst-case transition-estimation errors than the tested baselines.


## 精读解读（中文）
### 一、研究动机
未知MDP中的极小极大转移估计需要在有限交互预算下最小化所有状态-动作对上最坏的转移估计误差，但访问频率通过动力学耦合且目标非光滑。此前的频率派κ-Explorer虽通过参数化探索目标逼近该问题，却需要构造置信界并在可行转移核与占用测度上联合优化，计算负担较大。本文旨在保留其核心探索原则与收敛保证的同时，给出更易实现的后验方差驱动方案。

### 二、技术方案（Method）
作者在每条转移分布上放置独立Dirichlet先验，利用共轭性得到后验均值μ_t与后验集中度β_t，并采用后验均值作为转移核估计。后验期望平方ℓ2误差等于总后验方差，具有闭式V_t(s,a)=c_t(s,a)/(β_t(s,a)+1)，其中c_t由后验均值直接计算，形成无需额外置信界的探索信号。算法按回合运行：每回合用当前计数计算V_t，设探索奖励r_m(s,a)=V_t(s,a)^κ（κ≥1），在后验均值模型的带占用下限η的稳态占用域内求解最大化Σr_m d的占用测度并导出策略π_m，执行τ_m步后更新计数，最终返回后验均值μ_T。

### 三、结果（Result）
理论分析表明，在通信性与稳定性等假设下，该简化规划流程仍保留频率派κ-Explorer的Õ(T^{-1/3})替代目标收敛率，并给出最大后验方差M_T相对于最优渐近极小极大分配基准C*/T的显式上界。界中包含有限κ近似项、分配优化项与后验估计项，其中分配优化误差为Õ(T^{-1/3})，对后验方差的贡献为Õ(T^{-4/3})，后验估计项在访问下限下为Õ(T^{-3/2})。在Pendulum、Mountain Car和Taxi的离散表格实验中，该方法相比所测基线取得更低的最坏情形转移估计误差。

### 四、结论（Conclusion）
Bayesian κ-Explorer用Dirichlet后验方差替代频率派置信集构造，将联合优化转移核与占用测度简化为在后验均值模型下的单模型规划，同时保持可证明的收敛率与极小极大分配基准 bound。该工作给出了首个结合后验均值规划与最大后验期望平方转移估计误差定量保证的后验方差驱动探索算法，并在基准环境中验证了实用有效性。

### 五、方法论与关键技术细节
关键实现包括独立Dirichlet先验（如Jeffreys先验）、后验均值MMSE估计、由c_t与β_t构成的闭式后验方差，以及κ≥1的幂次探索奖励和η∈(0,1/(2SA))的占用下限；规划需在每个回合求解带稳态占用约束的线性目标，并按预设回合长度执行。理论依赖通信MDP与稳定性假设、足够大的T阈值和适当选择η与τ_m，保证以至少1-δ概率成立；局限在于主要针对有限表格MDP，实验为离散化环境，且性能受先验、κ、η和回合调度影响。
