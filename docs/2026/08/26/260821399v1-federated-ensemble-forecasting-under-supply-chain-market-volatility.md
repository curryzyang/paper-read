# Federated Ensemble Forecasting Under Supply-Chain Market Volatility

- 区域：速读区
- 排名：6
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Shunmukha Sagar Puppala
- 机构：SAP
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21399v1) · [PDF](https://arxiv.org/pdf/2608.21399v1)

## TLDR
FEF-NCL is a federated ensemble forecasting method with negative-correlation learning and drift-aware aggregation that improves supply-chain demand forecasts under market volatility, reducing weighted MAPE from 13.9% to 12.4% on a synthetic multi-client dataset.

## Abstract
Supply chain forecasting systems increasingly operate under market shocks, non-identically distributed regional demand, and limited willingness to centralize commercial data. This work proposes Federated Ensemble Forecasting with Negative-Correlation Learning (FEF NCL), a distributed method that trains specialized forecasting experts across client nodes while discouraging redundant model errors. The framework combines temporal feature encoders, client level drift scoring, reliability-weighted aggregation, and an explain ability layer that exposes the market and supplier variables most responsible for each forecast. A single synthetic dataset is used to evaluate the design. It contains 124,800 weekly SKU region observations from ten regional client nodes, 60 product families, 40 suppliers, five commodity groups, and a 2021-2024 volatility profile with explicit price-shock regimes. Because the dataset is synthetic, the reported results should be interpreted as controlled evidence of internal consistency rather than real-world validation. Across the synthetic test split, FEF NCL reduces weighted mean absolute percentage error from 13.9% for the best federated baseline to 12.4%, improves delay-risk macro-F1 from 0.755 to 0.801, and lowers the high volatility quintile error by 2.1 percentage points relative to SCAFFOLD. The analysis suggests that negative-correlation specialization is useful when clients face different supplier, freight, and commodity conditions, although deployment would require stronger privacy analysis, live drift monitoring, and operational calibration. Index Terms federated learning, ensemble learning, negative correlation learning, supply chain forecasting, market volatility, data drift, demand planning, risk governance
