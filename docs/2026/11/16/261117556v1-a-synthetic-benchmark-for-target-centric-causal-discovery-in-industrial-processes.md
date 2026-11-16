# A Synthetic Benchmark for Target-Centric Causal Discovery in Industrial Processes

- 区域：速读区
- 排名：10
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Angelo Ziletti
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17556v1) · [PDF](https://arxiv.org/pdf/2611.17556v1)

## TLDR
The paper presents a modular synthetic benchmark based on a two-level structural causal model of batch production that enables controlled, target-centric variation of causal-discovery difficulty and evaluates eight methods, showing that performance degrades as difficulties combine in ways consistent with each method’s assumptions.

## Abstract
Causal discovery promises to find which recorded variables drive a process target such as product quality, yield or energy use. Process data with known causes are rare, and in existing benchmarks the difficulty of identifying the causes of a target is either fixed by the recorded data or set for the whole graph. We present a synthetic benchmark for target-centric causal discovery in industrial processes. Its generator is a two-level structural causal model inspired by batch production, assembled from components that each model one phenomenon of process data, such as a control loop or a delayed effect. The graph is built around the target: without sensor error, every non-cause can be distinguished from the direct causes by conditioning on them or by time order. Each component is set independently, so the difficulty can be varied one condition at a time. We evaluate eight methods, from association measures to effect estimation, with an error analysis by the role of the selected candidate; all degrade as the difficulties combine, each in a way consistent with its assumptions.
