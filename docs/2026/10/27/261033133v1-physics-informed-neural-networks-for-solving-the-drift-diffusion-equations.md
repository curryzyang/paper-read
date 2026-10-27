# Physics Informed Neural Networks for Solving the Drift-Diffusion Equations

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Luke Ragan, Matteo G. C. Alasio, Enrico Bellotti, Luca Dal Negro
- 机构：Politecnico di Torino, Boston University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33133v1) · [PDF](https://arxiv.org/pdf/2610.33133v1)

## TLDR
This paper demonstrates that Physics-Informed Neural Networks can accurately solve the nonlinear drift-diffusion equations for semiconductor PN junctions under all bias conditions, including 1D and 2D geometries, and can also solve inverse problems by reconstructing doping profiles from desired electric-field or potential distributions.

## Abstract
The drift-diffusion equations are the fundamental building block for the modeling, design, and optimization of modern semiconductor devices. Solutions of the drift-diffusion equations rarely give way to analytical forms, and exhibit strong nonlinearity, with the solutions ranging over several orders of magnitude. These attributes have led to research into numerical solvers, and while many commercial Technology Computer Aided Design (TCAD) packages now exist, they may require long simulation times, exhibit sensitivity to initial guesses, and rely on mesh generation. Further, these solvers are not well suited for inverse problems where the design parameters of a device are retrieved from its desired functional characteristics. To address all these challenges, this work demonstrates the usage of Physics Informed Neural Networks (PINNs) for the solution of the drift-diffusion equations with errors comparable to traditional simulation software using advanced training techniques to solve problems beyond the well-behaved equilibrium regime. For this study, we specifically choose an abrupt PN-junction in both one and two dimensions that features extreme gradients of the carrier concentrations at the Ohmic contacts and an abrupt discontinuity in the doping profile. Using the proposed PINN architecture, we are able to retrieve accurate results for all observables under all bias conditions. Additionally, we apply the PINN solver towards the inverse problem of retrieving doping profiles directly from desired electric field distributions or electrostatic potentials under non-zero applied biases. Our work establishes a powerful PINNs-based approach for semiconductor device modeling with the ability to solve inverse problems under non-equilibrium conditions for microelectronics research and discovery.


## 精读解读（中文）
### 一、研究动机
漂移-扩散方程是半导体器件建模、设计与优化的核心方程，但具有强非线性和跨数量级解，通常无解析解；传统TCAD的有限元/有限体积求解依赖网格、初值且仿真时间长，尤其不擅长从期望性能反推器件参数的逆设计问题。因此需要一种无网格、对初值不敏感且能统一处理正逆问题的求解框架。

### 二、技术方案（Method）
作者构建PINN求解稳态Poisson-漂移扩散方程组：以归一化位置为输入，用三个独立全连接网络分别输出静电势ψ及载流子变量，并采用准费米能级表述与Slotboom变量归一化以改善前向偏置下的精度和数值范围；Ohmic接触边界通过输出硬约束精确满足，二维绝缘边界以Neumann罚项加入损失，PDE残差由自动微分得到。训练采用Adam双精度优化、余弦学习率衰减，先联合训练三个网络，再按Gummel分裂方式各网络仅优化自身方程与边界损失，并以SRH复合模型闭合方程。

### 三、结果（Result）
在1D和2D突变PN结上，所提PINN在所有偏置条件（包括远离平衡的非平衡条件）下均能准确复现各可观测量，误差与传统仿真软件相当；同时该求解器可执行逆问题，在非零偏置下从期望电场分布或静电势分布直接反演掺杂剖面。摘要未给出具体误差数值，但强调对Ohmic接触处载流子浓度极端梯度和掺杂突变均获得准确结果。

### 四、结论（Conclusion）
该工作表明，经过架构与训练策略改进的PINN能够有效求解半导体漂移-扩散方程的正问题与非平衡逆问题，克服传统求解器对网格和初值的依赖，并为微电子研究中器件自动设计和新型几何发现提供了可行路径。

### 五、方法论与关键技术细节
关键实现包括：变量采用ψ、φn、φp的准费米能级表述，并进一步使用归一化Slotboom变量ũ、ṽ∈[0,1]以消除偏置相关尺度；三个5隐藏层×32单元的全连接网络，sigmoid激活、线性输出，输入为归一化坐标；Ohmic边界以硬约束嵌入输出，2D Neumann边界作为损失罚项；损失由Poisson、电子连续性、空穴连续性及边界残差构成，复合采用SRH模型；Adam优化器ε=1e-12、双精度、学习率从1e-3余弦衰减至5e-5，基线训练30000轮；2–6层与8–128单元的系统研究表明5×32是覆盖所有偏置和可观测量准确性的最小架构，浅层网络常不收敛；训练分联合阶段与Gummel分裂阶段。局限性在于研究集中于1D/2D突变PN结，摘要未报告具体误差指标，也未充分展示复杂几何、时变或更广泛材料体系的泛化能力。
