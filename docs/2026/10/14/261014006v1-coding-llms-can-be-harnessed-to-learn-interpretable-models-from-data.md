# Coding LLMs Can Be Harnessed to Learn Interpretable Models from Data

- 区域：速读区
- 排名：8
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Aditya Kumar, Cassandra A. Cohen, William W. Cohen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14006v1) · [PDF](https://arxiv.org/pdf/2610.14006v1)

## TLDR
A simple harness that repeatedly prompts coding LLMs to generate the next rule in a rule set can learn interpretable classifiers from data, outperforming state-of-the-art rule-learning methods on tabular and text tasks while introducing a new class of coding benchmarks.

## Abstract
Since compact, interpretable classifiers correspond to simple programs, it is natural to ask if LLM-based coding agents can be used to learn interpretable models from data. In this paper we present a simple harness that repeatedly prompts a coding LLM to produce the next rule in a rule set, given a sample of labeled examples. We show that this approach is competitive with, and often superior to, state-of-the-art rule-learning methods on tabular data, especially with small training sets, and wins by large margins on text, including against another LLM-based rule learner; that this approach outperforms standard harnesses, and that the approach immediately leads to new kinds of interpretable models, since coding agents are not restricted to search a highly restricted hypothesis space. In addition to the advances made in learning interpretable models, these results are of interest because they introduce a new class of coding benchmarks - construction of interpretable classifiers - which includes quantitative measurements of output quality (i.e., test-set error) and existing mature ``specialist coding algorithms'' (i.e., existing learning methods).
