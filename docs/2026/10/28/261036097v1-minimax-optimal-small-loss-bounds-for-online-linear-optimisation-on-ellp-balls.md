# Minimax-Optimal Small-Loss Bounds for Online Linear Optimisation on $\ell_p$ Balls

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Jack J. Mayo
- 机构：University of Amsterdam, Kurtos.ai
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.36097v1) · [PDF](https://arxiv.org/pdf/2610.36097v1)

## TLDR
The paper constructs an anytime follow-the-regularised-leader (FTRL) algorithm for online linear optimisation on \(\ell_p\) balls that, without knowing the horizon or the cancellation slack \(\Delta_T\), achieves the minimax-optimal small-loss regret \(O_p\!\left(1+\min\{\Delta_T^{1-1/p},\,d^{1/2-1/p}\sqrt{\Delta_T}\}\right)\), with matching lower bounds, a sharp \(p\to\infty\) constant, and a switching extension that also guarantees regret at most twice that of follow-the-leader.

## Abstract
We study full-information online linear optimisation on the unit $\ell_p$ ball in $\mathbb{R}^d$, for fixed $2\le p<\infty$ and losses of dual norm at most one. Let $Δ_T$ denote the cumulative loss of the best fixed action above each round's minimum. A follow-the-regularised-leader (FTRL) algorithm attains, on every loss sequence and without knowing $T$ or $Δ_T$, regret $O_p(1+\min\{Δ_T^{1-1/p},\, d^{1/2-1/p}\sqrt{Δ_T}\})$. Matching lower bounds show that this rate is minimax for each fixed $p$, and its constant $(2+o(1))p/\log p$ is optimal as $p\to\infty$ among guarantees uniform in $d$ and $T$. The algorithm uses a bounded radial regulariser and switches at most once to its quadratic augmentation. On some paths where follow-the-leader (FTL) has regret one, its regret grows with $T$. A switching extension keeps the sharp constant and also guarantees $\mathrm{Reg}_T\le 2\,\mathrm{Reg}_T^{\mathrm{FTL}}$. For i.i.d. losses whose mean has no zero coordinates, we compute the exact $\log T$ coefficient of the expected regret, which separates FTL's variance term from the bias of the regulariser.


## 精读解读（中文）
### 一、研究动机
论文研究ℓp球上的全信息在线线性优化，目标是在不预知时间跨度T和最优固定动作累计损失（以小损失/抵消松弛Δ_T刻画）的情况下，取得同时覆盖多项式分支与维度相关平方根分支的最优后悔界。已有自适应正则化可达到依赖T的最优worst-case率，但能否用Δ_T替代T且不损失dimension crossover与常数最优性尚不明确。

### 二、技术方案（Method）
在B_p^d上设定每轮先选x_t、再观测满足‖θ_t‖_r≤1的全损失向量，并将损失平移为ℓ^+(x,θ)=‖θ‖_r+⟨x,θ⟩，用Δ_T=Σ‖θ_t‖_r−‖Σθ_t‖_r衡量最优动作相对每轮最小损失的累计松弛。算法为standalone FTRL：先用有界径向正则化构造其稳定性项可由学习者自身shifted loss支付的势函数，得到Δ_T^{1−1/p}分支；再加入该正则化的二次增广，得到d^{1/2−1/p}√Δ_T分支，并根据累计shifted loss自适应调节、至多从径向形式切换到增广形式一次，无需知道T或Δ_T。另设切换扩展，在FTL与standalone FTRL之间切换以控制平滑代价，并用i.i.d.分析计算期望后悔的log T系数。

### 三、结果（Result）
证明standalone FTRL对任意损失路径达到Reg_T≤O_p(1+min{Δ_T^{1−1/p},d^{1/2−1/p}√Δ_T})，且不需知道T或Δ_T；匹配下界表明该率对每个固定p是minimax的，且当p→∞时前导常数(2+o(1))p/log p在d、T一致保证中最优。切换扩展在保持该sharp常数和小损失界的同时额外保证Reg_T≤2Reg_T^{FTL}，无重启或加性比较项；对均值为非零坐标的i.i.d.损失，给出期望后悔的精确log T系数，分离FTL方差项与正则化偏差。

### 四、结论（Conclusion）
论文给出了ℓp球上固定p≥2的minimax最优小损失后悔界，说明通过一次切换的有界径向/二次增广FTRL即可实现horizon-free且常数渐近最优的保证。切换版本同时限制平滑相对FTL的路径代价，并给出随机损失下log T系数的可解释分解，为ℓp在线优化的小损失与FTL竞争问题提供了较完整刻画。

### 五、方法论与关键技术细节
关键实现是shifted loss、cancellation slack Δ_T及恒等式S_t=Δ_t+Reg_t，径向正则化在边界有有限值但斜率发散，二次增广提供维度上限；切换阈值由累计shifted loss触发，切换时势能增加不超过切换前近似误差，sharp常数还需半径相关FTL界和小slack修正。下界与上界联合确定minimax率，切换扩展不重启也不重置累计损失向量；随机部分要求i.i.d.且均值无零坐标以得到精确log T系数。适用范围为固定有限p≥2、已知损失范数界并可使用精确support/action oracle，FTL在某些路径仅有1后悔而standalone FTRL可增至√T/16（p=2）或log T量级（p>2），需切换扩展来消除这一平滑代价。
