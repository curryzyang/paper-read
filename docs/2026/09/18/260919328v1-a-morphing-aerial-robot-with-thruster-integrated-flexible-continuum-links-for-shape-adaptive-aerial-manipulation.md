# A Morphing Aerial Robot With Thruster-Integrated Flexible Continuum Links for Shape Adaptive Aerial Manipulation

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Eri Sawada, Kazuki Sugihara, Ayano Miyamichi, Kunio Kojima, Kei Okada
- 机构：The University of Tokyo
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19328v1) · [PDF](https://arxiv.org/pdf/2609.19328v1)

## TLDR
This paper presents a morphing aerial robot with thruster-integrated flexible continuum links that combines soft shape adaptability with an expanded wrench space, using a composite leaf-spring structure and vibration-suppressing control to achieve stable flight and versatile aerial manipulation.

## Abstract
In recent years, aerial manipulation has attracted increasing attention as a key to expand the application of aerial robots. In this work, we focus on two major research directions for achieving versatile aerial manipulation: (i) acquiring high environmental adaptability using soft manipulators, and (ii) expanding the feasible wrench space by distributing thrusters along the manipulator. However, no aerial robot has simultaneously satisfied these two requirements. Therefore, in this paper, we propose a morphing rotor-distributed aerial robot with flexible continuum links that achieves both high shape adaptability and an expanded wrench space. The flexible continuum links function as soft manipulators, passively conforming to the shape of the environment, while the thrusters distributed along the continuum links expand the feasible thrust wrench space and enable the end-effector to exert large interaction forces. To realize the proposed robot, it is essential to suppress vibrations of the lightweight continuum links. Thus, we develop a composite leaf-spring structure that provides both high torsional and vertical stiffness, and vibration-suppressing control methods. Using these implementations, we demonstrate stable flight and a variety of aerial manipulation tasks. To the best of our knowledge, this is the first work to realize aerial manipulations using flexible links with an integrated thruster.


## 精读解读（中文）
### 一、研究动机
空中操作要同时具备高环境适应性和较大的可行力旋量空间，软机械臂可提升适应性，沿机械臂分布推进器可扩展力旋量空间，但此前尚无空中机器人同时满足这两点。

### 二、技术方案（Method）
提出一种可变形的旋翼分布式空中机器人，其柔性连续体连杆作为软机械臂，可被动顺应环境形状；沿连续体连杆分布的推进器扩展可行推力旋量空间，使末端执行器能施加较大交互力。为实现该机器人，开发了可同时提供高扭转与垂直刚度的复合板簧结构，并采用振动抑制控制方法来稳定轻量连续体连杆。

### 三、结果（Result）
基于上述实现，论文展示了稳定飞行和多种空中操作任务；据作者所知，这是首个使用集成推进器的柔性连杆实现空中操作的工作。摘要未给出具体定量指标或对比基线的数值结果。

### 四、结论（Conclusion）
该工作通过柔性连续体连杆与分布式推进器集成，同时实现高形状适应性和扩展的力旋量空间，验证了柔性连杆集成推进器用于空中操作的可行性，为形状自适应空中操作提供了新方案。

### 五、方法论与关键技术细节
关键实现细节包括：柔性连续体连杆作为被动顺应软机械臂、推进器沿连杆分布以扩展力旋量空间、复合板簧结构提供高扭转和垂直刚度、振动抑制控制用于抑制轻量连杆振动；摘要未提供数据规模、损失函数、超参数、复杂度或定量局限性等细节。
