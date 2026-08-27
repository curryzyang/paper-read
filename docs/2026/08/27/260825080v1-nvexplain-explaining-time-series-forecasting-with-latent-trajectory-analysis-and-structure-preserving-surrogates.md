# NVExplain: Explaining Time Series Forecasting with Latent Trajectory Analysis and Structure-Preserving Surrogates

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Muyan Anna Li, Manikandan Ravikiran, Aditi Gautam
- 机构：NVIDIA
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.25080v1) · [PDF](https://arxiv.org/pdf/2608.25080v1)

## TLDR
NVExplain introduces a model-agnostic time series forecasting explainability framework that attributes each forecast horizon to relevant historical lags via latent trajectory semantic flow and structure-preserving surrogates, achieving competitive or superior faithfulness with high computational efficiency.

## Abstract
Time series forecasting models are widely used in high-stakes settings, yet their predictions remain difficult to interpret because existing post-hoc methods often ignore temporal dependence and fail to provide horizon-specific explanations. We propose a model-agnostic explainability framework that explains forecasting predictions by attributing each forecast horizon to temporally relevant historical lags. The framework models forecasting as a latent trajectory and introduces semantic flow to quantify how information evolves across time in the model's internal representations. By aggregating semantic flow, it constructs a lag-horizon attribution matrix that captures horizon-resolved temporal influence. To improve explainability, we further generate structure-preserving perturbations and fit sparse local surrogate models, producing human-readable and temporally coherent explanations. We evaluate the method using faithfulness and stability diagnostics across multiple benchmark datasets. Results show that the semantic-flow variant achieves competitive or superior faithfulness compared to standard post-hoc baselines, while being substantially more computationally efficient. Stability analysis further demonstrates that the explanations are robust and identifies regimes where interpretation should be applied with caution.
