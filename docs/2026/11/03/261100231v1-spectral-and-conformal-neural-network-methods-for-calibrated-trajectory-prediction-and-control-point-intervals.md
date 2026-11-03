# Spectral and Conformal: Neural Network Methods for Calibrated Trajectory Prediction and Control-Point Intervals

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Jasmine Ratchford, Raffaele Romagnoli
- 机构：Duquesne University, CMU Software Engineering Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00231v1) · [PDF](https://arxiv.org/pdf/2611.00231v1)

## TLDR
**TLDR:** The paper presents a fast, calibrated trajectory-prediction framework that combines a constrained spectral neural network with modified conformal quantile regression and interval arithmetic over B-spline control points to provide joint trajectory-level uncertainty guarantees, achieving approximately 100 Hz inference on a Raspberry Pi Zero 2 W.

## Abstract
Autonomous systems that navigate their environment need methods to quickly assess the feasibility and safety of desired trajectories. Traditional solutions that rely on numerical integration can be computationally heavy, while fast data-driven surrogates lack the formal guarantees that numerical approaches provide. This work demonstrates a framework that uses (1) a neural network with a spectral backbone to learn trajectories and quantile bands with built-in constraints (initial conditions and stability); (2) a modified conformal quantile regression to provide calibrated, joint trajectory-level coverage; and (3) interval arithmetic to extend noise-free coverage guarantees to control points. After refactoring the network for inference, the trajectory inference time for a quadrotor under a closed-loop linear quadratic regulator is 3.45~ms on a Raspberry Pi Zero 2 W. The total pipeline time, including trajectory inference time, is 9.81~ms, or approximately 100~Hz, consistent with typical control rates.


## 精读解读（中文）
### 一、研究动机
自主系统需要快速评估候选轨迹的可行性与安全性，但传统数值积分方法计算开销大，而快速数据驱动代理模型又缺乏形式化保证。作者希望在不反复数值积分的前提下，获得带校准不确定性的轨迹预测，并将轨迹级覆盖保证转化为可用于安全验证的紧凑 B 样条控制点区间。

### 二、技术方案（Method）
方法以 12 维初始条件为输入，先用全连接 SiLU 编码器升维并与初始状态拼接，再通过稳定谱层 Qθ exp(Λθτ) Qθ^H 在连续时间上线性演化，其中通过参数化约束 Re Λθ≤−εmin<0 保证稳定性；随后投影到物理状态子空间，并用均值解码器和两个 ReLU 门控分位数解码器在停止梯度的非物理残差上输出均值、下界和上界，α 在预热后启用以保证 τ=0 时输出等于初始条件。训练损失由轨迹 MSE、按通道标准化的 MSE、上下分位数的 pinball 损失以及可选的积分一致性惩罚组成；推理后采用改进的保形分位数回归，以所有维度和时间步上的最大非一致性分数构造联合轨迹级覆盖，再通过 B 样条伪逆和区间算术把轨迹分位带映射为控制点区间。

### 三、结果（Result）
在四旋翼闭环 LQR 场景和 Raspberry Pi Zero 2 W 上，重构后的网络单次轨迹推理时间为 3.45 ms，包含保形校准与区间扩展的总流水线时间为 9.81 ms，约 100 Hz，满足典型控制频率。校准实验使用 100000 条轨迹，其中 40000 条用于尺度参数、40000 条用于校准分位数、20000 条作为留出评估，方法可给出联合轨迹级覆盖并将分位带转换为控制点区间。

### 四、结论（Conclusion）
该工作表明，谱神经网络与改进保形分位数回归结合，可在不进行数值积分的情况下生成校准的轨迹预测和验证就绪的控制点不确定性区间。其紧凑 B 样条表示和约 100 Hz 的端到端延迟使实时安全评估在受限硬件上可行，为数据驱动代理模型补充了概率性覆盖保证。

### 五、方法论与关键技术细节
网络约 75K 参数，输入状态维度 d=12，时间点为固定采样集合，B 样条采用给定节点向量且三次样条控制点数 n_cp=n_int+4；分位数采用对称设置，保形分数取轨迹内最坏单元以获得联合覆盖。关键实现包括拼接初始条件以防升维信息丢失、谱层稳定性参数化、停止梯度残差解码、ReLU 保证上下界顺序、α 预热、可选积分一致性损失以及可选自适应节点放置。局限在于方法面向由初始条件唯一确定的自治 ODE，通常要求系统稳定或时域较短以适合低阶样条，且安全结论依赖交换性等保形假设，属于概率性评估而非确定性形式验证。
