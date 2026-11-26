# Attributing Agentic Failure in Reasoning Vision-Language Models with Interactive 2D Environments

- 区域：速读区
- 排名：8
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Pranav Guruprasad, Sean Rivera, Helen Lu, Arushi Jain, Hangliang Ren, Harshvardhan Sikka
- 机构：Tufts University, Georgia Institute of Technology, Fig, Manifold Research Group
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33162v1) · [PDF](https://arxiv.org/pdf/2611.33162v1)

## TLDR
The paper introduces MultiNet v2.0-Gridworld, an interactive maze benchmark with independently controllable mechanisms and an exact BFS oracle to attribute vision-language models’ agentic failures to specific causes such as affordance discovery, ordering, execution, and recovery, revealing very low success and distinct failure modes across three models.

## Abstract
Agentic benchmarks report a success rate that confounds distinct causes of failure: misreading the environment, never working out how components of the environment operates, operating the components in the wrong order, and failing to recover from a mistake, each of which calls for a different fix. We present an early preview of MultiNet v2.0-Gridworld - an interactive maze environment built for attribution rather than ranking. Four different types of mechanisms, namely key-door pairs, switch-gate pairs, distractors and decoys, and ordered combinations of these mechanisms, can be added, modified, or removed independently while the renderer, the action space, and the scoring function stay fixed. A breadth-first search over the joint state of position, facing direction, inventory, and mechanism state gives every instance an exact optimal action count, which sets its difficulty and grades unfinished episodes. We fix the evaluation protocol on 15 held-out mazes over 540 episodes, then evaluate three vision-language models on 50 mazes. They solve 6 of 150 episodes, 45 of the 50 mazes were not solved by any model, and no episode containing a switch-gate mechanism was solved.
