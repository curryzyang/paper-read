# Selected-Risk Calibration for Feasibility at Returned Decisions

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Raghav Thind, Youran Sun, Ling Liang, Haizhao Yang
- 机构：University of Tennessee, Knoxville, University of Maryland, College Park
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10050v1) · [PDF](https://arxiv.org/pdf/2611.10050v1)

## TLDR
The paper proposes Selected-Risk Calibration (SRC), a finite-sample, distribution-free framework that calibrates a learned surrogate constraint against the optimizer’s returned decisions to guarantee that, with high probability, the probability a returned decision violates the true constraint is bounded—addressing the failure of standard conformal random-input coverage to ensure feasibility at selected decisions.

## Abstract
When an optimization problem uses a surrogate constraint, a decision that is feasible for the surrogate need not be feasible for the true constraint. We propose Selected-Risk Calibration (SRC), a framework that calibrates a learned constraint against the optimizer's returned decisions for objectives drawn from a given distribution. SRC guarantees that, with probability at least $1-δ$, every margin it certifies on held-out objectives has selected risk, the probability that the returned decision is infeasible, of at most $γ$. We also show that the random-input coverage guarantee of split conformal prediction does not bound the selected risk, and that likelihood-ratio reweighting for feedback covariate shift does not apply when the learned constraint is active at the returned decision. Our experiments show that a conformal margin covering about $90\%$ of random inputs covered as few as $17\%$ of the returned decisions, and every certified margin had a violation rate below its target on unseen objectives. Moreover, at equal cost, SRC's correction had fewer or equal infeasible solutions to the baselines in 57 of 62 comparisons. The SRC framework applies to any setting in which a surrogate model chooses a decision whose feasibility can be verified for a sample of instances.


## 精读解读（中文）
### 一、研究动机
在约束学习优化中，代理模型约束可行并不代表真实约束可行；优化器会返回在代理可行域边界附近、由目标函数驱动的决策点，而 split conformal 只保证随机输入点的覆盖率，不能约束该返回决策的真实不可行概率。论文因此提出以优化器返回决策为校准对象，直接控制 selected risk，即随机目标下返回决策违反真实约束的概率。

### 二、技术方案（Method）
方法以已训练代理约束 hhat、随机校准样本得到的 conformal 边距 qhat 和可加连续修正 g 为基础，部署可行域为 {x: hhat(x)+qhat+g(x)≤0}；对从目标分布 Q 独立抽取的目标 c 求解 min c(x) 得到返回决策 x*(c)，再用真实约束 oracle 检查 h(x*(c))>0 形成伯努利不可行指标。SRC 对候选边距或修正 g 在这些返回决策上估计 selected risk，并用有限样本置信上界进行认证：仅当上界不超过目标 γ 时认证该边距，多个候选时用联合界控制总体置信度 1-δ；部署时选择已认证的修正或边距，优化流程无需改变化。

### 三、结果（Result）
理论上证明随机输入 conformal 覆盖本身不能界定 selected risk，且当学习约束在返回决策处 active、残差连续时，返回决策分布与校准数据分布对几乎每个校准样本互奇异，因此 feedback covariate shift 的似然比重加权不适用。实验显示覆盖约 90% 随机输入的 conformal 边距在返回决策上覆盖率可低至 17%；所有被 SRC 认证的边距在未见目标上的违约率均低于目标，并且在等成本下 SRC 修正相对基线在 62 次比较中有 57 次不可行解更少或持平。

### 四、结论（Conclusion）
论文表明，OCL 中代理约束的随机点覆盖保证不能直接转化为优化器返回决策的真实可行性保证，必须针对 solver 返回的决策进行校准。SRC 提供了有限样本、分布无关的 selected-risk 控制框架，可后接于常规训练的代理模型，并适用于任何由代理模型选择决策且可离线核验样本可行性的场景。

### 五、方法论与关键技术细节
关键设置包括真实约束 h 只能通过昂贵 oracle 或模拟器离线查询，代理 hhat 用约束数据训练，conformal 校准样本大小为 m、水平为 α，目标从 Q 抽取且给定建模范式后独立于其他随机性，目标风险阈值 γ、置信水平 δ 和可选容差 τ 为超参；SRC 的复杂度主要来自对每个候选修正/边距在 n 个抽样目标上重复求解优化并查询 oracle，若候选多需多重检验或联合界。理论依赖可测选择、有限样本 Bernoulli 风险上界和固定目标分布 Q，实验为三个仿真基准；局限是需可离线核验返回决策、候选修正族和样本量影响认证与计算成本，且理论使用精确最小化器而认证适用于实际 solver 返回解。
