# Evaluating Large Language Models for Forced Outage Risk Prediction: Benefits and Comparison to Machine Learning

- 区域：速读区
- 排名：8
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Christos Petridis, Zoran Obradovic, Mladen Kezunovic
- 机构：Temple University, Texas A&M University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04272v1) · [PDF](https://arxiv.org/pdf/2609.04272v1)

## TLDR
Zero-shot large language models underperform supervised machine learning in accuracy for weather-related forced outage risk prediction, but offer complementary benefits in interpretability and scalability, suggesting hybrid approaches are preferable.

## Abstract
This study examines the ability of large language models (LLMs) to predict the risk of weather-related forced outages in the distribution grid in a zero-shot framework, without labeled training data. The problem is formulated as a binary severity classification task across three forecast horizons (3h, 6h, 12h), using six years of outage records and high-resolution weather data for a utility service area in central Texas. Four zero-shot LLMs are benchmarked against two supervised classifiers across two input configurations: one using current weather observations and the other using weather forecast data. Results show that supervised models outperform LLMs on macro-F1 and precision, while newer LLM generations achieve competitive scores. Beyond accuracy, LLMs offer complementary strengths in actionable reasoning and geographic scalability, suggesting that combining them with supervised models may be the best practice.
