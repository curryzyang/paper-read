# Foundation models for electricity price forecasting and battery arbitrage: Can they replace market-specific forecasting models?

- 区域：速读区
- 排名：7
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Arkadiusz Lipiecki, Rafał Weron
- 机构：Wrocław University of Science and Technology, Aarhus University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00089v1) · [PDF](https://arxiv.org/pdf/2609.00089v1)

## TLDR
Foundation models cannot universally replace market-specific electricity price forecasting models: only TabPFN consistently achieves superior statistical accuracy across Germany, Poland, and Spain, yet its economic dominance in battery arbitrage depends on trading strategy and risk tolerance.

## Abstract
Foundation models promise accurate forecasts with little or no task-specific training, but whether they can replace models designed specifically for electricity price forecasting remains unclear. We compare nine variants from five foundation model families, evaluated in zero-shot mode, with two state-of-the-art electricity price forecasting benchmarks in Germany, Poland, and Spain over 2021-2025. Their performance is assessed in terms of point and probabilistic forecasting accuracy, as well as economic value in battery energy storage arbitrage. Only the TabPFN models consistently and significantly outperform the benchmarks across all three markets and all statistical measures. However, this statistical dominance does not translate directly into economic dominance: TabPFN performs best under unlimited bids and riskier quantile-based strategies, whereas the Distributional Deep Neural Network benchmark is more profitable when risk tolerance is lower. Thus, foundation models cannot universally replace market-specific models, and their value depends on both model architecture and the decision problem.
