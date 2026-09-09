# AhaBench: Do Agents Learn from Prior Experience? A Benchmark for Long-Horizon Continual Learning

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Zerui Cheng, Jiawei Xu, Huacan Chai, Jiayang Sun, Pramod Viswanath, Maxm Pan
- 机构：Tsinghua University, Shanghai Jiaotong University, Princeton University, Tencent Hy, Hong Kong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05435v1) · [PDF](https://arxiv.org/pdf/2609.05435v1)

## TLDR
AhaBench is a benchmark suite that evaluates whether fixed language agents truly learn from prior experience over long horizons—via puzzle exploration, mathematical transfer, and simulated vending tasks—by measuring initial competence, post-experience performance, and the resulting "learning lift."

## Abstract
Modern language agents are expected to operate over long horizons: they ask follow-up questions, reuse worked examples, handle tool feedback, and adapt to delayed consequences. Most evaluations still reset the agent after a prompt or score only the final state of one trajectory. AhaBench asks a more operational question: when a fixed model receives useful experience, does its later behavior improve under a related evaluation condition where the obvious support has been removed, changed, or delayed? The suite contains three components. Aha-Puzzle tests no-hint exploration after solved hidden-state puzzles; Aha-Euler turns Project-Euler-style mathematical ideas into generated taught/held-out tasks with exact validators; and Aha-Vending, an open-source implementation inspired by Vending-Bench, tests whether a simulated vending agent remains profitable while handling delayed feedback and operational incidents. AhaBench reports a three-part scorecard: Initial Score measures starting competence, Post-Experience Score measures the later empirical outcome, and Learning Lift is their difference. This decomposition is the main empirical message: models that use visible support well, models that reach high post-experience scores, and models that improve most during a run are not always the same. On the common eight-model panel, Claude Opus 4.6 leads aggregate Post-Experience Score at 64.3 and aggregate Learning Lift at +25.8, with Gemini 3.1 Pro close behind at 63.4. The component results explain the split: puzzle traces raise supported scores but often fail to become no-hint exploration behavior; Aha-Euler full teaching reaches 78.6-100.0% while answer-only transfer ranges from 0.0 to 73.9%; and Aha-Vending separates profitable incident handling from bankruptcy and no-order failure. We release benchmark tasks, rubrics, validators, simulator code, and interfaces for evaluating new agents.
