# Logic-VLA: A Temporal Logic Conditioned Vision-Language-Action Model

- 区域：精读区
- 排名：5
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Celina Shiyu Wang, Yiqi Zhao, Junjie Ye, Yue Wang, Jyotirmoy V. Deshmukh
- 机构：University of Southern California
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20556v1) · [PDF](https://arxiv.org/pdf/2608.20556v1)

## TLDR
Logic-VLA conditions a pre-trained vision-language-action model on Signal Temporal Logic (STL) specifications via syntax-graph encoding and two-stage post-training (STL-conditioned supervised fine-tuning plus trajectory-level preference optimization), improving STL satisfaction by 24.8–40.7 percentage points in quadcopter navigation while preserving nominal natural-language task success.

## Abstract
Vision-language-action (VLA) models can follow natural-language (NL) task instructions, but such instructions may not precisely specify safety-critical or spatiotemporal requirements on the resulting behavior. We introduce Logic-VLA, a formal-requirement-aware VLA that conditions on Signal Temporal Logic (STL) specifications supplied at inference time. Logic-VLA uses a syntax-graph-based STL encoder pre-trained to capture temporal logic semantics. Policy adaptation proceeds in two stages: STL-conditioned supervised fine-tuning on satisfying demonstrations is followed by trajectory-level preference optimization over matched satisfying-violating rollout pairs using a flow-matching surrogate for Identity Preference Optimization. This formulation improves formal requirement satisfaction while preserving the nominal NL task. We evaluate Logic-VLA in closed-loop quadcopter navigation simulation across randomized photorealistic environments and test generalization to STL formulas unseen during training. Across the evaluation benchmarks, Logic-VLA improves STL satisfaction rate over an STL-blind base policy by 24.8 to 40.7 percentage points (pp) while reducing nominal NL task success by at most 1.8 pp, showing that a single VLA can adapt its behavior to varying formal requirements without requiring a separate policy for each specification.


## 精读解读（中文）
### 一、研究动机
自然语言任务指令难以精确表达安全攸关或时空类行为要求，预训练VLA在部署时可能无法保证轨迹满足形式化约束。Logic-VLA提出将Signal Temporal Logic (STL)规格作为推理时的额外条件输入策略，从而在不牺牲原自然语言任务跟随能力的前提下，让同一个策略适应不同的形式化部署要求。

### 二、技术方案（Method）
Logic-VLA基于π0.5构建，输入为视觉观测、自然语言任务和STL公式。STL公式先通过基于语法图（syntax-graph，借鉴TeLoGraF）的编码器映射到VLA条件空间，该编码器使用轨迹-公式对和STL鲁棒语义进行预训练以捕获时序逻辑语义。后训练分两阶段：第一阶段用满足STL的演示进行STL条件监督微调（SFT）；第二阶段构造匹配的满足/违反轨迹对，并采用流匹配代理的Identity Preference Optimization (IPO)进行轨迹级偏好优化。推理时策略联合条件于视觉观测、自然语言任务与STL规格，实现闭环动作生成。

### 三、结果（Result）
在随机真实感环境的闭环四旋翼导航仿真中，Logic-VLA相比不考虑STL的基础策略，将STL满足率提高24.8到40.7个百分点，同时名义自然语言任务成功率最多仅下降1.8个百分点；在训练中未出现过的STL公式上也展现了泛化能力。

### 四、结论（Conclusion）
Logic-VLA证明了一个单一的VLA可以通过将形式化STL要求作为策略输入，而不是为每个规格训练单独策略，来适应部署时变化的正式需求；该方法在显著提升形式化约束满足率的同时几乎不影响原始任务性能，为要求条件化VLA后训练提供了通用模板。

### 五、方法论与关键技术细节
关键细节包括：STL编码器使用语法图结构表示公式，并以STL鲁棒语义作为监督信号预训练；后训练数据来自域内数据集D=(s,a,l,o)，通过候选公式库采样得到满足演示和匹配的满足/违反轨迹对；STL条件SFT负责模仿满足行为，IPO偏好优化负责区分轨迹级满足质量，且使用流匹配替代目标以适配flow-matching型VLA；测试时假设自然语言任务与STL要求不冲突，否则问题不可行；实验主要在仿真中进行，未涉及真实硬件验证，具体超参数细节未在预览中充分展开。
