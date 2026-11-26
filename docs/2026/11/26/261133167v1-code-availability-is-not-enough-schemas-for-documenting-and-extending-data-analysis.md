# Code availability is not enough: schemas for documenting and extending data analysis

- 区域：速读区
- 排名：13
- 匹配度：3.1/10
- 来源：arxiv
- 作者：H. Sherry Zhang, Roger D. Peng
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33167v1) · [PDF](https://arxiv.org/pdf/2611.33167v1)

## TLDR
The paper proposes a natural-language schema for documenting a data analysis as a sequence of decisions, enabling LLMs to generate and validate analysis code and extend results into alternative multiverses—showing that reproducibility requires more than code availability.

## Abstract
A data analysis involves a sequence of decisions, from data cleaning to model specification, each of which can affect the reported result. Reproducing that result is not the same as understanding the sequence of decisions that produced it and the reasons for each: the code mixes those decisions with implementation details, while the manuscript states the major decisions and their rationale but scatters them across its sections and often leaves out the minor ones. A reader may then ask how the result would change under a different decision: the question itself is easy to pose, but implementing it is often non-trivial in practice. In this work, we propose a schema that represents a data analysis as a collection of decisions in natural language, from which large language models (LLMs) can generate and validate analysis scripts directly. This workflow can also expand a single analysis into a full multiverse of alternatives, specified in an alternative file, ready for comparison. We demonstrate the proposed workflow in two applications. In the first, we construct a schema for a published regression analysis of heaped smoking data and show that it reproduces the reported estimates, and that a reviewer-suggested alternative can be specified through the alternative file and turned into code automatically. In the second, where no schema is provided, we show how the workflow serves instead as a reproducibility check, applied to the many-analysts football study. As an intermediate representation between the manuscript and code scripts, our schema gives a self-contained account of an analysis and makes it extensible from a reader's perspective.
