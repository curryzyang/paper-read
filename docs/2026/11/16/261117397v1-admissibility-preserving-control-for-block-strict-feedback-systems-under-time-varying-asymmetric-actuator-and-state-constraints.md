# Admissibility-Preserving Control for Block Strict-Feedback Systems Under Time-Varying Asymmetric Actuator and State Constraints

- 区域：精读区
- 排名：1
- 匹配度：5.8/10
- 来源：arxiv
- 作者：Saurabh Kumar, Lohitvel Gopikannan, Shashi Ranjan Kumar, Abhinav Sinha
- 机构：Indian Institute of Technology Bombay, University of Cincinnati
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17397v1) · [PDF](https://arxiv.org/pdf/2611.17397v1)

## TLDR
The paper proposes a time-varying admissibility-preserving control framework that combines a dynamic input realization for moving asymmetric actuator constraints with logarithmic-barrier backstepping for full state constraints, proving exponential tracking convergence while keeping all states and inputs admissible.

## Abstract
This paper addresses the tracking control of block strict-feedback nonlinear systems subject to time-varying asymmetric actuator and full state constraints. To that end, we develop a time-varying Admissibility-Preserving Control (APC) framework, in which the Admissibility-Preserving Input Realization (APIR) generates the plant input through a dynamic realization. The APIR guarantees input admissibility under the moving actuator set whenever each actuator bound contracts slower than the decay rate of the realization, and a closed-form lower bound on its gain is derived. The state constraints are handled by a logarithmic barrier coordinate at every backstepping step, with widths measured from the virtual control to the moving envelope of the corresponding state. We prove that every state lies inside its envelope, with each virtual control only required to remain inside the envelope of the next state, while the tracking error converges to zero exponentially. Simulations demonstrate the efficacy of the proposed safety-critical control scheme.


## 精读解读（中文）
### 一、研究动机
工程系统中执行器限幅与状态约束常随时间变化，例如执行器降额、故障和工况变化；现有饱和/抗饱和、障碍Lyapunov反步、漏斗/预设性能及CBF-QP方法多针对定常或对称执行器约束，或依赖离线可行性检验、在线QP可行性或性能放宽。本文旨在为块状严格反馈非线性系统建立统一的时变APC框架，用单一显式条件同时认证输入容许性与全状态安全。

### 二、技术方案（Method）
针对块状严格反馈系统在时变非对称执行器集和全状态包络下的跟踪控制，构造APIR以微分方程动态生成实际输入，其有效增益在边界处消失，从而在每执行器界收缩慢于实现衰减速率时保持移动执行器集合前向不变，并推导实现增益的闭式下界。反步递推每一步采用对数障碍坐标，以虚拟控制到对应状态移动包络的宽度度量，替代传统BLF中为误差预留障碍宽度的可行性条件；将虚拟控制位于下一状态包络内的分离条件与APIR命令有界性合并为Lyapunov子水平集上的APC兼容性检验。闭环分析通过精确Lyapunov恒等式给出跟踪误差显式指数衰减率与幅值，并可经收紧执行器集将输入容许性传递到有界偏差的物理执行器。

### 三、结果（Result）
理论结果表明，在APC兼容条件下每个状态始终位于其移动包络内，移动执行器集合保持前向不变，所有闭环信号有界，跟踪误差以显式速率指数收敛到零且具有显式幅值；虚拟控制只需保持在下一状态包络内的分离条件。APIR在每执行器界收缩慢于实现衰减速率时保证输入容许性，并给出实现增益的闭式下界。仿真验证了所提安全关键控制方案的有效性，但未报告硬件实验。

### 四、结论（Conclusion）
本文将APC从定常非对称执行器集推广到时变非对称执行器与全状态约束下的块状严格反馈系统，用APIR保证输入容许性、用逐步对数障碍坐标保证全状态安全，并以单一兼容性条件统一认证两类约束。该结果给出指数跟踪收敛与前向不变性的可证明保证，为执行器降额、故障等时变安全约束控制提供了一种可解释的递归设计思路。

### 五、方法论与关键技术细节
实现上无需训练和损失函数，输入为光滑的块状严格反馈模型、时变非对称状态/执行器上下界及初始条件；关键条件是执行器界收缩率慢于APIR实现衰减率、APIR增益存在闭式下界，以及分离条件与命令有界性构成的APC兼容性在Lyapunov子水平集上可验证。误差与障碍坐标的闭式比值携带相邻坐标交叉项，使闭环Lyapunov恒等式精确并给出显式衰减率；在线复杂度主要来自n步反步障碍坐标与兼容性集检验，APIR为一阶动态实现。局限包括速率与兼容性条件可能保守、依赖模型光滑性和时变边界信息，当前仅仿真验证，物理执行器需采用收紧集并允许有界输入偏差，兼容性不满足时不能无条件保证。\n
