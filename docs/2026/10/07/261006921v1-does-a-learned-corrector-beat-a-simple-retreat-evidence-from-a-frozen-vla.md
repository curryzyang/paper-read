# Does a Learned Corrector Beat a Simple Retreat? Evidence from a Frozen VLA

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Chenchao Sheng, Zhuang Jiang, Liuhaichen Yang, Ningwei Bai, Zezhi Tang
- 机构：University College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06921v1) · [PDF](https://arxiv.org/pdf/2610.06921v1)

## TLDR
In a paired, placebo-controlled evaluation of a frozen π0.5 VLA across four RoboTwin tasks, a learned runtime corrector significantly improved success only on beat_block_hammer (+13.5 pp) and was not detectably better than a simple scripted retreat, showing that most apparent recovery gains reflect base-policy variability and task-specific recoverability rather than the learned corrector’s complexity.

## Abstract
Before deploying runtime recovery for a frozen vision-language-action (VLA) policy, one must establish that an intervention improves success beyond ordinary run-to-run variation and that its complexity adds value over a simple action. We evaluate these questions on frozen $π_{0.5}$ across four RoboTwin tasks. For each test seed, we pair rollouts with and without correction and include a same-seed base-policy re-run as a placebo. Seed-cluster intervals and prespecified comparison rules assess net gains against stochastic outcome changes. Across 3,888 paired episodes, the full pipeline raises success on beat_allowbreak block_allowbreak hammer by $+13.5$\,pp (95\% interval $[+9.4,+17.7]$), with no detectable gain on the other three tasks at the deployed weight. Among failed base episodes on the responsive task, $43.2\%$ succeed on a plain re-run, compared with $63.5\%$ after correction; many nominal rescues therefore reflect the base policy's own variability. A fixed-time trigger and scripted return to an earlier joint configuration produce a net gain with no detected difference from the learned pipeline across two rounds, although our prespecified equivalence criterion is not met consistently. Pausing and a constant-action control do not yield comparable gains. On this benchmark, the decision to intervene depends strongly on the task, and a paired placebo plus a simple retreat baseline are needed to establish what learned correction contributes.
