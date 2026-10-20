# Learning Whole-Body Kinetic Coordination for Wheeled-Quadruped Long-Range Throwing

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Qinglian Wu, Yidian Hu, Weiqi Fan, Yutian Zhang, Siyuan Ma, Jiaqi Zhai, Wei Dong, Li Xu
- 机构：Zhejiang University, Hainan University, Tsinghua University, Hangzhou Yunshenchu Technology Co., Ltd. (DEEP Robotics), Harbin Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23883v1) · [PDF](https://arxiv.org/pdf/2610.23883v1)

## TLDR
The paper presents a whole-body kinetic-coordination framework that combines kinetic-chain-based SQP arm trajectory optimization with reference-guided reinforcement learning for a wheeled-quadruped manipulator, enabling robust long-range throwing on unstructured terrain with up to 16.64 m/s release speed and 28.25 m distance when whole-body coordination is enabled.

## Abstract
Long-range throwing on unstructured terrain is a key capability for mobile robots in delivery and retrieval tasks, but it requires high release velocity, coordinated whole-body motion, and robustness to terrain-induced disturbances. We present a whole-body kinetic-coordination framework for a wheeled-quadruped manipulator that combines kinetic-chain arm modeling with SQP-based trajectory optimization and a reference-guided reinforcement learning policy for coordinated base motion. The manipulator is first reduced to a kinetic-chain model and optimized under kinematic and dynamic constraints to produce a high-speed throwing reference. On a stationary base, the optimized arm trajectory reaches a release speed of 12.75 m/s and a throwing distance of 16.68 m. When whole-body coordination is enabled, the system further increases the release speed to 16.64 m/s and the throwing distance to 28.25 m. We then integrate the mobility of the wheeled-quadruped platform and validate the complete policy through hardware experiments on flat ground, grass, slopes, and rough roads. The results show that kinetic-chain optimization and whole-body coordination together enable robust long-range throwing across diverse unstructured terrains.


## 精读解读（中文）
### 一、研究动机
轮式四足机械臂在非结构化地形上执行远程抛掷，对配送与取回任务很重要，但需要高释放速度、全身协调运动以及对地形扰动的鲁棒性。现有学习式运动控制多关注底盘移动，全身控制多面向一般操作，抛掷研究又常局限于固定基座或慢速移动基座，尚未充分解决地形扰动下机械臂反作用力与底盘稳定性的耦合问题。为此，作者希望将类人动能链的近端到远端能量传递与地形鲁棒的全身稳定控制统一起来。

### 二、技术方案（Method）
方法分两阶段：先将机械臂简化为保留J2、J3、J5三个主动矢状关节的3-DOF动能链模型，用等效刚体组、耦合惯量项和动能Hessian推导惯性矩阵，并在近端关节高速、远端零力矩的近似下导出三个关节的正弦基函数形式。随后以基函数幅值、频率、相位、偏置和释放时刻为决策变量，用SQP最大化沿目标方向的加权末端释放速度，约束包括关节位置、速度、由完整动力学计算的力矩以及释放时刻位于有效抛掷区间。最后将优化得到的机械臂参考轨迹嵌入参考引导的全身强化学习策略，由策略协调轮式四足底盘并对机械臂施加小残差修正，同时利用基于历史信息的潜在表示适应地形，在仿真中联合训练后部署到硬件。

### 三、结果（Result）
在固定基座下，优化后的机械臂轨迹达到12.75 m/s的释放速度和16.68 m的抛掷距离；启用全身协调后，释放速度提升到16.64 m/s，抛掷距离提升到28.25 m。作者进一步集成轮式四足平台 mobility，在平地、草地、斜坡和粗糙路面完成硬件实验，验证了完整策略的 run-and-throw 行为。结果表明动能链优化与全身协调结合能够显著扩展抛掷能力，并在多种非结构化地形上保持鲁棒。

### 四、结论（Conclusion）
该工作表明，将动能链驱动的机械臂高速抛掷参考与参考引导的全身强化学习控制结合，可以在轮式四足平台上实现地形鲁棒的远程抛掷。其核心贡献在于统一处理机械臂反作用力、底盘稳定性和近端到远端能量传递，并通过多地形硬件实验证明该方法对非结构化环境具有实用性。

### 五、方法论与关键技术细节
关键实现上，动能链分析忽略重力并使用远端零力矩的被动响应近似，仅用于推导正弦基函数形式，实际轨迹可行性由完整机器人动力学和力矩约束在SQP中保证。优化目标中的正定权重矩阵用于强调期望抛掷方向上的释放速度分量，有效抛掷区间由正弦关节参考的零速度点定义。强化学习策略不直接替代优化轨迹，而是在优化参考附近学习底盘协调与机械臂残差修正，并用历史编码潜在表示增强地形适应。预览未给出完整RL超参数和训练规模，且方法依赖简化动能链建模与仿真到硬件的迁移验证，但其约束覆盖关节位置、速度、力矩和释放时刻，实验覆盖平地、草地、斜坡和粗糙路面。
