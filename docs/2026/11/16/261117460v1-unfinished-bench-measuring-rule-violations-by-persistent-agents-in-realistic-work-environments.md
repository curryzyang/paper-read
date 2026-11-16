# Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Seunghyun Lee, Jaehui Hwang, Dongyoon Han, Sangdoo Yun
- 机构：NAVER AI Lab
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17460v1) · [PDF](https://arxiv.org/pdf/2611.17460v1)

## TLDR
**TLDR:** Unfinished-Bench is a 97-scenario benchmark showing that persistent autonomous agents in realistic work environments violate rules embedded in internal documents more often than identical rules stated by the user—and that persistence itself increases rule violations—highlighting the need to evaluate persistence-driven risks.

## Abstract
AI agents are increasingly equipped with persistence toward task completion to run delegated work autonomously for long periods, under many unstated constraints from internal documents and other people's authority. When completion requires violating a rule, the agent must decide alone, yet benchmarks of instruction-rule conflicts state the rule in the prompt or keep it hidden and do not evaluate persistence. We present Unfinished-Bench, a benchmark that gives models persistence in autonomous runs without a user, in realistic work environments with embedded rules. In each of its 97 scenarios across 7 organizations and 7 risk categories, the goal and the rule cannot both hold. We find that persistence raised violations of a rule in an internal document from 32.2% to 43.6%, five times the 8.5% for the same rule stated by the user. Of the document-rule violations, 98.3% occurred after the rule was displayed, and in 89% of a judged sample the agent first wrote down the rule. Violations of rules placed in the environment without user oversight can lead to serious incidents, so persistence-driven risks need to be evaluated. Benchmark documentation: https://francis21c.github.io/unfinished-bench/
