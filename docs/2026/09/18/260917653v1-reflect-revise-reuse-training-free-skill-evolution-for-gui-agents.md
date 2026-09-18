# Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents

- 区域：速读区
- 排名：12
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Bofan Chen, Boxuan Zhang, Fei Tang, Zhengxi Lu, Yong Du, Tongbo Chen, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- 机构：UESTC, Zhejiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17653v1) · [PDF](https://arxiv.org/pdf/2609.17653v1)

## TLDR
EvoSkill-GUI is a training-free framework that enables GUI agents to evolve structured, editable skill packages at deployment time through a reflect–revise–reuse loop, improving task success on MobileWorld, AndroidWorld, and OSWorld without additional training.

## Abstract
GUI agents execute long-horizon tasks on dynamic graphical user interfaces, where pop-ups, delayed loads, and relocated widgets routinely invalidate plans fixed before execution. Recent agent-skill frameworks encapsulate reusable procedural knowledge to mitigate this, yet existing skill designs are largely developed without targeting GUI execution dynamics and treat skills as static artifacts produced before deployment rather than living procedural knowledge that improves through it. We argue that what GUI agents need is not better static skills, but skills that can be revised from execution feedback at deployment time, without additional training. We propose \textbf{EvoSkill-GUI}, a training-free framework in which each skill is a structured multi-file package containing retrieval metadata, executable plans, backup localization, failure-recovery rules, accessibility utilities, and failure cases. EvoSkill-GUI operates through a \textbf{\emph{reflect-revise-reuse}} loop: the executor performs instant in-rollout revisions, an isolated critic diagnoses failed trajectories under strict information isolation, and the executor edits specific skill files through a restricted tool interface. Across MobileWorld, AndroidWorld, and OSWorld, three mainstream GUI benchmarks spanning mobile and desktop platforms, EvoSkill-GUI consistently improves multiple base models without any training, with maximum gains of $+16.2\%$, $+6.0\%$, and $+10.5\%$ respectively, and evolved skill libraries continue to benefit related tasks rather than being rebuilt from scratch. Our code is available at https://github.com/ZJU-REAL/EvoSkill-GUI.
