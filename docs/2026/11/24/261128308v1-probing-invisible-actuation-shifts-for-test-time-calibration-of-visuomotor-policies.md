# Probing Invisible Actuation Shifts for Test-time Calibration of Visuomotor Policies

- 区域：精读区
- 排名：10
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Jie Liu, Hui Xie, Qinfeng Feng, Joaquin Vanschoren
- 机构：Eindhoven University of Technology, The University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28308v1) · [PDF](https://arxiv.org/pdf/2611.28308v1)

## TLDR
The paper proposes PEA, a test-time calibration method that uses a short active probe to identify and compensate for invisible actuation shifts (e.g., gain, delay, and drift) in frozen visuomotor policies, while a removable low-rank adapter handles visual shifts.

## Abstract
Visuomotor policies such as vision-language-action models (VLAs) and world action models (WAMs) are increasingly deployed on robots whose cameras and controllers differ from those used to collect their training data. Such deployment introduces two kinds of shifts. Visual shifts, such as a moved camera, change the observed images; actuation shifts, such as a retuned controller, latency or an added payload, change only how commanded actions translate into robot motion. Invisible to the policy, actuation shifts sharply degrade its success, even under domain randomization. In this work, we propose PEA, a test-time calibration method that identifies actuation shifts through active probing before task execution. Specifically, before each episode, the robot executes a short probe that moves one arm axis at a time with known commands, so that gain, delay and drift leave separable traces. A closed-form identifier estimates them from the response, and PEA compensates every subsequent command so that the robot executes the motion the policy intends. The identifier requires no policy training and thus applies to any frozen visuomotor policy. Since visual shifts remain visible to the policy, PEA further adapts the frozen policy with a removable low-rank adapter, addressing coupled visual and actuation shifts. Experiments on LIBERO with a WAM and a VLA show that, without any policy training, the identifier of PEA recovers most of the success lost to actuation shifts and generalizes to shifts unseen during training (e.g., from 61.0% to 89.7% on LIBERO-Spatial with Cosmos-Policy).


## 精读解读（中文）
### 一、研究动机
部署时相机与控制器常与训练数据不一致，带来视觉偏移和驱动偏移；视觉偏移改变图像，而驱动偏移只改变指令到运动的映射，首帧与指令不变，因此对策略不可见，即使域随机化也会显著降低成功率。现有测试时自适应多在执行中或失败后推断动力学，或依赖随机激励与学习模块，证据晚且难辨识，因此需要任务前主动探测。

### 二、技术方案（Method）
PEA在每回合前用30步自由空间探针：先2步静止，随后对6个机械臂轴逐一施加零和双脉冲+c,+c,-c,-c（c=0.5），最后开合空夹爪；记录末端每步位置与旋转增量，按轴取4个推动步及后3步组成L=7响应。用低维模型Δx_(t,i)≈k_i g_i a_(t−δ,i)+β_i建模各轴增益g_i、共享延迟δ（≤3）和漂移β_i，闭式辨识器从响应估计参数。随后对每个指令做增益与漂移逆补偿a'_t,i=a_t,i/g_i+b_i（b_i=−β_i/(k_i g_i)），延迟用保持规则处理；对视觉偏移在冻结策略上附加可移除LoRA适配器，并用同一探针条件化，离线仅用训练偏移族和特权教师校准，测试时不调参。

### 三、结果（Result）
在LIBERO上使用WAM Cosmos-Policy和VLA OpenVLA-OFT，PEA无需策略训练即可恢复大部分因驱动偏移损失的成功率：Cosmos-Policy在LIBERO-Spatial未见偏移下从61.0%提升到89.7%，并对刚度、负载和延迟等训练中未见的偏移泛化。视觉与驱动耦合偏移下，可移除LoRA适配器进一步改善，例如Cosmos-Policy在LIBERO-Spatial耦合偏移下从42.8%显著提升，且基本保持标称性能。

### 四、结论（Conclusion）
PEA将驱动偏移视为需要主动激励才能观测的系统辨识问题，用任务前短探针、闭式估计和指令补偿解决不可见执行偏移，用LoRA处理可见视觉偏移，且保持策略冻结、策略无关、每回合仅30步交互。实验表明该方法能显著提升WAM/VLA在多种未见偏移及耦合偏移下的鲁棒性，具有部署期校准价值；但模型对刚度仅作有效增益与滞后近似，未覆盖跨轴耦合与时变负载。

### 五、方法论与关键技术细节
关键实现包括：探针采用零和双脉冲且逐轴激励以分离增益、延迟和漂移；测量末端位置差乘100、旋转向量乘10，响应窗口为4个推动步加后3步以捕获≤3步延迟；闭式辨识器由经典系统辨识组件组装并离线校准一次，测试时不更新策略权重也不在测试偏移上调参。约束为冻结策略、每回合最多K=30步自由空间交互、离线仅用训练偏移族和特权教师；主要局限是低维一阶模型对刚度、载荷、跨轴耦合和时变动力学近似有限。
