# Towards Principled Continual Anomaly Detection: A Systematic Framework and Benchmark Scenarios

- 区域：速读区
- 排名：12
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Kamil Faber, Mateusz Smendowski, Roberto Corizzo
- 机构：AGH University of Krakow, American University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18289v1) · [PDF](https://arxiv.org/pdf/2607.18289v1)

## TLDR
This paper introduces a systematic framework for constructing and validating continual anomaly detection benchmark scenarios from tabular data, delivering five principled scenarios with diverse task orderings from three cybersecurity datasets.

## Abstract
Continual anomaly detection (CAD) studies how models can adapt to evolving data distributions while retaining performance on previously observed regimes. CAD benchmarks, however, depend critically on how tasks are defined, filtered, ordered, and validated. In tabular domains, task boundaries are rarely given, and arbitrary splits can create unlearnable, redundant, or overly transferable tasks that obscure genuine continual-learning behavior. To this end, we introduce a systematic framework for reproducible benchmark scenario design from existing tabular anomaly-detection datasets. The framework discovers candidate tasks, filters unsuitable tasks, and derives principled orderings that expose diverse dynamics. The framework allows us to deliver five benchmark-ready scenarios from three large-scale cybersecurity anomaly detection datasets, yielding both single-dataset and multi-dataset CAD settings.
