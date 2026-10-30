# Learning Without Clocks: Partition-Invariant Neural Network

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Han Wang, Jingyuan Bao, Juntao Wu, Saiao Zhou, Yuman Nie
- 机构：University of Science and Technology of China, Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37823v1) · [PDF](https://arxiv.org/pdf/2610.37823v1)

## TLDR
The paper proves that clock-free neural networks on asynchronous event streams achieve tie-order invariance and timestamp continuity exactly when event updates commute, derives time-mediated non-commutative models that retain temporal-order sensitivity, and introduces a linear-cost Clock-Free Event layer that outperforms additive baselines on event-based benchmarks.

## Abstract
Event cameras, spiking cochleas and similar sensors emit asynchronous events, yet most learning systems first bin them into frames or packets, so the output depends on how the stream was sliced. Networks whose state is updated exactly at every event and evolves in closed form between events are invariant to this slicing. We ask what more makes the output (i) independent of the processing order of simultaneous events and (ii) continuous in the time stamps, even when two events cross in time, while (iii) staying sensitive to temporal order. For arbitrary nonlinear event models we prove that (i) and (ii) are each equivalent to pairwise commutation of the event updates, and that once updates commute, all order dependence comes from their non-commutation with the inter-event dynamics and vanishes linearly in the time lag. This identifies a class of time-mediated non-commutative (TM) models and yields a resolution-robustness bound for any model. We construct the minimal TM layer, a learnable, provably Lipschitz generalization of the Hassenstein-Reichardt correlator; prove that no single additive layer can uniformly represent ordered pair interactions, whereas a three-dimensional TM state can; show that each TM layer adds two levels of temporal nesting versus one for additive layers; and give a single-layer higher-order construction (TM-k) and a stacking rule preserving all three properties. We instantiate these results as the Clock-Free Event (CFE) layer, linear in the number of events, give a topology-free variant for temporal point processes with closed-form likelihoods, and specify a preregistered clock-robustness protocol with a physical-time threat model for spike-retiming attacks. In preliminary development-set experiments, the TM state beats an otherwise identical additive state by 3.5-9.1 points on DVS128 Gesture and by 24.5 and 30.6 points on SHD and Speech Commands.


## 精读解读（中文）
### 一、研究动机
事件相机、脉冲耳蜗等传感器输出异步带时间戳事件，但多数学习系统先分帧或打包，导致输出依赖分片方式。分区不变性本身仍不足：还要求同时事件处理顺序无关、时间戳交叉时连续，同时保留对时间顺序的敏感性。

### 二、技术方案（Method）
论文将事件流建模为类型事件序列和由连续漂移半流与事件跳变映射组成的事件模型，证明平局顺序不变、交叉连续分别等价于跳变两两交换，并刻画时间介导非交换TM模型。其最小TM层用快迹u接收事件、漂移把u复制为延迟迹s、事件再从s读入累加器v，形成可学习的Lipschitz Hassenstein–Reichardt相关器推广，并给出TM-k高阶构造与保持性质的堆叠规则。CFE层按事件逐个更新或用并行扫描精确计算，代价随事件数线性，并扩展出无拓扑点过程变体与闭环似然、send-on-delta编码器。推理可在任意查询时刻读取状态，训练按事件精确展开或并行扫描，评估采用预注册时钟鲁棒性协议。

### 三、结果（Result）
理论上，单加性层无论宽度和读出都不能均匀表示有序成对交互，而三维TM状态即可；每个TM层提供两层时间嵌套，加性层仅一层，并给出分辨率–鲁棒性界：在时差δ、间隔m下分辨顺序需至少m/(2δ)的时间敏感度。初步开发集实验中，有序TM状态相对同构加性状态在DVS128 Gesture上依观察窗提高3.5–9.1个百分点，在SHD和Speech Commands上分别提高24.5和30.6个百分点。论文还证明在跳变不交换时任何平局规则都无法恢复交叉连续性，而跳变交换后顺序效应仅来自跳变与漂移的非交换并随时滞线性消失。

### 四、结论（Conclusion）
论文提出无时钟、分区不变的事件学习框架，以TM非交换结构在平局不变和交叉连续之间保留时间顺序信息，并给出可实现的CFE层与评估协议。当前结果限于理论、架构、协议和开发集初步实验，未宣称SOTA，官方测试集结果尚待后续版本。

### 五、方法论与关键技术细节
关键细节包括事件流允许相等时间戳形成平局组，包不拆分平局组；分区不变等价于包处理器满足半群同态，仿射模型中跳变写为J_c=G_cx+b_c、G_c=I+N_c，漂移为e^{δΛ}。TM状态可理解为对有序事件对的指数加权和，具有可证Lipschitz性和线性事件复杂度；顺序敏感度受物理时间分辨率约束，需在观测窗、时钟偏移、不重训和算力匹配基线条件下评估。局限包括只报告初步开发集实验、依赖精确事件时间与闭式漂移、对高维传感器和堆叠深层模型的实证尚不完整，且针对脉冲重定时攻击的物理时间威胁模型仍需正式测试集验证。
