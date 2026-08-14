# Learning Under Treatment-Induced Label Indeterminacy with Expert Annotations of Counterfactual Outcomes: A Case Study in Neurological Prognostication

- 区域：速读区
- 排名：13
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Xiaobin Shen, Chloe Y. H. Huang, Jonathan Elmer, George H. Chen
- 机构：Carnegie Mellon University, University of Pittsburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12477v1) · [PDF](https://arxiv.org/pdf/2608.12477v1)

## TLDR
A TLDR: This paper formalizes treatment-induced label indeterminacy in post-cardiac-arrest prognostication, proposes a split evaluation framework that separately assesses models on certain observed outcomes and expert-annotated counterfactual outcomes for uncertain cases, and shows that optimizing uncertain-case alignment can trade off against certain-case accuracy in ways standard metrics conceal.

## Abstract
Clinical prediction models are often developed as if the outcome of interest were cleanly observed for every patient. This assumption fails when treatment decisions make the clinically relevant outcome permanently unobservable. As a case study of this problem, we consider post-cardiac-arrest neurological prognostication using a cohort of 2,497 patients, including 1,429 patients whose outcomes were rendered indeterminate by treatment decisions. These patients with indeterminate outcomes were reviewed by independent clinical experts, who provided their guesses of counterfactual outcomes about what would have happened to the patients. We refer to these patients as uncertain cases. We also have patients for whom we observe their clinically relevant outcomes; we refer to these patients as certain cases. We propose a framework for evaluating prediction models that explicitly splits the evaluation between certain and uncertain cases. Here, we cannot easily evaluate both types of cases in a uniform manner as the available target labels differ. We then propose a simple prediction model that uses target labels from both certain and uncertain cases in a manner that allows us to trade off between them. Across the proposed neural model and a collection of tabular baselines, models with similar certain-case AUROC can nevertheless differ substantially in both certain-case Brier score and their probability estimates for uncertain cases. Improving alignment with target labels of uncertain cases for our proposed model generally comes at the cost of worse accuracy on certain cases, highlighting an explicit tradeoff that standard evaluation conceals. These results show that when treatment decisions determine whether clinically meaningful outcomes remain observable, conventional evaluation metrics can miss important failure modes in the very patients for whom prognostic support matters most.
