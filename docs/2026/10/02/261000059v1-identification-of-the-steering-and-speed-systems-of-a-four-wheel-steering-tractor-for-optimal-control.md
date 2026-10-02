# Identification of the Steering and Speed Systems of a Four-Wheel-Steering Tractor for Optimal Control

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Riikka Soitinaho, Timo Oksanen
- 机构：Technical University of Munich
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00059v1) · [PDF](https://arxiv.org/pdf/2610.00059v1)

## TLDR
This paper uses data-driven gray-box system identification to model the steering and speed actuation of a four-wheel-steering agricultural tractor as first-order systems with estimated time constants and transport delays, combined with a kinematic model for model-based path-tracking control.

## Abstract
Model-based control design requires sufficiently accurate model of the system-to-be-controlled. This paper addresses the system identification of steering and speed control of a four-wheel-steering agricultural tractor for the purpose of developing path tracking control. To this end, we investigate the steering and speed control systems of the tractor. These are complex systems with digital, mechatronic, and hydraulic components challenging to model based on first principles. We take a data-driven approach to estimating the system models. The resulting model combines the kinematic model of the vehicle, actuators modelled as first-order systems, and estimated values for time constants and transport delays.


## 精读解读（中文）
### 一、研究动机
基于模型的控制设计，尤其是路径跟踪中的模型预测控制，需要足够精确的被控对象模型。四轮转向农用拖拉机的转向与速度系统由数字、机电和液压部件构成，难以用第一性原理建模，因此本文采用数据驱动灰箱辨识为后续最优控制提供模型。

### 二、技术方案（Method）
以G-trac四轮转向拖拉机为对象，构建运动学自行车模型与执行器模型：前轮转向、后轮转向和速度均用带纯延迟的一阶SISO传递函数描述，先验设定稳态增益K=1，仅辨识时间常数τ和传输延迟T。在田间自动驾驶模式下通过CAN总线发送方波激励，分别激励单个执行器而其余执行器保持零转角或恒速，采集输入输出数据；随后用MATLAB系统辨识工具箱，采用自适应子空间高斯-牛顿迭代最小化模型仿真响应与实测响应误差，并用不同实验数据进行验证。

### 三、结果（Result）
辨识得到前轮转向τ=0.73 s、T=0.43 s，拟合估计数据91.5%；后轮转向τ=0.62 s、T=0.39 s，拟合95.1%；速度τ=1.13 s、T=0.39 s，拟合91.0%。验证拟合范围为：速度84.9%–93.2%，前轮66.5%–89.4%，后轮85.7%–91.4%，表明模型总体可较好复现执行器响应，但前轮转向在大幅值和部分工况下泛化拟合偏低。

### 四、结论（Conclusion）
带传输延迟的一阶执行器模型结合四轮转向运动学模型，能以数据驱动灰箱方式充分描述该拖拉机的转向与速度控制响应，支持后续模型预测路径跟踪控制设计和田间实验；不过模型精度仍受激励数据覆盖范围与单一田间条件限制。

### 五、方法论与关键技术细节
实验在德国南部农田同一天完成，作物高度约10 cm，地形最大高程差约1.6 m，发动机恒定1430 RPM；转向激励为10 s或20 s相位宽、50%占空比的双极方波，幅值覆盖前轮最高34°和后轮最高15°，速度激励为最高2.34 m/s的单极方波，每个幅值与波形仅重复一次。参数标准差为前轮sd(τ)=0.0066、sd(T)=0.0046，后轮sd(τ)=0.0035、sd(T)=0.0024，速度sd(τ)=0.0135、sd(T)=0.0117；关键先验包括K=1、一阶传递函数与纯延迟结构，关键局限是未开展控制设计、单日单场地数据、样本量小，且未显式建模液压非线性、车辆侧向动力学和载荷变化。
