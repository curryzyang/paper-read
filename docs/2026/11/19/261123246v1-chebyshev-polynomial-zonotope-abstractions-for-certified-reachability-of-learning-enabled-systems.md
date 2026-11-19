# Chebyshev Polynomial Zonotope Abstractions for Certified Reachability of Learning-Enabled Systems

- 区域：精读区
- 排名：1
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Peng Xie, Amr Alanwar
- 机构：Technical University of Munich
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23246v1) · [PDF](https://arxiv.org/pdf/2611.23246v1)

## TLDR
This paper shows that replacing Taylor expansions with Chebyshev polynomial-zonotope abstractions removes the convergence-radius cap caused by complex poles near the real axis, enabling provably wider and more accurate certified reachability analysis for nonlinear and learning-enabled systems.

## Abstract
Nearly all current methods for computing reachable sets of nonlinear dynamics propagate them with truncated Taylor expansions plus rigorous remainders. The expansion is pointwise: once its argument is a whole set rather than a point, one polynomial must stay accurate across that set, and it reaches only as far as its disc of convergence. The limit binds hardest on the rational terms and sigmoid gates of modern controllers: smooth as these look on the real line, in the complex plane they blow up at points just off the real axis, closer as a gate sharpens, and those points cap the set width a Taylor expansion can cover, most tightly on the switching surface where the controller decides. We prove a dichotomy: no Taylor degree certifies sets wider than that cap, while a Chebyshev abstraction of equal degree, anchored to the whole set in the same polynomial-zonotope pipeline, has no cap and gains width at a geometric rate in degree. Measured walls match the formulas to between 89 and 94 percent. We give closed-form rigorous remainders, among them the first polynomial softmax transformer; existing sound treatments are linear relaxations. On closed loops, certificates survive where the Taylor ones diverge, and specifications flip from unknown to proven; on trained classifiers up to real MNIST digits, the Chebyshev frontier certifies input territory the Taylor basis surrenders. Every certified claim passed large Monte-Carlo harnesses with zero violations, and an applicability map states in advance where the basis provably cannot matter.


## 精读解读（中文）
### 一、研究动机
现有非线性可达集传播几乎都依赖截断 Taylor 展开加严格余项，但 Taylor 是点式展开，要求一个多项式在整个集合上同时准确，因此受收敛圆盘和复平面极点限制。该限制对现代控制器中的有理项、sigmoid/softmax 门最严重：门越尖锐，复极点越靠近实轴，切换面附近的集合宽度越难认证。

### 二、技术方案（Method）
保持现有稀疏多项式 zonotope 管线不变，仅把标量抽象基从 Taylor 换成集合锚定的 Chebyshev：对每个超越原语在当前整个参数区间上计算 Chebyshev 系数，并配套闭式严格余项，同时评估多个独立可靠界并取最紧者，再与多项式像做 Minkowski 和得到一步过近似。初始集可为盒或任意多项式 zonotope，逐步传播 K 步；闭环中神经控制器逐层精确组合，softmax 走 log-sum-exp 路径构造多项式可靠余项，连续时间模型用 RK4 一步离散并另计流缺陷与步内时间包络。

### 三、结果（Result）
理论证明二分：Taylor 认证半宽被 d·tol^(1/N) 封顶，任何阶数都不能认证更宽集合；等阶 Chebyshev 无此上限，认证宽度随阶数线性增长、误差几何下降，sigmoid 门满足温度律 d=sqrt(m^2+π^2τ^2)，且切换面处认证半径最小。实验测得 Taylor 墙从上方收敛到预测上限，N=32 时约在 2% 内，Chebyshev 墙在 N≈20 穿越，公式符合度 89%–94%；闭环中 Taylor 证书发散而 Chebyshev 证书存活，规范从 unknown 翻为 proven，softmax 决策半径 Chebyshev 1 阶达到而 Taylor 需 8 阶，MNIST/螺旋边界分类器恢复 5–7 个输入平面面积点，所有认证声明经大规模 Monte-Carlo 检验零违例。

### 四、结论（Conclusion）
Chebyshev 多项式 zonotope 是可插入现有认证管线的基替换，能在 Taylor 受复极点限制的场景显著扩大可认证范围并保持可靠性。但它并非普适增益：多项式动力学两者逐位相同，整函数型非线性只获常数因子，高阶收益受盒表示限制，适用性图可提前预判基选择无效的场景。

### 五、方法论与关键技术细节
关键点包括：输入为盒或多项式 zonotope 的初始集，每步 Chebyshev 多项式锚定当前整个 enclosure 而非中心点，余项族含闭式严格界、奇异性感知界和 interval-Lagrange 界，Chebyshev 节点因首一多项式极小性可再获 2^N 因子；softmax 用 log-sum-exp 保持多项式共享符号表示。核心超参为多项式阶数 N、容差 tol、门温度 τ 和 RK4 步长 h，无训练损失，实验预注册并用密集 Monte-Carlo 与角点校验。复杂度/约束来自多项式 zonotope 的符号维度、盒表示和余项族多次评估，局限性是离散时间证书仅针对 Φ，连续流需额外 validated RK 流缺陷与步内包络，且高维盒表示会限制高阶收益。
