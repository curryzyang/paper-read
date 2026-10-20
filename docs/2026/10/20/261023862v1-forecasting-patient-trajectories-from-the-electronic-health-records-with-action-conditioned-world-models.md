# Forecasting Patient Trajectories from the Electronic Health Records with Action-Conditioned World Models

- 区域：速读区
- 排名：10
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Simon A. Lee, Jiahang Hank Sha, Soomin Chung, Kai Akamatsu, Eran Halperin, Jeffrey N. Chiang
- 机构：UCLA, New York University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23862v1) · [PDF](https://arxiv.org/pdf/2610.23862v1)

## TLDR
The paper introduces an action-conditioned latent world model for EHR data that separates patient states from clinical actions and learns a state-dependent linearized transition operator to forecast and simulate patient trajectories, achieving competitive downstream performance with a much smaller parameter footprint than large EHR foundation models.

## Abstract
We introduce a predictive world model for electronic health records (EHR) that represents patient histories as action conditioned latent trajectories. Rather than modeling clinical events solely through autoregressive token prediction, our framework explicitly separates patient states from observed clinical actions and learns their evolution through a state and action conditioned transition operator. At its core is a state dependent linearization predictor that propagates local changes in latent patient state, enabling time resolved prediction, multi step rollout, and action conditioned simulation. Empirically, we show that generated latent trajectories preserve downstream predictive signal, temporal structure, and subgroup level statistical relationships present in encoder derived representations. We further decode free running rollouts into the original clinical feature space and evaluate future clinical measurements against observed values using task matched forecasting baselines, demonstrating that the learned dynamics retain predictive information beyond latent space agreement. Across binary classification and time to event tasks, EHR WM achieves competitive, though task dependent, performance relative to substantially larger EHR foundation models while using a 30x smaller parameter footprint. Finally, perturbing observed action sequences produces corresponding changes in generated trajectories, demonstrating the action sensitivity of the learned dynamics. Together, these results support world modeling as a complementary framework for learning explicit, time indexed representations of patient evolution from longitudinal EHR.
