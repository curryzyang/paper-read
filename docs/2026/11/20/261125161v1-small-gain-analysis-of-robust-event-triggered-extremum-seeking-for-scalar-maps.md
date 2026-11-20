# Small-Gain Analysis of Robust Event-Triggered Extremum Seeking for Scalar Maps

- 区域：精读区
- 排名：1
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Victor Hugo Pereira Rodrigues, Tiago Roux Oliveira, Miroslav Krstic, Zhong-Ping Jiang
- 机构：State University of Rio de Janeiro (UERJ), University of California San Diego (UCSD), New York University (NYU)
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25161v1) · [PDF](https://arxiv.org/pdf/2611.25161v1)

## TLDR
This paper presents a small-gain, averaging-free analysis of sample-and-hold event-triggered gradient extremum seeking for scalar quadratic maps, showing that triggering on the measured demodulated gradient with a positive offset achieves exponential practical convergence with closed-form residual bounds and a positive minimum inter-event time, thereby excluding Zeno behavior.

## Abstract
We study a sample-and-hold implementation of gradient extremum seeking for a scalar quadratic map in which the control signal is refreshed only when an event occurs. The event generator acts on the demodulated gradient signal as it is actually measured, rather than on its averaged version, and contains a strictly positive offset, following the small-gain philosophy for robust event-triggered control. Rather than invoking averaging theorems, we work directly with the exact dynamics of the parameter estimation error. In the scalar setting, the demodulated gradient has an explicit sinusoidal structure, which is exploited through a change of variables that absorbs the zero-mean oscillatory perturbation, together with a quadratic Lyapunov function and the persistence of excitation of the probing signal. For a sufficiently fast dither, the estimation error is shown to decay exponentially to a residual neighborhood of the origin whose size is quantified by the dither amplitude and frequency, and by the relative threshold and the offset of the event generator. All constants, including the input-to-state stability gain of the extremum seeking loop, the admissible dither frequency and the positive lower bound on the time between two consecutive events, are given in closed form, so that Zeno behavior is excluded. A simulation example illustrates the results.


## 精读解读（中文）
### 一、研究动机
事件触发极值搜索可减少嵌入式或网络平台的控制刷新与带宽消耗，但已有方法多在平均模型上设计触发器，难以直接保证真实振荡回路在持续扰动下的鲁棒性；本文旨在用ISS小增益框架直接分析精确的事件触发极值搜索动力学，处理解调梯度中的振荡和采样误差。

### 二、技术方案（Method）
针对标量二次映射，采用正弦探测与解调得到梯度估计Ĝ=M y，估计器为积分器并使用零阶保持，仅在事件时刻更新u=kĜ(t_k)；事件发生器基于实际测量的解调梯度设置|e|>σ|Ĝ|+ε，其中e=Ĝ(t_k)-Ĝ(t)。分析上不调用平均定理，而是写出参数估计误差的精确闭环，将周期零均值扰动通过变量变换吸收，结合二次Lyapunov函数、探测信号持续激励以及事件发生器作为线性增益加偏置的ISS小增益条件推导稳定性。

### 三、结果（Result）
在抖动频率足够快时证明估计误差局部指数实用稳定，收敛到原点邻域，其残差大小由抖动幅值、频率、事件触发相对阈值σ和正偏置ε以及映射参数显式量化；所有常数包括极值搜索回路的ISS增益、允许频率和连续事件最小时间下界均给出闭式表达，从而排除Zeno行为。仿真示例验证了结果。

### 四、结论（Conclusion）
论文表明无需平均近似即可用精确动力学和小增益思想稳健地分析标量事件触发极值搜索，并在保证事件间隔正下界的同时获得可调残差收敛。该结果为资源受限平台上的极值搜索事件触发实现提供理论依据，但结论主要限于标量二次型局部模型，多变量情形需另作处理。

### 五、方法论与关键技术细节
关键实现只需输出测量和上次发送的Ĝ(t_k)来评估触发条件，不依赖θ*、Q*、H*；仅已知H*符号，增益k满足sgn(k)=-sgn(H*)，β(t)=1-cos(2ωt)保证适应增益符号与持续激励，并利用Δ的周期零均值原函数ΨΔ吸收振荡。分析中将采样误差和二次项合并为χ=e+d_q，并用|χ|≤ρ_R|θ̃|+δ得到小增益，δ=σd̄+ε，ρ_R含R项；主要局限是标量二次映射、局部结果、需要足够快抖动和已知曲率符号，且验证以仿真为主。
