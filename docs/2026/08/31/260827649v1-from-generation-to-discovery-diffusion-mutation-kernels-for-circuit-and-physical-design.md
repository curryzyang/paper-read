# From Generation to Discovery: Diffusion Mutation Kernels for Circuit and Physical Design

- 区域：精读区
- 排名：10
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Dinithi Jayasuriya, Aravind Saravanan, Nilesh Ahuja, Amanda Rios, Amit Trivedi
- 机构：University of Illinois Chicago, Intel Corporation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27649v1) · [PDF](https://arxiv.org/pdf/2608.27649v1)

## TLDR
TLDR: This paper introduces a diffusion-based discovery framework that learns mutation kernels to transform existing valid designs into novel, feasible candidates, enabling surrogate-free search with risk-controlled pruning that discovers improved prefix adders, analog amplifier topologies, and macro placements validated entirely by external engineering tools.

## Abstract
Generation and discovery are different problems. A generative model trained on valid artifacts reproduces a distribution, whereas discovery must produce artifacts that lie outside the observed corpus, satisfy hard structural constraints, and improve on established designs under evaluation that the model cannot influence. We introduce a diffusion-based discovery framework. Unlike conventional generative models that sample from learned distributions, it learns transition operators that transform existing artifacts into new candidates. Controlled partial re-noising followed by denoising defines a diffusion mutation kernel, a learned transition distribution that preserves the structural regularities of feasible designs while moving between regions of the design space. The learned model supplies feasibility structure only, and all correctness and performance judgments remain with external engineering tools. Intermediate diffusion trajectories are additionally monitored under a conformal risk budget so that unpromising candidates are discarded before expensive evaluation. We evaluate the framework on three electronic design spaces, an environment that supplies rigorous non-differentiable evaluators in the form of simulation, formal equivalence checking, and industrial physical implementation. The framework discovers 32-bit prefix adders that are formally verified equivalent to addition over all 2^64 input pairs and reduce delay by 17% and area by 18% relative to Kogge-Stone under a placed-and-timed flow; seven independently re-simulated amplifier topologies absent from the training corpus, spanning gains of 21.9-66.1 dB and bandwidths of 72.9 kHz-207 MHz; and macro placements on held-out netlists reaching 0.68x wirelength of an industrial placer.


## 精读解读（中文）
### 一、研究动机
生成与发现是不同任务：生成模型只能复现已见数据分布，而发现需要生成训练语料之外、满足硬约束并在外部评价下优于已有设计的工件。现有演化方法依赖手工设定的变异算子，代理优化会因近似目标偏差而被利用。因此需要一种可学习的迁移算子，由数据学习可行设计空间中工件如何演化，同时将正确性与性能判断完全交给外部工程工具。

### 二、技术方案（Method）
提出SteerGenSE框架：以条件扩散模型学习可行设计的结构规律，训练数据分别是用16,269个32位前缀加法器结构（含Ripple/Sklansky/Kogge-Stone/Brent-Kung变体）编码的类别网格、模拟电路motif图和宏单元连续坐标；将父代设计部分加噪到gamma*T再执行去噪，得到扩散变异核K_gamma(x'|x)，其中gamma控制局部细化与全局探索（前缀和布局用0.3，模拟用0.5）。推理/搜索采用种群循环：从当前种群按K_gamma生成子代，父代子代合并后由外部评估器（SAT形式验证、SPICE、OpenROAD）计算性能与可行性，再经Pareto选择形成下一代；仅在外部工具判定后淘汰或保留。中间轨迹用预测端点做conformal risk control（alpha=0.1）剪枝，剪枝释放的算力通过sequential Monte Carlo按健康度重采样重新分配，但健康度只能分配资源不能终止轨迹。模型只学可行性结构，不学习任何目标函数近似，训练使用标准扩散去噪目标，条件信息包含扩散步和目标深度/算子数。

### 三、结果（Result）
在32位前缀加法器上，384个零样本中全部解码合法，325个结构不在训练集，最终16个新型加法器在技术映射前后均通过SAT等价性验证（覆盖2^64输入对）；最优设计延迟0.302 ns、面积373 um^2，比Kogge-Stone延迟降低17%、面积降低18%。模拟电路发现7个训练集中不存在的拓扑，经独立重仿真覆盖增益21.9-66.1 dB、带宽72.9 kHz-207 MHz。宏布局在留出网表上达到工业布局器线长的0.68倍。在同一192样本预算下，条件扩散采样超体积67.8高于SMC的53.6，最优延迟0.342 ns vs 0.362 ns。

### 四、结论（Conclusion）
结果表明，扩散变异核把生成模型从采样器变成可学习的搜索算子，能够在不手工设定变异规则、不代理目标函数的前提下，在离散与连续设计空间中同时保持可行性、新颖性和可验证的高性能。形式验证与外部工具裁决使发现结果可信，风险受控剪枝能减少昂贵评估；该方法可作为电路与物理设计生成的通用发现框架。

### 五、方法论与关键技术细节
关键实现要点：前缀加法器用固定尺寸类别网格表示体系结构，解码为DAG并用SAT miter判定g(x)=1（不满足则结构/功能非法）；训练语料16,269个唯一32位结构；性能用NanGate45实现流程的place-based时序与面积；新颖性用调度无关的规范指纹度量；模拟电路用结构性门控+ngspice评估；布局用legalization+OpenROAD。超参：gamma=0.3/0.5，alpha=0.1，前缀样本预算192、SPICE评估预算128，种群Pareto选择规模mu未给具体值；conformal winner-preservation保证需要校准集与固定策略下可交换性，生成/评估/检查点/赢家定义改变后必须重新校准。局限性：SMC重采样在前缀空间把192个粒子坍缩成7个不同结构，故该域不用重采样；steering只有在评估成本高且中间轨迹能提供可靠失败信号时才有收益；模型不提供目标梯度，所有质量判断依赖外部工具；无监督/conditioning需要目标深度和算子数等条件。
