# Temperon: Full-Time SAM Quality at a Third Less Wall-Clock

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Stamatis Mastromichalakis
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17575v1) · [PDF](https://arxiv.org/pdf/2609.17575v1)

## TLDR
Temperon matches full-time sharpness-aware minimization (SAM) accuracy at roughly a third less wall-clock by using plain SGD for the first 43% of training, then scheduling a single hand-off of the entire final cosine anneal to a SAM-wrapped Muon refiner, with the same allocation law transferring to GPT-2 pretraining and GLUE fine-tuning.

## Abstract
Sharpness-aware minimization (SAM) doubles the cost of every training step, yet its benefit concentrates where training ends. We study where an expensive training mode should be spent and propose Temperon: a plain-SGD explorer for the first 43% of the epoch budget, then one scheduled hand-off that gives the entire final cosine anneal to a SAM-wrapped Muon refiner. On CIFAR-10/100, SVHN and Tiny ImageNet (five seeds, times reported as epochs-to-target times an idle-GPU-calibrated epoch cost), Temperon matches the best full-time-SAM recipe on accuracy everywhere while reaching the hardest common target 35%, 34% and 32% sooner on three of the four, and sits a tier above the published SAM+SGD recipe at level cost. Ablations make the attribution exact: the Muon refiner is worth +0.85pp with everything else fixed; the explorer's shape and its restarts are worth nothing, and we withdraw them as contributions. Re-running the closest rival, late-phase SAM, at matched budget shows the frontier: it is fastest to every mid-level target, but the tier the Muon refiner buys (0.83 on CIFAR-100, 0.97 on CIFAR-10) is reached by no SGD-refined method in any seed, and on Tiny ImageNet, where Muon buys no tier, the rival simply wins -- the measured boundary of the method. The allocation law transfers to GPT-2 pretraining (full-SAM quality at -29% wall-clock) and GLUE fine-tuning (never worse than full-time SAM at a third of its SAM cost). Two constants organize the economics: skipping SAM early buys a fixed credit, and a Muon epoch costs 1.50x a SAM+SGD epoch on all four datasets. Finally, the hand-off cannot be timed from the trajectory: under cosine schedules the accuracy curve is plateau-then-surge, so the information lives in the schedule, making the scheduled switch principled rather than convenient. Code and a pip-installable implementation are released.
