# From Concepts to Actual Causes: Toward Closing the Concept-Malfunction Gap in Robot Foundation Models

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Gihyuk Ko
- 机构：NC AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00155v1) · [PDF](https://arxiv.org/pdf/2611.00155v1)

## TLDR
This position paper argues that pinpointing which internal components caused a specific robot foundation model failure requires reformulating fault isolation as a well-specified actual-causality query—covering temporal scope, realizable counterfactuals, searched contingencies, and rollout-level outcomes—and shows that current mechanistic interpretability methods misspecify these conditions, potentially producing conflicting causal verdicts, before outlining four open research tasks to close the concept–malfunction gap.

## Abstract
Post-incident analysis of a robot foundation model poses a singular causal question: which internal components caused this failure, and to what degree? Mechanistic interpretability (MI), however, establishes general causal claims by decoding the concepts a policy has learned, yet knowing which concepts are encoded is insufficient for identifying the actual cause of a specific incident. In this position paper, we analyze this concept-malfunction gap by posing fault isolation in the framework of actual causality. Specifically, we formalize a fault-isolation query as a tuple of intervened internal components, counterfactual values, contingencies, and read-outs, and lay out conditions for it to be well-specified. Through this lens, we identify shortcomings of current MI approaches: they assume fixed contingencies and read out only immediate effects, letting backups obscure actual causes. We demonstrate on a toy example that these shortcomings can lead to conflicting verdicts. Lastly, based on the well-specification conditions, we outline four open research tasks toward closing the gap.
