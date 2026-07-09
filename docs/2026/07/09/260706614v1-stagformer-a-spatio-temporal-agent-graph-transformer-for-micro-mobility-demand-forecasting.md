# STAGformer: A Spatio-temporal Agent Graph Transformer for Micro Mobility Demand Forecasting

- 区域：速读区
- 排名：1
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Ye Zihao
- 机构：City University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06614v1) · [PDF](https://arxiv.org/pdf/2607.06614v1)

## TLDR
STAGformer introduces a spatio-temporal agent graph transformer with a linear-complexity agent attention mechanism that efficiently captures global dependencies by using learnable spatial and temporal agent tokens, achieving state-of-the-art demand forecasting accuracy on large-scale bike-sharing datasets.

## Abstract
Accurate station-level demand forecasting is essential for the efficient operation of bike-sharing systems, yet it remains challenging due to complex spatio-temporal dependencies and the large scale of urban networks. This paper presents STAGformer, a Spatio-Temporal Agent Graph Transformer that achieves efficient global modeling with linear computational complexity. The model introduces a two-step agent attention mechanism, where a small set of learnable spatial and temporal agent tokens first aggregate global information and then broadcast it back to individual stations and time steps, effectively capturing long-range interactions while reducing the quadratic cost of standard self-attention to O(NT). STAGformer integrates four core modules: a spatio-temporal encoder that fuses dynamic node features with external contextual factors (weather, time, points of interest), a graph propagation module for spatial neighbor aggregation, a temporal convolution module for local pattern extraction, and the agent attention module for global dependency modeling. Extensive experiments on two real-world datasets -- NYC Citi-Bike and Chicago Divvy-Bike -- demonstrate that STAGformer consistently outperforms state-of-the-art baselines across multiple prediction horizons, achieving significant improvements in both RMSE and MAE. Ablation studies validate the contribution of each component, with the agent attention mechanism proving critical for modeling global spatio-temporal dependencies.
