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

## 精读解读（中文）

### 一、研究动机
在无人机安全关键应用中，目标检测需要大规模、持续更新的数据集，但集中化训练会引发隐私、监管、存储和带宽挑战。分布式无人机部署中，机载数据难以或不宜传输到中心基础设施。因此，本研究探索联邦学习能否在避免原始图像集中的情况下，恢复多机协作训练的大部分性能增益。

### 二、技术方案（Method）
基于Sherpa.ai FL平台实现联邦目标检测管道，使用KIIT-MiTA无人机数据集，将数据按非独立同分布划分到四个分布式节点。采用YOLO nano系列轻量模型（如YOLO26 nano），对比单机、集中式和联邦学习三种训练范式。联邦学习采用标准FedAvg策略，各节点本地训练后聚合模型参数，不交换原始图像。

### 三、结果（Result）
联邦学习性能接近集中式训练，且显著优于单机训练。最佳轻量模型YOLO26 nano在mAP@0.50上相对单机提升52.89%，在mAP@0.50:0.95上提升67.80%。联邦学习在各类别上均实现一致增益，验证了其在不集中数据下的有效性。

### 四、结论（Conclusion）
联邦学习能够实现分布式无人机舰队的可扩展、高性能且隐私保护的目标检测，无需数据集中化。通过协作学习，模型可以利用更广泛的数据多样性，同时遵守隐私法规和带宽限制。

### 五、方法论与关键技术细节
数据集为KIIT-MiTA无人机航拍图像，按非IID方式划分为4个客户端以模拟实际分布。使用YOLO nano系列（如YOLO26 nano）作为轻量骨干，适合边缘部署。FL平台为Sherpa.ai，采用FedAvg聚合。损失函数由定位损失（IoU-based）和分类损失（交叉熵）组成，通过λ_loc和λ_cls超参数平衡。对比基线包括单机训练（数据局限于一节点）和集中训练（数据全部汇集）。实验在固定轮次和本地epoch下进行，未详细讨论通信成本或对极端非IID的鲁棒性。

