# Real-Time Ground Normal Vector Estimation for Spherical Mobile 3D Mapping using LiDAR-Inertial Odometry

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Tim Schubert, Fabian Arzberger, Andreas Nüchter
- 机构：Julius-Maximilians-Universität Würzburg
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28701v1) · [PDF](https://arxiv.org/pdf/2610.28701v1)

## TLDR
The paper proposes two RANSAC-based ground normal vector estimation methods for spherical mobile 3D mapping—single-scan estimation and LIO-based estimation using a global 3D map—and shows that the LIO-based approach is significantly more accurate and robust and improves pose estimation when integrated into the motion model.

## Abstract
Accurate ground plane normal estimation is essential for odometry in spherical mobile mapping systems (SMMS), which face challenges from rapid rotations and limited ground coverage. We propose two RANSAC-based approaches: single-scan estimation with normal vector scoring and multi-step validation, and LiDAR-inertial odometry (LIO)-based estimation using a global 3D map. Evaluated across diverse real-world datasets against terrestrial laser scanner ground truth, results show that LIO-based estimation significantly outperforms single-scan methods in accuracy and robustness. Integrating ground normal estimates into the motion model improves pose estimation, supporting autonomous navigation in challenging and hazardous environments.
