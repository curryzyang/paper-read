# WorldBridge: Bridging Video and Action for Task Generalization in World Action Models

- 区域：速读区
- 排名：2
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Jun Cen, Yubo Guo, Hao Li, Liangkai Li, Yaoxu Lyu, Meng Wei, Zeqi Xiao, Sizhe Yang, Yuqiang Yang, Yifan Ye, Shanghang Zhang, Duo Zheng
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40748v1) · [PDF](https://arxiv.org/pdf/2610.40748v1)

## TLDR
WorldBridge is a World Action Model that separates video and action experts—linked by structured attention and trained with joint flow matching—to leverage broad video prediction for task generalization and sparse action supervision for grounding these predictions into executable robot behavior, achieving state-of-the-art manipulation performance.

## Abstract
Achieving the broad task generalization of embodied models in physical environments remains a central challenge in robot learning. We study this challenge in World Action Models (WAMs) through two complementary capabilities: video generalization, which predicts the visual evolution of new tasks, and action generalization, which translates these predictions into executable behavior through a video-to-action bridge. By varying video and action supervision for tasks outside an initial training set, we examine their respective contributions to task transfer. On RoboTwin 2.0, using only in-distribution video-action supervision yields a 25.07% success rate on out-of-distribution tasks. Introducing videos of these tasks without their action labels raises success to 55.90%, while adding just one action-labeled demonstration per task further improves it to 70.70%. These findings suggest that broader video coverage enables task transfer by leveraging existing inverse-dynamics capabilities, while even sparse action supervision further strengthens those capabilities. Guided by this perspective, we introduce WorldBridge, a WAM with separate video and action experts connected through structured attention and trained with joint flow matching. WorldBridge incorporates visual memory at two temporal scales and action forcing, alongside a unified data processing pipeline that standardizes and filters heterogeneous robot trajectories and egocentric hand-derived supervision. Across multiple manipulation benchmarks, WorldBridge achieves state-of-the-art performance among the compared methods, including 96.23% on RoboTwin 2.0 full data setting and 80.9% on clean to random setting, 82.8% on RoboCasa GR1 TableTop, and 57.6% on DOMINO Level-1. Our study highlights the complementary roles of video prediction and action grounding in developing robots that generalize across tasks.
