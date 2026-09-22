# Do Spinning Radar Doppler Velocity Measurements Improve Vehicle Detection and Tracking?

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Eric Xie, Daniil Lisus, Timothy D. Barfoot
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.21000v1) · [PDF](https://arxiv.org/pdf/2609.21000v1)

## TLDR
This paper demonstrates that Doppler velocity measurements from spinning FMCW radars improve vehicle detection via ego-motion-based undistortion and tracking via a per-vehicle velocity prior, yielding gains of up to +2.37 mAP and +13.68 MOTA on an automatically labeled Boreas dataset.

## Abstract
Spinning frequency-modulated continuous-wave (FMCW) radars have been gaining popularity in autonomous vehicle perception on account of their robustness to adverse weather conditions and 360° field of view. Recently, scanning radars have also been shown capable of generating per-azimuth Doppler velocity. In this paper, we investigate whether these Doppler velocity measurements improve spinning radar vehicle detection and tracking performance. For detection, we estimate the ego motion and use it to undo the Doppler range distortion of the radar image before passing it to a network. For tracking, we propose a new way to estimate a per-vehicle velocity and use it as a prior for the tracker's motion model. Since Doppler-enabled spinning radar data is not available in any dataset with ground-truth dynamic object labels, our first contribution is an automatic labelling pipeline that uses an ensemble of fine-tuned off-the-shelf lidar detectors to label all 643 km of the Boreas Road Trip dataset. We then transfer detections to radar, and use over 250 km of vehicle-dense sequences as ground-truth training data. By training and evaluating two state-of-the-art detectors, we show that Doppler undistortion can improve detection accuracy by up to $2.37$ points on mean average precision. Furthermore, we show that the Doppler velocity prior can improve tracking accuracy by $13.68$ points on multi-object tracking accuracy (MOTA) versus the zero-velocity initialization baseline, while achieving $99.7\%$ of the MOTA obtained using ground-truth velocities as the prior.


## 精读解读（中文）
### 一、研究动机
旋转式调频连续波雷达因对恶劣天气鲁棒且具360°视场，在自动驾驶感知中日益流行；近期扫描雷达还能输出逐方位多普勒速度。本文旨在检验这些多普勒速度测量能否提升旋转雷达的车辆检测与跟踪性能，并解决缺乏带动态目标真值标签的多普勒旋转雷达数据集的问题。

### 二、技术方案（Method）
作者先用一组微调过的现成激光雷达检测器集成，对Boreas Road Trip数据集全部643 km进行自动标注，再将检测结果迁移到雷达，筛出超过250 km车辆密集序列作为真值训练数据。检测阶段估计自车运动，用其校正雷达图像中的多普勒距离畸变后再送入网络，并训练评估两个SOTA检测器；跟踪阶段提出逐车辆速度估计方法，将其作为跟踪器运动模型的先验，与零速度初始化和真值速度先验对比。

### 三、结果（Result）
实验表明，多普勒去畸变最多可将检测平均精度mAP提升2.37个点；在跟踪中，多普勒速度先验相对零速度初始化基线可将多目标跟踪准确率MOTA提升13.68个点，并达到使用真值速度先验所得MOTA的99.7%。

### 四、结论（Conclusion）
结果表明，旋转雷达的逐方位多普勒速度能有效改善车辆检测与跟踪，尤其通过自车运动去畸变和逐车速度先验带来显著收益。该工作也提供了一个基于自动标注与迁移的大规模训练评估方案，为后续多普勒雷达感知研究奠定基础。

### 五、方法论与关键技术细节
关键实现包括：使用激光雷达检测器集成自动标注643 km Boreas Road Trip，并迁移至雷达；以超过250 km车辆密集序列训练评估；检测端先估计自车运动以补偿多普勒距离畸变；跟踪端将估计的逐车速度作为运动模型先验。评价指标为mAP与MOTA，基线为零速度初始化和真值速度先验；局限在于真值来自自动标注/迁移而非人工动态标签，且性能依赖自车运动与速度估计质量。
