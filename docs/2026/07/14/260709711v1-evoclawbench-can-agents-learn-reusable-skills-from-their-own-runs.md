# EvoClawBench: Can Agents Learn Reusable Skills from Their Own Runs?

- 区域：速读区
- 排名：10
- 匹配度：1.9/10
- 来源：arxiv
- 作者：Zhiyuan Peng, Xin Yin, Chenhao Ying, Zhe Cui, Zixiang Ding, Zhenhua Liu, Jiang Wu, Yuan Luo
- 机构：Zhejiang University, Hithink Research, Shanghai Jiao Tong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09711v1) · [PDF](https://arxiv.org/pdf/2607.09711v1)

## TLDR
EvoClawBench is a benchmark that evaluates whether LLM agents can learn reusable skills from their own past runs, revealing that such self-authoring is selective and cost-sensitive rather than universally beneficial.

## Abstract
Existing agent benchmarks primarily test task completion, tool use, or skill utility, but do not isolate whether a runtime can convert evidence from its own runs into reusable skills that improve fresh executions after authoring overhead. We introduce EvoClawBench, a benchmark for this closed-loop skill-learning question on repeated, fixture-backed tasks. EvoClawBench compares direct execution without skills, PreSkill authoring before execution, and PostSkill summarization from first-run evidence followed by a fresh second execution. The suite contains 100 tasks and 502 sub-problems across coding, data, office, security, operations, and domain-document workflows, with support for multiple agent runtimes. Experiments with OpenClaw and nanobot under local execution show that direct baseline performance is strongly runtime-dependent: OpenClaw remains below 20% across models, while nanobot ranges from 56.45% to 96.13%. Self-authored skills have mixed effects. nanobot GPT-5.4 stays above 96% in all modes and MiniMax-M2.7 improves from 90.97% to 94.50% under PostSkill, but nanobot DeepSeek-V4-Pro drops from 77.77% to 4.80% with PreSkill and 0.99% with PostSkill. OpenClaw shows similarly non-monotonic behavior, with some skill runs near baseline and others collapsing. These results indicate that learning reusable skills from an agent's own runs is selective and cost-sensitive, rather than an automatic benefit of adding skill authoring to an agent loop.
