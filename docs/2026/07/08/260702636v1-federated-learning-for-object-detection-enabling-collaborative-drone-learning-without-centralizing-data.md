# Federated Learning for Object Detection: Enabling Collaborative Drone Learning Without Centralizing Data

- 区域：精读区
- 排名：4
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Daniel M. Jimenez-Gutierrez, Enrique Zuazua, Georgios Kellaris, Joaquin del Rio, Oleksii Sliusarenko, Xabi Uribe-Etxebarria
- 机构：Sherpa.ai
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02636v1) · [PDF](https://arxiv.org/pdf/2607.02636v1)

## TLDR
This paper demonstrates that federated learning enables drones to collaboratively train object detection models with performance close to centralized training while keeping image data local and private, achieving substantial gains over single-drone baselines.

## Abstract
Object detection is a fundamental capability for AI-driven perception in safety-critical drone and edge-vision systems, including disaster response, operational security environments, infrastructure monitoring and defense applications. Robust model performance in such environments depends on large, continuously updated datasets. However, training high-performing detectors typically requires centralizing aerial imagery, which raises privacy, regulatory, storage, and bandwidth challenges. This is especially problematic in distributed drone deployments, where visual data is generated onboard and is often impractical or undesirable to transfer to a centralized infrastructure.
  In this work, we apply Federated Learning (FL) for object detection, enabling drones to improve a shared model while keeping image data local and private. We implement a federated object detection pipeline using the Sherpa.ai FL platform on the KIIT-MiTA dataset, and compare it with Single-drone and Centralized baselines using mean Average Precision (mAP) at IoU thresholds of 0.50 and 0.50-0.95. In our experiments, the proposed FL approach remains close to Centralized training while dramatically improving over Single-drone training, with the best lightweight model (YOLO26 nano), suitable for deployment even on very limited edge infrastructure, achieving relative gains of 52.89% and 67.80% in mAP@0.50 and mAP@0.50:0.95, respectively. These results show that FL enables scalable, high-performing, and privacy-preserving object detection across distributed drone fleets without data centralization.


## 精读解读（中文）
### 一、研究动机
在无人机安全关键应用中，目标检测需要依赖大规模且不断更新的数据集，但集中化训练会引发隐私、监管、存储和带宽等问题。分布式无人机部署中，视觉数据产生于机载设备，传输到中心基础设施往往不切实际或不可取，因此需要一种无需集中数据即可协同训练的方法。

### 二、技术方案（Method）
本文基于Sherpa.ai联邦学习平台，采用KIIT-MiTA无人机目标检测数据集，并将其非独立同分布地划分给四个分布式节点。每个节点本地训练轻量级YOLO nano模型（最佳为YOLO26 nano），通过FedAvg算法聚合模型参数，实现无需传输原始图像的协同训练。实验设定单无人机、集中式和联邦三种场景，使用平均精度（mAP）在IoU阈值0.50和0.50-0.95下评估性能。

### 三、结果（Result）
联邦学习方案在性能上接近集中式训练，同时显著优于单无人机训练。最佳轻量模型YOLO26 nano在mAP@0.50和mAP@0.50:0.95上相对单无人机训练分别提升52.89%和67.80%。联邦训练一致优于单节点学习，且各场景下保持了相近的实用性。

### 四、结论（Conclusion）
联邦学习使得分布式无人机机群能够在无需数据集中化的情况下，实现可扩展、高性能且保护隐私的目标检测。该方法兼顾了数据隐私与模型泛化能力，为实际部署提供了可行方案。

### 五、方法论与关键技术细节
数据使用KIIT-MiTA无人机数据集，采用非IID划分模拟真实分布；模型选用YOLO nano系列（特别是YOLO26 nano），适合边缘部署；优化算法为标准FedAvg；评估指标为mAP@0.50和mAP@0.50:0.95。本文未提出新检测器架构或联邦优化算法，而是进行可控实验比较，研究联邦训练在无需原始数据集中化时能否保持竞争性能。
