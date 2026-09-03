# WMLLM: Self-Evolving Optimization Agents via Predict-Then-Act World Modeling

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Zhongzheng Li, Qingsong Ran, Shikun Feng, Nian Ran, Wenhao Li, Xiaoyuan Zhang, Yue Wang, Xiaoguang Zhao
- 机构：Zhongguancun Academy, Chinese Academy of Sciences, University of Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01608v1) · [PDF](https://arxiv.org/pdf/2609.01608v1)

## TLDR
WMLLM is a self-evolving LLM-based optimization agent that uses predict-then-act world modeling, population search, and reinforcement learning to improve sample efficiency in black-box optimization, achieving state-of-the-art results on multi-objective molecular optimization.

## Abstract
Black-box optimization problems remain challenging because of large, weakly structured, and high-dimensional search spaces. Existing methods often suffer from poor sample efficiency because they rely on direct candidate generation or trial-and-error refinement. A natural way to improve search efficiency is to use world modeling, which can help identify promising optimization directions before costly evaluation. Large language models can predict the outcomes of these candidates with nontrivial accuracy because of their implicit knowledge. Motivated by this observation, we propose WMLLM, a self-evolving optimization-agent framework based on predict-then-act world modeling. The agent first predicts promising directions and then acts to generate candidates. Combined with agentic multi-turn refinement, population-based search, and reinforcement learning, WMLLM refines both its implicit world model and its optimization strategy during search. Experiments on black-box optimization tasks, especially multi-objective molecular optimization, show that WMLLM improves sample efficiency and final optimization performance. On the multi-objective molecular optimization benchmark, WMLLM achieves state-of-the-art results under a limited evaluation budget.
