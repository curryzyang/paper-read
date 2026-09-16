# Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement

- 区域：精读区
- 排名：6
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Loc X. Nguyen, Avi Deb Raha, Huy Q. Le, Eui-Nam Huh, Dusit Niyato, Choong Seon Hong
- 机构：Kyung Hee University, Nanyang Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13236v1) · [PDF](https://arxiv.org/pdf/2609.13236v1)

## TLDR
This survey examines post-deployment self-improvement for humanoid robots by formalizing their evolving policy, perception, memory, workflow, and body as a state updated through a safety-constrained evolution operator, taxonomizing self-evolution mechanisms from self-learning to self-generation, and advocating trajectory-level evaluation while identifying the lack of dedicated benchmarks and open algorithmic, systems, and governance challenges.

## Abstract
Humanoid robots are becoming an important part of embodied artificial intelligence, driven by advances in reinforcement learning for locomotion, world models for prediction, and vision-language-action models for general control. However, most of these systems remain static after deployment. A policy is trained offline for a fixed objective and then frozen, even though the tasks, environments, and robot bodies keep drifting over time. An emerging paradigm of self-evolving agents aims to address this problem by allowing systems to improve from their own post-deployment experience. Since most existing studies focus on disembodied software agents, this survey examines how self-evolution changes when an agent has a physical body. We first define self-evolution for humanoids and represent a deployed robot using a state tuple that includes its policy, perception, memory, workflow, and body. This state is updated by an evolution operator in a slow outer loop with a lifelong objective. We then organize the literature into four complementary mechanisms of self-evolution, presented in increasing order of autonomy: self-learning, self-adaptation, self-optimization, and self-generation. Since changes to a humanoid can introduce physical hazards, we treat safety and uncertainty as key design dimensions of the evolution operator, and further formulate admissible evolution as a constraint enforced by a world-model verification gate within a human-oversight envelope. Finally, we present that evaluation should track the robot's evolving trajectory rather than a fixed checkpoint, and we identify the lack of a benchmark designed specifically for self-evolving humanoids. Moreover, we outline open challenges spanning AI algorithms, on-board systems, and governance.


## 精读解读（中文）
### 一、研究动机
人形机器人虽受益于强化学习、世界模型和视觉-语言-动作模型，但多数系统部署后被冻结，面对任务、环境、用户乃至本体硬件持续漂移时性能会退化。现有自演化智能体研究主要针对无实体软件智能体，缺少对具身系统中身体变化和实时物理安全约束的讨论，因此需要重新定义并系统梳理部署后人形机器人自我改进的机制、安全与评估。

### 二、技术方案（Method）
本文将部署后人形机器人形式化为状态元组 sτ=(πτ,Φτ,Mτ,Wτ,Bτ)，分别对应策略、感知、记忆、工作流与身体，部署经验 eτ 通过演化算子 E 在慢外循环中更新状态，并以终身目标 V 和元更新 F 调整演化机制本身；E 可分解为策略、感知、记忆、工作流和身体五类子算子，子算子相互耦合。方法上按自主性递增将文献组织为自学习、自适应、自优化和自生成四类机制，并按机制、子算子、触发条件、平台和更新时机分类，同时将安全与不确定性建模为演化算子的约束，要求候选更新位于可接受区域 C 并经过世界模型验证门与人类监督包络。评估则从固定检查点转向轨迹级评价，提出自适应速率、遗忘速率、瞬态代价和安全回退率四类指标，并规划面向自演化人形机器人的基准套件。

### 三、结果（Result）
该综述通过对比相关调查指出，现有人形机器人、VLA、运动规划、持续学习和自演化智能体综述均未同时覆盖具身性、部署后自我改进、身体或硬件演化、实时安全约束和终身轨迹评估，而本文将五者均作为核心议题。文献分析发现三个趋势：部署后变化越来越通过小型可逆模块而非直接修改主模型权重实现，验证责任逐渐从人工监督转向世界模型，以及在持续变化环境中一定程度的遗忘对适应是必要的。同时识别出两个安全缺口：现有系统未显式强制单调性以防止安全关键能力丢失，且当前防护很大程度上忽视身体算子；标准化评估与专用基准仍然缺失。

### 四、结论（Conclusion）
本文的结论是，人形机器人应从一次离线训练后冻结部署转向终身、安全约束下的自演化，其中安全应被视为演化算子自身的属性而非事后补丁。评价也应跟踪机器人随时间演化的轨迹，而不是只比较固定检查点，因此需要建立专门面向自演化人形机器人的基准与治理框架，并在算法、机载系统和治理层面继续解决开放挑战。

### 五、方法论与关键技术细节
关键细节包括：状态五元组分别映射到感知编码器与状态估计、RL或VLA控制策略、技能库或回放或世界模型、任务分解与规划、标定与运动学动力学自模型；部署经验来源涵盖图像、视频、力触觉、本体感知、成败轨迹和人类反馈。方法遵循快内循环毫秒至秒级固定状态行动、慢外循环小时至月级用经验更新，并受可塑性与稳定性权衡约束，终身目标 V 对应约束优化而非单一损失。评估指标为自适应速率、遗忘速率、瞬态代价和安全回退率。局限在于本文是综述，缺少统一实验与基准，四类机制和五层安全框架的成熟度不同，身体算子风险、实时验证复杂度、不确定性校准、机载算力与治理约束仍未被充分解决。
