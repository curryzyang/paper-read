# Weight Certificates for Convex Multi-Objective MPC: Geometric Characterization, $\ell^1$ Construction, and $\ell^2$ Foreclosure

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Hadi Hajieghrary, Benedikt Walter, Chaitanya Shinde, Miguel Hurtadoand Jerry Lopez
- 机构：TORC Robotics LLC
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12520v1) · [PDF](https://arxiv.org/pdf/2608.12520v1)

## TLDR
Weighted-sum scalarization reproduces lexicographic multi-objective MPC optima exactly only when the weight vector supports the achievement map's upper image—constructible via a linear program for hinge penalties but impossible for squared-hinge penalties—and although calibrated weights improve rulebook compliance in nuPlan simulations, the certificate is pointwise and too short-lived to replace exact lexicographic solves without monitored fallback.

## Abstract
Automated-driving rulebooks rank rule violations lexicographically, and model predictive control enforces that ranking either exactly, through $L{+}1$ sequential programs per tick, or approximately, through a weighted sum tuned by the separation heuristic $w_1\gg w_2\gg\cdots\gg w_L$. We show the heuristic answers the wrong question. For a convex priority-ordered program, a weighted sum reproduces the lexicographic optimum precisely when its weight, augmented by a unit performance coefficient, supports the upper image of the achievement map at the lexicographic point; the admissible weights form the unit-performance slice of an outward normal cone. Under hinge penalties this slice is a polyhedron obtained by projecting a scaled-KKT system, and a linear program returns an interior weight with a certified margin; under squared-hinge penalties no finite weight is exact whenever the limiting multiplier is nonzero, with violation along the local minimizer branch decaying as $O(1/w)$. Calibrated on held-out logs, the resulting weights have near-equal tier components in nine of eleven calibration-eligible scenario classes and roughly double legal-tier event precision against a matched heuristic weight in closed-loop nuPlan experiments on a 25-rule rulebook. The certificate is, however, pointwise: no single weight is valid across the sampled ticks of an episode, the median lifetime is one sampling interval (zero subsequent ticks at the native rate), and persistence tracks active-set stability. These findings motivate monitored weighted solves with selective cascade fallback, although the compliance-pattern monitor detects only a subset of measured lapses.


## 精读解读（中文）
### 一、研究动机
自动驾驶规则手册以字典序对规则违规进行排序，模型预测控制通常通过分离启发式 w1≫w2≫⋯≫wL 的加权和来近似实现该排序。本文指出该启发式回答了错误的问题：对于凸优先级排序程序，加权和精确复现字典序最优需要满足特定的几何支撑条件，而非简单的大权重分离。

### 二、技术方案（Method）
针对凸优先级排序的多目标MPC，本文建立加权和与字典序最优等价的几何条件：权重（辅以单位性能系数）必须在字典序点的achievement map的上镜像处提供支撑，可行权重构成外法锥的单位性能切片。在hinge惩罚下，该切片是缩放KKT系统的投影多面体，可通过线性规划求解得到带认证裕度的内点权重；在squared-hinge惩罚下，当极限乘子非零时不存在有限精确权重，违规沿局部极小值分支以 O(1/w) 衰减。实验采用25条规则手册，在nuPlan闭环仿真中基于留出日志校准权重。

### 三、结果（Result）
在11个可校准场景类中，9个场景类校准得到的权重各层分量接近相等；与匹配的启发式权重相比，闭环nuPlan实验中法律层事件精度大约翻倍。然而证书是逐点成立的：没有任何单一权重在整个episode的所有采样时刻均有效，权重中位寿命仅为一个采样间隔（原生频率下后续时刻为零），其持续性受active-set稳定性影响。

### 四、结论（Conclusion）
这些发现支持采用带监控的加权求解并辅以选择性级联回退策略，而非依赖单一固定加权和；同时需注意所提出的合规模式监控器只能检测到实际违规的子集，仍有局限性。

### 五、方法论与关键技术细节
关键细节包括：证书的点态性质导致权重需逐时刻验证；中位寿命为一个采样间隔意味着权重的有效性极短；持续性依赖于active-set稳定性；squared-hinge下违规以O(1/w)衰减但无法精确；校准权重在多数场景类中接近相等，表明分离启发式可能导致过大的权重差异；实验范围为仿真环境nuPlan-mini，不涉及真实道路部署。
