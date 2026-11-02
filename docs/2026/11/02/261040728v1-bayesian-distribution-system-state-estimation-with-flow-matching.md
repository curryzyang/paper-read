# Bayesian Distribution System State Estimation with Flow Matching

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Nan Lin, Peter Palensky, Pedro Vergara Barrios
- 机构：Delft University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40728v1) · [PDF](https://arxiv.org/pdf/2610.40728v1)

## TLDR
PoSE is a Bayesian distribution system state estimation method that learns a flow-matching prior over substation injections and combines it at sampling with a noise-aware AC power-flow correction to produce calibrated, physically consistent posterior samples, improving accuracy and uncertainty while avoiding retraining across measurement sets, noise levels, and topologies.

## Abstract
Medium-voltage feeders have few real-time measurements, so distribution system state estimation (DSSE) rests on pseudo-measurements of the secondary substations, a prior in Bayesian terms. Weighted least squares keeps the power flow exact but reduces this prior to a mean and variance, while supervised deep learning estimators also learn the power flow and are tied to one measurement set. We propose PoSE (posterior sampling for state estimation), which keeps the Bayesian structure of DSSE and learns only what the distribution system operator does not know, namely the distribution of substation injections, modelled by a neural network trained with flow matching on historical data. The power flow equations, grid topology and measurements enter only at sampling, through a noise-aware Kalman-type correction. The neural network therefore never approximates the power flow, but every posterior sample is a physically consistent operating point, and one trained prior serves any measurement set, noise level and topology. On the IEEE 33-bus feeder, PoSE lowers the probabilistic injection error (CRPS) by 6.7-7.5% against a full-covariance Gaussian prior in all 12 tested settings. It provides reliable uncertainty: the 90% intervals contain the true injection almost exactly as often as exact posterior samples would, whereas those of supervised estimators contain it in only 37-78% of cases. On the 240-bus unbalanced three-phase Iowa feeder, it gives the lowest injection, voltage and branch-current errors of all estimators. A fast variant matches this accuracy at 0.2-0.6s per snapshot and, without retraining, beats Gaussian priors and retrained supervised estimators on seven reconfigured topologies.


## 精读解读（中文）
### 一、研究动机
中压配电网实时量测稀少，配电系统状态估计主要依赖二次变电站注入的伪量测，也就是贝叶斯框架中的先验；但加权最小二乘把这一先验简化为均值与方差，监督式深度学习又绑定单一量测配置且需近似潮流。作者希望同时保留贝叶斯结构、AC潮流一致性和校准不确定性，并让一个先验可服务任意量测集、噪声水平和拓扑。

### 二、技术方案（Method）
PoSE先用历史二次变电站注入数据训练条件流动匹配先验：对注入按节点标准化，在线性路径上回归速度场，网络为带自适应层归一化的残差MLP，月份、时刻用傅里叶特征、日类型用嵌入表示；该先验不包含传感器、噪声或电网模型。推理时从先验采样，并在每个Euler步用Kalman型端点校正把样本拉向量测：残差始终通过AC潮流h计算，校正矩阵H取LinDistFlow线性化，噪声协方差用R_eff=R+Σ_lin吸收线性化误差；三相不平衡网络通过固定的不平衡LinDistFlow线性算子和相别功率分配进入校正，无需重训先验。最终每个后验样本再经AC潮流映射为物理一致运行点；PoSE-fast仅沿量测方向构造端点协方差，使计算量随量测数而非状态维数增长。

### 三、结果（Result）
在IEEE 33节点馈线上，PoSE在全部12种测试设置中把注入概率误差CRPS相对全协方差高斯先验降低6.7%–7.5%；其90%区间对真实注入的覆盖率接近精确后验样本，而监督式估计器仅37%–78%。在240节点不平衡三相Iowa馈线上，PoSE取得所有估计器中最低的注入、电压和支路电流误差；PoSE-fast每快照耗时0.2–0.6 s并保持精度，且不重训即在7种重构拓扑上优于高斯先验和重训的监督式估计器。

### 四、结论（Conclusion）
PoSE表明，将DSO已知的潮流方程、拓扑与量测噪声作为似然，把未知的变电站注入联合分布作为一次性学习的生成先验，可以在推理时得到校准且物理一致的后验样本。该方法无需按量测配置或拓扑重训，能直接给出电压越限和支路过载概率，适合作为可迁移的贝叶斯DSSE方案。

### 五、方法论与关键技术细节
关键实现包括：先验仅在注入空间学习，网络不近似潮流；校正残差用AC模型而H用LinDistFlow，并将AC与线性化量测差异的协方差Σ_lin并入R_eff；三相不平衡通过固定线性H和相别功率分配处理。训练使用AdamW、学习率1e-3、1000步预热后余弦衰减、批量1024、权重衰减0.1、dropout 0.1、EMA 0.999，训练10000步并按验证流动匹配损失选模；网络4个残差块、宽度512（Fluvius数据256）、嵌入128维。局限在于先验依赖历史数据代表性，快速变体对端点协方差做量测方向近似，线性化误差仅以协方差补偿而非严格消除。
