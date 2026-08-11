# A Disturbance in the Force: Force Actuation on the RAVEN II Surgical Robot with Parallel Motor-Cable Units

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Haonan Peng, Dun-Tin Chiang, Jordan Hendricks, Andrew Lewis, Jared Shing, Haokun Feng, Yun-Hsuan Su, Blake Hannaford
- 机构：Mount Holyoke College, University of Washington
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06488v1) · [PDF](https://arxiv.org/pdf/2608.06488v1)

## TLDR
A parallel motor-cable force actuation system was developed to apply precise external forces (within ~1 N error) to the RAVEN II surgical robot, enabling collection of training data for learning-based force estimation without extra sensors.

## Abstract
Difficulty in haptic feedback for surgical robots has been a long-term problem for decades. In recent years, learning-based force estimation from robot states suggests desirable accuracy without the necessity of extra sensors. However, challenges remain in obtaining representative training data in which the robot moves in the workspace under various external forces. In this work, a parallel motor-cable system is developed. With six motor-cable units installed around the robot workspace, cables with controllable tension connected to the robot end-effector can provide the desired external force without interfering with the movement of the surgical robot. The development of the system includes motor-unit hardware, control software, sensor drivers, simulations, and more. Preliminary experiments suggest an accuracy of force actuation with errors less than 1 N.


## 精读解读（中文）
### 一、研究动机
外科手术机器人的力反馈长期难以实现，基于学习的力估计方法虽无需额外传感器，但缺少机器人在工作空间移动且受到各种外部力作用的代表性训练数据。

### 二、技术方案（Method）
开发了一套平行电机-缆绳力驱动系统，在工作空间周围安装6个电机-缆绳单元，缆绳连接RAVEN-II末端执行器，通过控制电机扭矩和缆绳张力施加任意方向和大小的外力。系统包括硬件（直流电机、缆绳卷盘、拉力传感器、固定框架）、基于ROS的控制软件（接收力指令、根据电机位置和末端位置计算缆绳方向、用SLSQP优化求解目标张力、两层反馈控制）、320 Hz传感器电子设备、系统仿真（蒙特卡洛工作空间分析、包围盒干涉检查）以及利用MicroScribe和Kabsch算法进行电机单元定位。

### 三、结果（Result）
初步实验表明，在X、Y、Z方向实际施加力与期望力的平均绝对误差分别为0.80 N、0.79 N和0.44 N，均小于1 N。

### 四、结论（Conclusion）
该平行电机-缆绳力驱动系统能够向RAVEN-II手术机器人的末端执行器施加期望外力，可用于收集学习型力估计模型的训练数据。未来将训练神经网络估计外力，并改进控制平滑性和稳定性，将电机驱动器和单片机从RAVEN-II系统中独立出来。

### 五、方法论与关键技术细节
系统保持最小缆绳张力以确保力驱动平稳；负载单元驱动以320 Hz提供张力反馈；仿真用于确定电机位置以平衡缆绳弹性影响和张力变化；定位需将设备坐标系转换到机器人坐标系；当前电机控制依赖RAVEN-II右臂并修改控制软件，未来将分离为独立驱动。局限性包括控制平滑性与稳定性有待改进，且系统尚未与RAVEN-II完全独立。
