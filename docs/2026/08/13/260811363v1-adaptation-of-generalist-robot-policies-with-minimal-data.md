# Adaptation of Generalist Robot Policies with Minimal Data

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Shreyas Kowshik, Sreyas Venkataraman, Leo Wang, Niharika Pant, Max Simchowitz, Aviral Kumar
- 机构：Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11363v1) · [PDF](https://arxiv.org/pdf/2608.11363v1)

## TLDR
MiDAS enables a pre-trained robot policy to adapt to a new task with as little as a single demonstration by anchoring it via few-shot behavior cloning and then improving it with residual value-based online RL, achieving strong performance across simulated benchmarks and real-robot bimanual manipulation.

## Abstract
A central goal in robot learning is to move beyond task-specific human data collection toward robots that improve through autonomous interaction. Yet fully autonomous learning remains difficult with current policies: sparse rewards and weak zero-shot exploration make it unlikely that a robot will discover successful behavior from scratch. We study minimal-data adaptation, a regime in which a pre-trained robot policy must learn a new task from as little as one demonstration followed by autonomous online interaction. This setting serves as the closest tractable proxy for fully autonomous improvement, allowing us to study whether minimal human guidance can bootstrap autonomous learning and what algorithmic ingredients make it feasible. We build MiDAS, a simple offline-to-online RL recipe that first anchors a pre-trained VLA to the target task with behavior cloning on single/few demonstrations, then improves it through value-based online RL on a residual policy parameterization. Across LIBERO and RoboCasa, MiDAS recovers strong task performance from as little as one demonstration, substantially outperforming baselines and generalizing beyond demonstrated conditions. We further evaluate MiDAS on a bimanual YAM platform. Starting from a fragile low-success policy obtained from a single demonstration, MiDAS improves its robustness and learns new successful behaviors over ~6 hours of online interaction. To the best of our knowledge, this is the first demonstration of reliable robot policy adaptation from a single task demonstration.


## 精读解读（中文）
### 一、研究动机
完全自主的机器人学习在当前策略下仍然困难，稀疏奖励和弱零样本探索使机器人难以从零开始发现成功行为。本文研究最小数据适应，即预训练策略仅需一条演示即可引导自主在线学习，以作为完全自主改进的最接近可行代理，并探究哪些算法要素使其可行。

### 二、技术方案（Method）
提出MiDAS，一个简单的离线和在线强化学习两阶段方案。第一阶段在单条或少量演示上用行为克隆微调预训练视觉-语言-动作模型，得到任务锚定策略；第二阶段冻结该策略，在其表示之上训练轻量级残差策略和价值函数，通过基于价值策略无关强化学习进行在线改进，并使用成功回放平衡等技巧稳定稀疏奖励下的训练。

### 三、结果（Result）
在LIBERO和RoboCasa基准上，MiDAS从仅一条演示即可恢复强任务性能，显著优于基线并泛化到演示之外的条件。在真实双臂YAM平台上，从单条演示得到的脆弱低成功率策略出发，约6小时在线交互即可提升鲁棒性并学习新的成功行为，这是首次从单条任务演示实现可靠机器人策略适应的展示。

### 四、结论（Conclusion）
最小数据适应对当今通用机器人策略是可行的，单条成功演示即可启动自主适应。其成功源于预训练、演示与在线交互的协同：预训练提供可复用特征和行为先验，演示锚定任务并使成功行为可达，在线强化学习补充细粒度修正和鲁棒性。

### 五、方法论与关键技术细节
数据方面使用单条或少量成功演示及自主交互收集的转移数据；机制上在Stage I对VLA使用LoRA微调骨干和完整动作头进行流匹配行为克隆，在Stage II采用基于状态的Q函数与动作块，利用成功回放缓冲抑制稀疏奖励下策略崩溃；关键超参包括warmup步数、成功回放比例等。局限性在于完全自主仍需安全重置与硬件支撑，且依赖预训练策略具备足够的任务相关先验。
