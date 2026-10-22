# VeriCalib: Verifiable Target-Based LiDAR-Camera Calibration

- 区域：速读区
- 排名：9
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Xiangcheng Hu, Xieyuanli Chen, Feiyi Chen, Shengli Ren, Shiyang Chen, Guoqiang Ye, Hao Wang, Ping Tan, Steven L. Waslander, Fuchun Sun, Jin Wu
- 机构：National University of Defense Technology, Independent Researcher, Tsinghua University, University of Science and Technology Beijing, X Square Robot Technology (Shenzhen) Co., Ltd., University of Toronto, Hong Kong University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28791v1) · [PDF](https://arxiv.org/pdf/2610.28791v1)

## TLDR
VeriCalib formulates target-based LiDAR–camera extrinsic calibration as a verifiable estimation problem, using structured covariance, consistency checks, and direction-wise detectability bounds to output a calibration state that tells users whether to accept the result or how to improve data collection.

## Abstract
Target-based extrinsic calibration estimates the rigid transform between sensors from a few observations of a known target, and its result is commonly assessed by the root-mean-square error of the fitted residuals. However, this scalar error is computed on the same observations and therefore cannot indicate whether to accept the result, re-extract, recollect or add observations. This paper presents VeriCalib, which formulates extrinsic calibration as a verifiable estimation problem and reports a calibration state. The key insight is a two-level extrinsic compensation mechanism, in which the extrinsic compensates the rigid part of each observation error at the residual level, and rotation and translation compensate each other at the parameter level. Consequently, the fitted residual can reveal neither an inconsistency between the observations and the model nor whether the estimated extrinsic is reliable in every direction. Accordingly, we assess the calibration through a structured covariance that jointly propagates the uncertainty of the camera and LiDAR board features with a known-geometry prior, and estimate its scale as a variance component from the residuals. On this covariance, we decouple rotation and translation to resolve the precision along each direction and guide data collection toward the weakest one. Since this precision presumes consistent observations, we further develop within-view and cross-view checks that examine the internal residual and the rigid discrepancy between observations, respectively, with thresholds that hold their significance level under an unknown noise level. We also extend the minimal detectable bias to the extrinsic to bound the smallest detectable fault along each direction. These criteria form a calibration state that indicates whether to accept the result or how to collect the data...
