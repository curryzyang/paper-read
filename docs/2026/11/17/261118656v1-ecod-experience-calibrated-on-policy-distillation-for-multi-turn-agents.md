# ECOD: Experience-Calibrated On-Policy Distillation for Multi-Turn Agents

- 区域：精读区
- 排名：4
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Jie Jin, Shengqin Wang, Yan Gao, Xin Tan, Yuan Xie
- 机构：East China Normal University, Shanghai Artificial Intelligence Laboratory, Shanghai Innovation Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18656v1) · [PDF](https://arxiv.org/pdf/2611.18656v1)

## TLDR
ECOD is an experience-calibrated on-policy distillation method that allocates teacher supervision across task, trajectory, and turn levels using matched teacher–student success outcomes, failed student trajectories, and successful teacher lengths, improving multi-turn agents on ALFWorld and WebShop over standard OPD and its variants.

## Abstract
Sparse and delayed rewards make reinforcement learning challenging for long-horizon language agents. On-policy distillation (OPD) complements environmental rewards with dense teacher feedback on student-generated contexts. Standard OPD can misalign supervision with relative teacher competence, student trajectory outcomes, and the temporal structure of task execution. Recent variants adjust guidance through divergence-based weighting and temporal schedules, while joint calibration from task-completion experience remains underexplored. We introduce Experience-Calibrated On-Policy Distillation (ECOD), which allocates teacher supervision at the task, trajectory, and turn levels. ECOD compares teacher and student success-rate posteriors under matched task conditions, restricts direct supervision to failed student trajectories, and derives a temporal prior from successful teacher lengths. The resulting weight applies to teacher losses or teacher-derived advantages. We evaluate ECOD on ALFWorld and WebShop with Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct. Under matched teacher settings, ECOD improves standard OPD by up to 4.06% in relative ALFWorld unseen success. Across both model scales, ECOD-assisted SOD, TCOD-F2B, and ATOD configurations yield average paired relative gains of 6.20% on ALFWorld unseen and 7.05% on WebShop, with WebShop gains ranging from 2.29% to 21.60%. These results support experience-calibrated supervision allocation as a reusable mechanism across distinct distillation objectives.


## 精读解读（中文）
### 一、研究动机
长程语言智能体面临稀疏且延迟的环境奖励，强化学习难以对多轮决策进行有效信用分配；on-policy distillation 虽能在学生生成的上下文上提供密集教师监督，但标准 OPD 的监督分配可能与教师相对能力、学生轨迹结果及任务执行的时间结构不匹配。现有基于散度权重和时间调度的变体多依赖单一信号，仍缺乏从任务完成经验出发对任务、轨迹和轮次三个层级进行联合校准的机制。

### 二、技术方案（Method）
ECOD 在任务级、轨迹级和轮次级为教师监督分配权重：任务级用匹配任务条件下教师与学生的成功率后验比较教师相对能力，以 Beta(1,1) 先验得到后验均值，并计算 q(u)=Pr(p_T>p_S) 及成功率均值差，形成 C(u)=[2q(u)-1]_+×[μ_T(u)-μ_S(u)]_+；轨迹级仅对失败的学生轨迹开放直接教师监督，即 F(u,k)=1[Y_S,u,k=0]，成功轨迹仍参与奖励学习；轮次级由成功教师轨迹长度构造时间先验 H_T(u,t)，即成功教师轨迹中包含第 t 轮的经验比例。三者相乘得到 g(u,k,t)=C(u)F(u,k)H_T(u,t)，并以 stop-gradient 方式加权教师损失，或加权教师派生优势后与奖励优势结合，同时保留基础 RL 目标、奖励优势构造和在线学生 rollout 流程。

### 三、结果（Result）
在 ALFWorld 与 WebShop 上使用 Qwen2.5-1.5B-Instruct 和 Qwen2.5-7B-Instruct 评估，匹配教师设置下 ECOD 相对标准 OPD 在 ALFWorld unseen 上最高提升 4.06% 相对成功率。ECOD 辅助的 SOD、TCOD-F2B 和 ATOD 配置在 ALFWorld unseen 与 WebShop 上分别取得平均配对相对增益 6.20% 和 7.05%，其中 WebShop 增益范围为 2.29% 至 21.60%，且六项 WebShop 比较均优于对应基线。ECOD 辅助的 GRPO 与 GiGPO 在两个基准上也高于纯 RL 对应方法，表明其可跨不同蒸馏目标复用。

### 四、结论（Conclusion）
ECOD 将教师监督分配统一为任务级能力校准、失败轨迹选择和轮次级时间先验的乘积权重，可同时用于教师损失加权和教师优势加权两类 OPD 形式。实验支持经验校准的监督分配能缓解多轮 OPD 中的监督错配，并在不同模型规模、RL 骨干和蒸馏目标上稳定带来相对增益，且推理阶段仅使用学生模型。

### 五、方法论与关键技术细节
关键实现包括使用缓存教师 rollout 与当前学生 rollout 估计成功率后验，学生统计仅来自当前 rollout 策略；权重各因子均在 [0,1] 内，乘积有界，优化期间固定并作用于教师贡献，基础教师系数 λ 和各方法原有调度仍保留。实验训练 150 次更新，每 5 次更新在 128 个任务上验证，主结果使用指定 checkpoint，消融使用第 150 次更新；除部分 seen 条目外，均值与样本标准差来自固定权重下的 8 次解码运行。WebShop 采用 1000 产品合成目标配置，教师为同规模冻结模型；局限包括每个配置仅训练一次、教师规模匹配且评估依赖指定 checkpoint，结论主要覆盖 ALFWorld/WebShop 与 Qwen2.5 系列。
