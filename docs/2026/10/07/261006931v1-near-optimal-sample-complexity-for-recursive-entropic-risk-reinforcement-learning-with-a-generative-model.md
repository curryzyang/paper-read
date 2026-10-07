# Near-Optimal Sample Complexity for Recursive Entropic Risk Reinforcement Learning with a Generative Model

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Amirparsa Bahrami, Oliver Mortensen, Mohammad Sadegh Talebi
- 机构：University of Copenhagen, Sharif University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06931v1) · [PDF](https://arxiv.org/pdf/2610.06931v1)

## TLDR
This paper provides refined \((\varepsilon,\delta)\)-PAC sample complexity bounds for model-based risk-sensitive Q-value iteration in finite discounted MDPs under recursive entropic risk, showing near-optimal value and policy learning guarantees that eliminate the previous exponential gap in the effective horizon and match existing lower bounds up to logarithmic factors.

## Abstract
In this paper, we study the sample complexities of value and policy learning in finite discounted Markov decision processes (MDPs) under recursive entropic risk preferences with risk parameter \(β\neq 0\), assuming access to a generative model of the MDP. We provide a refined analysis of model-based risk-sensitive Q-value iteration (MB-RS-QVI), a plug-in model-based method introduced in prior work, and derive \((\varepsilon,δ)\)-PAC guarantees for both learning the optimal \(Q\)-value function and an \(\varepsilon\)-optimal policy. Our bounds improve the exponential dependence on the effective horizon \(1/(1-γ)\) compared with the best existing guarantees for this setting. In particular, they match the existing lower bounds in their exponential dependence on \(|β|/(1-γ)\), as well as in \(S\), \(A\), \(\varepsilon\), and \(|β|\), up to logarithmic factors. Consequently, our analysis removes the exponential gap between the previously known upper and lower bounds, leaving only a polynomial gap in the effective horizon.


## 精读解读（中文）
### 一、研究动机
传统强化学习多面向风险中性期望回报，难以适用于医疗、交通、运筹等高风险场景；递归熵风险（ERM）可对每一步的回报风险建模，但已有生成模型下MB-RS-QVI的样本复杂度上界与下界在有效时域1/(1-γ)上存在指数差距。本文旨在给出更精细的分析，缩小该差距。

### 二、技术方案（Method）
研究有限折扣MDP，状态数为S、动作数为A、折扣因子为γ，风险参数β≠0，目标为递归熵风险准则；假设可访问生成模型，可对任意状态-动作采样。方法为基于模型的插件式风险敏感Q值迭代MB-RS-QVI：先对每个状态-动作采样估计经验转移与奖励，构造经验MDP，再在经验模型上执行递归ERM的Bellman算子或对数指数变换后的Q值迭代至收敛，最后输出最优Q值估计和贪心策略；理论分析结合集中不等式与风险敏感算子的收缩性质导出(ε,δ)-PAC保证。

### 三、结果（Result）
论文证明值学习样本复杂度为 tilde O(SA/(ε^2(1-γ)^2|β|^2)·e^{|β|/(1-γ)})，策略学习为 tilde O(SA/(ε^2(1-γ)^2|β|^2)·min{S,1/(1-γ)^2}·e^{|β|/(1-γ)})，且ε覆盖(0,1/(1-γ)]。相比先前上界的e^{2|β|/(1-γ)}，新界将指数项降为e^{|β|/(1-γ)}，在|β|/(1-γ)、S、A、ε、|β|上与现有下界匹配至对数因子，从而消除指数级上下界差距，仅保留有效时域上的多项式差距。

### 四、结论（Conclusion）
MB-RS-QVI在生成模型下对递归熵风险折扣MDP达到近乎最优的样本复杂度，说明插件式模型方法可有效处理风险敏感RL中的值学习和策略学习问题。该结果显著收紧了理论保证，并为后续研究更紧的策略学习界和进一步消除1/(1-γ)多项式差距提供了基础。

### 五、方法论与关键技术细节
关键设定是递归熵风险而非静态风险，β>0对应风险规避、β<0对应风险寻求，β→0退化为风险中性。算法核心是对经验MDP做风险敏感Q值迭代，分析难点在于指数效用与对数指数算子带来指数集中项，因此样本复杂度必然含有e^{|β|/(1-γ)}因子。上界仍含(1-γ)^-2以及策略学习中的min{S,1/(1-γ)^2}因子，与下界尚有有效时域多项式差距；结论限于表格有限折扣MDP和可任意状态-动作采样的生成模型，不直接覆盖在线、离线或函数逼近情形。
