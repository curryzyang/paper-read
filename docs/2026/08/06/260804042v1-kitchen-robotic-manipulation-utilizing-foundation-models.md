# Kitchen Robotic Manipulation utilizing Foundation Models

- 区域：速读区
- 排名：9
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Myung-Hwan Jeon, Sankalp Yamsani, Joohyung Kim
- 机构：Kumoh National Institute of Technology, University of Illinois Urbana-Champaign
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04042v1) · [PDF](https://arxiv.org/pdf/2608.04042v1)

## TLDR
A modular perception pipeline integrating multiple foundation models (best: LLMDet + SAMv2 + DINOv2 + GeoTransformer) enables robust 6D pose estimation and grasp planning for kitchen dishware manipulation, achieving 89.12% ADI on a cluttered kitchen benchmark and successfully transferring to real robots without environment-specific retraining.

## Abstract
Deploying robots in everyday human environments requires perception systems that are both robust and adaptable to diverse, dynamic conditions. In this work, we present a modular perception pipeline for household manipulation tasks, with a focus on dishware handling in kitchen environments. The pipeline integrates open-vocabulary object detection, multi-view segmentation, instance-aware 3D reconstruction, and a 2D-3D feature fusion strategy for 6D pose estimation and grasp planning. Its modular design enables systematic substitution of multiple visual and geometric foundation models, allowing us to identify the best-performing configuration through extensive evaluation on a custom kitchen dataset. The best-performing configuration (LLMDet + SAMv2 + DINOv2 + GeoTransformer) achieves an ADI of 89.12\% on the 20-scene kitchen benchmark with cluttered and occluded conditions. Furthermore, real-world demonstrations confirm that the best configuration can be deployed on physical robots without environment-specific retraining, successfully executing tasks such as sink-to-dishwasher transfer and cup stacking. It validates the adaptability and scalability of the pipeline and highlights its potential as a practical framework for household robotic systems. Our code and supplementary materials are available at https://raivlab.github.io/FM_kitchen .
