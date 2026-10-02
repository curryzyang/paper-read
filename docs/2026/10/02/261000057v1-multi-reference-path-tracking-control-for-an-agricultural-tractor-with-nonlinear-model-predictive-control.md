# Multi-Reference Path Tracking Control for an Agricultural Tractor with Nonlinear Model Predictive Control

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Marcel Moll, Timo Oksanen
- 机构：Technical University of Munich
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00057v1) · [PDF](https://arxiv.org/pdf/2610.00057v1)

## TLDR
This paper presents a nonlinear model predictive path-tracking controller for an agricultural tractor that incorporates multiple piecewise-linear reference segments directly into its objective function, achieving a 6.1 cm mean absolute cross-track error in field tests with an average solver time of 3.45 ms.

## Abstract
Guiding a tractor along a predefined reference path is a key component of precision agriculture. This study develops a path tracking controller based on Nonlinear Model Predictive Control, which incorporates multiple segments of a piecewise-linear reference path directly into the objective function. In addition, methods for selecting viable reference segments from the full path are presented. The control system is evaluated during a field test with a tractor controlled via the Tractor Implement Management steering interface. The NMPC solver converged on average after 3.45 ms and tracked the curved reference path with a mean absolute cross-track error of 6.1 cm.


## 精读解读（中文）
### 一、研究动机
精准农业中引导拖拉机沿预定路径行驶是核心任务，但已有基于 NMPC 的路径跟踪方法通常只将单一直线参考段纳入成本函数，在弯曲路径上会产生锯齿形跟踪误差且无法充分利用长预测时域。本文旨在将预测时域内的多个分段线性参考段直接纳入目标函数，以提升弯曲路径的预测跟踪能力，并在带 TIM 转向接口的拖拉机上完成田间验证。

### 二、技术方案（Method）
控制器采用非线性模型预测控制，系统模型为连续时间运动学自行车模型，状态含全局平面坐标 xg、yg、航向 psi_g、拖拉机坐标系速度 vt、转向角 delta_t 及转向角导数 delta_dot_t，控制量为转向角导数，速度由驾驶员控制并作为每次迭代更新的常数参数。成本函数由多段参考距离项和转向角导数项组成：对每个有限线段计算带符号交叉轨迹距离和归一化进度 s，再用 sigmoid 平滑构造 alpha_i、beta_i 选择器，使距离成本在预测位置附近仅激活最近或当前参考段，并把第一段和最后一段的窗口不钳位以保持路径外可行参考。路径处理模块负责加载和预处理路径、保证最小段长、生成直线或 Dubins 启动轨迹、每控制周期根据车辆位姿更新路径索引且只检查相邻两段，并在参考点不足时线性延长最后段、在首段与后续段夹角超过 60 度时用最后有效段的线性延长替代后续段。实时实现使用 acados 与 CasADi 生成 C 代码，QP 子问题由 HPIPM 求解，预测时域 100 步、步长 100 ms，通过 ISO 11783 CAN 和 TIM 转向接口控制拖拉机，并用 Runge-Kutta 积分按 300 ms 估计执行器延迟传播先前控制命令，以预测时刻状态初始化 NMPC。

### 三、结果（Result）
田间试验在草地八字形变曲率路径上完成，NMPC 求解器平均 3.45 ms 收敛，跟踪平均绝对横向误差为 6.1 cm；交叉轨迹误差均值为 0.2 cm、标准差 8.4 cm，最大负误差 -26.5 cm、最大正误差 32.9 cm。转弯时控制器跟踪半径略大于规划路径，但因对称路径而抵消；中段存在振荡误差，部分来自线性分段和平滑残差，局部振荡可能与无 IMU 时 GNSS 未投影到地面、地形起伏引起横滚导致不必要转向有关。

### 四、结论（Conclusion）
结果表明，将多个分段线性参考直接放入 NMPC 目标函数可有效跟踪弯曲路径，并能在基于 TIM 的农用拖拉机上实时运行；该扩展相较单参考段方法更适合长预测时域下的曲线跟踪，但横向误差振荡、最大误差和 GNSS/IMU 约束仍是后续改进方向。

### 五、方法论与关键技术细节
试验车为 Fendt 314 Vario Gen 4，双 GNSS 天线基线 1.625 m，Septentrio mosaic-H RTK 定位，主天线估计精度 2 cm、航向标准差 0.15 度，速度取自 ISO 11783-7，转向角取自 TIM 消息；控制器权重 W 为 diag(3,0,0,0,0.01)，sigmoid 斜率 k=3，轴距 2.42 m，执行器延迟 300 ms，速度 1.2 至 2.5 m/s，转向角约束正负 30 度，转向角速率约束正负 40 度每秒。关键先验是分段线性路径和运动学自行车模型，损失为非线性最小二乘形式的距离项加转向角导数项，预测时域 100 步、100 ms，实时性依赖 acados/CasADi/HPIPM；主要局限是 sigmoid 有限斜率会扭曲参考并在相邻段之间产生距离成本为零的临界区，k 需按段长和转角调节，预测时假设速度恒定且执行器延迟与速度变化会降低精度，缺少 IMU 和地面投影也会导致振荡。
