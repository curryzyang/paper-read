# A Bayesian framework for the uncanny valley in humanoid robot design

- 区域：速读区
- 排名：8
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Shimon Honda, Rin Shibano, Hideyoshi Yanagisawa
- 机构：The University of Tokyo
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13060v1) · [PDF](https://arxiv.org/pdf/2607.13060v1)

## TLDR
This paper proposes a hierarchical Bayesian generative model that operationalizes uncanny valley heuristics into mathematical design variables, showing through simulations and a human experiment that prediction and observational uncertainty shape affinity toward humanoid robots.

## Abstract
The uncanny valley is a long-standing empirical rule in humanoid robot design: making robots more human-like can reduce, rather than increase, affinity. Yet existing guidelines, such as adopting robot-like appearances, avoiding excessive realism, and reducing cross-modal mismatches, remain difficult to use for algorithmic design because they are not expressed as manipulable variables. Here, we propose a hierarchical Bayesian generative model that operationalizes these guidelines as mathematical design variables. The model represents affinity toward humanoid robots as posterior-weighted negative category-conditional surprise and explains category ambiguity and perceptual mismatch as increases in surprise. It maps uncanny-valley mechanisms onto four variables: deviation from the predicted robot-category mean, inconsistency in human likeness across modalities, prediction uncertainty, and observational uncertainty. Simulations showed that category ambiguity and appearance--motion mismatch can produce affinity reductions, and that uncertainty reshapes the valley. In a human-subject experiment with robot--human morphing images, we manipulated prediction uncertainty using blurred prior robot stimuli and observational uncertainty using blurred evaluation stimuli. Increased observational uncertainty attenuated the decrease in familiarity ratings at intermediate human likeness, whereas low prediction uncertainty increased ratings for robot-like appearances. This framework turns empirical uncanny-valley heuristics into a computational basis for algorithmically evaluating and optimizing humanoid robot appearance and behavior.
