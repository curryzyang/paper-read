# EEGAgentBench: Benchmarking LLM Agents on Short- and Long-Horizon EEG Analysis

- 区域：速读区
- 排名：9
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Huyu Wu, Weining Weng, Yuchen Liu, Yiqiang Chen, Yang Gu
- 机构：Chinese Academy of Sciences, University of Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31632v1) · [PDF](https://arxiv.org/pdf/2609.31632v1)

## TLDR
EEGAgentBench is a unified benchmark for evaluating LLM agents on short- and long-horizon EEG analysis across six tasks and ten deterministic tools, revealing that current agents still struggle with sustained evidence accumulation and multi-step reasoning.

## Abstract
Electroencephalography (EEG) analysis is evolving from short-segment classification toward long-horizon interpretation that demands iterative evidence accumulation, multi-step reasoning, and coordinated use of specialized signal-processing tools. Although large language models (LLMs) have recently shown promise as autonomous agents for EEG analysis, existing EEG agentic evaluations remain fragmented, covering limited tasks over narrow temporal horizons with inconsistent protocols, and providing no comprehensive assessment of agents' reasoning, tool-use, and workflow construction capabilities. To address this gap, we propose \textbf{EEGAgentBench}, a unified benchmark for systematically evaluating LLM agents on short- and long-horizon EEG analysis. EEGAgentBench spans six representative EEG applications ranging from knowledge question answering to sleep staging. It encompasses signal durations from 2 seconds to nearly 23 hours, with prediction targets ranging from class labels to event intervals and epoch-level sequences. This design supports unified evaluation across knowledge reasoning, short-horizon interpretation, long-horizon event detection, and sequential understanding. The benchmark further provides 10 deterministic EEG analysis tools that expose only task-relevant signal measurements. Agents must therefore select tools autonomously, accumulate evidence iteratively, and construct multi-step workflows. For evaluation, we benchmark 29 frontier LLMs from 15 model families. Results demonstrate that EEGAgentBench effectively distinguishes agent capabilities beyond model scale and inference cost, while revealing substantial limitations of current LLM agents in long-horizon EEG analysis, particularly in sustained evidence accumulation and multi-step reasoning.
