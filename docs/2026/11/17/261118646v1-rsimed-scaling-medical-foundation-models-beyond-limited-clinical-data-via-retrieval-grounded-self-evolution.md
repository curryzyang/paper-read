# RSIMed: Scaling Medical Foundation Models beyond Limited Clinical Data via Retrieval-Grounded Self-Evolution

- 区域：速读区
- 排名：8
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Wei Dai, Qianchu Liu, Guanghui Qin, Xing Han, Tristan Naumann, Sheng Zhang, Paul Pu Liang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18646v1) · [PDF](https://arxiv.org/pdf/2611.18646v1)

## TLDR
RSIMed is a retrieval-grounded, self-evolving medical foundation model pipeline in which a task proposer co-evolves with a diagnostic solver to generate source-grounded clinical questions from real records, enabling scalable rare-disease diagnosis beyond limited labeled data and outperforming larger off-the-shelf models at lower inference cost.

## Abstract
Rare diseases are hard to diagnose, and the labeled clinical records needed to train models for them are few, private, and slow to extend, since a specialist must read every case. A model that writes its own training tasks could learn beyond these records, but no program can check a model-written diagnosis, and a wrong answer key corrupts training. To tackle this dilemma between data scarcity and difficulty of data annotations, we introduce RSIMed, Recursive Self-Improvement in Medicine, one of the first self-evolving pipelines in which a task proposer co-evolves in context with a diagnostic solver on real clinical records. Seeded by training admissions, a frozen copy of the solver writes each clinical question from retrieved medical evidence, so its answer rests on a source, and steers topics and difficulty toward what the solver still gets wrong. On rare-disease diagnosis from MIMIC-IV admissions, the accuracy of RSIMed-27B grows linearly with training compute, while a static pool of generated tasks collapses. Without any external model, RSIMed-27B and RSIMed-9B reach 0.516 and 0.488 diagnostic accuracy, above every off-the-shelf GPT-5.6 setting, whose best reaches 0.399 at 38 times the inference cost of RSIMed-27B. Tasks written by four external teachers, including GPT-5.5, train a less accurate diagnostician than the solver's own. Trained only on diagnosis, RSIMed-RL-27B also improves on the physician-written tasks of HealthBench Professional, from 0.291 to 0.303 in adjusted score.
