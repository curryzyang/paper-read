# Measure Learning at Steady State: A BIRD-SQL Formula 1 Case Study

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Manoj Bajaj
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31640v1) · [PDF](https://arxiv.org/pdf/2609.31640v1)

## TLDR
On a longer BIRD-SQL Formula 1 schedule, measuring steady-state learning in the late window shows that naive full-context ICL cuts SQL probes but roughly doubles API cost and grows context to ~95k tokens, so short-horizon gains understate the exploration saving and miss the cost inversion, making unbounded ICL a poor candidate for a learning mechanism.

## Abstract
Continual Learning Bench scores learning as short-horizon gain versus a reset baseline and finds naive full-context ICL strongest among the memories it tested. We treat ICL as one learning system and score it on a longer shared-world schedule. Steady-state learning is the gap versus baseline on a pre-set late window (last 40 of 174 BIRD-SQL formula-1 questions). We split the score into exploration efficiency (SQL probes), task reward (hits), and delivery cost (API dollars and context size). On gpt-5.6-luna, late probes fall from 4.6-5.6 to 0.95 while hits rise only modestly and ICL context grows to about 95k tokens with cost roughly doubling. Short-horizon gain understates the late probe saving and misses the cost inversion, so we find that unbounded ICL is a poor candidate for the learning mechanism.
