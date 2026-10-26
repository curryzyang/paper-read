# Rapid stabilization for Stokes and Navier-Stokes systems with localized disturbance

- 区域：精读区
- 排名：1
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Christian Calle, Patricio Guzmán, Hugo Parada, Jefferson Prada
- 机构：Pontificia Universidad Católica de Chile, Université de Lorraine, Universidad Técnica Federico Santa María
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31790v1) · [PDF](https://arxiv.org/pdf/2610.31790v1)

## TLDR
This paper proposes a multivalued Lyapunov-frequency feedback with a sign operator to achieve robust rapid exponential stabilization of Stokes and 2D/3D Navier–Stokes systems under unknown spatially localized disturbances, with well-posedness established via differential inclusions and guarantees allowing arbitrarily large disturbance bounds.

## Abstract
In this study, we analyze the rapid stabilization of Stokes and the two- and three-dimensional Navier-Stokes systems in the presence of an unknown spatially localized disturbance. A multivalued feedback control strategy is proposed which combines the Lyapunov frequency method with the multivalued sign operator. This methodology connects Lyapunov-based stability analysis with spectral inequalities, while the inclusion of the sign operator provides robustness against disturbance. The closed-loop system is governed by a differential inclusion, for which well-posedness is proved via the theory of maximal monotone operators. This approach guarantees global rapid exponential stabilization for the Stokes system and local rapid exponential stabilization for the two- and three-dimensional Navier-Stokes systems, with arbitrarily large disturbance bounds. In three dimensions, we obtain global strong solutions and rapid exponential stabilization for initial data sufficiently small in the $L^2$-norm with a prescribed, arbitrarily large bound in the $H^1$-norm.


## 精读解读（中文）
### 一、研究动机
本文关注在未知空间局部扰动下，Stokes方程以及二维、三维不可压Navier–Stokes系统的快速指数稳定问题。已有频率Lyapunov方法能实现任意指定衰减率，多值符号反馈能增强鲁棒性，但将二者结合并推广到含不可压约束、压力项、非线性对流和三维适定性难题的流体系统仍非平凡。论文旨在给出显式、鲁棒且可证明适定的快速稳定反馈机制，并允许扰动幅值上界任意大。

### 二、技术方案（Method）
在光滑有界区域Ω中，控制与未知扰动均通过指示函数1_ω局部作用于控制区ω，扰动仅假设满足d∈L1_loc(0,∞;L2(ω))且ess sup||d(·,t)||L2(ω)≤D。作者构造多值反馈Gλ:H→2^{L2(Ω)}，将Xiang的频率Lyapunov方法与多值sign算子结合：利用Lebeau–Robbiano谱不等式设计低频有限维反馈，并以sign型多值项抵消匹配的局部未知扰动。闭环系统写成微分包含，借助极大单调算子理论证明Stokes闭环的适定性；对二维和三维Navier–Stokes系统，先构造截断系统的强解并建立H与V能量估计，再分别在二维直接移除截断、三维结合H小范数与V有界性移除截断。整体流程包括反馈设计、谱不等式估计、先验稳定估计、闭环适定性与截断去除。

### 三、结果（Result）
对Stokes系统，任意y0∈H和任意满足假设的扰动d均得到唯一广义解，并满足||y(t)||H≤Cλ e^{-λt/4}||y0||H。对二维Navier–Stokes系统，当||y0||H≤ρλ时得到唯一广义解及相同指数衰减；对三维系统，当y0∈V、||y0||V≤R/2且||y0||H≤ρ_{λ,D,R}时，对任意T得到唯一全局强解，H范数按e^{-λt/4}衰减，且sup_{t≥0}||y(t)||V≤R/√2。稳定常数可显式取为Cλ=√μλ=C1e^{C1√λ}，仅依赖Ω、ω和λ，且扰动界D可任意大而不要求扰动随时间衰减或幅值小。

### 四、结论（Conclusion）
论文证明多值频率Lyapunov–sign反馈可在未知局部匹配扰动下实现精确扰动抑制和任意指定速率的快速指数稳定：Stokes为全局稳定，二维Navier–Stokes为局部稳定，三维在H范数小且V范数有给定界的初值条件下获得全局强解与稳定。该结果将鲁棒快速稳定框架从热方程推广到不可压Stokes/Navier–Stokes系统，并给出显式稳定常数和适定性分析；主要限制是三维情形需要足够小的H初值，且扰动界越大所需初值越小。

### 五、方法论与关键技术细节
关键实现点包括：扰动仅在控制通道1_ω内匹配进入，并只知道L2(ω)意义下的一致上界D；反馈是多值的，因而闭环为微分包含，适定性依赖极大单调算子理论；频率Lyapunov部分使用Lebeau–Robbiano谱不等式处理低频模态，sign算子提供对未知扰动的鲁棒性；二维和三维均通过截断系统先证强解，再以H和V能量估计移除截断，三维额外保留完整Stokes耗散并利用V范数有界控制非线性项；衰减率为λ/4，稳定成本常数随√λ指数增长；局限在于三维要求||y0||H≤ρ_{λ,D,R}且ρ随D增大而减小，结果本质为局部稳定，且假设Ω光滑、ω非空、扰动仅具L2(ω)有界性而不具结构信息。
