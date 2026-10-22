# Measure First, Then Allocate: Calibrated Rollout Budgets for MCP Agents in Reinforcement Learning

- 区域：速读区
- 排名：3
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Hieu Tran, Zonghai Yao, Sunjae Kwon, Hong Yu
- 机构：University of Massachusetts Amherst, University of Massachusetts Lowell
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28785v1) · [PDF](https://arxiv.org/pdf/2610.28785v1)

## TLDR
The paper introduces Discord and BRACE to use reward disagreement for harness evaluation and to forecast mixed-reward rollout groups before allocating training rollouts, improving the sample efficiency and performance of MCP agents in reinforcement learning.

## Abstract
Training tool-using language models requires costly interaction, yet identical rewards within a rollout group provide no group-relative learning signal. We use reward disagreement to guide harness evaluation and the allocation of rollouts for policy training in Model Context Protocol (MCP) environments. We first introduce Discord, which tests harness edits using exact paired inference and decision-preserving early stopping: only disagreeing paired outcomes favor one harness over another. This insight motivates prospective allocation in BRACE (Bank-calibrated Rollout Allocation under Correlated Episodes). BRACE combines historical task evidence, uncertainty in task success rates, and a correlated reward model to forecast mixed-reward groups before allocating generation budget. Controlled harness experiments favor Discord, while live MCP experiments expose a retention-cost trade-off. At three Qwen3-VL model scales, BRACE exceeds the strongest plotted baseline peaks with fewer new training rollouts; historical-bank collection is counted separately. It also leads the compared methods on BFCL and NESTFUL without further training. Ablations probe the bank, estimator, and allocation score; prospective evaluation checks forecast calibration. These results support forecasting reward contrast before generation.
