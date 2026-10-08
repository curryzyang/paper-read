# Directed Temporal Representations for Offline Visual Control

- 区域：精读区
- 排名：4
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Chenyang Yuan, Haoyu Wang, Zhuo Sun, Xiaoyuan Cheng
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08960v1) · [PDF](https://arxiv.org/pdf/2610.08960v1)

## TLDR
DTRC learns a directed temporal quasimetric over frozen visual world-model features from offline trajectories and uses its distance changes as a goal-relative progress critic to train a direct goal-conditioned policy, achieving strong control performance across ten visual tasks without test-time planning.

## Abstract
Predictive world models provide compact visual representations for control. Control requires a latent geometry aligned with temporal reachability rather than predictive similarity alone. We introduce Directed Temporal Representations for Control (DTRC), which learns such a geometry from offline visual trajectories on top of frozen LeWorldModel (LeWM) features. DTRC constructs a directed temporal quasimetric over the learned control representation. Short-range temporal offsets calibrate the distance scale. Bootstrapped targets extend temporal reachability across longer horizons. Action-conditioned consistency aligns the representation with local transition dynamics. The resulting distance estimates temporal reaching cost, and its change across a transition defines goal-relative temporal progress. We use this progress signal as a temporal critic for direct goal-conditioned policy learning. Model-assisted targets provide an additional training-time refinement under behavior-support and dynamics-agreement constraints. Across ten visual control tasks, DTRC achieves strong goal-conditioned control performance relative to planning and direct-policy baselines. Held-out diagnostics on the four LeWM tasks show consistent short-range temporal calibration, task-dependent long-range and directional structure, and positive transition-level progress. Temporal supervision improves the same flow-policy parameterization across all four LeWM tasks, while the resulting policy acts directly without iterative trajectory search at test time.


## 精读解读（中文）
### 一、研究动机
预测式世界模型学到的视觉表征主要按预测相似性组织，但控制真正需要的是与时间可达性对齐的隐空间几何，因为视觉上相似的状态未必在控制上彼此易达。为此作者提出 Directed Temporal Representations for Control（DTRC），在冻结的 LeWorldModel（LeWM）特征之上直接学习一种有向的时间几何，使表征中的距离对应目标到达代价。

### 二、技术方案（Method）
输入为离线视觉轨迹，视觉编码沿用冻结的 LeWM 特征，只在其上学习控制表征。核心模块是一个有向时间拟度量（quasimetric，非对称，允许 d(s,s') 与 d(s',s) 不等）：用短程时间偏移样本标定距离尺度，用自举（bootstrapped）目标把时间可达性外推到更长的时间跨度，并用动作条件一致性把表征与局部转移动力学对齐。由此得到的距离估计时间到达代价，其沿一次转移的变化定义目标相对时间进度，该进度信号作为时间 critic 直接驱动目标条件策略（flow policy）学习；训练时另用模型辅助目标，在行为支撑与动力学一致性约束下做进一步细化。推理时策略直接输出动作，不做迭代轨迹搜索。

### 三、结果（Result）
在十个视觉控制任务上，DTRC 的目标条件控制性能优于规划类与直接策略类基线。在四个 LeWM 任务的 held-out 诊断中，观察到一致的短程时间标定、随任务变化的长程与方向结构，以及正向的转移级时间进度。用相同的 flow-policy 参数化，时间监督在四个 LeWM 任务上均带来提升，且所得策略在测试时直接行动，无需迭代轨迹搜索。

### 四、结论（Conclusion）
结果表明，面向控制的隐空间几何应以有向时间可达性（到达代价）为核心，而不仅是预测相似性。在冻结世界模型特征之上加一层时间拟度量监督，即可显著改善目标条件控制，并同时消除测试时的规划开销。

### 五、方法论与关键技术细节
数据为离线视觉轨迹（观测序列与动作），全程无在线交互，视觉骨干固定为 LeWM 特征以隔离表征学习效果；关键先验是有向拟度量假设，即到达代价非对称且满足三角不等式一类的拟度量结构。损失由短程时间标定项、长程自举目标项、动作条件一致性项、以时间进度为 critic 的目标条件策略损失，以及受行为支撑与动力学一致性约束的模型辅助目标组成。主要约束与局限在于：长程能力依赖自举目标的可靠性，可能出现偏差累积；模型辅助目标只在行为支撑覆盖范围内可信；整体性能受冻结 LeWM 特征质量与离线数据中目标状态覆盖度限制；测试时零迭代搜索使推理开销低，但也意味着策略质量完全由训练期的时间监督决定。
