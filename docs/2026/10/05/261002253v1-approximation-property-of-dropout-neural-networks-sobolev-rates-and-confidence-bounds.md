# Approximation Property of Dropout Neural Networks: Sobolev Rates and Confidence Bounds

- 区域：精读区
- 排名：3
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Jia-He Yao
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02253v1) · [PDF](https://arxiv.org/pdf/2610.02253v1)

## TLDR
This paper derives matching upper and lower bounds on the size of constant-depth ReLU dropout networks required to uniformly approximate the unit ball of \(W^{n,\infty}([0,1]^d)\) with high probability, showing that the optimal accuracy exponent is \(\max\{d/n,2\}\) up to logarithmic and retention-probability factors and quantifying the extra cost of dropout-induced randomness.

## Abstract
The universal approximation property of dropout neural networks does not by itself describe the network size required for an accurate random realization. In this work, we study approximation of the unit ball of $W^{n,\infty}([0,1]^d)$ by ReLU networks whose edges are retained independently with probability $p$. The approximation error is measured uniformly over the input domain, and the guarantee holds with probability at least $1-δ$ for a single sampled network. We construct networks of constant depth and size $\widetilde O_{n,d}(p^{-9}\varepsilon^{-\max\{d/n,2\}} \log(1/δ))$. The construction combines bounded local subnetworks, localization on a successful approximation event, and a multiscale Taylor decomposition. Conversely, Sobolev capacity imposes a lower bound on the number of surviving edges, while approximation of a fixed affine function requires an output-layer cost of order $((1-p)/p)\varepsilon^{-2}\log(1/δ)$ at sufficiently high confidence. For fixed $p\in(0,1)$ and $δ<\min\{1/2,1-p\}$, the upper and lower bounds match in the accuracy exponent under a fixed or logarithmic depth budget. When $d\leq2n$, they also match in confidence up to logarithms of accuracy. We extend the lower bounds to $W^{n,r}$ targets with $L^s$ error, and distinguish this extension from the upper bound for $W^{n,\infty}$. The optimal retention dependence and logarithmic factors remain open.


## 精读解读（中文）
### 一、研究动机
dropout 网络的通用逼近性无法刻画一次随机实现达到给定精度所需的网络规模，而已有权重确定性逼近率也未考虑随机删边带来的波动。本文旨在回答：在独立边 dropout 下，为一致逼近 Sobolev 单位球并保证单次采样高概率成功，网络需要多大。

### 二、技术方案（Method）
作者研究独立边保留概率为 p 的 ReLU dropout 网络，目标是以一致范数逼近 W^{n,∞}([0,1]^d) 的单位球，要求 P{sup_x |F_R(x)-f(x)|≤ε}≥1−δ。上界构造采用常深度网络，结合有界局部子网络、仅在成功事件上的局部化、以及多尺度 Taylor 分解：先对局部窗口电路使用 Manita 等人的去偏恒等式获得无偏随机表示，再用共同断点上的并集界把标量集中转为一致估计；随后对 F_J=F_0+Σ(F_j−F_{j−1}) 逐尺度实现并先在同一尺度内求和以保留误差预算。下界方面，用 Sobolev 容量和确定性地界网络 VC 维，约束每个成功实现中存活边数；并对仿射目标 f_0(x)=(1+x_1)/2 直接分析输出层随机和的逼近失败概率，导出输出层代价。

### 三、结果（Result）
主要定理给出上界 S_*≤C_{n,d} p^{−9} ε^{−max{d/n,2}} (log(1/δ)+log(1/ε))（忽略对数因子），构造深度为常数 L_{n,d}，即精度指数为 max{d/n,2}。下界为 S_*≥c_{n,d} max{ p^{−1} max{ ε^{−d/n}/(L log(1/ε)), ε^{−d/(2n)} }, ((1−p)/p) ε^{−2} log(1/δ) }。因此固定 p、δ<min{1/2,1−p} 且深度固定或对数深度时，上下界在精度指数上匹配；d≤2n 时置信度依赖也匹配至精度对数因子。下界可推广到 W^{n,r} 目标与 L^s 误差，而上界仅针对 W^{n,∞}。

### 四、结论（Conclusion）
dropout 随机逼近的规模由空间分辨率代价 ε^{−d/n} 与输出随机波动代价 ε^{−2} 的较大者决定，而非二者相乘；在固定保留率和高置信度下，常深度 ReLU dropout 网络能达到最优精度指数。最优保留率依赖和精确对数因子仍未解决，d>2n 时的联合置信度下界也尚未建立。

### 五、方法论与关键技术细节
模型为独立边 dropout，偏置不掩码，输出为仿射；大小 S=E+U+1，深度按计算层计，权重无幅值或比特限制。关键技巧包括：用 σ(Z−η) 在成功事件上恢复非负局部支撑；仅对小型局部窗口电路应用去偏恒等式以避免指数级子集展开；多尺度 Taylor 分解中第 j 项幅度约 2^{−jn}、项数约 2^{jd}，乘以 η^{−2} 局部代价后求和得 ε^{−2}Σ2^{j(d−2n)}，从而产生 max{d/n,2}；下界结合 Sobolev 容量、VC 维与输出层方差论证。局限性是未给出有界权重或有限比特实现，上下界仅在精度指数意义下匹配，保留率 p 的最优依赖和 d>2n 的联合下界仍开放。
