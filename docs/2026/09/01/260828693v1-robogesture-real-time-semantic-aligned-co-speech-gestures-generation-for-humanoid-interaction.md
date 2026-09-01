# RoboGesture: Real-Time Semantic-aligned Co-Speech Gestures Generation for Humanoid Interaction

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Zifan Wang, Ziang Ren, Pengyang Shi, Zirui Wang, Chenghuai Lin, Tianze Wang, Zekun Qi, Liangliang Zhao, He Wang, Li Yi
- 机构：Harbin Institute of Technology, Beijing Institute of Technology, Shanghai Qi Zhi Institute, Peking University, Tsinghua University, Galbot Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28693v1) · [PDF](https://arxiv.org/pdf/2608.28693v1)

## TLDR
RoboGesture presents a robot-centric framework that co-designs data, modeling, and control to enable real-time, semantically aligned, and safety-aware co-speech gesture generation on physical humanoids, overcoming data scarcity, audio-neglect, and sim-to-real gaps via a large-scale collision-free dataset, a hierarchical semantic-acoustic aligner, anti-inertia CFG masking, and an MPC-based safety filter.

## Abstract
Enabling humanoid robots to respond to human speech with synchronized and semantically meaningful gestures is fundamental to natural human-robot interaction. However, this task faces three critical barriers: the scarcity of semantically rich datasets, the "modality eclipse" where models ignore audio cues in favor of kinematic inertia, and the sim-to-real gap regarding physical safety. We propose RoboGesture, a robot-centric framework that co-designs data, modeling, and control to power a complete interactive human-humanoid system in which the robot listens, responds, and gestures in real time. We first establish the RoboGesture dataset featuring over 300 gesture categories and develop an automated pipeline to synthesize large-scale collision-free, robot-specific audio-motion pairs. Our architecture features a Hierarchical Semantic-Acoustic Aligner that extracts multi-granular prosodic and semantic cues directly from raw audio tokens. These cues drive a Streaming Conditional Motion Generator based on a diffusion transformer with conditional flow matching. To ensure high responsiveness, we introduce Anti-Inertia CFG Masking, which prevents the model from collapsing into repetitive historical patterns by compelling it to proactively mine control signals from the audio modality. Finally, an MPC-based safety filter ensures real-time, collision-free execution on physical hardware. Experiments on a Unitree G1 humanoid demonstrate that RoboGesture generates safer, more rhythmic, and more semantically appropriate responses compared to state-of-the-art baselines.
