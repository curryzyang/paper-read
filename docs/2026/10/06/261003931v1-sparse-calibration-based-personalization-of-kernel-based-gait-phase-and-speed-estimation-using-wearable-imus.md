# Sparse Calibration-Based Personalization of Kernel-Based Gait Phase and Speed Estimation Using Wearable IMUs

- 区域：速读区
- 排名：14
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Myeongju Cha, Pilwon Hur
- 机构：GIST
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03931v1) · [PDF](https://arxiv.org/pdf/2610.03931v1)

## TLDR
Sparse calibration with three speeds and PCA-based personalization of kernel-based wearable-IMU gait phase and speed estimation reduced phase error offline and proved real-time feasible online, but speed effects were not significant and larger-cohort validation is needed.

## Abstract
This paper presents sparse calibration-based personalization for kernel-based gait phase and walking speed co-estimation from wearable inertial measurement units (IMUs). A 28-speed reference library was constructed from bilateral thigh and shank trajectories in a 20-subject locomotion dataset. Rather than directly applying population-average kernels, the method combines a user-specific baseline estimated from three calibration speeds with a principal-component (PC) model of baseline-centered kinematic deviations. Offline validation showed that personalized kernels reduced phase error relative to the population kernel. In a single-participant online pilot evaluation, the personalized kernels produced numerically lower mean phase and speed errors and ran in real time on embedded hardware. However, the speed effect was not significant, and pairwise phase differences did not remain significant after multiple-comparison correction. The pilot evaluation establishes wearable implementation feasibility while indicating reference-to-online dataset mismatch and the need for larger-cohort validation.
