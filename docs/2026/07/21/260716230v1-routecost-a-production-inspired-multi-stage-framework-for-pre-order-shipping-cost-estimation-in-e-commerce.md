# RouteCost: A Production-Inspired Multi-Stage Framework for Pre-Order Shipping Cost Estimation in E-Commerce

- 区域：速读区
- 排名：10
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Xianling Zeng, Zihan Yu, Sichen Zhao, Yalun Qi, Zhiming Xue
- 机构：Northeastern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16230v1) · [PDF](https://arxiv.org/pdf/2607.16230v1)

## TLDR
A multi-stage framework (RouteCost) decomposes pre-order shipping cost estimation into demand forecasting, baseline pricing, residual correction, and consolidation inference, improving predictive accuracy and interpretability over static or monolithic approaches.

## Abstract
Accurate pre-order shipping cost estimation is important in e-commerce because it affects price presentation, margin planning, and conversion. In practice, shipping cost is shaped not only by distance but also by destination demand mix, billable weight, dimensional pricing, surcharge triggers, and latent operational effects such as shipment consolidation. Static lookup methods therefore miss important sources of variation, while monolithic regressors may exploit strong but non-causal correlations. We propose RouteCost, a production-inspired multi-stage framework that decomposes the problem into time-aware demand forecasting, fee-card-informed baseline pricing, Stage 2 residual correction, and proxy-based box-consolidation inference. Route-level cost estimates are aggregated through a route-weighted expectation formulation to produce product-level shipping cost predictions. Across over 250,000 orders, 260 products, and 18 months of order history, the framework improves predictive quality and aggregate calibration while preserving route-level interpretability.
