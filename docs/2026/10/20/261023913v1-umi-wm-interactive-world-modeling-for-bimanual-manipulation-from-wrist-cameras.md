# UMI-WM: Interactive World Modeling for Bimanual Manipulation from Wrist Cameras

- 区域：速读区
- 排名：9
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Jingxiang Guo, Haoyu Zhao, Xidong Zhang, Yuhang Zheng, Hao Wu, Chen Gao, Jianshu Zhou, Shuicheng Yan, Weihao Yuan
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23913v1) · [PDF](https://arxiv.org/pdf/2610.23913v1)

## TLDR
UMI-WM is an action-conditioned bimanual world model that jointly generates consistent left/right wrist-camera videos from UMI observations and per-arm camera/gripper actions, with a distilled four-step student that achieves strong action-following fidelity while generating paired views 6.9× faster than its teacher.

## Abstract
Universal Manipulation Interface (UMI) pairs wrist-camera videos with camera trajectories and gripper openings, providing scalable, robot-free data for learning how bimanual actions change a shared scene. Existing interactive world models, however, typically rely on text or single-camera control and struggle to follow each arm's actions while maintaining consistency between the two wrist views. We introduce UMI-WM, an action-conditioned bimanual world model that jointly generates both wrist views from observation history, per-arm relative camera poses, and gripper widths, with cross-view consistency, action following, and visual fidelity. UMI-WM injects each arm's actions into its own wrist stream, while sparse hub tokens exchange scene information between the two streams. Camera-aware geometry conditioning and camera-guided noise further support per-view motion control and cross-view geometric exchange. We adapt the model for block-causal generation and distill the 30-step Teacher into a Student with four denoising steps. We train UMI-WM on self-collected open-world and in-studio UMI recordings combined with public manipulation data. To evaluate action following, we use an inverse dynamics model (IDM) to recover relative camera poses and gripper widths from generated videos, and introduce Bimanual Action Fidelity (BAF) to measure how closely these recovered actions match the conditioning actions. UMI-WM achieves the best results on all five reference-video fidelity metrics and the best or competitive performance on VBench and WorldArena. The Teacher and Student outperform all compared baselines in action following, while the four-step Student generates paired wrist videos 6.9 times faster than the Teacher.
