# On a Gradation for Asymptotic Stability

- 区域：精读区
- 排名：5
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Yiğit Narter, Inigo Incer
- 机构：University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03120v1) · [PDF](https://arxiv.org/pdf/2609.03120v1)

## TLDR
This paper introduces a graded classification of asymptotic stability—ranging from degree 0 (exponential stability) to positive integer or real degrees corresponding to algebraic decay \(t^{-1/m}\)—and provides Lyapunov-based tests, converse results, and examples (Hopf, Bautin, fractional-order, time-varying) for certifying the exact convergence rate of asymptotically stable equilibria.

## Abstract
Classical asymptotic stability guarantees convergence but does not quantify the rate at which convergence occurs. This paper introduces a gradation of asymptotic stability where degree zero corresponds to exponential stability and degree $m>0$ corresponds to algebraic decay of order $t^{-1/m}$. We provide direct and converse Lyapunov tests for admissible degrees and conditions for certifying the exact stability degree. Hopf, Bautin, fractional-degree, and time-varying examples demonstrate how the degree identifies the leading stabilizing mechanism.


## 精读解读（中文）
### 一、研究动机
经典渐近稳定性只保证收敛，却不区分收敛速率，导致指数收敛与代数衰减都被归为同一类；而Hopf和Bautin分岔附近的例子表明，不同首个非零稳定项会产生截然不同的收敛律，因此需要一种基于速率的细粒度框架来刻画渐近稳定性。

### 二、技术方案（Method）
引入非负参数m作为稳定度指标：m=0对应指数稳定，m>0对应代数衰减阶t^{-1/m}。定义比较包络族φ_m^α(t;ρ)=ρe^{-αt}（m=0）和ρ(1+mαρ^m t)^{-1/m}（m>0），并进一步定义可容许的degree-m估计与uniform degree-m估计。在Lyapunov框架下，给出上耗散不等式用于证明degree-m可容许性，给出匹配的下耗散不等式在前向不变集上成立，从而证明轨迹以t^{-1/m}阶衰减并排除更快degree，进而确立精确稳定度。还利用解沿轨线的上Dini导数建立了非光滑逆Lyapunov定理，适用于时变系统。

### 三、结果（Result）
证明了一致degree估计蕴含局部一致渐近稳定性；degree m>0对应轨迹的O(t^{-1/m})代数衰减。通过Hopf和Bautin范式实例展示了不同degree的分离：Hopf范式区分指数decay（degree 0）与t^{-1/2}衰减（degree 2）；Bautin范式进一步区分指数、t^{-1/2}和t^{-1/4}衰减（对应degree 0、2、4），说明degree能够识别主导稳定机制。

### 四、结论（Conclusion）
提出的稳定度分级框架将指数和代数收敛统一在单参数梯度下，补充了经典Lyapunov稳定性理论，使渐近稳定平衡点的衰减率成为显式结构属性，为分岔研究中‘稳定但不同收敛速率’的现象提供了量化工具。

### 五、方法论与关键技术细节
关键点包括：degree参数m与代数衰减指数β满足β=1/m，degree越大收敛越慢；比较包络由标量比较方程ẑ=-αz^{m+1}启发，且当m→0+时趋于指数包络；可容许性具有单调性，即若degree m可容许则所有q>m也可容许；精确degree定义为最小可容许degree并需下界不等式排除更快衰减；存在非可达情形，如log时间修正导致可容许集合为开区间(m*,∞)，此时最小degree为inf但不被达到；框架可处理时变系统，且与固定rate-order并优化常数的Jagt-Peet方法不同，本工作将代数阶本身作为分类对象，也与Lyapunov指数不同（代数衰减轨迹的Lyapunov指数均为零，无法区分不同代数阶）。
