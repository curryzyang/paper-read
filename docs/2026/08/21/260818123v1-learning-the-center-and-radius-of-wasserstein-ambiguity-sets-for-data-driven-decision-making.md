# Learning the Center and Radius of Wasserstein Ambiguity Sets for Data-Driven Decision Making

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Junjie Guo
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18123v1) · [PDF](https://arxiv.org/pdf/2608.18123v1)

## TLDR
This paper develops a flexible Wasserstein distributionally robust optimization framework where both the ambiguity set's center (from a predictive model) and its radius (via a learned, data-dependent rule) are calibrated to contain the true distribution with finite-sample guarantees, showing that such learned and calibrated sets improve reliability but do not universally yield smaller radii or better decisions.

## Abstract
Wasserstein distributionally robust optimization (DRO) is commonly built around the empirical distribution, with the ambiguity radius selected from a concentration bound. Although this construction provides useful statistical guarantees, it can be conservative and does not fully exploit predictive information about the underlying distribution or the difficulty of a particular decision problem. We develop a more flexible framework in which a predictive model determines the nominal distribution and a separate model estimates a data-dependent radius. The key requirement is not that the ambiguity set be centered at the empirical distribution, but that it contain the unknown data-generating distribution with the desired probability. We establish finite-sample guarantees and asymptotic consistency for arbitrary learned centers, derive tractable reformulations for non-uniform discrete predictive distributions, separate predictive-model and scenario-discretization errors, and prove stability under simultaneous perturbations of the center and radius. We further characterize the oracle conditional-quantile radius as the smallest conditionally valid rule and introduce a split-conformal procedure for finite-sample marginal calibration. Experiments on newsvendor problems, synthetic portfolios, distribution shifts, and real financial data show that learned and calibrated ambiguity sets can improve reliability, but do not automatically yield smaller radii or better decisions. Overall, the proposed framework treats calibration as a practical mechanism for reliable decision making rather than a universal guarantee of improved optimization performance.


## 精读解读（中文）
### 一、研究动机
传统Wasserstein分布式鲁棒优化通常以经验分布为模糊集中心，并依据集中不等式选取固定半径；这种做法虽有统计保证，但偏保守，且没有充分利用关于真实分布的预测信息或具体决策问题的难度。本文提出更灵活的框架：由预测模型决定名义分布，由另一个模型估计数据依赖的半径，核心要求不是让模糊集以经验分布为中心，而是让随机模糊集以期望概率包含未知数据生成分布。

### 二、技术方案（Method）
整体流程为：输入历史观测和可用的协变量，先由预测模型生成名义分布，并将其离散化为带非均匀权重的场景分布；再由半径模型基于样本量、维度、预测诊断、波动率或不确定性估计等特征预测数据依赖半径。理论上对一般非均匀离散名义分布推导了Wasserstein模糊集的最坏情形期望对偶形式和有限凸重构；将预测模型误差与场景离散化误差分离并证明二者在半径上相加，同时建立中心和半径同时扰动下鲁棒值的联合稳定性。校准采用分裂保形（split-conformal）程序获得有限样本边际覆盖。实验涵盖新闻vendor问题、合成组合、分布偏移和真实金融数据，采用无泄漏的嵌套拟合-校准-测试流程、配对推断、分布偏移压力测试和交易成本设置。

### 三、结果（Result）
理论结果建立了任意学习中心下的有限样本有效性和渐近一致性；证明oracle条件分位数半径是逐点最小的条件有效半径规则，并给出有限样本边际校准的分裂保形程序。实验表明，学习并校准的模糊集可以提高可靠性，但不会自动产生更小的半径或更好的决策；在受控设置下校准可靠，但没有一致的半径效率或决策价值优势。

### 四、结论（Conclusion）
本文强调覆盖原则本身是一种实用的可靠决策机制，而非提升优化性能的普遍保证。只要随机模糊集能以目标概率覆盖真实分布，经验分布并非逻辑必需；学习中心和半径可以在不依赖经验中心的情况下提供可靠性，但对实际决策收益需谨慎评估。

### 五、方法论与关键技术细节
关键细节包括：光尾假设A=E[exp(||ξ||^a)]<∞用于集中不等式；任意学习中心需要满足覆盖条件而非固定为经验分布；非均匀离散预测分布需重新推导对偶和凸重构；误差分解为预测模型误差与场景离散化误差之和；条件分位数半径是最小条件有效规则，近似半径预测器需加入安全余量；分裂保形校准依赖可交换性，滚动金融实验中不能朴素随机划分否则会泄漏；区分了通用分布覆盖与任务特定证书覆盖，并给出高概率和期望遗憾保证。局限性在于学习与校准不保证半径更小或决策更优，且高维场景下集中不等式半径可能偏保守。
