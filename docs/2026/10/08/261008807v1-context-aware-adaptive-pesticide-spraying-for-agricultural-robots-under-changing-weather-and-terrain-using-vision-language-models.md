# Context-Aware Adaptive Pesticide Spraying for Agricultural Robots under Changing Weather and Terrain Using Vision-Language Models

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Cong-Thanh Vu, Yen-Chen Liu
- 机构：National Cheng Kung University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08807v1) · [PDF](https://arxiv.org/pdf/2610.08807v1)

## TLDR
This paper proposes a context-aware adaptive pesticide-spraying framework for agricultural robots that uses Vision-Language Models to integrate crop, pesticide, and weather information with MPPI-based trajectory tracking, improving crop-row detection by at least 30% while enabling flexible spray-volume and speed adjustments to reduce pesticide drift.

## Abstract
Precision pesticide spraying is essential for optimizing application efficiency and ensuring uniform chemical distribution. Spraying performance is influenced by multiple factors, including environmental conditions such as temperature and wind speed, pesticide type, and the robot's capability to accurately perceive crops and target spray locations. Existing approaches predominantly emphasize crop detection and rely on predefined spraying parameters, whereas human operators dynamically adjust their spraying strategies by considering environmental conditions, region-specific crop characteristics, and the type of pesticide being applied. In this study, we propose a context-aware adaptive spraying framework based on Vision-Language Models (VLMs), which enables robots to leverage spatial reasoning and integrate information from multiple sources, including crop type, pesticide type, and weather data, to make adaptive and optimized spraying decisions. Subsequently, a trajectory-tracking controller based on Model Predictive Path Integral (MPPI) control is employed to ensure precise navigation and accurate spraying at crop locations. The comparative results demonstrate that the proposed method improves accuracy by at least 30% in detecting crop rows. In addition, the experimental evaluations conducted in two environments further demonstrate the robot's ability to flexibly adjust spraying volume and travel speed, while reducing pesticide drift.


## 精读解读（中文）
### 一、研究动机
现有精准喷洒多聚焦作物检测并依赖预设喷洒参数，缺乏像人类操作员那样综合天气、地形、作物类型和农药类型进行动态调节的能力，导致喷洒效率、漂移和化学浪费问题。研究旨在利用视觉语言模型的空间推理与多源信息融合，实现农业机器人上下文感知的自适应喷洒。

### 二、技术方案（Method）
系统先以3D LiDAR和IMU通过Fast-LIO2构建全局地图，并用ZED X相机与YOLOv8检测树木或作物，将局部坐标变换到全局并形成工作地图；随后将树木位置与ID投影为2D表示，用提示工程加少样本提示让VLM识别作物行，生成行间中心线并连接成锯齿形全局路径；喷洒阶段向VLM输入RGB图像、带行颜色与全局路径及Windy API风向的2D可视化，以及作物类型、地理位置、季节时间、农药类型、温湿度风速等语义信息，用思维链提示输出每行或每株对应的行驶速度与喷量；最后MPPI控制器跟踪路径并避障，按机器人到植株的欧氏距离阈值与喷洒侧触发喷头。

### 三、结果（Result）
对比结果显示，基于VLM的作物行检测准确率较KMeans、DBSCAN或人工调整等基线至少提升30%，并在两种田间环境中验证机器人能依据环境灵活调整喷量与行驶速度，同时减少农药漂移。

### 四、结论（Conclusion）
该框架把VLM的上下文推理能力引入农业机器人喷洒决策，使机器人能在变化天气与地形下做出类人自适应策略，并通过MPPI保证精准导航与定点喷洒。结果表明方法在行检测精度、变量喷洒和降低漂移方面具有潜力，为精准农业自主喷洒提供了新思路。

### 五、方法论与关键技术细节
关键实现包括Fast-LIO2建图、YOLOv8作物检测、局部到全局坐标变换、2D树木ID图输入VLM、行检测使用规则约束与少样本提示、喷洒决策使用CoT提示并约束输出ID与格式，喷洒触发依赖距离阈值和正确侧，速度由MPPI执行；硬件为Bunker Mini履带底盘、Jetson Orin、ZED X、Livox Mid-360、ROS2 Humble、左右独立泵与Arduino PWM驱动。局限性在于VLM推理对边缘算力与实时性有要求、性能依赖提示设计与外部天气API，且实验仅覆盖两种环境，完整量化指标和长期鲁棒性仍需更多验证。
