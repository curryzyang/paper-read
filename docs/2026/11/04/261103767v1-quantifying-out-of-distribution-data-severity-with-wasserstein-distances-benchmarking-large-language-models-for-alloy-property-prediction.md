# Quantifying out-of-distribution data severity with Wasserstein distances: benchmarking large language models for alloy property prediction

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：YuJie Liu, Dezhen Xue, Jun Sun, Xiangdong Ding, Zhibin Gao, Turab Lookman
- 机构：Xi’an Jiatong University, AiMaterial Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03767v1) · [PDF](https://arxiv.org/pdf/2611.03767v1)

## TLDR
This paper benchmarks general-purpose LLMs against domain-specific materials models for alloy property prediction and shows that a prior-guided hybrid LLM correction framework, combined with high-similarity data retrieval and Wasserstein-based out-of-distribution severity quantification, achieves accurate, cost-effective predictions where data quality dominates quantity.

## Abstract
As general-purpose Large Language Models (LLMs), such as Gemini and DeepSeek, exhibit increasingly advanced reasoning capabilities, a critical question arises: how do their property prediction abilities compare to those of domain-specific pretrained materials models? In this study, we evaluate predictions for Ti, steels, high-entropy alloy (HEA) and Al, demonstrating that general-purpose LLMs surprisingly outperform SteelBERT, MatSciBERT, and SciBERT. To further enhance performance, we introduce a hybrid approach that utilizes numerical priors from a prior model, such as CatBoost or SteelBERT, to guide the general LLMs (Deepseek V3.1, Gemini-2.5-Flash). By inputting these initial estimates from a prior model as prompts, the LLM acts as a reasoning corrector, achieving accuracy superior to the prior model and "unguided mode". Furthermore, we investigate the impact of data strategy using a similarity-based metric, revealing that data quality dominates quantity; using merely 5% of high-similarity reference data of training set as input yields performance similar to the results of using 100% of training set. Additionally, the LLMs demonstrate excellent uncertainty calibration, where self-reported "high" confidence strongly correlates with minimal deviation from ground truth. Our findings suggest that synergizing general-purpose LLMs with prior model numerical baselines and high-quality data curation creates a cost-effective and accurate paradigm for materials discovery, reducing the need for expensive domain-specific pretraining.
