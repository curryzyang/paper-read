# Fuel-Efficient Formation Flying via Constrained Extremum Seeking

- 区域：精读区
- 排名：4
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Kwang Hak Kim, Luis G. Crespo, Michael J. Acheson
- 机构：NASA Langley Research Center, UC San Diego
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33305v1) · [PDF](https://arxiv.org/pdf/2611.33305v1)

## TLDR
This paper proposes APOGEE, a model-free constrained extremum-seeking guidance architecture that enables a trailing aircraft to safely learn and track a time-varying vortex for fuel-efficient formation flight while modulating excitation, adapting learning rates, and enforcing safety constraints to avoid abrupt rolling disturbances.

## Abstract
This paper presents a model-free autonomous guidance architecture for minimal drag of a trailing aircraft in formation flight. Realizing the fuel savings resulting from such a formation requires learning and tracking a time-varying vortex while avoiding locations where the aircraft experiences an abrupt rolling moment disturbance. A guidance architecture for fuel-efficient safe flight, called Adaptive Plateau-seeking Optimal Guidance with ModulatEd Excitations (APOGEE), is proposed herein. Key features of APOGEE are its ability to modulate the amplitude of the excitation required to learn the unknown objective and constraint functions, to adaptively adjust the learning rates, and to keep the flight safe during the search for the optimal formation. A threshold-gated modulation reduces the amplitude of excitation when the objective function reaches an acceptably large value, thus improving flying qualities and further reducing fuel consumption. Furthermore, a Newton-based learning rule, whose estimate of the inverse of the Hessian is spectrally clamped, adapts the learning rates to the local curvature of the objective function in order to accelerate convergence and lower the chance of overshooting the optimum. Finally, a safety filter having an unknown constraint function is used to prevent a loss of control event prompted by the above mentioned disturbance. The efficacy of APOGEE is demonstrated by using a high-fidelity model of an F-16 jet and an experimentally obtained vortex model. Being model-free, APOGEE does not require modeling the dependence of the unknown functions on the characteristics of the leading aircraft, the flight condition, the crosswind, and the vortex-induced turbulence.


## 精读解读（中文）
### 一、研究动机
编队飞行中后机可利用前机涡流显著减阻，但最优相对位置未知、时变，且靠近下洗或滚转反扭区域会引发突发滚转力矩甚至失控。基于涡模型的估计方法受模型偏差影响，传统极值搜索又存在激励抖动耗油、收敛慢和暂态不安全等问题，因此需要一种无模型、安全且燃油高效的自主引导架构。

### 二、技术方案（Method）
APOGEE作为外环制导生成相对横侧向与垂向位置指令，经PD控制器映射为滚转角与俯仰角指令，再由LQG加L1自适应内环控制F-16；内环被视为黑箱，并通过离线辨识的延迟按β_i=-ω_iτ_i补偿解调相位。外环对未知目标函数施加正弦抖动，解调测量输出以估计梯度，并采用Newton型学习规则更新位置，其中Hessian逆估计经Riccati型更新和谱截断限制；同时用阈值门控调制激励幅值，并用含未知约束函数的CBF-QP安全滤波器修正指令。目标函数取涡致滚转力矩系数C_l最大作为最小阻力的代理，实时实现中可用Kalman滤波器或干扰观测器获得较平滑的C_l估计。

### 三、结果（Result）
论文以F-16高保真模型和实验获得的涡模型验证APOGEE的有效性，表明该架构能够在未知时变涡场中搜索并跟踪有利编队位置。阈值门控在目标函数达到可接受值后降低激励幅值，从而改善飞行品质并进一步减少油耗；Newton型学习规则依据局部曲率调整学习率，加快收敛并降低越过最优点的风险；安全滤波器则防止突发滚转力矩扰动导致失控。文中还引用NASA Armstrong飞行实验背景指出最优编队位置可减阻约22%，但APOGEE本身的核心验证结论是无模型搜索、收敛改善与安全保持。

### 四、结论（Conclusion）
APOGEE将无模型极值搜索、曲率自适应Newton学习和未知约束安全滤波结合，为后机提供了一种无需对前机特性、飞行条件、侧风及涡致湍流建模的燃油高效编队制导方案。其优势在于能在线学习时变涡场、在接近安全边界时保持可控，并在获得可接受性能后减少持续激励带来的燃油代价。各机制的保证是局部且实践性的，论文没有给出组合系统的形式化稳定性证明。

### 五、方法论与关键技术细节
关键实现包括：以C_l最大值近似最小阻力，要求目标映射二阶连续可微、有界并存在局部极大值；抖动频率需与内环跟踪、估计和更新时间尺度分离，内环延迟需在激励频率处可辨识并用于相位补偿；Newton更新需对Hessian逆估计进行谱截断以避免病态曲率导致过大步长；安全滤波器使用未知约束函数h(p)并以CBF-QP形式防止进入滚转反扭或下洗危险区；阈值门控根据目标值切换激励幅值。局限性在于依赖可测代理信号、C_l最优与阻力最小存在小偏差、噪声和速率限制会影响估计，且理论保证为局部实际保证，未覆盖多机制组合的全局稳定性。
