# A Unified Inertial Encoder for Human and Humanoid Motion

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Yutian Chen, Shibo Zhao, Rocky Duan, Karen Liu, Carmelo Sferrazza, Guanya Shi, Yuheng Qiu, Koushil Sreenath
- 机构：UC Berkeley, Carnegie Mellon University, Amazon FAR, Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10137v1) · [PDF](https://arxiv.org/pdf/2611.10137v1)

## TLDR
The paper proposes a unified inertial encoder trained on human and kinematically retargeted humanoid motion through a shared inertial interface, enabling zero-shot transfer to a physical Unitree G1 for accurate inertial odometry and language-grounded motion understanding without simulation, real-robot trajectories, or fine-tuning.

## Abstract
Learning humanoid state estimation and language-grounded motion understanding from robot recordings ties training coverage to the robot's motion repertoire. Human motion datasets offer broader coverage, yet transferring this knowledge requires overcoming differences in body geometry, sensing, and physical disturbances. To enable this transfer, we propose a unified inertial encoder whose shared inertial interface uses kinematic IMU synthesis to represent human and humanoid motion at corresponding body sites. Within this common input space, joint training on human and kinematically retargeted humanoid motion combines velocity estimation and motion--text alignment with continuous-time encoding and sensor and motion randomization. The resulting model transfers zero-shot to a physical Unitree G1 without physics simulation, real-robot training trajectories, or fine-tuning, achieving the lowest velocity error among evaluated methods across five datasets, including 0.099m/s on real G1. Its motion-description retrieval also extends to retargeted G1 motion categories observed only in human training, demonstrating how human motion knowledge can support the generalization of humanoid inertial odometry and language-grounded motion understanding.
