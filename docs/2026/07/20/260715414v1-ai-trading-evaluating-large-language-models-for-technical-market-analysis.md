# AI Trading: Evaluating Large Language Models for Technical Market Analysis

- 区域：速读区
- 排名：13
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Geofrey Ntale
- 机构：Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15414v1) · [PDF](https://arxiv.org/pdf/2607.15414v1)

## TLDR
This paper systematically evaluates five large language models (GPT-4 Turbo, Claude 3 Opus, Gemini 1.5 Pro, Llama 3 70B, and FinGPT) on technical market analysis tasks, finding that GPT-4 Turbo achieves the highest returns and Sharpe ratio among general-purpose models while domain-specialized FinGPT offers competitive risk-adjusted performance, but all models suffer from failure modes like numerical hallucination and inconsistent behavior in sideways markets.

## Abstract
Large Language Models (LLMs) have emerged as powerful tools for processing the heterogeneous information environments of modern financial markets. This paper presents a systematic, comparative evaluation of five prominent LLMs: GPT-4 Turbo, Claude 3 Opus, Gemini 1.5 Pro, Llama 3 70B, and the domain-specialized FinGPT, with respect to their capacity for technical market analysis. The evaluation spans four structured tasks: candlestick pattern recognition from OHLCV data, directional signal generation (BUY/SELL/HOLD), backtesting of signal quality through a simulated execution pipeline, and financial report comprehension. Our experimental framework employs rigorous quantitative metrics, including Sharpe ratio, maximum drawdown, Sortino ratio, information coefficient, F1-score, and BLEU score. Findings from simulated backtesting indicate that GPT-4 Turbo achieves the highest annualized return and Sharpe ratio among general-purpose models, while FinGPT demonstrates competitive risk-adjusted performance due to domain-specific fine-tuning. Both models outperform a passive S&P 500 benchmark under the tested conditions. The study identifies persistent failure modes across all evaluated models, including numerical hallucination, context-window limitations, and inconsistent performance in sideways market regimes. We conclude that while LLMs hold genuine promise within AI trading systems, robust deployment requires careful task decomposition, rigorous backtesting protocols, and domain-aware fine-tuning strategies.
