# MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics

- 区域：速读区
- 排名：4
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Albert Wilcox, Frank Chang, Nhi Nguyen, Aishani Chakraborty, Jeremy A. Collins, Vaibhav Saxena, Benjamin Joffe, Siddharth Karamcheti, Animesh Garg
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05567v1) · [PDF](https://arxiv.org/pdf/2611.05567v1)

## TLDR
MESA is a reproducible evaluation framework and benchmark for language-conditioned robotic manipulation that isolates in-distribution performance and four axes of generalization—spatial configuration, object instance, object category, and subtask composition—using a scalable data-generation pipeline and both single-arm and bimanual suites to diagnose where and why current policies fail.

## Abstract
Despite growing interest in foundation models for robotic manipulation, systematic evaluation of their capabilities remains elusive. Existing benchmarks are either narrow and saturated, offering little signal on SOTA methods, broadly scoped, providing diversity at the cost of controlled experimentation, or require training on large, messy open-source datasets. We introduce MESA, an evaluation framework designed for precise, reproducible measurement of language-conditioned policy generalization. MESA provides five evaluation suites that isolate in-distribution performance and four distinct axes of generalization: spatial configuration, object instance, object category, and subtask composition, enabling researchers to diagnose where and why policies fail, not just whether they fail. To populate these suites at scale, we develop MESA-Gen, a pipeline for task and demonstration generation built by improving MimicGen. We instantiate the framework on two platforms and release both: the single-arm MESA suite, and BiMESA, the first large-scale benchmark for bimanual generalization. We evaluate seven baseline methods spanning diffusion policies, VLM-based approaches, and pretrained VLAs, finding that the strongest model achieves only 52% on MESA and 49% on BiMESA, providing meaningful signal while leaving ample room for progress. MESA rankings are broadly consistent with RoboArena scores, suggesting that MESA captures method-level differences relevant beyond simulation. Project website: https://pairlab.github.io/MESA.
