# Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics

- 区域：精读区
- 排名：5
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Shuangyu Xie, Kaiyuan Chen, Ken Goldberg
- 机构：University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18227v1) · [PDF](https://arxiv.org/pdf/2608.18227v1)

## TLDR
An LLM coding agent (Claude Code) autonomously generates a demonstration-free procedural controller for the Push-T task that achieves 100% success with 46% fewer steps than a diffusion policy trained on human demonstrations, and further scales to Push-A–Z and cross-embodiment 3D simulations.

## Abstract
Push-T is an iconic benchmark for learning manipulation policies from human demonstrations. The robot must use a single point of contact to push a T-shaped block into a target pose. In this short paper, we revisit the Push-T task in the context of emerging advances in Agentic Robotics where an LLM coding agent -- Claude Code with Fable 5 -- is prompted to create an algorithmic solution that does not require any demonstration data. We study how effective the agentic coding loop can solve the Push-T task, and compare the resulting code as policy with the visuomotor imitation learning policy. Results suggest that the agent found the 2D gym simulation online, and used sim experiments to learn push mechanics, iteratively optimizing to achieve 100% success rate using 46% fewer steps than the best diffusion policy trained with 200 human demonstrations. The coding agent also solve extensions from T to the full alphabet (Push-A to Push-Z) using a self generated curriculum and generated simulation code for the Franka and UR5 robot arms in 3D cross-embodiment simulations with visual feedback. Videos, policies and details will be posted online.


## 精读解读（中文）
### 一、研究动机
重新审视经典的Push-T机器人操作基准，探索新兴的Agentic Robotics范式能否在无需任何人类演示数据的情况下，由LLM编码代理自动生成程序化控制器，并与基于模仿学习的视觉运动策略进行对比，同时进一步扩展至更广泛的任务与具身形态。

### 二、技术方案（Method）
使用Claude Code with Fable 5作为LLM编码代理，仅基于自然语言任务描述启动自主循环：生成代码、在仿真中执行、观察成败、诊断并迭代修订方案。初始的Claude_state_controller采用几何混合反馈控制器，将环境状态表示为5维向量，通过离散接触库和准静态接触模型，在plan、approach、push、retreat四阶段状态机中贪心选择动作，并结合短视域执行与闭环重规划。随后通过提示添加视觉反馈，构建包含逐帧工作区感知（颜色分割、IoU拟合）、一次性标定、逐次推挤参数自适应（摩擦增益更新）的三阶段感知管线，形成Claude_vision_controller。在扩展到Push-Alphabet时，代理自生成26个字母形状的基准和自课程，通过多轮自我改进从47.1%提升至更高性能，并将视觉MPC控制器移植到Franka和UR5e仿真环境进行跨具身验证。

### 三、结果（Result）
在gym_pusht的200个固定种子评估中，Claude_state_controller达到100%成功率，平均步数120.1，平均推挤次数3.72，而LeRobot Diffusion Policy（200个人类演示训练）成功率仅62.5%，平均步数223.7，平均推挤次数6.38；Claude_vision_controller成功率97.2%。Push-Alphabet任务中，状态输入下的MPC控制器达到99.4%成功率，平均推挤次数5.15；视觉MPC在UR5e仿真上成功率为98.5%，在Franka仿真上为89.8%。整个开发过程生成约950万输出token，API成本约1500-2000美元，耗时约221小时。

### 四、结论（Conclusion）
实验表明，明确的几何接触推理结合闭环重规划能够成为基于人类演示的视觉运动策略学习的有效替代方案；Agentic编码循环可以生成无需演示数据的程序化策略，不仅解决Push-T，还能以自生成课程扩展到26个字母形状，并跨不同仿真机械臂实现具身迁移，展示了Agentic Robotics在机器人操作任务中的潜力。

### 五、方法论与关键技术细节
关键细节包括：任务提示明确禁止使用学习策略但允许现有机器人数据；状态空间包含推杆位置和T块位姿的5维向量；控制器依赖结构分解（面法向推挤平移、偏置推挤旋转）；视觉感知采用颜色分割、粗略到精细IoU拟合和摩擦参数自适应更新公式f←f·r^{-η}；评估阈值在Push-T为95%覆盖率，Push-Alphabet为90%；Push-Alphabet的自我学习经历了五个阶段，包括基线规划、旋转-平移权衡、薄笔画角覆盖、困难几何杠杆机制和恢复规则；经典Dubins pushing基线通过代理编写的适配器从83.8%提升至97.2%成功率；限制在于模拟器可能被代理利用API或数值规律，且对真实物理环境中的感知误差、校准漂移、摩擦变化等鲁棒性未验证。
