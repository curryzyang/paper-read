# Toward Explainable and Policy-Aware AI for Carbon Credit Price Prediction: A Research Framework for Emerging Carbon Markets

- 区域：速读区
- 排名：13
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Summaiya Unnisa Begum, Mohammed Nadeem Ullah, Mohammed Abdul Ghani Khan
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01765v1) · [PDF](https://arxiv.org/pdf/2609.01765v1)

## TLDR
EPA-CarbonNet, a six-layer policy-aware and explainable carbon-price forecasting architecture, was built and tested on 11 years of S&P carbon data, yielding largely negative results—a random walk beat it on five-day RMSE, SHAP explanations were unstable, and policy attention did not align with regulatory events—though it led baselines in directional accuracy.

## Abstract
Carbon markets put a price on emissions, yet that price remains hard to forecast. Work in this area clusters on the EU and Chinese schemes, compresses regulatory text into a sentiment score, and reports accuracy without calibration or explanation stability. We distil ten recurring gaps into an impact-feasibility matrix and propose EPA-CarbonNet, a six-layer architecture that fuses market series with policy text by cross-attention and calibrated intervals alongside policy-attributed explanations. We then build and test it on eleven years of daily S and P carbon index data. The findings are largely negative, and reported as measured: a random walk beats the model on five-day RMSE (0.0365 against 0.0475), SHAP rankings agree at rho = 0.54 across resampled backgrounds, and policy attention never coincides with documented regulatory events. Directional accuracy, at 58.6 percent, leads every baseline. Code, data documentation and all result artifacts are available at https://github.com/Kimalice/Toward-Explainable-and-Policy-Aware-AI-for-Carbon-Credit-Price-Prediction
