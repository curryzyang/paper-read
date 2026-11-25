# Geometric Control Analysis of an Internally Actuated Flying Wing

- 区域：精读区
- 排名：4
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Jonathan Becker, Ella M. Atkins
- 机构：Virginia Tech
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31463v1) · [PDF](https://arxiv.org/pdf/2611.31463v1)

## TLDR
This paper rigorously analyzes the geometric accessibility and controllability of a control-surface-free flying wing actuated by an internal moving mass, momentum wheel, and thrust—explicitly accounting for time-varying inertia—and demonstrates nonlinear MPC trajectory tracking under wind disturbances.

## Abstract
This paper presents a rigorous geometric accessibility and controllability analysis for a fixed-wing Uncrewed Aircraft System (UAS) actuated solely by an internal moving mass, a momentum wheel, and external thrust. This configuration eliminates traditional control surfaces, which in turn reduces the combinatorial set of computational fluid dynamics (CFD) studies necessary for high-fidelity modeling of flight through unsteady flow fields. Using Lie bracket computations and the strong Lie Algebra Rank Condition, it is shown that the full nonlinear dynamics are generically small-time locally accessible, with singular configurations explicitly characterized and shown to be immediately escapable by direct mass actuation. The stronger property of small-time local controllability is shown to hold for the attitude subsystem at equilibrium points, using Sussmann's condition. A key contribution is the explicit treatment of the time-varying inertia tensor via the Huygens-Steiner Theorem, which introduces nontrivial coupling between the control vector fields. The momentum wheel provides direct yaw authority that, combined with inertia variation from the moving mass, generates a full-rank accessibility Lie algebra. A nonlinear Model Predictive Controller (MPC) is derived with consideration of flight envelope constraints and is applied to track different trajectories under unperturbed and perturbed flow field conditions.


## 精读解读（中文）
### 一、研究动机
传统固定翼无人机依赖副翼、襟翼、升降舵和方向舵等控制面，导致高保真CFD建模需覆盖大量控制面组合，计算成本高且难以支撑低空非定常流场中的模型预测控制。现有移动质量控制在航天器、水下航行器和再入飞行器中有研究，但在飞机上多局限于配平点附近线性化分析，且单独移动质量缺乏协调转弯所需的偏航权限。本文因此研究仅由内部移动质量、动量轮和外部推力驱动的飞翼，并补足其非线性动力学、可及性与可控性的严格数学分析。

### 二、技术方案（Method）
论文建立15维状态向量，包含位置、速度、欧拉角、机体角速度、动量轮转速以及移动质量的弦向和展向位置；控制输入为移动质量弦向速度、展向速度、动量轮力矩和推力，并假设内部质量速度可控、二阶加速度可忽略。动力学建模采用刚体运动学、有限翼/升力线理论计算升阻力、风场相对速度计算迎角和侧滑角，旋转动力学以König定理处理内部角动量交换，并用Huygens-Steiner平行轴定理显式构造随移动质量位置变化的惯量张量。分析上使用李括号计算和强Lie Algebra Rank Condition证明全非线性动力学的一般小时间局部可及性，显式刻画奇异构型并说明可由直接质量驱动逃逸；对姿态子系统在平衡点应用Sussmann条件证明小时间局部可控性。控制部分推导带飞行包络约束的非线性模型预测控制器，用于无扰动和扰动流场下的爬升及8字轨迹跟踪。

### 三、结果（Result）
分析表明该飞翼的全非线性动力学在一般条件下是小时间局部可及的，奇异构型被明确表征且可由直接质量驱动立即逃逸；姿态子系统在平衡点满足更强的小时间局部可控性。动量轮提供直接偏航权限，并与移动质量引起的惯量变化耦合，生成满秩的可及性李代数，从而弥补单独移动质量缺乏偏航控制的不足。仿真案例将非线性MPC应用于爬升和8字轨迹跟踪，并在连续风场及Dryden湍流扰动下验证其效用；摘要未报告具体跟踪误差数值，因此可复现结论主要是定性的可及性、姿态可控性和扰动下轨迹跟踪可行性。

### 四、结论（Conclusion）
该无传统控制面的内驱动飞翼通过内部移动质量、动量轮和推力即可获得几何意义上的可及性，并在姿态子系统平衡点具备小时间局部可控性。去除控制面还使气动响应主要依赖流速和迎角，降低高保真数据驱动代理模型所需的CFD维度。结合带飞行包络约束的非线性MPC，该构型在无扰动和风扰条件下具备执行爬升与8字轨迹跟踪的潜力。

### 五、方法论与关键技术细节
关键实现细节包括15维状态与4维输入的欠驱动模型、内部质量准瞬时速度控制假设、对称翼气动俯仰矩为零的简化、König定理与平行轴定理对时变惯量的处理，以及强LARC和Sussmann条件的几何控制证明路径。NMPC显式考虑飞行包络约束，测试场景覆盖连续风场和Dryden湍流；但标称模型依赖有限翼/升力线理论，质量加速度被忽略，且摘要未给出MPC超参数、损失权重和定量跟踪指标。主要局限是姿态子系统可控性不等同于全状态小时间局部可控性，奇异构型虽可逃逸但仍需在控制器中规避，CFD降维优势也需后续高保真验证。
