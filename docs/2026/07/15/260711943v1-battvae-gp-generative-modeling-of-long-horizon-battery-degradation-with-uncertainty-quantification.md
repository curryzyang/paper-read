# BattVAE-GP: Generative Modeling of Long-Horizon Battery Degradation with Uncertainty Quantification

- 区域：精读区
- 排名：6
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Raghvender Raghvender, Mahdi Abid, Ferran Brosa Planella, Charles Delacourt, Arnaud Demortière
- 机构：INRIA, CNRS, The Faraday Institution, Université de Picardie Jules Verne, University of Warwick
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11943v1) · [PDF](https://arxiv.org/pdf/2607.11943v1)

## TLDR
BattVAE-GP proposes a hybrid physics-probabilistic framework that combines a variational autoencoder (VAE) with a sparse multitask Gaussian process (GP) to efficiently and uncertainty-quantifiably surrogate long-horizon lithium-ion battery degradation trajectories under unseen charging rates.

## Abstract
Long-horizon physics-based simulations of battery degradation provide mechanistic insight but remain computationally expensive, limiting their use for dense exploration of operating conditions over extended cycle life. Here, we propose a hybrid physics-probabilistic learning framework for surrogate modeling of lithium-ion battery degradation trajectories at unseen charging rates. Cycle-resolved degradation data generated with a DFN/P2D electrochemical model in PyBaMM are first transformed into capacity-aligned voltage and derivative features and encoded using a Variational Autoencoder (VAE). The resulting two-dimensional latent space organizes degradation trajectories according to both cycle progression and charging protocol. A sparse multitask Gaussian process (GP) is then trained in this latent space using cycle number and C-rate as input variables, providing continuous interpolation of latent degradation dynamics together with posterior uncertainty estimates. Under protocol-level holdout evaluation, the latent-space GP accurately recovers unseen C-rate trajectories and exhibits uncertainty behavior consistent with the support of the training data. When queried at unseen interior C-rates, the model generates latent trajectories that remain coherently positioned between neighboring simulated protocols. Decoding the GP-predicted latent states through the frozen VAE decoder yields smooth voltage-capacity evolution, while Monte Carlo propagation of the GP latent posterior through an auxiliary latent to State of Health (SOH) predictor provides uncertainty-aware SOH estimates. The proposed BattVAE-GP framework therefore offers a computationally efficient and uncertainty-aware surrogate for long-horizon degradation modeling, providing a structured basis for extending battery health prediction toward richer operating conditions and future simulation-experiment fusion.


## 精读解读（中文）
### 一、研究动机
长周期基于物理的电池退化模拟虽然提供了机理洞察，但计算成本高昂，限制了在扩展循环寿命内对运行条件进行密集探索。现有方法难以在未见充电倍率下可靠预测退化轨迹，且缺乏不确定性量化。

### 二、技术方案（Method）
使用PyBaMM中的DFN/P2D电化学模型生成NMC811/石墨电池在多个恒流充电倍率下长达5000个循环的退化数据。每个循环的充电和放电段通过容量对齐插值到统一网格，并提取电压、差分电压和增量容量特征组成六通道输入。VAE编码器采用带傅里叶位置编码和掩码均值池化的Transformer，将每个循环映射为二维潜在变量。解码器采用基线-残差结构，基线学习共享容量坐标函数，残差由潜在变量调制。在潜在空间中训练稀疏多任务高斯过程（GP），以循环数和C-rate为输入进行连续插值，并通过蒙特卡洛传播GP后验通过辅助SOH预测器获得不确定性估计。模型联合优化掩码重建损失、KL散度（β-VAE调度为1e-7）和SOH预测损失（权重0.3）。

### 三、结果（Result）
在协议级留出评估中，GP准确恢复未见C-rate的退化轨迹，其不确定性行为与训练数据支持区域一致；在未见内部C-rate查询时，生成的潜在轨迹自然位于相邻训练协议之间。解码后的电压-容量曲线平滑，SOH估计伴随合理的不确定性区间。

### 四、结论（Conclusion）
BattVAE-GP框架为长周期退化建模提供了计算高效且具有不确定性意识的代理模型，能够可靠插值未见充电倍率下的全生命周期行为，为向更丰富操作条件扩展及未来模拟-实验融合奠定了基础。

### 五、方法论与关键技术细节
数据来源为PyBaMM等温DFN/P2D仿真（无热模型），仅隔离C-rate影响；VAE潜在维度设为2，编码器使用4层Transformer（4头，GELU）；KL系数从0线性调度至1e-7，SOH损失权重固定0.3；GP为稀疏多任务形式，输入为循环数和C-rate；主要局限性在于模拟与真实电池间的潜在不匹配，需通过实验数据微调或域适应策略弥合。
