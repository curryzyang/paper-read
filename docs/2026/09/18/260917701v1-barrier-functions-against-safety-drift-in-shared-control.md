# Barrier Functions Against Safety Drift in Shared Control

- 区域：精读区
- 排名：3
- 匹配度：5.4/10
- 来源：arxiv
- 作者：M. Yusuf Uzun, Yildiray Yildiz
- 机构：Bilkent University, Illinois Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17701v1) · [PDF](https://arxiv.org/pdf/2609.17701v1)

## TLDR
This paper proposes a pilot-anchored control barrier function framework that prevents unsafe automation-induced workload safety drift in shared control by enforcing constraints relative to an unassisted baseline trajectory, guaranteeing feasibility and forward invariance, and demonstrating effectiveness on an F-16 pitch-tracking task.

## Abstract
Shared-control arbitration mechanisms can fail structurally when they are driven by quantities that evolve on the same automation-assisted trajectory that unsafe automation can corrupt. Under unsafe assistance, arising from faults or flawed design, the arbitration logic can adapt to the corrupted trajectory instead of resisting it. Focusing on workload regulation, this paper proposes a framework that prevents this problem by anchoring the safety constraints to an unassisted pilot trajectory. A baseline model evolving without automation assistance generates the acceptable workload envelope, while an assistance-induced deviation barrier and a closed-form mismatch bound relate actual and baseline workload evolution. The resulting control barrier function based quadratic program is always feasible and guarantees forward invariance of an augmented safe set. Simulations on an F-16 pitch-tracking problem show that the proposed method prevents workload-constraint drift under unsafe assistance.


## 精读解读（中文）
### 一、研究动机
共享控制仲裁若依赖与自动化辅助轨迹共同演化的量（如工作量），在故障或错误设计导致持续不安全辅助时，仲裁逻辑可能适应被污染的轨迹而非抵抗它，形成“变坏”循环，因此需要把安全约束锚定到不受辅助影响的飞行员基线上。

### 二、技术方案（Method）
将人-被控对象耦合建模为聚合线性系统 dx/dt=A x+B_ya y_a+B_r r，其中飞行员模型为 k_p(T_p s+1)/(T_z s+1)，工作量定义为 w_p=y_h^2+dot(y_h)^2。构造仅飞行员、零辅助的基线模型 d x_bar/dt=A x_bar+B_r r，并以 x_bar(t0)=x(t0) 初始化；实际与基线偏差 e=x-x_bar 满足 de/dt=A e+B_ya y_a。安全滤波用三个障碍函数：工作量下界 b1=w_p-w_L、上界 b2=w_U-w_p，以及辅助诱导偏差障碍；通过 ACBF 条件在 y_a=0 处定义并在二次规划中最小化 ||y_a-y_a,nom||^2，约束为 L_a b_i+alpha_i(b_i)>=0，从而在线输出过滤后的辅助命令。

### 三、结果（Result）
在 F-16 俯仰跟踪问题上的仿真显示，所提方法在四类严重不安全辅助场景下防止了工作量约束漂移。摘要报告所得 ACBF 二次规划始终可行，并保证增广安全集的前向不变性；但可获取文本未给出具体数值指标或基线对比数据。

### 四、结论（Conclusion）
将安全包线从受调节的辅助中解耦，并锚定到无辅助飞行员基线，可避免不安全辅助通过污染仲裁变量而持续准入自身的结构性问题。该框架在保持 ACBF 仲裁系统性、模块化和可行性的同时，为共享控制中的安全漂移提供了一种防护方案。

### 五、方法论与关键技术细节
关键实现细节包括：仅针对线性被控对象与线性飞行员模型给出闭式工作量障碍和可计算失配界；假设输出相对度满足 C_p B_p=0 且 C_p A_p B_p≠0，从而 H B_ya=0，避免工作量代数依赖待求 y_a；若飞行员训练良好则 A 为 Hurwitz，参考信号 r 及其到所需阶导数已知；辅助集 Y_a 含原点，令 y_a=0 即保证可行性。局限是依赖模型、线性化与仿真验证，未报告 F-16 之外或真实飞行实验，也未给出定量性能数据。
