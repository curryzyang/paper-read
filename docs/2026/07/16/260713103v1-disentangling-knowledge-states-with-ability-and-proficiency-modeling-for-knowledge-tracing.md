# Disentangling Knowledge States with Ability and Proficiency Modeling for Knowledge Tracing

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Duantengchuan Li, Yingqian Bi, Jinsong Chen, Rui Zhang, Mingwen Tong
- 机构：Hubei University of Technology, Wuhan University, Central China Normal University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13103v1) · [PDF](https://arxiv.org/pdf/2607.13103v1)

## TLDR
PAKT introduces a phase-aware decomposition of student learning sequences into ability and proficiency phases, modeled via a multi-branch Transformer with a type-aware readout module, to improve knowledge tracing performance by consistently outperforming baselines across six benchmarks.

## Abstract
Knowledge tracing (KT) aims to predict students' future performance by modeling their evolving knowledge states from historical interactions. Existing KT methods usually treat the raw interaction sequence as a unified behavioral process, overlooking the phase-specific nature of learning behaviors. Our preliminary observations show that students are more likely to correctly answer previously failed knowledge concepts after sufficient practice, suggesting a transition from ability-building to proficiency-oriented learning. Motivated by this, we propose Phase-Aware Knowledge Tracing (PAKT), a KT framework that decomposes student interactions into ability and proficiency phases based on the tailored decomposition mechanism. To effectively exploit the decomposed sequences, we design a multi-branch Transformer with a type-aware readout module to jointly capture phase-specific and holistic knowledge states. We further provide a causal analysis to reveal the confounding bias caused by entangling complex learning behaviors in phase-agnostic KT models. Extensive experiments on six public benchmarks demonstrate that our method consistently outperforms representative baselines, with a maximum AUC gain of 1.33% and an average gain of 0.82%.
