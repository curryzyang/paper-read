# Sample-Adaptive Zeroth-Order Post-Training

- 区域：精读区
- 排名：5
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Haiyuan Wan, Yanyi Li, Weicheng Lin, Cong Fang
- 机构：Peking University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12566v1) · [PDF](https://arxiv.org/pdf/2610.12566v1)

## TLDR
SAZO introduces a sample-adaptive zeroth-order optimization method that online-estimates per-example importance from existing directional differences and tracks it via exponential moving averages, enabling adaptive query allocation for memory-efficient LLM fine-tuning with up to 6× faster convergence than MeZO and no extra model evaluations.

## Abstract
Zeroth-order (ZO) optimization offers a memory-efficient alternative to backpropagation for fine-tuning large language models. However, existing ZO methods typically sample training examples uniformly, overlooking their evolving importance and leaving avoidable estimation variance. To address this limitation, we propose Sample-Adaptive Zeroth-Order Optimization (SAZO), which learns sample importance online and adaptively allocates queries to accelerate convergence. SAZO extracts gradient-norm information from existing directional differences to estimate sample importance without access to true gradients. Furthermore, to track evolving importance from sparse minibatch feedback, SAZO maintains per-example exponential moving averages that aggregate observations across updates. The method requires no additional model evaluations and only $O(N)$ additional scalar state compared with MeZO. We prove that SAZO asymptotically matches the leading convergence term of the minimum-variance sampling oracle, and achieves a strictly faster convergence rate than standard methods. Extensive experiments across four model families demonstrate improved average downstream performance and up to $6\times$ faster convergence to the same training loss in terms of query count.


## 精读解读（中文）
### 一、研究动机
零阶（ZO）优化如 MeZO 仅用两次前向评估即可微调大模型，内存接近推理开销，但现有方法对训练样本均匀采样，忽视了样本重要性的差异及其随训练演化，从而留下可避免的估计方差；作者指出由于 ZO 梯度估计方差在最坏情况下比一阶方法大 Ω(d) 倍，ZO 对采样异质性更敏感，因此样本分配是尚未被利用的加速维度。

### 二、技术方案（Method）
SAZO 在 MeZO 式有限差分框架下工作：每步采样样本 I_t 与独立高斯方向 z_t，用 s_{i,t}=(f_i(x_t+μ_tz_t)-f_i(x_t-μ_tz_t))/(2μ_t) 计算方向差分，并按重要性加权更新 x_{t+1}=x_t-η·s_{I_t,t}/(N p_{I_t,t})·z_t，保持对全量 ZO 更新的无偏性（误差 O(μ_t²)），最优分配为 p*_i∝||∇f_i(x_t)||。为在无真实梯度下估计重要性，SAZO 复用已有的方向差分构造 Y_{i,t}=sqrt(π/2)|s_{i,t}| 作为梯度范数的近似无偏估计；为应对稀疏小批量反馈，对每个样本维护单独的指数滑动平均 m_{i,t+1}=(1-β)m_{i,t}+βY_{i,t}（仅对被采样样本更新，其余保持不变），再按 p_{i,t}=(1-ε)m_{i,t}/Σ_j m_{j,t}+ε/N 混合均匀探索后采样。实现上先用普通 MeZO 做 4 个完整无放回 burn-in pass 初始化 m_i 并计入预算，随后切换为有放回自适应采样；同一小批量共享一个扰动方向，重复抽样只评估一次但保留其重数于加权更新，推荐 β=0.05、ε=0.1。

### 三、结果（Result）
理论上，作者定义采样遗憾 Reg_T=Σ E[V_t(p_t)-V_t*]，其中 V_t(p)=(d+2)/N²·Σ a_{i,t}²/p_{i,t}、V_t*=(d+2)/N²·(Σ a_{i,t})²，证明在步长等超参满足 κ=192Λ_dη²/(εr²)<1（r=βε/N）时 SAZO 的采样遗憾有上界，渐近上匹配最小方差采样 oracle 的首阶收敛项，并比均匀采样等标准方法具有严格更快的收敛速率。实验上，在四个模型族上平均下游性能提升，在 MeZO 级内存与单步开销下，达到相同训练损失所需查询数最多减少 6×；在 SST-2 上可视化显示每样本梯度范数在 0/10K/30K 步存在显著跨样本异质性与时间演化，且 SAZO 的相对累积采样遗憾低于均匀采样和固定在初始化的 oracle 分配，对应更快的训练损失下降。

### 四、结论（Conclusion）
样本级查询分配是零阶微调中被忽视的有效加速维度：通过从已有方向差分中提取梯度范数信息并在线追踪其演化，SAZO 在不增加任何模型评估、仅增加 O(N) 标量状态的条件下显著降低梯度估计方差、加速收敛并提升下游性能，为 ZO 后训练提供了一个与参数空间自适应（如预条件、低秩扰动）正交的改进方向。

### 五、方法论与关键技术细节
关键实现细节包括：重要性估计 Y_{i,t}=sqrt(π/2)|s_{i,t}| 的期望等于 a_{i,t}+O(μ_t²)，即借助高斯方向投影的期望绝对值性质，无需额外查询；EMA 系数 β=0.05 与探索率 ε=0.1 在所有主实验统一使用且对较宽范围不敏感；初始化依赖 4 个完整稳定顺序的无放回 burn-in pass，这些查询计入总预算。存储成本为每样本一个标量，1000 个样本以 FP64 计约 8 KiB，远小于推理内存，每步查询数与 MeZO 相同。理论依赖假设：各 f_i 梯度全局 Lipschitz、F 平滑下有界、Hessian 全局 Lipschitz，并需满足 κ<1 的步长/超参条件。局限性在于需要保存全部样本的重要性状态并假设可分样本损失与平滑性，有限差分误差项 O(μ_t²) 的系数可能依赖采样概率与梯度范数，且遗憾分析为渐近/有限时域界，未覆盖极端非平滑或在线数据分布变化场景。
