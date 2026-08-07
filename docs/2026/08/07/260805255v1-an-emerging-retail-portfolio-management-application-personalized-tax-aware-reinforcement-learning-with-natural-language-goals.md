# An Emerging Retail Portfolio Management Application: Personalized, Tax-Aware Reinforcement Learning with Natural Language Goals

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Ramin Pishehvar
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05255v1) · [PDF](https://arxiv.org/pdf/2608.05255v1)

## TLDR
TLDR: This paper presents a fully built, integration-tested retail portfolio management application that translates plain-language investment goals into personalized, tax-aware recommendations via a three-phase reinforcement learning pipeline—self-supervised cross-asset encoding, a Mixture-of-Experts allocation policy, and per-user LoRA personalization—validated through live brokerage API integration and backtests, though not yet deployed to real users.

## Abstract
Retail investors lack access to the kind of personalized, tax-aware portfolio management that institutional clients take for granted -- existing robo-advisors use static, rule-based allocation, and institutional-grade systems require account minimums and technology stacks unavailable to individual investors. We present a fully built, integration-tested application that closes this gap: a FastAPI backend and web dashboard that let a user describe an investment goal in plain language (e.g. "I want steady growth but need to sell some shares next month for a down payment"), routes that goal to one of six investment mandates, and produces a live, broker-integrated portfolio recommendation from athree-phase reinforcement learning system -- a self-supervised cross-asset encoder, a Mixture-of-Experts (MoE) allocation policy with a learned intent router, and a lightweight LoRA adapter that personalizes recommendations from an individual's revealed brokerage behavior without retraining the shared model. The system is functionally complete and integration-tested end-to-end against a live brokerage API (Alpaca, paper-trading mode), including multi-user authentication, a trust first preview-before-apply confirmation flow, daily email digests, and an auditable action-integrity chain, but has not yet been opened to real end-users; we report this honestly as an emerging, pre-deployment application with a concrete path to full deployment, alongside 14-day walk-forward backtests (bootstrapped confidence intervals included) as preliminary, pre-deployment validation rather than production performance. We also report several practical engineering lessons -- silently-inactive integration paths, hanging third-party API calls, and the value of end-to-end empirical verification over trusting checkpoint metadata -- that we believe generalize to other applied RL systems built on external, live data sources.
