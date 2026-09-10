# AccelMPC: High-Rate, Low-Power FPGA-Accelerated Model Predictive Control for Tiny Drones

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Andrea Grillo, Brian Plancher
- 机构：Dartmouth College, École Polytechnique Fédérale de Lausanne
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09380v1) · [PDF](https://arxiv.org/pdf/2609.09380v1)

## TLDR
AccelMPC enables 1 kHz onboard constrained model predictive control for a 35g Crazyflie via an end-to-end co-designed FPGA-accelerated ADMM solver and custom 6g PCB, achieving up to 15.6× faster solve times and 195.4× better energy-delay product than state-of-the-art embedded MCU solvers while handling over 20,000 optimization variables.

## Abstract
Unlocking the potential of tiny aerial robots requires order of magnitude improvements in the performance of embedded edge control. In particular, although recent cached model predictive control (MPC) solvers can handle the fast system dynamics and complex constraints required for agile drone flight, their computational demands remain prohibitive for resource-constrained robots, forcing prior implementations to operate at reduced control rates. AccelMPC overcomes this challenge through an end-to-end co-design approach that jointly optimizes the solver algorithm, numerical representation, hardware mapping, and physical integration. AccelMPC pairs a co-designed FPGA-accelerated alternating direction method of multipliers (ADMM)-based MPC solver with a custom 6g PCB, providing high-bandwidth communication for deployment on a 35g Crazyflie. Hardware experiments demonstrate 1 kHz onboard constrained MPC with dynamic obstacles, up to 15.6x faster solve times and 195.4x improvement in energy-delay product over state-of-the-art embedded microcontroller-based solvers, all while scaling to optimization problems with over 20,000 optimization variables and a comparable number of constraints. We release our PCB design files, firmware, and FPGA solver code open source.


## 精读解读（中文）
### 一、研究动机
微型空中机器人受尺寸、重量与功耗（SWaP）限制，其快速不稳定动力学却要求接近千赫兹的反馈频率，因此片上控制性能亟需数量级提升。已有的缓存式MPC求解器（如TinyMPC）虽能在Crazyflie级MCU上实现实时MPC，但在千赫兹控制率下每步只能完成一到两次ADMM迭代，约束激活时收敛不足，只能降低控制频率。这造成MPC承诺的显式约束预测控制与资源受限机器人实际能力之间的根本性差距。

### 二、技术方案（Method）
AccelMPC采用算法—数值表示—硬件映射—物理集成的端到端协同设计：输入为线性MPC问题，按交错顺序堆叠状态与输入得到块带状稀疏QP，用ADMM求解，其中w-更新为结构化线性方程组、y-更新为盒投影、λ-更新为对偶上升。离线缓存P、M与惩罚参数ρ，并预计算系数矩阵P+ρM^T M的带状Cholesky因子L（带内元素仅h个），在线求解退化为前代与回代两遍流式替换；同时将TinyMPC的矩阵级Riccati递推替换为标量级流水线友好的替换过程。在线阶段每控制步执行固定次数的ADMM迭代（保证确定性时延），对偶变量与辅助变量跨控制周期热启动，仅初始状态、参考窗口与约束上下界l、u在运行时更新。数值上使用32位定点算术，ρ限制为2的幂使乘除退化为移位，并把Cholesky每行对角元倒数存入行末以消除在线除法。两套互补的FPGA映射分别面向能效与可扩展性，配合自研6g PCB与Crazyflie（35g）通过高带宽低时延链路通信，部署于真实飞行闭环。

### 三、结果（Result）
硬件实验在35g Crazyflie上实现了1 kHz全机载带约束MPC，并在飞行中完成对动态障碍物的在线避障轨迹调整。相比最先进的嵌入式MCU求解器，求解时间最高快15.6倍，能量—时延积（EDP）改善最高达195.4倍，同时可扩展到超过20,000个优化变量及数量相当的约束。定点实现与IEEE-754单精度实现对比，量化带来的额外误差可忽略：预测位置RMSE差异约1e-6 m及以下、最大约束违反约1e-7 m、控制RMSE约1e-7。

### 四、结论（Conclusion）
结果表明，通过求解器结构、数值精度、硬件映射与物理集成的联合协同设计，FPGA加速的在线MPC可在极度受限的微型机器人平台上实现高带宽、显式约束的预测控制，突破了此前必须降频运行的瓶颈。作者据此提出FPGA硬件—算法协同设计是资源受限机器人实现高率约束预测控制的关键使能途径，并开源了PCB设计文件、固件与FPGA求解器代码（github.com/A2R-Lab）。

### 五、方法论与关键技术细节
关键点包括：采用TinyMPC式缓存ADMM，P、M、ρ离线固定，仅初始状态、参考窗口与l/u在线更新，牺牲少量灵活性换取大幅性能提升；用带状Cholesky因子替代Riccati递推或全矩阵求逆，前向/后向替换的循环依赖降到固定深度h的标量级，单次迭代复杂度随变量数线性增长O(N_var)，h由局部阶段耦合决定且几乎与预测时域无关，因此可流式流水线化；对比GPU方案需存储完整矩阵逆会超出嵌入式FPGA片上内存；32位定点、ρ取2的幂、存储对角元倒数消除在线除法，使在线算术仅含加、乘、移位与比较；每控制步固定ADMM迭代次数以保证确定性1 ms级控制周期与时延；对偶/辅助变量跨控制周期热启动利用时间相干性；局限在于定点量化精度、ρ调参自由度受限、依赖约束上下界在线可更新而P、M不变的结构假设，以及需自研PCB与FPGA带来额外硬件集成成本。
