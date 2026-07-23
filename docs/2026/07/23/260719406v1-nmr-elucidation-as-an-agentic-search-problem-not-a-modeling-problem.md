# NMR Elucidation as an Agentic Search Problem, Not a Modeling Problem

- 区域：速读区
- 排名：9
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Irina Espejo Morales, Damon Hinz, Marvin Alberts, Geraud Krawezik, Haewon Jeong, Shirley Ho
- 机构：Princeton University, New York University, Flatiron Institute, Independent, PolymathicAI, University of California, Santa Barbara
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19406v1) · [PDF](https://arxiv.org/pdf/2607.19406v1)

## TLDR
By reframing NMR structure elucidation as an agentic search problem guided by a frozen LLM with domain-specific tools rather than an end-to-end modeling task, the proposed system achieves top-1 accuracy comparable to or exceeding that of graduate students and outperforms zero-shot deep learning models on several experimental datasets.

## Abstract
Structural elucidation from Nuclear Magnetic Resonance (NMR) data remains a fundamental bottleneck across chemistry, materials science, and biology. We demonstrate that an agentic AI system can perform this task at a level comparable to graduate-level chemistry students. Instead of training a model to directly map spectra to structures, we build a single autonomous agent, backed by a frozen LLM, that interacts with a curated environment with access to domain-specific processing tools, validation checks, tabulated chemical shifts, and instructions that outline the stepwise nature of a chemist's thinking process. On the Alberts dataset, our agent elucidates structures with a top-1 accuracy of 71%, comparable to the performance of graduate students at 66% top-1 accuracy. On the van Bramer and AstraZeneca datasets, our agent achieved 80% and 20% top-1 accuracy respectively, outperforming zero-shot end-to-end deep learning models which were trained on large datasets of simulated spectra. These results show that reframing NMR elucidation as an LLM-guided constrained search, rather than a modeling task, yields substantial gains and suggests a path toward multi-step orchestration frameworks that integrate a variety of tools, models, and domain knowledge to assist in automating spectroscopic analysis.
