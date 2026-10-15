# PMO-Dock: Benchmarking Docking, Specificity, and Generalization in Molecular Optimization

- 区域：速读区
- 排名：15
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Gor Simonyan, Tatevik Abrahamyan, Narek Abelyan, Tigran Fahradyan, Hrant Khachatrian
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19011v1) · [PDF](https://arxiv.org/pdf/2610.19011v1)

## TLDR
PMO-Dock introduces a standardized benchmark and protocol for docking-based molecular optimization across 25 tasks, including specificity, under strict oracle budgets, and shows that no method universally dominates and hyperparameter transfer is limited, enabling fair evaluation of generalization and sample efficiency.

## Abstract
The Practical Molecular Optimization (PMO) benchmark standardized evaluation in molecular optimization, but it is built on simple property-based oracles that do not capture structure-based drug design. As the field has moved to docking-based objectives, evaluation practice has become unstandardized, and different methods report results on different docking tasks, often without a shared protocol for fair comparison or sample-efficiency constraints. To address this, we introduce Practical Molecular Optimization for Docking (PMO-Dock), a benchmark and protocol for docking-based optimization consisting of 25 tasks covering hit generation, lead optimization, and a new specificity task requiring strong on-target binding while penalizing off-target interactions. The protocol separates model development from final evaluation: validation tasks are used for hyperparameter tuning, and test tasks are held out for final evaluation and are not used during development. Evaluation on the test tasks is done under a strict oracle budget to reflect realistic drug-discovery settings. We benchmark four diverse high-performing methods spanning different optimization paradigms, Saturn (reinforcement learning), GenMol (discrete diffusion), Genetic-guided GFlowNet, and ChemLlama (LLM-based evolutionary search). Our results show no universally best method across tasks, additional analyses of hyperparameter transfer (cross-task and cross-category) and sensitivity show that transfer is often limited and varies by method, motivating method-dependent selection strategies. This benchmark provides a concrete standard for evaluating generalization to unseen tasks and sample efficiency under a limited test-time oracle budget.
