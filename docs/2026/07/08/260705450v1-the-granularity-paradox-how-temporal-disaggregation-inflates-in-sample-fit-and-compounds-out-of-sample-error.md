# The Granularity Paradox: How Temporal Disaggregation Inflates In-Sample Fit and Compounds Out-of-Sample Error

- 区域：精读区
- 排名：7
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Hugo Moreira
- 机构：Iscte - Instituto Universitário de Lisboa
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.05450v1) · [PDF](https://arxiv.org/pdf/2607.05450v1)

## TLDR
Finer temporal disaggregation in time-series forecasting improves in-sample fit but degrades out-of-sample accuracy due to recursive error compounding over longer horizons, revealing a non-monotonic trade-off where model performance depends on the interaction between granularity, horizon length, and recursive feedback topology.

## Abstract
This paper explores the "Granularity Paradox" in time-series forecasting, wherein finer temporal disaggregation (e.g., Monthly to Weekly/Daily) improves in-sample diagnostics and dataset size (N), but degrades out-of-sample accuracy due to recursive error compounding over longer horizons (H). Conversely, coarse aggregation (Annual) eliminates recursive error propagation but reduces data available to estimators. We formalize this trade-off and benchmark 10 models - spanning naïve, statistical, machine learning, and deep learning architectures - across six granularities using a 13-year public procurement dataset. The empirical results reveal a non-monotonic threshold structure: recursive autoregressive and seasonal models degrade substantially under high-frequency forecasting (e.g., Holt-Winters reaches a Test R-squared of -151 and TPFE of 425.85% at the Daily grain), while the LSTM traces a U-shaped error curve, worsening from Monthly (19.66%) through Bi-Weekly (35.94%) before overcoming the error propagation penalty at Daily (TPFE of 4.35%, R-squared of 0.66). Linear Regression remains stable across all granularities (16.3-17.0% TPFE), confirming that the paradox is driven by recursive feedback topology, not model complexity. The results demonstrate that standard pointwise metrics (RMSE, MAE) systematically mask cumulative error propagation, and that evaluating forecasts without goal-dependent cumulative metrics produces misleading assessments of model adequacy. We introduce a consensus-dissensus diagnostic comparing the directional behaviour of pointwise metrics against cumulative TPFE across granularities, enabling the identification of models whose standard diagnostics mask systematic error propagation.


## 精读解读（中文）
### 一、研究动机
时间序列预测中，更细的时间粒度（如从月到日）虽然能增加样本量并改善样本内拟合，但会因递归误差累积导致样本外精度显著下降，形成“粒度悖论”。本文旨在形式化这一权衡，并揭示点评价指标在评估多步预测时的系统性误导作用。

### 二、技术方案（Method）
使用葡萄牙公共采购IT服务领域13年（2012-2024）数据集，将序列重采样为年（N=13, H=1）、季（N=52, H=4）、月（N=156, H=12）、双周（N=341, H=26）、周（N=680, H=52）和日（N=4754, H=365）六种粒度。评估10个模型：朴素基线（持久、漂移、滚动均值）、统计/自回归（线性回归、ARIMAX、SARIMAX、Holt-Winters）、机器学习（XGBoost）和深度学习（LSTM、N-BEATS）。采用扩展窗口回测（8折），每折重新优化参数；超参数在首折网格搜索后跨粒度固定。使用点评价指标（RMSE、MAE）和累积指标（累计百分比误差TPFE、累计绝对误差TAFE）评估，并引入共识-分歧诊断：比较点评价与TPFE随粒度变化的趋势方向是否一致。

### 三、结果（Result）
实证揭示非单调阈值结构：递归自回归和季节性模型在高频递归预测下严重退化，例如Holt-Winters在日粒度测试R²为-151、TPFE为425.85%；LSTM误差曲线呈U形，从月度19.66%恶化至双周35.94%，但在日粒度（TPFE=4.35%、R²=0.66）克服误差传播惩罚；线性回归跨粒度稳定（TPFE 16.3-17.0%）。点评价指标（RMSE、MAE）系统性低估累积误差传播，例如持久性模型训练R²=0.78但测试TPFE=23.89%。共识-分歧诊断成功识别出掩盖误差传播的模型（如日粒度下LSTM等模型的点评价改善而累积指标恶化）。

### 四、结论（Conclusion）
本文验证了“粒度悖论”：时间粒度变细导致样本内诊断虚高而样本外误差因递归累积放大。点评价指标（RMSE、MAE）无法捕捉累积误差，必须结合目标依赖的累积指标（如TPFE）才能正确评估模型。共识-分歧诊断可识别模型中隐藏的系统性误差传播，为实际预测中的粒度选择提供指导。

### 五、方法论与关键技术细节
数据：葡萄牙IT服务公共采购，13年、CPV Division 72；先验假设：递归反馈拓扑是悖论核心驱动，非模型复杂度；损失函数：训练使用标准损失（如MSE），评价引入TPFE、TAFE；超参数：LSTM种子42，N-BEATS使用Darts默认，XGBoost网格搜索跨粒度固定；计算复杂度：LSTM参数密集需大数据量，N-BEATS可解释但需足够样本；局限性：深度学习结果仅单种子点估计，方向稳健但精确幅度非最优下界；粗粒度（如年）下部分模型训练R²为负（如LSTM年-2.28），表明样本量不足时参数空间无法解析。
