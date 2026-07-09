# Evaluating Time Series Foundation Models for Electricity Price Forecasting: Contamination Risk, Distributional Shifts, and Covariate Dependence

- 区域：精读区
- 排名：6
- 匹配度：2.0/10
- 来源：arxiv
- 作者：Zhenghua Pan, Ahmed Aziz Ezzat
- 机构：Rutgers, The State University of New Jersey, USA
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02623v1) · [PDF](https://arxiv.org/pdf/2607.02623v1)

## TLDR
This paper benchmarks time series foundation models for electricity price forecasting, finding they are competitive but critically depend on covariate support and often underperform domain-specific methods, while simple ensembles of both approaches yield strong performance.

## Abstract
Time series foundation models (TSFMs) have shown strong zero-shot forecasting performance, but their generalization in covariate-driven, non-stationary settings is underexplored. Electricity price forecasting (EPF) presents a challenging testbed due to complex temporal dependencies, distributional shifts, and strong reliance on structural and contextual information. We propose a two-dataset-benchmarking framework for EPF to mitigate contamination risk and enable fair evaluation of TSFMs. We examine key aspects of EPF including point and probabilistic forecasting performance, tail behavior, price spikes, and comparisons against domain-specific methods. We find that TSFMs are highly competitive and often outperform general-purpose baselines. Yet, their performance depends critically on covariate support, and they do not consistently surpass domain-specific methods tailored to EPF. Interestingly, simple ensembles of TSFMs and domain-specific methods appear to have significant potential, suggesting that the two approaches capture complementary predictive information.


## 精读解读（中文）
### 一、研究动机
时间序列基础模型（TSFMs）在零样本预测中表现强劲，但其在协变量驱动、非平稳场景下的泛化能力尚未充分探索。电力价格预测（EPF）因复杂时间依赖性、分布偏移和对结构及上下文信息的强依赖，成为挑战性测试平台。本研究旨在系统评估TSFMs在EPF中的表现，重点关注污染风险、分布偏移和协变量依赖问题。

### 二、技术方案（Method）
提出双数据集基准测试框架，使用标准基准GEFCom2014-P和新建GridStatus2025数据集以减少污染风险。评估四种TSFMs（Chronos 2、TimesFM 2.5、TabPFN-TS、TOTO 1.0）及其协变量支持变体，对比统计模型（Seasonal Naïve、Auto-ARIMA等）、深度学习模型（DeepAR、TFT、TiDE等）和领域特定方法（LEAR、DNN、CING-LEAR）。采用滚动评估协议，计算MAE、RMSE和平均分位数损失（aQL）等指标，并分析尾部行为和价格尖峰场景下的鲁棒性。

### 三、结果（Result）
在GEFCom2014-P上，TSFMs零样本性能接近但未进入前五；在GridStatus2025上，协变量支持的Chronos 2 w.和TabPFN-TS w.表现最佳，优于统计和深度学习基线，但领域特定方法CING-LEAR仍具竞争力。简单集成（Chronos 2 w. + CING-LEAR）取得最优性能（MAE 3.922, RMSE 5.470, aQL 1.541），表明两者捕获互补信息。TSFMs在概率预测和尾部平衡性上优于统计模型，但协变量支持至关重要；TOTO 1.0在GEFCom2014-P上表现良好却在GridStatus2025上大幅退化，凸显污染风险。

### 四、结论（Conclusion）
TSFMs在EPF中具有竞争力，但其性能关键依赖于协变量支持；领域特定方法仍需作为强基线；简单集成策略通过结合预训练和领域知识展现出显著潜力。评估中必须考虑数据污染风险，双数据集框架提供了更可靠的泛化评估。TSFMs在概率预测和极端事件处理上更鲁棒，但协变量的接入是决定性因素。

### 五、方法论与关键技术细节
双数据集设计：GEFCom2014-P（1997-2011）作为标准基准，GridStatus2025（2022-2025）用于最小化时间重叠污染。评估指标包括MAE、RMSE和9个分位数的平均分位数损失（aQL）。尾部性能分析显示TSFMs在低分位数（如Q(0.01)）上显著优于统计模型，而领域模型CING-LEAR在所有分位数上表现稳健。价格尖峰定义为低于5%或高于95%分位数，TSFMs在极端事件中预测误差相对较小。简单集成方法仅平均两个模型的预测，未使用加权或学习，但已显著提升性能。局限性：部分TSFM训练数据不透明，污染风险仅通过时间隔离缓解；TOTO 1.0在GridStatus2025上表现差可能源于市场差异而非污染，但无法完全排除。
