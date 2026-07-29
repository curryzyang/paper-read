# FinAbstain: Uncertainty-Calibrated Multimodal RAG for Selective Financial Forecasting

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Dorothy Torres, Wei Cheng, Henan Huang
- 机构：New Jersey City University, The Pennsylvania State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24875v1) · [PDF](https://arxiv.org/pdf/2607.24875v1)

## TLDR
FinAbstain proposes a time-safe, multimodal RAG framework for selective financial forecasting that uses calibrated uncertainty estimates and a controller to abstain when evidence is contradictory or sparse, trading coverage for lower error and drawdown.

## Abstract
Large language models (LLMs) can synthesize financial narratives but may express high confidence when evidence is sparse, stale, or contradictory. This failure is especially consequential in forecasting, where filings, news, prices, volume, and technical signals can disagree. We present FinAbstain, a research framework for uncertainty-calibrated multimodal retrieval-augmented generation (RAG) with selective prediction. A point-in-time retriever admits only information public at the forecast timestamp and supplies modality-specific evidence to fundamental, news, technical, risk, and verification agents. Their probabilistic assessments are aggregated with retrieval relevance, evidence contradiction, repeated-sample consistency, and historical calibration statistics. Temperature scaling, isotonic regression, conformal prediction, and a proposed hybrid uncertainty score are evaluated under a common chronological protocol. A controller predicts bullish, bearish, or neutral outcomes only when uncertainty is below a validated threshold; otherwise it abstains, requests evidence, reduces exposure, or routes the case to human review. The evaluation covers one- and five-day abnormal-return direction, twenty-day volatility intervals, and abstention decisions, using accuracy, calibration, risk--coverage, citation, trading, latency, and cost metrics. To make the design auditable before a full data collection is complete, we report explicitly labeled simulated results rather than empirical claims. These results illustrate the intended hypothesis: calibrated abstention may trade coverage for lower selective error and drawdown. The contribution is a time-safe architecture, a composite uncertainty formulation, and a reproducible evaluation blueprint for evidence-grounded selective financial forecasting.
