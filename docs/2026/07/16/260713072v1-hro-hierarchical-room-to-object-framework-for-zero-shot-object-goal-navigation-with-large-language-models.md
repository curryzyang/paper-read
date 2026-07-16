# HRO: Hierarchical Room-to-Object Framework for Zero-Shot Object Goal Navigation with Large Language Models

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Luyuan Jia, Yinfeng Yu
- 机构：Xinjiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13072v1) · [PDF](https://arxiv.org/pdf/2607.13072v1)

## TLDR
The HRO framework introduces a hierarchical, LLM-driven coarse-to-fine approach for zero-shot object goal navigation, using room-type inference and semantic affinity scoring to outperform existing flat reasoning methods on Gibson and HM3D datasets.

## Abstract
Zero-shot object-goal navigation aims to enable an intelligent agent to explore and navigate to objects of unknown categories in an unfamiliar environment without specific target training. In zero-shot navigation tasks, pre-trained large models are usually employed to leverage their prior knowledge for guiding the agent's navigation. However, existing zero-shot object-goal navigation methods based on large language models (LLMs) merely utilize LLMs as flat reasoning tools to directly associate objects or regions. They lack the hierarchical spatial cognition modeling of human-like room semantics to object localization, which leads to strong blindness in exploration, insufficient accuracy in semantic association, and failure to fully unleash the common-sense reasoning potential of LLMs. This paper proposes an LLM-driven hierarchical room-to-object (HRO) framework for zero-shot object-goal navigation, which guides the agent to explore and navigate to the target object in a coarse-to-fine manner. Experiments on Gibson and HM3D datasets verify that our HRO framework achieves superior success rate and generalization over existing LLM-based methods, underscoring LLMs' strong potential for zero-shot object-goal navigation.
