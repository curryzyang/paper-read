# Evaluating Time Series Foundation Models for Electricity Price Forecasting: Contamination Risk, Distributional Shifts, and Covariate Dependence

- 区域：精读区
- 排名：6
- 匹配度：2.0/10
- 来源：arxiv
- 作者：Zhenghua Pan, Ahmed Aziz Ezzat
- 机构：Rutgers, The State University of New Jersey, USA
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02623v1) · [PDF](https://arxiv.org/pdf/2607.02623v1)

## TLDR
This paper benchmarks time series foundation models for electricity price forecasting, finding that while they are competitive and benefit from covariate support, they often do not outperform domain-specific methods, yet simple ensembles of both capture complementary information and achieve the best overall performance.

## Abstract
Time series foundation models (TSFMs) have shown strong zero-shot forecasting performance, but their generalization in covariate-driven, non-stationary settings is underexplored. Electricity price forecasting (EPF) presents a challenging testbed due to complex temporal dependencies, distributional shifts, and strong reliance on structural and contextual information. We propose a two-dataset-benchmarking framework for EPF to mitigate contamination risk and enable fair evaluation of TSFMs. We examine key aspects of EPF including point and probabilistic forecasting performance, tail behavior, price spikes, and comparisons against domain-specific methods. We find that TSFMs are highly competitive and often outperform general-purpose baselines. Yet, their performance depends critically on covariate support, and they do not consistently surpass domain-specific methods tailored to EPF. Interestingly, simple ensembles of TSFMs and domain-specific methods appear to have significant potential, suggesting that the two approaches capture complementary predictive information.

## 精读解读（中文）

### 一、研究动机
时间序列基础模型在零样本预测中表现强劲，但在协变量驱动且非平稳的电价预测场景下的泛化能力尚未充分探索。由于电力价格具有复杂的时序依赖、分布漂移以及对结构性和上下文信息的强烈依赖，为系统评估这些模型带来了独特挑战。本研究旨在评估TSFMs在电价预测中的表现，同时控制数据污染风险。

### 二、技术方案（Method）
提出一个双数据集基准框架以减轻污染风险，在GEFCom2014-P和GridStatus2025两个数据集上评估四种TSFMs（Chronos 2、TimesFM 2.5、TabPFN-TS、TOTO 1.0），并对比其无协变量与有协变量版本。同时与统计基线（如Auto-ARIMA）、深度学习基线（如DeepAR、TFT）及领域特异性模型（如LEAR、CING-LEAR）进行比较，涵盖点预测、概率预测、尾部行为及价格尖峰分析。

### 三、结果（Result）
TSFMs在零样本预测中表现出强竞争力，通常优于通用基线，但性能严重依赖协变量支持，且未能持续超越领域特异性模型。简单集成TSFM（Chronos 2 w.）与领域模型（CING-LEAR）在所有指标上取得最优结果。在GridStatus2025上，Chronos 2 w.和CING-LEAR为最佳个体模型，而TOTO 1.0表现严重退化，凸显污染风险评估的重要性。

### 四、结论（Conclusion）
TSFMs在电价预测中具有潜力，但领域特异性建模仍然重要，两者捕捉互补的预测信息，简单集成可显著提升性能。分布漂移和尾部行为评估揭示TSFMs在极端价格下表现更均衡，但污染风险需通过精心设计的基准框架加以控制。

### 五、方法论与关键技术细节
数据方面，使用GEFCom2014-P（标准化基准）和GridStatus2025（2022-2024训练，2025测试，协变量包括负荷、太阳能、天然气和燃料价格）。评估指标包括MAE、RMSE和平均分位数损失（aQL）。模型为零样本预测，无微调。局限性包括：TSFMs的预训练数据可能包含污染，但双数据集设计部分缓解；TOTO在GridStatus2025上的劣化暗示污染风险；简单集成仅用平均法，更复杂集成可能进一步改进；实验仅聚焦短期电价预测，泛化性需验证。

