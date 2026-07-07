# Federated Learning for Object Detection: Enabling Collaborative Drone Learning Without Centralizing Data

- 区域：精读区
- 排名：4
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Daniel M. Jimenez-Gutierrez, Enrique Zuazua, Georgios Kellaris, Joaquin del Rio, Oleksii Sliusarenko, Xabi Uribe-Etxebarria
- 机构：Sherpa.ai
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02636v1) · [PDF](https://arxiv.org/pdf/2607.02636v1)

## TLDR
This paper demonstrates that federated learning enables drones to collaboratively train object detection models without sharing raw data, achieving performance close to centralized training while significantly outperforming single-drone training.

## Abstract
Object detection is a fundamental capability for AI-driven perception in safety-critical drone and edge-vision systems, including disaster response, operational security environments, infrastructure monitoring and defense applications. Robust model performance in such environments depends on large, continuously updated datasets. However, training high-performing detectors typically requires centralizing aerial imagery, which raises privacy, regulatory, storage, and bandwidth challenges. This is especially problematic in distributed drone deployments, where visual data is generated onboard and is often impractical or undesirable to transfer to a centralized infrastructure.
  In this work, we apply Federated Learning (FL) for object detection, enabling drones to improve a shared model while keeping image data local and private. We implement a federated object detection pipeline using the Sherpa.ai FL platform on the KIIT-MiTA dataset, and compare it with Single-drone and Centralized baselines using mean Average Precision (mAP) at IoU thresholds of 0.50 and 0.50-0.95. In our experiments, the proposed FL approach remains close to Centralized training while dramatically improving over Single-drone training, with the best lightweight model (YOLO26 nano), suitable for deployment even on very limited edge infrastructure, achieving relative gains of 52.89% and 67.80% in mAP@0.50 and mAP@0.50:0.95, respectively. These results show that FL enables scalable, high-performing, and privacy-preserving object detection across distributed drone fleets without data centralization.
