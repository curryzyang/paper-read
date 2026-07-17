# Local Additive Feature Attribution: A Mathematical Taxonomy and Reporting Checklist

- 区域：速读区
- 排名：7
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Rebecca Afriyie Sarpong, Daniel Commey
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14271v1) · [PDF](https://arxiv.org/pdf/2607.14271v1)

## TLDR
This paper presents a mathematical taxonomy and reporting checklist for local additive feature attribution, emphasizing that attribution results are meaningful only relative to the five specification choices (value function, reference, path, perturbation distribution, and conservation rule) and their underlying assumptions, which must be explicitly reported.

## Abstract
Feature-attribution methods are central to explainable artificial intelligence. Their assumptions are expressed in several mathematical languages: cooperative-game values, path integrals, gradient operators, perturbation distributions, and backpropagation rules. This survey proposes a common framework for local additive feature attribution. It organizes Shapley, path-based, gradient/backpropagation, perturbation, and CAM-style methods around five specification choices: value function, reference, path, perturbation distribution, and conservation rule. It then compares these methods through an axiom-by-method matrix and links common failure modes, including baseline sensitivity, off-manifold perturbations, sanity-check failures, adversarial manipulation, and method disagreement, to the assumptions that produce them. Finally, the survey proposes a ten-item reporting checklist for studies that use local additive attributions. The central message is that attribution results are meaningful only relative to the mathematical assumptions under which they are defined, and that those assumptions should be reported.
