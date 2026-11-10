# BATCH: Behavior Alignment for Cross-Embodiment Learning from Humans

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Zeyi Liu, Shuran Song
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10148v1) · [PDF](https://arxiv.org/pdf/2611.10148v1)

## TLDR
BATCH is a cross-embodiment learning framework that explicitly aligns human and robot behaviors via self-supervised cycle-consistent temporal representations and behavior-aligned co-training/style transfer, enabling more effective transfer from human demonstrations to robot manipulation policies and improved generalization.

## Abstract
Human demonstrations provide a scalable source of diverse manipulation data, but leveraging them for robot learning remains challenging due to differences in embodiment, viewpoint, action spaces, and temporal structure. We introduce BATCH, a cross-embodiment learning framework that explicitly aligns human and robot behaviors. BATCH learns self-supervised temporal representations with a cycle-consistency objective to establish cross-embodiment correspondences without manual annotation. We further introduce two complementary training objectives that leverage these correspondences within an autoregressive videoaction diffusion model: behavior-aligned co-training and human-to-robot style transfer. On real-world manipulation tasks, BATCH improves generalization to unseen task configurations compared with training on unaligned data and prior cross-embodiment baselines, with additional gains from the style-transfer objective. Our results demonstrate that explicit behavior alignment enables more effective transfer from human demonstrations to robot policies.


## 精读解读（中文）
### 一、研究动机
人类演示数据可扩展且任务多样，但直接用于机器人学习会受具身形态、视角、动作空间和时间结构差异的限制。论文旨在通过显式对齐人类与机器人行为，提升从人类演示到机器人策略的迁移效率与泛化能力。

### 二、技术方案（Method）
BATCH 先利用带循环一致性目标的自监督时序表征学习，在无需人工标注的情况下建立跨具身对应关系。随后在自回归视频-动作扩散模型中引入两个互补训练目标：行为对齐协同训练和人类到机器人风格迁移，使对齐后的跨具身数据共同参与策略学习。整体流程以人类演示与机器人数据为输入，先学习时序对应，再通过扩散模型进行动作生成训练与推理。

### 三、结果（Result）
在真实世界操作任务上，BATCH 相比使用未对齐数据训练以及先前跨具身基线，在未见任务配置上的泛化表现更好。加入风格迁移目标还能带来额外性能提升，说明显式行为对齐有助于更有效地利用人类演示。

### 四、结论（Conclusion）
结果表明，跨具身学习的关键在于显式对齐人类与机器人行为；通过自监督对应关系与协同训练/风格迁移结合，可以更有效地将人类演示迁移为机器人策略，并改善对新任务配置的泛化。

### 五、方法论与关键技术细节
关键实现包括自监督时序表征、循环一致性对应学习、无人工标注的跨具身匹配，以及在自回归视频-动作扩散模型中使用行为对齐协同训练和人类到机器人风格迁移两个目标。评估基于真实世界操作任务，并与未对齐数据和先前跨具身基线比较；摘要未给出具体网络规模、超参数、数据规模和计算复杂度，对应关系质量及人类与机器人域差异可能是主要约束。
