# MicroSplat: Towards Automating 3D Small-Scale Reconstruction

- 区域：速读区
- 排名：15
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Roman Mineyev, Robert Azarcon, Suvrat Jain, Chuizheng Kong, Shreyas Kousik
- 机构：Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23899v1) · [PDF](https://arxiv.org/pdf/2610.23899v1)

## TLDR
MicroSplat automates sub-millimeter 3D Gaussian Splatting reconstruction of small objects by pairing a robotic manipulator with a low-cost microscope and running an unattended capture-to-model pipeline that uses robot-pose initialization and per-view focus stacking, which outperforms blur-aware 3DGS methods.

## Abstract
Reconstructing sub-millimeter detail of small objects underpins tasks such as circuit-board defect detection, specimen digitization, and archiving. 3D Gaussian Splatting (3DGS) makes photorealistic reconstruction possible from posed images alone, but macro optics violate two conditions it depends on. The field of view (FOV) and the depth of field (DoF) shrink to millimeters, so viewpoint error can take a sample out of frame, and only a thin focal plane is sharp in frame. Existing automated macro-capture rigs handle the shallow DoF with per-view focus stacking, but typically rely on classical photogrammetry and offline, human-in-the-loop processing. We present MicroSplat, which generates a 3DGS using a low-cost consumer microscope on a manipulator arm. After a single up-front object-localization step, the system runs unattended. It performs calibration, plans collision-free viewpoints, captures and fuses a focal stack at each viewpoint, segments the object across all views, and optimizes a 3DGS model warm-started with the arm's own poses. We further compare against blur-aware 3DGS methods, which infer sharp scenes from defocused images, and find that measuring sharpness with a controlled focal sweep outperforms inferring it. We provide real and synthetic datasets (including robot and camera parameters) and the fitted 3DGS reconstructions.
