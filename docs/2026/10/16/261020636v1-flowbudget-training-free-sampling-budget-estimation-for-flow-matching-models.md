# FlowBudget: Training-Free Sampling-Budget Estimation for Flow Matching Models

- 区域：精读区
- 排名：1
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Zahra Dehghani, Pablo Piantanida, Mohammadhadi Shateri
- 机构：ILLS, LIVIA, ÉTS Montréal, Mila -- Quebec AI Institute, CNRS, CentraleSupélec -- Université Paris-Saclay
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20636v1) · [PDF](https://arxiv.org/pdf/2610.20636v1)

## TLDR
FlowBudget is a training-free method that estimates the required sampling budget (NFEs) for a fixed pretrained flow matching model and solver by using simulation-free interpolation probes to estimate solver-relative discretization complexity, avoiding expensive FID-versus-NFE sweeps.

## Abstract
Sampling from continuous flow-based generators such as flow matching models requires numerical ODE or SDE integration, making inference cost depend on the number of function evaluations (NFEs). In practice, the sampling budget is inherited from prior work or selected through expensive FID-versus-NFE sweeps, using FID to assess image-generation quality, requiring sample generation and evaluation at multiple budgets. This makes sampling-budget selection dependent on repeated empirical evaluation. We therefore ask a complementary question to solver design and timestep allocation: for a fixed pretrained model and solver, what numerical resolution is sufficient? We introduce FLOWBUDGET, a training-free estimator of solver-relative sampling complexity. Using simulation-free interpolation probes of the learned dynamics, FLOWBUDGET normalizes the leading one-step discretization error by the motion, estimates its coefficient from interpolation probes, and maps a numerical tolerance to a step budget using the solver order. We derive estimators for numerical solvers in flow~matching sampling, namely Euler and Heun for ODE sampling and additive-noise Euler--Maruyama for SDE sampling, and connect the ODE coefficients to terminal integration error. Experiments on SiT, FlowDCN and Rectified Flow models, spanning flow-model architectures and formulations, test whether FLOWBUDGET can estimate the NFE budget without generating samples at multiple budgets or performing an FID-versus-NFE sweep. The code is available at https://github.com/Yasaman-dt/FlowBudget


## 精读解读（中文）
### 一、研究动机
Flow matching 采样依赖 ODE/SDE 数值积分，NFE 直接决定推理成本，但实际常继承固定预算或通过昂贵的 FID–NFE 扫描选择预算，需要在多个预算下反复生成与评估。本文提出一个互补问题：在固定预训练模型与求解器时，多少数值分辨率才足够？因此希望无需训练、无需质量扫描地估计采样步预算。

### 二、技术方案（Method）
FlowBudget 在少量数据子集上构造无模拟插值探针 x_t=(1−t)x_0+tε、t∼U[0,1]，对给定求解器定义单步局部误差 L_S 与位移尺度 D_S，并用稳定化相对误差 E_S=L_S/(D_S+ε|h|^β_S) 和归一化系数 r=q_S/(d_S+ε) 刻画；由小步长展开 L=κ|h|^α q、D=|h|^β d，得到平均相对误差约等于 κ C_S K^{−γ}，其中 C_S=E_μ[r]、γ=α−β，故给定容差 τ 的预算为 K=ceil((κ C_hat_S/τ)^{1/γ})。对 Euler ODE，q=||aθ||、d=||vθ||、α=2、β=1、γ=1，K_E=ceil(C_hat_E/(2τ))、NFE=K，其中 aθ=∂t vθ+J_x vθ vθ；对 Heun，q=||2gθ−cθ||、α=3、γ=2，K_H=ceil(sqrt(C_hat_H/(12τ)))、NFE=2K，其中 gθ=J_x vθ aθ、cθ 为二阶方向导数组合；对加性噪声 Euler–Maruyama SDE，先用速度估计 score sθ=−(x_t+(1−t)vθ(x_t,t))/t 与漂移 fθ=vθ−1/2 w_t sθ，令 A=J_x fθ G、B=∂t G，q=sqrt(||A||_F^2+||B||_F^2+<A,B>_F)、d=||G||_F、α=3/2、β=1/2、γ=1，K_EM=ceil(C_hat_EM/(√3 τ))。C_hat_S 由 N 个独立探针 Monte Carlo 平均，并用 Hoeffding 不等式给出集中界与预算置信区间；ODE 系数在 Lipschitz 稳定性假设下还与终端积分误差关联，EM 使用同一布朗路径的强局部误差。

### 三、结果（Result）
在 SiT、FlowDCN 和 Rectified Flow 上的实验用于检验 FlowBudget 能否在不进行多预算采样和 FID–NFE 扫描的情况下估计 NFE 预算；报告的核心是估计得到的预算对应可用的质量-成本工作点，并覆盖不同流模型架构与表述。方法同时给出 ODE 系数与终端积分误差的理论联系，以及有限探针下 C_hat_S 的 Hoeffding 集中界，说明估计误差可按探针数控制。由于摘要未给出具体 FID 或 NFE 数值，本文层面的主要实证结论是估计流程可行且跨模型适用，而非报告单一最优 FID。

### 四、结论（Conclusion）
FlowBudget 将固定模型-求解器下的采样预算选择转化为数值局部误差估计，提供无需训练、无需 FID 扫描的模型-求解器相对复杂度估计；它与求解器设计、时间步分配互补，可用于 Euler、Heun 与加性噪声 Euler–Maruyama。其主要价值是在给定容忍度 τ 时直接映射到步数/NFE，减少经验扫描成本，但结论限于数值积分误差和探针近似，不保证直接对应 FID。

### 五、方法论与关键技术细节
关键实现点包括：用训练数据小子集构造无模拟插值探针；用稳定化分母 ε 防止零运动处发散；C_S 是 population 系数，C_hat_S 用 N 个独立探针 Monte Carlo 估计，值域有界时 Hoeffding 给出 |C_hat−C|≤R sqrt(log(2/η)/(2N))；ODE 的 Euler 每步 1 NFE、Heun 每步 2 NFE；SDE 需在扩散项主导的探针时间域 [t_min,t_max] 且 inf||G||>0，并共享布朗路径定义强局部误差；理论依赖小步长均匀展开、Lipschitz 稳定性和足够小 h，且只针对固定预训练模型下的数值误差，不覆盖学习近似误差与 FID 映射。
