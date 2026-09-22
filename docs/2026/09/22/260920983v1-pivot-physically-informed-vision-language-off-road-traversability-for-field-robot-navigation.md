# PIVOT: Physically Informed Vision-Language Off-Road Traversability for Field Robot Navigation

- 区域：精读区
- 排名：8
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Aoran Jiao, Wenda Zhao, Hshmat Sahak, Timothy D. Barfoot
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20983v1) · [PDF](https://arxiv.org/pdf/2609.20983v1)

## TLDR
PIVOT is a LiDAR-only off-road navigation system that physically grounds VLM-predicted traversal energy, vibration, and wheel slip against real robot measurements to form a unified traversability score, using geometry-based planning as the nominal mode and VLM semantic replanning only as a fallback, thereby increasing autonomy from 59.6% to 97.0% and mean distance between interventions from 69.2 m to 412.9 m over ~6.4 km of mixed-terrain closed-loop trials.

## Abstract
Terrain assessment is a critical capability for off-road mobile robots, enabling safe and reliable navigation through unstructured and geometrically complex environments. Conventional geometry-based terrain assessment is fast to compute but often overly conservative in unstructured environments. We present PIVOT: a Physically Informed Vision-Language Off-Road Traversability navigation system that augments conventional geometry-based planning with vision-language-model (VLM)-based semantic reasoning for field robots. To physically ground this assessment, we quantify how strongly the VLM's predicted traversal energy cost, robot vibration, and wheel slip correlate with real-world measurements and introduce a unified traversability score that weights each modality by its prediction-measurement correlation. For efficiency, we design a two-level navigation architecture that retains geometry-based planning as the nominal mode and invokes semantic replanning only when that mode fails to find a path. Across five repeated closed-loop trials on a mixed-terrain route totalling around $6.4$ km, the proposed system increases overall autonomy from $59.6\%$ to $97.0\%$, reduces human interventions from $11$ to $3$, and increases the mean distance between interventions (MDBI) from $69.2$ m to $412.9$ m compared with geometry-only navigation. These results demonstrate that physically grounded VLM-based terrain assessment can substantially extend autonomous navigation beyond the limitations of geometry alone, while preserving efficient geometric planning as the nominal mode.


## 精读解读（中文）
### 一、研究动机
非结构化野外环境中，传统基于几何的地形评估虽计算高效但常过于保守，而基于视觉语言模型（VLM）的语义可通行性评估多以启发式方式融入导航，缺乏对机器人实际物理穿越特性的验证，限制了其在安全关键场景的应用。因此需要将VLM预测与可测量的机器人-地形交互物理量关联，构建物理落地的可通行性评估，并在保留几何规划效率的同时扩展自主导航能力。

### 二、技术方案（Method）
PIVOT采用仅LiDAR的两级导航架构：标称模式对下采样点云做二维栅格划分与平面拟合，由坡度、粗糙度、点密度和相对高度生成几何代价地图，并用C-BIT*规划路径；当几何规划找不到可行路径时，触发语义回退，通过OpenAI API调用GPT-5，输入五幅同步视图（原始LiDAR强度图、高亮感兴趣区域的强度图，以及俯视90°/-90°、前视20°/180°、左侧视10°/90°三幅以机器人为中心的三维点云渲染图），固定提示词要求模型以JSON返回功率消耗、振动、车轮打滑三个[0,1]分数。为物理落地，使用LiDAR里程计累计距离对齐空间窗口，分别以电池电压电流乘积的均值功率、重力补偿IMU加速度PSD在[f_min,f_max]的带功率、以及指令速度与LiDAR里程计速度之差的绝对值作为三个物理量，归一化后按VLM预测与对应物理量的Pearson相关系数平方归一化得到权重，加权求和为统一可通行性分数。语义回退时用该分数修正局部代价地图，再由C-BIT*重规划；若仍失败则请求人工干预。

### 三、结果（Result）
离线数据集上，GPT-5预测的功率、振动和打滑分数与对应归一化物理量呈正相关，线性拟合R²分别为0.74、0.67和0.57，且统一可通行性分数与三项归一化物理量均值参考分数正相关。在混合地形路线上进行五轮重复闭环试验，总里程约6.4 km，PIVOT将总体自主率从几何-only导航的59.6%提升至97.0%，人工干预从11次降至3次，平均干预间距（MDBI）从69.2 m提升至412.9 m。

### 四、结论（Conclusion）
结果表明，将VLM地形评估与机器人实际物理测量进行相关性加权，可在几何评估失效的区域提供有效补充，显著减少人工干预并延长连续自主行驶距离。以几何规划为标称模式、仅在失败时调用语义重规划的两级架构，能在保持计算效率的同时扩展野外自主导航能力。

### 五、方法论与关键技术细节
系统仅使用LiDAR，强度图对光照变化不敏感，所有VLM查询为包含固定提示词和高亮目标区域输入图的自包含API请求，不使用历史对话或前序输出；空间窗口按LiDAR里程计累计距离定义并允许时间长度随速度变化；权重由离线数据估计的Pearson相关系数平方归一化得到，非负且和为1，归一化缩放参数来自采集数据集；语义回退仅在几何规划失败时触发以控制在线VLM调用开销；实验平台为Clearpath Warthog UGV，搭载Ouster 3D LiDAR、IMU、电池遥测和机载计算机，评估局限于一条约6.4 km的混合地形路线与单一平台，权重与阈值依赖离线数据集，VLM推理依赖外部API。
