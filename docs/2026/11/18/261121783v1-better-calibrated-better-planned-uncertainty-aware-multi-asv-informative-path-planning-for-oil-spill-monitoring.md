# Better Calibrated, Better Planned: Uncertainty-Aware Multi-ASV Informative Path Planning for Oil Spill Monitoring

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Alejandro Casado-Pérez, Marija Popović, Daniel Gutiérrez-Reina, Sergio L. Toral., Samuel Yanes
- 机构：TU Delft, Universidad de Sevilla
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21783v1) · [PDF](https://arxiv.org/pdf/2611.21783v1)

## TLDR
In multi-ASV informative path planning for oil spill monitoring, the calibration and closed-loop robustness of the reconstruction model’s uncertainty dominate final mapping performance over planner choice, with Evidential Deep Learning yielding the best-calibrated, lowest-error reconstructions in a single fast forward pass.

## Abstract
Monitoring oil spills with fleets of Autonomous Surface Vehicles (ASVs) requires mapping a heterogeneous pollutant field from sparse, noisy measurements under tight time and energy budgets. Informative Path Planning (IPP) addresses this problem by coupling a reconstruction model, which infers the field and its uncertainty, with a planner that decides where to sample next. Prior work has focused on planning strategies and has largely relied on Gaussian Processes (GPs), leaving the calibration of the model's uncertainty underexplored. We study how uncertainty calibration conditions multi-vehicle IPP with a fleet of ASVs that coordinates online through a shared uncertainty map. We introduce Evidential Deep Learning (EDL) as an uncertainty-calibrated information model. We benchmark EDL, Monte Carlo Dropout and Deep Ensembles against a GP in closed loop with five planners on physics-based oil spill simulations. Across 60 maps, the choice of model dominates the outcome, explaining 80\% of the variance of the final reconstruction error, against 1\% for the planner among the deep models. EDL achieves the lowest error and the highest IoU under every planner, is the best calibrated model and runs at 3.9 ms per step. With 50 cells per vehicle it reconstructs the spill better than MC Dropout and Deep Ensembles with 150. Deep Ensembles become more confident as their error grows, whereas EDL is unaffected. Robustness of the information model to the data its own planner collects is therefore a requirement of uncertainty-aware IPP.


## 精读解读（中文）
### 一、研究动机
油污监测需要ASV舰队在严格时间和能量预算下，从稀疏含噪测量中重建非均匀污染物场，而信息路径规划（IPP）的性能取决于重建模型给出的不确定度是否能指示误差位置。既有工作多关注规划策略并主要依赖高斯过程，忽视了不确定度校准，且在闭环中模型会被自身不确定度引导的采样数据查询。本文因此研究不确定度校准如何影响多ASV IPP，并主张更校准的不确定度能带来更好的路径选择和更低重建误差。

### 二、技术方案（Method）
将监测区域离散为二维栅格，把稀疏观测编码为两通道图像（访问掩码与测量值），用共享U-Net骨干完成场重建；MC Dropout、Deep Ensembles和Evidential Deep Learning（EDL）仅在不确度估计方式上不同，并与RBF核高斯过程基线比较。深度模型用异方差负对数似然在可航行掩码上训练，EDL输出Normal-Inverse-Gamma参数并以Student-t边缘似然训练，单次前向得到均值、偶然与认知不确定度；MC Dropout用多次随机前向、Deep Ensembles用多个独立模型估计认知不确定度。闭环中4艘ASV通过共享不确定度图在线协调，将归一化总不确定度交给Value-Greedy、Uncertainty-Greedy、ε-Greedy、Receding Horizon Orienteering和MCTS五种规划器选择下一采样点，并满足节点互斥与单艇电池/距离预算约束。为分离不确定度对路径与重建的影响，所有舰队采集的观测最终用同一网络重建，并在60幅物理油污模拟地图上评估RMSE、IoU和校准。

### 三、结果（Result）
在60幅地图的闭环实验中，信息模型选择主导最终重建误差，解释约80%的方差，而深度模型间规划器仅解释约1%。EDL在所有五种规划器下均取得最低误差和最高IoU，是校准最好的模型，单步推理仅3.9 ms；每艇50个采样单元时，其重建效果仍优于每艇150个单元的MC Dropout和Deep Ensembles。Deep Ensembles在误差增大时反而更自信，而EDL不受此影响，说明其对自身规划器采集数据的鲁棒性更好。

### 四、结论（Conclusion）
多ASV油污监测IPP中，不确定度校准比规划器选择更关键；校准良好的信息模型能让规划器选择更有信息量的目标，从而降低重建误差。EDL以单次前向提供快速、校准且对闭环自采集数据更鲁棒的重建与不确定度，适合实时不确定度感知的舰队监测。信息模型对自身规划器所采数据的鲁棒性应作为不确定度感知IPP的基本要求。

### 五、方法论与关键技术细节
数据为60幅基于物理的油污模拟地图，场假设静态，观测含独立零均值高斯噪声，栅格已知且仅场未知；方法假设定位精确、通信瞬时无损、所有艇共享同一模型，并排除到达目标前的航行阶段。关键实现包括共享U-Net、可航行水域掩码、异方差NLL损失、EDL的NIG参数约束（ν>0、α>1、β>0）及Student-t边缘NLL，以及规划器使用归一化总不确定度进行排序。复杂度上，深度模型推理成本与样本数无关，但MC Dropout和Deep Ensembles需多次前向，EDL仅一次前向；GP精确推理随样本数呈O(D^3)且后验方差主要依赖采样位置而非测量值。局限性包括EDL的认知不确定度为启发式而非精确后验、实验基于模拟静态场、已知占据栅格和理想定位通信，真实动态油污与传感器/通信误差下的泛化仍需验证。
