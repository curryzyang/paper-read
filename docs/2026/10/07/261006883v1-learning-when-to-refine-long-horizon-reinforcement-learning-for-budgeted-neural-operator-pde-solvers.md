# Learning When to Refine: Long-Horizon Reinforcement Learning for Budgeted Neural-Operator PDE Solvers

- 区域：精读区
- 排名：2
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Ange Tong
- 机构：National Research Tomsk State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06883v1) · [PDF](https://arxiv.org/pdf/2610.06883v1)

## TLDR
This paper introduces rollout-verified policy improvement (RV-PI), a long-horizon reinforcement learning method for budgeted neural-operator PDE solvers that decides when and how many local patch corrections to apply by evaluating their downstream trajectory effects through real solver rollouts, yielding lower trajectory error than immediate-only allocation on shallow-water and Brusselator benchmarks.

## Abstract
Neural operators provide fast surrogates for time-dependent PDEs, but autoregressive deployment creates a refinement-allocation problem: prediction errors vary over space and time, while only a finite number of local corrections can be committed along a trajectory. We formulate this as budgeted adaptive neural-operator solving. A global Fourier neural operator advances the full field, a local operator proposes patch-wise residual corrections, and a set-aware selector chooses where to refine. A macro policy decides when and how much of the remaining refinement budget to spend. We introduce rollout-verified policy improvement (RV-PI), which evaluates feasible refinement counts through actual continuation rollouts of the learned PDE solver, converts long-horizon advantages into conservative policy targets, and accepts an update only when held-out trajectory error improves. On the shallow-water benchmark with a 32-intervention budget, RV-PI achieves a three-seed mean trajectory relative L2 error of 0.6910, improving over immediate-only policy improvement by 5.37% and RandomMacro by 2.41%. On the forcing-driven Brusselator benchmark with a 76-intervention budget, RV-PI attains 0.09954, improving over immediate-only policy improvement by 2.31% and RandomMacro by 5.32%. These results show that, under a fixed refinement budget, the value of a local correction depends on its downstream effect on the autoregressive trajectory, not only on its immediate error reduction.


## 精读解读（中文）
### 一、研究动机
神经算子虽能作为含时偏微分方程的快速代理求解器，但自回归部署会把自身预测作为下一步输入，导致局部误差在轨迹上传播累积；与此同时，只有有限次数的局部修正在整条轨迹上可以被提交，而误差在空间和物理时间上分布不均，因此核心问题不是再设计一个算子骨干，而是在固定预算下决定在哪里、何时以及投入多少局部修正。作者把该问题形式化为预算受限的自适应神经算子求解，并指出即时误差下降并不等价于长时程轨迹价值。

### 二、技术方案（Method）
方法采用分层固定网格求解器：全局条件FNO根据状态历史与外部上下文（浅水方程用静态条件场a(x,y)，Brusselator用已知标量强迫）产生临时下一状态；局部FNO从同一临时状态一次性为所有固定patch生成残差修正提案并冻结，以保证多patch动作语义与选取顺序无关；集合感知的Transformer选择器条件化地决定在哪些patch施加修正，宏策略在{0,1,2,4}中选择本步消耗的修正数q_t，在硬轨迹预算下由归一化重叠权重同时混合已选冻结修正，得到送入下一步物理转移的状态。宏策略先由仅用训练集的beam-search教师初始化，随后用RV-PI优化：在多个可部署策略采样的状态上枚举所有可行修正数，用真实学习求解器前向rollout到轨迹末端得到验证后的长时程回报与动作优势，将其转化为带行为正则和KL正则的保守soft策略目标，并仅在留出验证集轨迹相对L2误差下降时才接受该更新，否则回滚；对照的ImmediateOnlyPI仅把回报截断到当前转移。

### 三、结果（Result）
在官方浅水基准、32次干预预算下，RV-PI取得三seed平均轨迹相对L2误差0.6910，较ImmediateOnlyPI降低5.37%、较RandomMacro降低2.41%；在强迫驱动的Brusselator基准、76次干预预算下达到0.09954，较ImmediateOnlyPI降低2.31%、较RandomMacro降低5.32%，说明在同等的局部调用预算下RV-PI在两个差异很大的基准族上都最优。Brusselator骨干的对齐训练也显示，采用带轻度幅度保护的六步闭环目标后，验证轨迹相对L2从8.2505降到0.09369，同时单步误差也改善。

### 四、结论（Conclusion）
在固定修正预算下，一次局部修正的价值取决于它对自回归轨迹的下游影响，而不仅是它带来的即时误差下降；因此把时间分配建模为对物理时间的序贯决策、并用真实求解器rollout验证回报，比即时贪心或随机分配更能降低整条轨迹误差。

### 五、方法论与关键技术细节
数据与设定：浅水实验使用Laplace Neural Operator基准发布的官方条件场与72帧256×256轨迹，Brusselator使用39帧28×28轨迹加时变标量强迫；预算按已提交的修正干预次数计，而非端到端FLOPs，因为提案池是在一次批量局部算子前向中物化的。关键实现：所有候选patch修正均来自同一临时状态并被冻结，避免逐步重生成改变后续动作含义与开销；选择器采用集合感知结构以处理patch重叠与冗余；动作集为{0,1,2,4}；真值只在训练期用于构造选择器增益、rollout回报和验证接受，推理阶段完全无真值。RV-PI更接近可验证的近似策略迭代而非通用无模型RL，其更新目标与接受准则均以求解器的部署目标表达。局限：预算解释为干预次数而非直接的计算量度量，且整体框架依赖已训练好的全局算子与局部修正机制，骨干容量与算子族被刻意固定以隔离分配效应。
