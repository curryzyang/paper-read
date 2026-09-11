# Disturbance rejection for classes of nonlinear systems

- 区域：精读区
- 排名：1
- 匹配度：6.0/10
- 来源：arxiv
- 作者：Saverio Messineo
- 机构：Salzburg University of Applied Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10553v1) · [PDF](https://arxiv.org/pdf/2609.10553v1)

## TLDR
TLDR: This paper designs non-adaptive global robust disturbance-rejection schemes for two nonlinear system classes—high-gain plus sliding-mode control for strict-feedback systems with unmatched disturbances and unavailable zero-dynamics, and open-loop-observer-based output feedback for minimum-phase uncertain systems with relative degree greater than one and matched disturbances—achieving input-to-state stability or global uniform boundedness with convergence to an arbitrarily small attractor.

## Abstract
This paper addresses the problem of non-adaptive global robust disturbance rejection for two distinct classes of nonlinear systems. The first class, denoted by C1, consists of nonlinear systems in strict-feedback form, with linear and Hurwitz zero-dynamics (whose states are unavailable for feedback), and enhanced - within this work - by forcing, unmatched, additive disturbances. Nonlinear tools are herein employed to demonstrate that the proposed control architecture - based on the high-gain paradigm - achieves closed-loop input-to-state stability with respect to the forcing disturbances, along with global asymptotic convergence towards an attractor which can be rendered as small as desired. Then, owing to the established input-to-state stability property, a uniformly bounded control action is additionally embedded within the control architecture. The additional unit, designed following the sliding-mode paradigm, is aimed at improving the disturbance rejection task, by potentially lowering the required high-gain control expenditure. The second class of systems, denoted by C2, is constituted by minimum-phase, uncertain, nonlinear systems with relative degree greater than one, featuring possibly unbounded, with possibly unbounded derivatives, output-dependent nonlinearities, with matched additive forcing disturbances. To solve the problem of output-feedback, non-adaptive, global robust disturbance rejection for systems within C2, first, an open-loop observer is employed in lieu of a classic dynamic extension adopted in earlier works, as the latter is no longer implementable due to the presence of unknown forcing disturbances. Subsequently, the results derived for C1 are then adapted to C2, to yield an output-feedback dynamic controller providing closed-loop global uniform boundedness, along with asymptotic regulation towards an attractor which can be rendered as small as desired.


## 精读解读（中文）
### 一、研究动机
本文研究两类非线性系统的非自适应全局鲁棒干扰抑制问题。第一类C1为严格反馈形式、零动态线性且Hurwitz但零动态状态不可反馈，并含不匹配加性强迫扰动；第二类C2为最小相位、不确定、相对阶大于1且含匹配加性强迫扰动的非线性系统。作者意图填补这两类设定下全局鲁棒干扰抑制，尤其是部分状态反馈和输出反馈情形的理论空白。

### 二、技术方案（Method）
对C1，系统由不可测零动态z与可测状态ξ_i组成，假设F(μ) Hurwitz、控制增益b_i有正下界、仅ξ_i可反馈；控制采用u=u1+ud，u1为高增益项−γ(y)y，ud为按滑模思想设计的均匀有界补偿项。基于Lyapunov函数V=z^T P z+y^2及P F+F^T P=−I证明V_dot≤−ε(‖z‖^2+y^2)+δΔ_1^2，并把该单步引理沿r级严格反馈归纳推广，得到闭环ISS与可任意小吸引子。对C2，由于未知匹配扰动使经典动态扩张不可实现，改用开环观测器处理相对阶大于1和输出反馈，再将C1的高增益加有界滑模单元结果适配到观测器误差系统，构造输出反馈动态控制器。

### 三、结果（Result）
C1闭环对强迫扰动具有输入到状态稳定性，并全局渐近收敛到可任意小的吸引子；附加滑模单元保持均匀有界，可改善干扰抑制并潜在降低所需高增益控制开销。C2输出反馈控制器实现闭环全局一致有界、对开环观测器估计误差的ISS，并渐近调节到可任意小吸引子。文中未给数值仿真指标，核心结论以稳定性定理和Lyapunov不等式给出。

### 四、结论（Conclusion）
本文建立了非自适应全局鲁棒干扰抑制框架，将高增益ISS性质与有界滑模补偿相结合，并扩展到输出反馈的不确定最小相位系统。主要贡献是证明C1的ISS并允许任意合适干扰抑制设计嵌入，以及用开环观测器解决C2在未知匹配扰动下的输出反馈问题。

### 五、方法论与关键技术细节
关键实现包括：μ需为常数以保证F(μ) Hurwitz，而另一组不确定参数可为时变或状态相关但需一致有界；扰动d_i和Δ_m一致有界且可不保持严格反馈结构；控制增益满足b_i≥b_i0>0。滑模补偿项形如u_d_bar(y)=−y p^2/(|y|p+η)，p尽量大、η尽量小，并给出V_dot≤−(ε/β)V+2β_3η；证明采用归纳Lyapunov方法以避免维数灾难。局限是非自适应、不估计扰动，仅保证有界、ISS与任意小残差而非精确抑制，C2还受开环观测器误差与相对阶假设约束。
