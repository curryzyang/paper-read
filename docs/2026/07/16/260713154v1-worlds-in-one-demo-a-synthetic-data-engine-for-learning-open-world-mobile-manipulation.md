# Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation

- 区域：精读区
- 排名：7
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Lingxiao Guo, Huanyu Li, Guanya Shi
- 机构：Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13154v1) · [PDF](https://arxiv.org/pdf/2607.13154v1)

## TLDR
WANDA is a synthetic data engine that, from a single human demonstration, reconstructs and generates diverse 3D worlds, rearranges robot-object interaction segments into new trajectories with spatial and state diversity, and renders photo-realistic observations, enabling open-world mobile manipulation policies to achieve long-horizon robustness, broad spatial generalization, cross-environment generalization, and zero-shot cross-embodiment transfer.

## Abstract
Learning open-world mobile manipulation policies requires vast data to achieve spatial generalization, long-horizon robustness, and scene generalization. Current prevailing data collection paradigms, teleoperation and UMI, demand prohibitive human effort and cost at scale. To scale beyond the limits of manual data collection, we seek to maximize the value of each human demonstration by scalable data generation. To this end, we introduce WANDA: learning open-World mobile mANipulation from one demonstration via a synthetic DAta engine. WANDA first reconstructs background Gaussian splats and robot-object interaction trajectories from source RGBD observations, as a world substrate for later planning and rendering. It then rearranges contact-rich robot-object interaction segments into extensive spatial configurations, utilizing whole-body motion planning to chain them into new trajectories. To enhance long-horizon robustness, it applies Corrective State Expansion to increase the robot and object state diversity at different stages of mobile manipulation. To unlock cross-environment generalization, trajectories are synthesized on diverse generated 3D worlds from everyday photos. Furthermore, we synthesize photo-realistic observations by compositing rendered robot and object meshes with Gaussian splatting backgrounds. We evaluate our approach on extensive simulation and real-world tasks in various scenes. Experiments show that policies trained with WANDA achieve long-horizon robustness, broad spatial generalization and cross-environment generalization from one real demonstration. Moreover, WANDA naturally supports cross-embodiment data generation, validated by zero-shot deployment on another mobile manipulator with a distinct morphology.


## 精读解读（中文）
### 一、研究动机
学习开放世界移动操作策略需要大量数据以实现空间泛化、长程鲁棒性和场景泛化，但当前主流的数据收集范式（遥操作和UMI）在规模上需要过高的人力和成本。为超越手动数据收集的限制，本文旨在通过可扩展的数据生成来最大化每次人类演示的价值，从而提出WANDA方法，从单个演示中学习开放世界移动操作。

### 二、技术方案（Method）
WANDA首先从源RGBD观测中重建背景高斯溅射（使用MAtCha）和机器人-物体交互轨迹（使用BundleSDF），作为后续规划与渲染的世界基底。然后，将接触丰富的机器人-物体交互片段重新排列到大量空间配置中，利用全身运动规划（RRT-Connect和逆运动学）将它们链接成新轨迹。为增强长程鲁棒性，采用校正状态扩展，在移动操作的不同阶段增加机器人和物体状态多样性（物体状态扩展模拟导航漂移，机器人状态扩展通过锥形采样和关节扰动扩大状态覆盖）。为解锁跨环境泛化，从日常照片（单张输入）使用Marble生成多样化3D世界，并在这些世界上合成新轨迹。最后，通过将渲染的机器人/物体网格与高斯溅射背景合成，进行因子化渲染以生成逼真的视觉观测。

### 三、结果（Result）
实验表明，WANDA训练的策略从单个真实演示实现了长程鲁棒性、广泛空间泛化和跨环境泛化。在仿真中，Bigym任务上使用100个生成演示达到与40-60个人工演示相当的性能（约50倍样本效率）；BEHAVIOR Challenge上使用1360个生成演示训练的π0.5取得0.67的Q-score，远超200个人工演示的0.38。在真实世界中，五个长程移动操作任务（LunchBox、Utensil、DropTrash、Pour、Fridge）从单个演示取得平均54.8%的成功率，并展示了零样本跨形态泛化（在另一形态移动操作手上直接部署）。

### 四、结论（Conclusion）
WANDA通过合成数据引擎最大化单个演示的价值，成功实现从单个演示学习开放世界移动操作策略，在空间泛化、长程鲁棒性和场景泛化上显著超越了传统数据收集方法。该方法自然支持跨形态数据生成，为大规模机器人学习提供了高效、可扩展的范式。

### 五、方法论与关键技术细节
关键细节：1) 背景重建使用MAtCha（稀疏视图2D高斯溅射），无需高精度SLAM，通过前向运动学对齐相机高度；2) 物体重建使用BundleSDF同时跟踪6D姿态和重建网格，支持铰接物体；3) VLM（Gemini 3.1 Pro）指导初始配置采样，利用常识从场景图像推断可操作区域；4) 校正状态扩展包含物体状态扩展（扰动物体姿态后重新IK）和机器人状态扩展（导航起始锥形采样、臂关节随机扰动、锥形摆线EE轨迹）；5) 因子化渲染：背景用高斯溅射快速渲染，前景用Isaac Sim渲染（带光照随机化），避免大型场景渲染开销；6) 局限性：需要手工编辑物体交互片段，碰撞检测可能失败，生成质量受重建精度限制，未建模动力学效应可能导致物理不一致。
