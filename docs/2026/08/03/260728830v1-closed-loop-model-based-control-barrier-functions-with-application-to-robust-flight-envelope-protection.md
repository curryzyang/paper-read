# Closed-Loop Model-Based Control Barrier Functions with Application to Robust Flight Envelope Protection

- 区域：精读区
- 排名：2
- 匹配度：6.0/10
- 来源：arxiv
- 作者：Johannes Autenrieb, Mark Spiller, Peter A. Fisher, Junhyeok Yoon, Spilios Theodoulis, Anuradha Annaswamy
- 机构：Massachusetts Institute of Technology, German Aerospace Center (DLR), Delft University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28830v1) · [PDF](https://arxiv.org/pdf/2607.28830v1)

## TLDR
This paper introduces a closed-loop model-based control barrier function (CLM-CBF) framework that enforces flight envelope safety at the reference level using an explicit closed-loop model, thereby preserving the underlying controller's stability and robustness while enabling modular integration.

## Abstract
Ensuring operation of aerospace systems within prescribed flight envelope limits is a fundamental requirement for modern flight control architectures. Flight envelope protection aims to prevent violations of aerodynamic and structural constraints, thereby mitigating risks such as stall and excessive load factors. Control barrier functions (CBFs) have emerged as a principled tool for enforcing safety by ensuring that the system state remains within a prescribed safe set. In most existing approaches, safety constraints are imposed at the control input-level based on an open-loop model of the system. While this open-loop model-based CBF formulation enables modular design, it may alter the closed-loop system dynamics, potentially compromising robustness guarantees and complicating integration into existing flight control architectures. This paper proposes a closed-loop model-based control barrier function (CLM-CBF) framework for flight envelope protection. The key idea is to enforce safety at the reference-level using an explicit model of the closed-loop system, thereby preserving the stability and robustness properties of the underlying controller. This formulation enables safety filtering without modifying the control law, facilitating modular integration and retrofitting into existing systems.


## 精读解读（中文）
### 一、研究动机
现有飞行包线保护方法大多基于开环模型在控制输入层施加安全约束，这类开环模型控制障碍函数（OLM-CBF）虽然模块化，但会改变闭环系统动态，可能削弱鲁棒性保证，且难以集成到已认证的飞行控制架构中，甚至引发积分器饱和等问题。为此，本文提出闭环模型控制障碍函数（CLM-CBF）框架，在参考信号层利用闭环系统显式模型实施安全过滤，以保持底层控制器的稳定性与鲁棒性。

### 二、技术方案（Method）
该方法针对纵向导弹短周期模型，将非线性动力学在配平点线性化为状态x=[α,q]的LTI系统，控制输入为舵偏角δ。首先建立从参考指令r到状态x的闭环模型，即包含底层控制器动态的显式映射；然后基于闭环模型设计控制障碍函数条件，将安全约束（攻角界限）转化为关于参考信号的约束；最后构造二次规划（QP）安全过滤器，在满足闭环安全条件的前提下，求解对参考信号的最小侵入式修正，该修正不改变原有控制律，仅调整参考输入。

### 三、结果（Result）
在具有非线性气动特性和执行器约束的纵向导弹模型上进行仿真，结果显示CLM-CBF方法在激进机动过程中能够可靠地防止攻角等状态违反包线约束，同时保持期望的闭环行为，并保留了底层控制器的鲁棒性保证。与开环模型CBF方法相比，该方法避免了因修改控制输入而导致的闭环动态改变和稳定性裕度损失。

### 四、结论（Conclusion）
本文提出的CLM-CBF框架通过将安全过滤移至参考层并利用闭环模型，实现了安全保护与原有控制器性能的兼容，为飞行包线保护提供了一种可模块化集成、可改造现有系统的方案，尤其适用于追求严格鲁棒性的高性能飞行器。

### 五、方法论与关键技术细节
关键点包括：飞行包线安全约束被保守地转化为攻角α的上下界；闭环模型是设计核心，需准确反映从参考指令到状态的映射；安全过滤器采用QP形式，以参考信号修正量最小为目标；约束为CBF条件L_f h + L_g h u + α(h) ≥ 0基于闭环导数；执行器幅值与速率限制（±30°和±90°/s）在模型与控制器设计中需纳入；方法假设存在准确或可辨识的闭环模型，模型失配会影响安全保证，文中未给出完整复杂度分析和保守性量化。
