# Fenchel-Young Duality Gaps: Certified Early Stopping for Regularized Inverse Problems

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Pierre-Cyril Aubin-Frankowski, Yohann de Castro
- 机构：Institut Universitaire de France, École Centrale Lyon, Institut Polytechnique de Paris
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17629v1) · [PDF](https://arxiv.org/pdf/2609.17629v1)

## TLDR
The paper derives an exact Fenchel–Young duality-gap decomposition for regularized inverse problems that yields computable, oracle-free error bounds and certified early-stopping rules via dual-feasible proxies, illustrated on Generalized Beurling–Lasso and deep-learning optimizers such as Lion-K and Muon.

## Abstract
We study computable error bounds and certified early stopping for regularized inverse problems, where a data-fidelity term is traded against a regularizer. The analysis relies on an exact duality-gap identity that splits the total gap of $F(Φμ)+λR(μ)$ into a data-fidelity Fenchel--Young loss and a regularizer Fenchel--Young loss, $ Δ(μ,h)=L_F(Φμ\parallel h)+λL_R(μ\parallelη),\qquad η=-Φ^\star h/λ, $ valid for any primal point $μ$ and any dual point $h$. The data-fidelity term $F$ is strictly convex, so wherever $F^\star$ is differentiable the loss $L_F(Φμ\parallel h)$ is the Bregman divergence of~$F$ between the prediction $Φμ$ and $\nabla F^\star(h)$, and it vanishes exactly at \emph{Mirror Alignment} $h=\nabla F(Φμ)$. Evaluated at a dual-feasible point $\tilde h$, the gap~$Δ(μ,\tilde h)$ is computable and \emph{oracle-free}, meaning that it uses no knowledge of the solution, and it bounds the suboptimality of $μ$. Under the source condition, the same Fenchel--Young losses give \emph{a priori} bounds on the estimation and prediction errors. Their scale is the irreducible model and noise error $L_F(Φμ^\star\parallel h^\star)$, which vanishes exactly when Mirror Alignment holds at the certificate. This gives an early-stopping rule: run the algorithm until the regularizer Fenchel--Young loss falls below a tolerance $ε$. A constructive version of the Brøndsted--Rockafellar theorem then turns the current pair into an exact \emph{dual-feasible} one, and this proxy lifts to an exact primal certificate. We build the proxy by a proximal step in the geometry of the fidelity, with Bregman kernel $F^\star$ and tilted by the prediction $Φμ$: it recovers the Euclidean step of Carlier when $F$ is the squared error, and it reduces the duality gap by the regularizer Fenchel--Young loss, up to a second-order remainder that vanishes in the quadratic case. Our running example is the Generalized Beurling--Lasso (GBL), where $R$ is the total-variation norm on signed measures. It contains the classical Beurling--Lasso, obtained with the squared error, and also covers robust, logistic, entropic and inverse-optimal-transport losses. The same duality gap certifies deep-learning optimizers such as Lion-K and Muon, in their proximal form, as solvers of the regularized program. A companion paper by the same authors builds on these error bounds to establish exact support recovery for the GBL under a non-degenerate source condition.


## 精读解读（中文）
### 一、研究动机
正则化反问题需在数据保真项 F(Φμ) 与正则项 λR(μ) 间权衡，但实际算法常缺乏无需真实解即可计算的误差界与停机准则；已有工作多局限于二次保真或特定稀疏反卷积。本文动机是建立一般严格凸 F 与一般凸 R 下可计算、无神谕的对偶间隙证书，并统一覆盖 GBL、稳健/逻辑/熵/逆最优传输等损失及深度学习优化器。

### 二、技术方案（Method）
方法对任意原始变量 μ 和对偶变量 h 证明精确恒等式 Δ(μ,h)=L_F(Φμ||h)+λL_R(μ||η)，其中 η=-Φ*h/λ，L_F 在 F* 可微时等于 F 在预测 Φμ 与 ∇F*(h) 间的 Bregman 散度，并在 Mirror Alignment h=∇F(Φμ) 处为零。对偶可行代理 h̃ 下，Δ(μ,h̃) 可计算且无需知道最优解，并给出原始次优性上界；在源条件 η∈∂R(μ) 下，同一 Fenchel-Young 损失还给出估计/预测误差的先验界，尺度为不可约模型噪声项 L_F(Φμ*||h*)。停机规则是运行算法直到正则项 Fenchel-Young 损失 λL_R(μ||η) 低于容差 ε；随后用 Brøndsted-Rockafellar 构造性版本把当前对偶对变成精确对偶可行代理，并提升为满足精确源条件的原始证书。代理通过以 F* 为 Bregman 核、由预测 Φμ 倾斜的镜像近端步构造，二次损失时退化为 Carlier 的欧氏近端步，并把对偶间隙降低 λL_R 量，非二次时仅剩二阶余项。

### 三、结果（Result）
结果给出精确对偶间隙分解、Mirror Alignment 最优性刻画、无神谕次优性上界以及源条件下估计/预测误差界；GBL 实例中 TV 正则涵盖经典 BLASSO，并扩展到稳健、逻辑、熵和逆最优传输保真。构造性 Brøndsted-Rockafellar 代理可将正则项 Fenchel-Young 损失低于 ε 的迭代提升为精确原始证书，实现认证早停。数值上，Lion-K/ISTA 的 ℓ1 压缩感知和 Muon/SVT 的核范数矩阵感知在病态实例中，无神谕的 Fenchel-Young 间隙 Δ_t 稳步趋零并始终上界真实原始最优性间隙，证明这些优化器在其近端形式下求解 F+λR 问题。伴随工作进一步利用这些误差界在非退化源条件下建立 GBL 的精确支撑恢复。

### 四、结论（Conclusion）
本文表明 Fenchel-Young 对偶间隙可为正则化反问题提供统一、可计算且有理论保证的误差证书与早停准则，突破了二次保真限制。该框架把 Bregman 散度、Mirror Alignment 和 Brøndsted-Rockafellar 构造联系起来，并为 GBL 及深度学习中 Lion-K、Muon 等优化器的近端解释与认证提供基础。

### 五、方法论与关键技术细节
关键细节包括：F 严格凸、R 为正常下半连续凸函数、Φ 有界弱*连续、λ>0；F* 可微处 L_F 为 F 的 Bregman 散度，源条件 η∈∂R(μ) 与 Mirror Alignment h=∇F(Φμ) 同时成立时最优，反之原始解也存在这样的对偶。构造性代理使用核 F*、由 Φμ 倾斜的镜像近端步，对范数正则可无条件提升为精确原始证书，但非二次保真下间隙减少仅到二阶余项。实验设置包括双精度前 10000 次迭代、ℓ1 压缩感知 AR(1) 相关设计 ρ=0.9 与 λ=0.05、核范数矩阵感知 p=120 个高斯测量与 λ=0.1，且间隙曲线在病态问题上收敛较慢。局限在于需构造对偶可行代理并依赖源条件/非退化条件，精确支撑恢复与更细统计速率由伴随论文处理。
