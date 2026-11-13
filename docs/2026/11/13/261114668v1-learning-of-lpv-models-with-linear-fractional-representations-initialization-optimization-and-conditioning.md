# Learning of LPV Models With Linear Fractional Representations: Initialization, Optimization, and Conditioning

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Roel Drenth, Maarten Schoukens, Roland Tóth
- 机构：HUN-REN Institute for Computer Science and Control, Eindhoven University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14668v1) · [PDF](https://arxiv.org/pdf/2611.14668v1)

## TLDR
This paper improves the reliability of learning LPV-LFR models by proposing a Best Linear Approximator (BLA)-based initialization and comparing unconstrained and encoder-based multiple shooting methods to mitigate ill-conditioning in the non-convex identification problem.

## Abstract
Linear Parameter-Varying (LPV) models with Linear Fractional Representation (LFR) can describe a wide class of nonlinear systems with a control-friendly structure. However, identifying these models together with their scheduling map from input-output data requires solving a non-convex optimization problem that is highly sensitive to initialization. Consequently, existing methods often rely on many random initializations. Instead, our work proposes an initialization strategy based on the Best Linear Approximator (BLA). Furthermore, motivated by an analysis of the impact of rational-dependency LPV-LFR models on the conditioning of the non-convex cost, two multiple shooting methods that improve the conditioning, unconstrained multiple shooting (UMS) and encoder-based multiple shooting (EBMS), are compared. The initialization and multiple shooting methods are evaluated on a nonlinear mass-spring-damper example, showing that BLA initialization consistently yields accurate results, whereas random initialization has a large spread. The results also show that both UMS and EBMS reduce the spread for randomly initialized models. UMS is simple to tune and well suited to few sub-records, whereas EBMS can exploit many short sub-records to further improve conditioning, at the cost of training an encoder and tuning additional hyperparameters.


## 精读解读（中文）
### 一、研究动机
LPV-LFR模型能以控制友好的结构描述广泛非线性系统，但联合辨识模型与调度映射需解强非凸优化问题，对初始化高度敏感，现有方法常依赖大量随机初始化。尤其有理依赖LPV-LFR会恶化代价函数条件数，而BLA初始化及多 shooting 方法在该模型类中的可靠性和复杂度权衡尚缺乏系统分析。

### 二、技术方案（Method）
论文考虑离散非线性状态空间数据生成系统，在输出加性白噪声和准平稳输入假设下，联合估计ResNet神经网络调度映射与LPV-LFR状态空间模型，采用预测误差/仿真误差最小化并用以Dzw=e^{-Psi S}构造的适定有理参数化保证LFR良定。方法上先用最佳线性近似BLA给出模型初值，再优化非凸代价；同时比较无约束多shooting UMS（将各子记录初态作为无约束可学习变量）与基于编码器的EBMS（用编码器从输入输出历史估计子记录初态，从而支持重叠子记录和小批量训练），并在非线性质量-弹簧-阻尼仿真算例上评估初始化与shooting策略。

### 三、结果（Result）
理论分析表明，有理调度依赖会通过LFR增益放大状态转移函数的Lipschitz常数，而仿真误差代价的Lipschitz常数随仿真长度T可能呈O(L_f^{2T})增长，因此限制递归深度可改善条件数。算例结果显示，BLA初始化稳定获得准确结果，而随机初始化结果散布很大；UMS和EBMS均能降低随机初始化模型的性能散布。UMS调参简单、适合少量子记录，EBMS可利用大量短子记录进一步改善条件数，但需训练编码器并调节额外超参数。

### 四、结论（Conclusion）
对LPV-LFR模型与调度映射的联合学习，BLA初始化可作为提高可复现性和降低随机重启依赖的默认策略；当仍存在病态条件时，应结合多shooting方法。实际选择上，数据较少或子记录数少时优先UMS，数据充足且可接受额外编码器训练与调参成本时可用EBMS以获得更好的条件数和小批量利用能力。

### 五、方法论与关键技术细节
关键实现包括离散时间非线性状态空间数据、准平稳输入和输出白噪声假设，调度映射采用带线性旁路的ResNet结构，LFR调度矩阵Delta(p)为分块对角且||p||∞≤1，适定参数化中Dzw=e^{-Psi S}、Psi=diag(e^{D_d})、S=D_A^T D_A+D_B-D_B^T+epsilon_S I。理论部分依赖有界状态输入、紧参数集及存在与Delta交换的W满足||W^{-1}DzwW||≤1-epsilon和条件数上界kappa_W，用于界定LFR有理增益gamma=kappa_W/epsilon并推导L_f各分量；分析为简化采用外部调度情形，自调度下p依赖x预计会更恶化条件。UMS的初态参数数随子记录数线性增长，EBMS需选择编码器维度、历史窗口长度等超参数并可能需较多短子记录，二者均避免约束优化器但存在复杂度与调参负担的取舍。
