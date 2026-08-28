# Muon with Finite Newton-Schulz: The Smoothing Benefit in Nonsmooth Nonconvex Optimization

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Mingyi Li, Taira Tsuchiya
- 机构：The University of Tokyo, RIKEN
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26288v1) · [PDF](https://arxiv.org/pdf/2608.26288v1)

## TLDR
Finite Newton–Schulz iterations in Muon smooth the discontinuous polar map into a Lipschitz spectral map, making the optimizer converge to stationary points in nonsmooth nonconvex optimization with only logarithmically growing iteration depth, whereas exact-polar Muon can fail.

## Abstract
Muon has emerged as a strong optimizer for the matrix-valued parameters in large language model pretraining, approximately orthogonalizing its momentum with a few Newton-Schulz iterations. Existing theory either replaces this iteration with the exact polar factor it approximates, or treats its finite depth as an approximation error, and thus the iteration Muon actually runs can only hurt the guarantees. We show that finite Newton-Schulz can instead be beneficial for nonsmooth nonconvex optimization. To this end, we analyze Muon through the online-to-nonconvex conversion, which views the update rule as an online learner and converts its regret bound into a stationarity guarantee. The finite Newton-Schulz iteration smooths the discontinuous polar map into a Lipschitz map of the singular values, and Muon with finite Newton-Schulz can be regarded as an online learner with a smoothed spectral potential. This smoothing is exactly what the conversion needs: we prove that a Newton-Schulz depth growing only logarithmically in the target accuracy suffices for convergence to stationary points in nonsmooth nonconvex optimization, whereas Muon with the exact-polar update may fail to converge. The resulting sample complexity bounds match the best-known guarantees for nonsmooth nonconvex optimization and are optimal for smooth nonconvex optimization up to problem-dependent factors. The argument extends beyond Newton-Schulz to general spectral maps with the same smoothing property.


## 精读解读（中文）
### 一、研究动机
Muon优化器在大语言模型预训练中表现优异，其核心是用有限次Newton-Schulz迭代近似极分解（polar factor）来正交化动量。然而现有理论要么用精确极分解替代该迭代，要么将有限深度视为近似误差，导致实际运行的有限Newton-Schulz只会损害理论保证。同时，非光滑非凸优化场景下，精确极分解的Muon可能无法收敛。本文旨在回答：有限Newton-Schulz迭代能否本身成为有益机制，使得带动量的Muon在非光滑非凸目标上找到稳定点。

### 二、技术方案（Method）
采用online-to-nonconvex conversion（O2NC）框架，将Muon的更新规则视为在线学习器，并将其遗憾界转化为驻点性保证。具体地，将有限Newton-Schulz迭代视为对不连续极分解映射的光滑化，诱导出关于奇异值的Lipschitz谱映射，从而将Muon解释为具有光滑谱势的在线梯度预测算法。该学习器等价于在折扣线性损失上的follow-the-regularized-leader（FTRL），其正则化器是光滑势的Fenchel共轭。分析中，用动量而非累积梯度来分解折扣遗憾为惩罚项和稳定性项，惩罚项随势接近核范数而减小，稳定性项随谱映射Lipschitz常数增大而增大。有限Newton-Schulz深度q控制两者权衡：惩罚项和稳定性项均以q的几何速率变化，平衡后得到q=O(log(1/ε))时的次线性折扣遗憾，再经O2NC转换为样本复杂度保证。

### 三、结果（Result）
证明了带动量且每轮执行q=O(log(1/ε))步Newton-Schulz的Muon，在期望内经过O(ρ^{-1}ε^{-3}+ε^{-2})次随机梯度评估即可找到(ρ,ε)-稳定点，该复杂度与非光滑非凸优化的最佳已知保证匹配，且在光滑非凸优化中达到问题相关因子意义下的最优。相比之下，使用精确极分解更新的Muon可能无法收敛。这是首个在非光滑非凸优化中有限Newton-Schulz作为平滑机制而非近似误差来保证收敛的理论结果。

### 四、结论（Conclusion）
有限Newton-Schulz迭代不是精确极分解的单纯近似误差，而是一种有益的平滑机制：它用Lipschitz谱映射替代不连续的极分解，使得O2NC框架能够提供非光滑非凸优化的驻点收敛保证。所需Newton-Schulz深度仅随目标精度对数增长，与实际中少量迭代即可工作的经验观察一致。该论证超越了Newton-Schulz，适用于具有相同平滑性质的一般谱映射，为设计其他正交化变体提供了理论依据。

### 五、方法论与关键技术细节
关键点包括：1）数据与输入：随机梯度不可靠（有偏噪声）的Lipschitz非光滑非凸目标，矩阵参数形状为R^{m×n}（m≤n），每次迭代维护动量的指数移动平均M。2）建模：有限Newton-Schulz将极分解映射平滑为奇异值的Lipschitz映射，光滑势的梯度恰好是Muon更新方向；q=0时正则化器为算子范数球上的平方Frobenius正则化，q→∞时正则化衰减为零并退化为follow-the-leader。3）关键操作：每轮计算动量M的SVD（理论分析用），应用q步Newton-Schulz多项式迭代得到近似正交化方向，再乘以学习率更新参数。4）复杂度与约束：q只需O(log(1/ε))，样本复杂度为O(ρ^{-1}ε^{-3}+ε^{-2})；精确极分解对应的稳定性项无界，导致线性遗憾和无法收敛。5）局限性：分析的Muon变体与实际部署版本仍有差异，论文在结论部分具体说明；对于其他谱映射（如softsign等平滑松弛）也适用但需满足一定条件。
