# Addendum to "Optimal Steering of a Linear Stochastic System to a Final Probability Distribution, Part II"

- 区域：精读区
- 排名：4
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Yongxin Chen, Tryphon T. Georgiou, Michele Pavon
- 机构：Università di Padova, Georgia Institute of Technology, University of California, Irvine
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40888v1) · [PDF](https://arxiv.org/pdf/2610.40888v1)

## TLDR
This addendum fixes a gap in the induction proof of state-covariance controllability for linear stochastic systems by proving a stronger induction that permits arbitrary finite endpoint jets of the control, while also noting an independent proof via strong controllability on \(\mathrm{GL}^+(n,\mathbb{R})\) that extends to additive noise.

## Abstract
We hereby fill in a gap in an induction argument used in the proof of a theorem on state-covariance controllability of linear stochastic systems in an earlier paper by the authors. The mathematical statement is true. The missing point in the proof concerns the assertion that, in the canonical single-input case, the control can be assigned arbitrary endpoint values. We amend the argument by proving a slightly stronger induction statement that permits arbitrary finite endpoint jets of the control. An independent approach to homogeneous state-covariance controllability was provided in a paper by Abdelgalil and Georgiou (2025) as a corollary of strong controllability results on $\GLp(n,\mathbb R)$, and shown herein that it extends to the case of additive noise as well.


## 精读解读（中文）
### 一、研究动机
原文定理断言线性随机系统的状态协方差可控，但原证明在对可控规范单输入情形做归纳时，隐含假设辅助控制可在两端取任意端点值，而该性质未被归纳步骤保持。本文旨在补上这一证明缺口，并说明定理陈述仍然成立。

### 二、技术方案（Method）
作者给出两条技术路线：其一是强化规范单输入情形的归纳命题，允许控制及其有限阶端点 jet 任意给定；将协方差分块，把 p 作为低维子系统的控制，借助对数变换与 Hermite 插值构造具有指定端点 jet 的正函数，再用 Schur 补保证正定性并反解控制。其二是利用 Abdelgalil–Georgiou 关于 GLp(n,R) 强可控性的结果，由状态转移矩阵构造 homogeneous Lyapunov 轨迹，并通过积分项 Gamma(tau) 与短时拼接把结论扩展到 Q>=0 的加性噪声情形。

### 三、结果（Result）
补正后的归纳证明表明，只要 (A,B) 可控，对任意 T>0、Sigma0,SigmaT 正定和 Q>=0，均存在光滑控制使差分 Lyapunov 系统在整个区间保持 Sigma(t) 正定并满足两端协方差条件。独立 GLp(n,R) 路线也给出同样的可达性结论，并在本文中被扩展到带加性噪声情形，因此可达协方差集合仍为正定锥。

### 四、结论（Conclusion）
原论文关于状态协方差可控性的数学结论正确，缺口在于端点控制值可插值性未被纳入归纳假设。本文通过允许任意有限阶端点 jet 的更强归纳命题修复证明，同时保留光滑性断言，并给出与独立强可控性方法一致的交叉验证。

### 五、方法论与关键技术细节
关键数学条件为 (A,B) 可控、Sigma0,SigmaT>0、Q>=0、T>0 以及有限 jet 阶数 r；规范情形取 B_n=e_n，控制到协方差变化率的映射在规范单输入下是单射，因此端点插值必须内置于归纳。证明只实际需要 r=0，但为保持光滑性需同时证明所有有限阶 jet；加性噪声通过 Gamma(tau)=int_0^tau e^{sA}Qe^{sA^T}ds 的小时间拼接处理。本文是证明补遗，不含数值实验或新数据集，独立路线依赖 Ballantine 型分解及后续显式因子构造算法。
