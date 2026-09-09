# Observability Analysis of Joint Steering and Extrinsic Calibration

- 区域：速读区
- 排名：3
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Subodh Mishra
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05498v1) · [PDF](https://arxiv.org/pdf/2609.05498v1)

## TLDR
TLDR: This paper analytically shows, via Lie-derivative-based nonlinear observability analysis of a planar bicycle model, that jointly estimating vehicle pose, planar LiDAR extrinsics, and steering-angle bias becomes fully locally weakly observable only when combining straight and curved motion, whereas stationary, straight-line, or constant-curvature motion alone leaves unobservable degeneracies.

## Abstract
This technical report studies the local weak observability of a planar bicycle-model vehicle when vehicle pose, planar LiDAR extrinsic calibration, and steering-angle bias are estimated jointly. A Lie-derivative-based nonlinear observability analysis is used to examine stationary, straight-line, constant-curvature, and combined straight-plus-arc motion. The resulting observability matrices and nullspaces describe how pose, LiDAR translation and yaw offsets, and steering bias become coupled under different motion primitives. Stationary motion and individual motion primitives retain unobservable directions, whereas the combination of straight and curved motion removes the identified degeneracies and yields full local weak observability of the seven-state system. The analysis provides a theoretical basis for selecting calibration trajectories that sufficiently excite both steering and sensor-extrinsic parameters.
