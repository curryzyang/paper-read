# MoMo: Dial Motion Mode in Robot Manipulation with Spatiotemporal Action Tokenization

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Yuhan Hu, Hugues Thomas, Peide Huang, Mouli Sivapurapu, Benoit Landry, Arto Kivila
- 机构：Apple
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26315v1) · [PDF](https://arxiv.org/pdf/2607.26315v1)

## TLDR
MoMo introduces a two-stage imitation-learning framework with spatiotemporal action tokenization that enables compositional generalization of motion modes—steady, dynamic, or intermediate—across unseen robot manipulation tasks.

## Abstract
To operate effectively across diverse contexts, robots must not only perform manipulation tasks accurately but also adapt how their actions unfold to the task, object, and interaction setting. We ask whether this execution-level variation can be learned as a reusable behavioral factor shared across tasks. We present \textbf{MoMo}, a two-stage imitation-learning framework consisting of a spatiotemporal action tokenizer and a behavior-cloning transformer that takes task and a continuous motion-mode condition as inputs. Across six real-robot manipulation tasks, varying this condition produces steady, dynamic, and intermediate behaviors that human raters can distinguish and that differ in joint speed, acceleration, and end-effector approach pitch. On tasks demonstrated in only one mode, MoMo transfers the unseen requested mode while largely preserving task success. Together, these results provide evidence of compositional generalization to unseen task--mode combinations and show that motion mode can be reused across tasks to control how a manipulation skill is performed.
