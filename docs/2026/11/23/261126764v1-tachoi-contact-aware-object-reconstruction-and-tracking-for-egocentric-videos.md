# TacHOI: Contact-Aware Object Reconstruction and Tracking for Egocentric Videos

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Jackson Codd, Haoyu Li, Xianyi Cheng
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26764v1) · [PDF](https://arxiv.org/pdf/2611.26764v1)

## TLDR
TacHOI is a training-free framework that fuses tactile contact with monocular egocentric video to jointly reconstruct and track hands and unknown objects—using the calibrated hand as a physical ruler to resolve scale–depth ambiguity without templates or depth sensors—reducing object pose error from 15.6 to 3.6 cm on ARCTIC and achieving 2.8 cm on HO3D.

## Abstract
Egocentric videos offer a scalable source of human demonstrations for robot learning. However, recovering metric object geometry and motion from monocular video is hindered by scale-depth ambiguity and hand-induced occlusion, while image-derived contact and shape priors alone cannot uniquely determine metric scale. We introduce TacHOI, a training-free framework that integrates tactile contact with monocular vision for joint hand-object reconstruction and tracking, without requiring object templates or depth sensors. Starting from pretrained visual estimates, TacHOI uses tactile contact to constrain object depth relative to the estimated hand, while spatially separated contacts on a metrically calibrated hand provide a physical ruler for object extent. It incorporates these constraints into a joint optimization of hand poses, object trajectories, and anisotropic object scale alongside visual alignment. Across 100 ARCTIC and HO3D sequences with synthesized tactile observations, TacHOI achieves the lowest median ADD-S* among the evaluated baselines, reducing error from 15.6 to 3.6 cm on ARCTIC and achieving 2.8 cm on HO3D. Additional experiments on OpenTouch demonstrate its applicability to measured tactile observations.
