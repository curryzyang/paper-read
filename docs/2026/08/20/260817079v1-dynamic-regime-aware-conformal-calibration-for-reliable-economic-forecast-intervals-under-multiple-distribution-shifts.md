# Dynamic Regime-Aware Conformal Calibration for Reliable Economic Forecast Intervals under Multiple Distribution Shifts

- 区域：精读区
- 排名：7
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Bogdan Oancea
- 机构：National Institute of Research and Development for Biological Sciences, University of Bucharest
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.17079v1) · [PDF](https://arxiv.org/pdf/2608.17079v1)

## TLDR
DRACP unifies density-ratio, kernel, regime-aware, and online self-tuning weighting into a single weighted-conformal framework to deliver reliable prediction-interval coverage under multiple distribution shifts, trading off wider intervals for calibration accuracy that stays closest to nominal across horizons and stress periods.

## Abstract
Conformal prediction provides distribution-free prediction intervals but relies on exchangeability, an assumption often violated in economic forecasting because of covariate shift, concept drift, local heterogeneity and latent regimes. We propose Dynamic Regime-Aware Conformal Prediction (DRACP), which combines density-ratio, localized kernel and probabilistic regime-aware weighting with a self-tuning online significance controller in a unified weighted conformal calibration framework. We distinguish three theoretical results: finite-sample validity under oracle importance weights, a coverage-gap bound for estimated weights with rates in effective sample size, and deterministic or regret guarantees for the online controller. We evaluate DRACP against six baselines on 48 real forecasting series covering euro-area and EU-27 HICP inflation, US macroeconomic and energy indicators, and daily financial series. Recent online methods (FACI, strongly-adaptive online conformal prediction and conformal PID) were verified against the authors' implementations. DRACP is not the most efficient method: strongly-adaptive online conformal prediction achieves the best interval score and intervals about 20% narrower. Instead, DRACP provides the most reliable calibration, achieving coverage closest to the nominal 0.90 (0.890), never falling below 0.80 on any series, maintaining the best coverage at all forecast horizons, and performing best during the 2021-2023 inflation surge. The strongly-adaptive method undercovers on 20 of 48 series versus 10 for DRACP. DRACP therefore offers a principled trade-off between calibration and efficiency, favoring reliable coverage when prediction intervals must satisfy coverage standards. An ablation study shows that the online controller and conditional-scale normalization provide most of the performance gain, whereas the weighting components make a smaller contribution.


## 精读解读（中文）
### 一、研究动机
经济预测中预测区间常因协变量漂移、概念漂移、局部异质性和潜在机制同时发生而违反可交换性，现有自适应共形方法通常只针对单一偏差，无法应对多重分布偏移同时作用的情况。因此需要一个统一的加权共形校准框架，能够同时处理多种非平稳性并保证可靠覆盖。

### 二、技术方案（Method）
DRACP将密度比权重、局部核权重、概率机制感知权重和自调优在线显著性控制器组合在一个加权共形校准步骤中。具体流程：先在训练块上拟合点预测器，得到过去各期的误差分数；然后对每个校准点计算四种权重——基于分类器估计的密度比（区分近期与较旧预测变量）、局部核（衡量预测变量相似性，带宽自适应且有有效样本量下限）、由混合模型分配的机制相似度、以及按时间几何衰减的最近性权重；四种权重相乘并归一化，在测试点加入原子权重后取加权分位数作为区间半径；在线控制器根据已实现覆盖率调整工作显著性水平，采用类似FACI的多专家指数加权聚合。所有量在时间t仅使用当时可得信息因果计算。

### 三、结果（Result）
在48个真实序列上对比六个基线，DRACP并非最有效：强自适应在线共形预测（SAOCP）取得最佳区间分数，区间约窄20%。但DRACP在覆盖率上最可靠：面板上平均覆盖率0.890最接近名义0.90，任何序列从未低于0.80，在所有预测期限上保持最佳覆盖率，且在2021-2023通胀激增期间表现最好。SAOCP在48个序列中20个欠覆盖，而DRACP只有10个。

### 四、结论（Conclusion）
DRACP提供了可靠覆盖与区间效率之间的原则性权衡，偏向于在预测区间必须满足覆盖标准时保证可靠覆盖。其价值在于面对多重同时发生的分布偏移时，能维持最接近名义水平的经验覆盖率，尽管区间较宽，因此适合作为需要严格覆盖保证的决策场景下的校准方法。

### 五、方法论与关键技术细节
理论结果区分三种：oracle重要性权重下的有限样本有效性、估计权重的覆盖差距界（以有效样本量而非名义样本量的速率表示）、以及在线控制器的确定性或遗憾保证。实现细节包括：密度比用分类器估计，局部核带宽自适应且带有效样本量下限，在线控制器采用多学习率专家聚合；数据涵盖欧元区和EU-27 HICP通胀、美国宏观经济和能源指标、每日金融序列；近期基线（FACI、SAOCP、conformal PID）均通过原作者实现验证。消融研究显示，在线控制器和条件尺度归一化贡献了大部分性能提升，而权重成分贡献较小；局限性是DRACP区间较宽，效率低于SAOCP。
