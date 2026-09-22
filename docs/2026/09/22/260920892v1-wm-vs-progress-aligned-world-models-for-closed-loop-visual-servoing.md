# WM-VS: Progress-Aligned World Models for Closed-Loop Visual Servoing

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Guanzhong Sun, Junyi Ma, Yixuan Zhou, Yuxuan Wu, Yanzi Miao, Hesheng Wang
- 机构：China University of Mining and Technology, Shanghai Jiao Tong University, Shanghai Innovation Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20892v1) · [PDF](https://arxiv.org/pdf/2609.20892v1)

## TLDR
WM-VS introduces a target-centric progress-aligned world model that uses offline DINOv2 correspondences to define a signed 4D servo coordinate, aligning action-conditioned latent transitions with task progress to train a reactive RGB-only closed-loop visual servoing policy that achieves high reaching and retention accuracy on a real 7-DoF system.

## Abstract
Closed-loop visual servoing requires predictions that indicate whether an action reduces task error, not only whether the action is plausible. We call this gap the prediction-control mismatch and introduce WM-VS, a target-centric progress-aligned world-model framework for closed-loop visual servoing. Offline target-region DINOv2 correspondences define a signed four-dimensional servo coordinate for translation, scale, and in-plane rotation. Stage 1 aligns action-conditioned latent transitions with this coordinate; Stage 2 freezes the world model and trains a reactive joint-velocity policy with action imitation, consequence supervision, and short imagined rollouts that favor error contraction. Deployment is RGB-only and reactive, without online trajectory optimization. On a real 7-DoF eye-to-hand system, WM-VS reaches a corner RMSE no larger than 10 percent of its initial value in 30/30 trials and retains this criterion at the final valid frame in 25/30 (83.33 percent). Removing future-error alignment reduces retention to 26.67 percent. The learned progress signal agrees with an external AprilTag corner error not used for training or control (mean Spearman rho = 0.8778). Without retraining, two unseen 3D targets achieve translation-error reductions of 86.48 percent and 90.27 percent and rotation-error reductions of 70.01 percent and 65.70 percent. These results link progress-aligned action consequences to repeated closed-loop correction and transfer. Code and data will be released as open source.
