# Auditing a Model-Hub Benchmark: Data Quality, Training Budgets, and Side Information in HuggingBench

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Michal Podstawski
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03727v1) · [PDF](https://arxiv.org/pdf/2611.03727v1)

## TLDR
TLDR: An audit of the HuggingBench model-hub benchmark reveals key data-quality flaws—especially item–entity identity violations in its knowledge graphs—along with truncated training budgets and neglected item text, and shows that fixing the KG join, extending training, and using simple text-plus-graph linear models substantially improve recommendation performance while releasing corrected artifacts and provenance practices.

## Abstract
Benchmarks built from model hubs combine interaction data, knowledge graphs (KGs) and resource documentation, but valid files do not ensure that these artifacts describe the same objects. Treating the release as a data product, we audit HuggingBench (SIGIR 2025), a benchmark for recommending Hugging Face resources, through data validation, a replication of its eleven recommendation methods and controlled experiments with three training seeds. In three of its four external KGs, the files pass key and range checks but violate the item-entity identity constraint on which KG recommenders rely. Correcting this join improves every KG-based method in every seed, by up to 73% in mean Recall@10, and consistently reverses ten of 27 comparisons between KG configurations. The protocol matters as well: the 100-epoch budget ends before early stopping in seven to eight of 29 validation-selected settings, and 21 of 23 such setting-seed pairs improve with a longer budget. The released item text, which no reported method uses, is the strongest signal: closed-form linear models with text and the item graph exceed the best reported Recall@10 by 18% while fitting in minutes on a CPU. Checks of other recommendation releases show that individually valid releases of one dataset can use incompatible identifiers. We release corrected files, mappings, validators and logs, and derive practices for preserving identity and provenance across the artifacts of benchmarks and model lakes.
