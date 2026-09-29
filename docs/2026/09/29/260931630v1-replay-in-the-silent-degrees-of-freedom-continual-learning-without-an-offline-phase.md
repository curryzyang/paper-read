# Replay in the Silent Degrees of Freedom: Continual Learning Without an Offline Phase

- 区域：精读区
- 排名：6
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Zhang Yanhai
- 机构：Nanyang Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31630v1) · [PDF](https://arxiv.org/pdf/2609.31630v1)

## TLDR
A biologically constrained continual-learning network can consolidate memories entirely during inference—by replaying old samples into hidden, currently unused “silent” synapses via k-winner-take-all isolation and refractory rotation—achieving competitive or superior class-incremental performance without any offline phase.

## Abstract
Replay-based continual learning almost always consolidates in a dedicated offline phase or by interleaving replayed samples with the input stream, whereas brains also consolidate during wakefulness through local sleep, brief use-dependent off-periods of individual circuits. We ask whether a network trained by local, biologically constrained rules can consolidate with no offline phase at all. An isolation rule confines replay updates to hidden synapses invisible to the current input under k-winner-take-all dynamics, with optimiser state advanced only inside the mask; a refractory rotation rule makes units that have just fired sit out the next competition, widening the consolidable set; a homeostatic pressure and a relative-novelty gate decide when replay bursts fire and when rotation runs. This inverts the usual direction of non-interfering continual learning: the hidden computation on the current input is held invariant (exactly on the proven channels, and for all but 0.3% of waking samples per update elsewhere) while past memories are written into the degrees of freedom the current batch leaves unused. On class-incremental split-MNIST the system reaches 91.6+-0.3% with no offline phase, at or above the best offline-night schedule on two held-out splits, tied with DER++ and above experience replay, ER-ACE, A-GEM and unmasked local replay; in a single pass it leads DER++ (91.8% against 90.1%) while the night falls to 76.9%. The advantage is largest at small buffers and gives way to the backpropagation references at large ones; on split CIFAR-10 the system leads offline rehearsal and experience replay but trails ER-ACE and DER++. Rotation carries most of the gain; isolation adds the invariance guarantee. The mechanism is not tied to the local rule: under the same schedule a backpropagation network with k-WTA hidden layers gains from rotation, and isolation is again free on top of it.


## 精读解读（中文）
### 一、研究动机
大脑可在清醒时通过局部睡眠、即单个皮层回路的短暂停歇完成巩固，而基于回放的持续学习几乎都依赖专门离线阶段或把回放样本与输入流交错。本文追问：由局部、生物约束学习规则训练的网络，能否完全取消离线阶段，只在推理过程中、利用当前输入未使用的自由度写入旧记忆。

### 二、技术方案（Method）
采用 d-512-256-C 的 k-WTA 稀疏局部学习器：前向为 a=Φ_k(relu(z)⊙(1-s))，k-WTA 保留每行最大 k 个激活，读出头为线性 C 类平方误差；误差经学习到的反馈权重 B 做单次自顶向下有界 burst 传播，无权重传输，前向与反馈按共享衰减 λ 的局部乘积更新，默认 heavy-ball SGD（μ=0.9，每突触一阶速度）。隔离规则定义 M=1[j∉A^{l-1}(X) 或 i∉A^l(X)]，其中 A 为当前唤醒批次激活集合，回放更新及其优化器状态仅在掩码内推进，掩码外速度冻结而非清零、衰减也被限制；不应期旋转让刚发放单元在下一轮竞争中暂停，扩大可巩固突触集合，并由稳态压力和相对新颖性门控决定回放 burst 与旋转时机。实验在类别增量 split-MNIST 与 split CIFAR-10 上进行，唤醒批 n_w=16， reservoir 缓冲区 K=1000 原始样本（另有 200/5000 缓冲轴），无离线阶段。

### 三、结果（Result）
在 split-MNIST 上无离线阶段达到 91.6±0.3%，在两个留出划分上达到或超过最佳离线夜间调度，与 DER++ 持平，并高于 BP+ER、ER-ACE、A-GEM 和未掩码局部回放，回放样本量约为夜间调度的两倍；单遍流式设置下达到 91.8%，高于 DER++ 的 90.1%，而离线夜间降至 76.9%。小缓冲区时优势最大，大缓冲区时让位于反向传播参考方法；在 split CIFAR-10 上超过离线排练和 BP+ER，但落后 ER-ACE 与 DER++ 约 2–3 个百分点。旋转贡献主要增益，隔离提供不变性保证；在带 k-WTA 隐藏层的反向传播网络上，同一调度下旋转在 5 轮内加约 0.5 个百分点、单遍加约 3 个百分点，隔离在其上仍然免费。

### 四、结论（Conclusion）
该方法反转了非干扰持续学习的保护方向：不再保护旧任务，而是保持当前唤醒输入上的隐藏计算不变，把旧记忆写入当前批次未使用的自由度，从而证明无需离线阶段也能完成回放巩固。机制不绑定于局部学习规则，在带 k-WTA 的反向传播网络上同样有效；但在 CIFAR-10 上仍落后最强反向传播回放方法，CIFAR-100 上所有方法绝对性能都在低位，说明其优势主要在中小缓冲与较简单任务，并需通过突触衰减控制器和局部学习跳连来扩展到更深网络。

### 五、方法论与关键技术细节
数据与协议：split-MNIST 为 5 个二分类任务、每任务 5 轮，split CIFAR-10 同协议且用 32×32 亮度输入；静态轴为同数据 i.i.d. 打乱；评估时关闭抑制掩码、仅保留 k-WTA，遗忘 F 为各旧任务从自身结束到最终结束的准确率平均下降，回放成本 R 以批次和样本计。精确性构造：掩码与所更新权重匹配时，对 silent 和 suppressed 单元严格不变；其他情况下每次更新约 99.7% 唤醒样本不变（即例外约 0.3%）。实现细节：优化器状态只在掩码内推进，支持 heavy-ball 与 Adam；前向-反馈单次扫描、无权重传输、Dale 定律、稀疏距离依赖连接、k-WTA 稀疏度约 10%；缓冲区为 reservoir 写入的 K 个原始样本。局限：配置曾在官方测试划分上选择后冻结，主比较用留出十分之一重训；不同 CPU 线程数因 k-WTA 不连续性等效于不同随机种子；能量代理仅计算术、非硬件实测；CIFAR-100 绝对数值处于地板，且方法在大缓冲和更强反向传播回放面前优势消失。
