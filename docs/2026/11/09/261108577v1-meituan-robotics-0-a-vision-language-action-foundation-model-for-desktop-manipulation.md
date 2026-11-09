# Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Meituan Robotics Team, Caicheng Wang, Chen Zhao, Chengpeng Jin, Duo Xu, Fengjiao Chen, Guanglu Wan, Heqing Yang, Jia Wang, Jiacong Zhou, Jie Hu, Jiyuan Ru, Lingfeng Zhang, Linjiang Huang, Manyuan Zhang, Ningchu Liu, Shijie Zhou, Si Liu, Shuo Li, Tianyi Zhang, Xi Zhang, Xin Chen, Xuezhi Cao, Xunliang Cai, Yanbin Zeng, Yang Yang, Yang Yi, Yanli Tan, Yifu Xu, Yimeng Jia, Yuchen Tang, Yuchen Xie, Yuxiang Zheng, Zerwei Chng, Zilong Huang, Zipeng Ye, Ziyuan Qin, Ziqin Wang
- 机构：Meituan
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08577v1) · [PDF](https://arxiv.org/pdf/2611.08577v1)

## TLDR
Meituan-Robotics-0 (MR0) is a vision-language-action foundation model and event-driven embodied-agent system for desktop manipulation that combines 147M vision-language samples with 15,060 hours of cross-embodiment robot data and a three-stage training recipe—discrete action-token pre-training, flow-matching mid-training, and real-world post-training with Rollback-based CFG-DAgger—to enable robust cross-embodiment control, smooth asynchronous execution, and long-horizon task memory and resumption.

## Abstract
We present Meituan-Robotics-0 (MR0), a vision-language-action foundation model and embodied-agent system for stationary-base desktop manipulation. MR0 combines 147 million vision-language samples with 15,060 hours of curated robot trajectories spanning 12 embodiments. A three-stage training recipe aligns multimodal representations with robot behavior through discrete action-token pre-training, transfers these priors to continuous cross-embodiment control through flow-matching mid-training, and adapts the policy through real-world post-training. We introduce Rollback, which pairs replaced policy segments with human corrections to provide positive and negative supervision for CFG-DAgger without value learning or advantage labeling. A unified end-effector interface supports heterogeneous embodiments, while asynchronous action-chunk merging maintains smooth execution under variable inference latency. An event-driven agent maintains persistent task events and reassesses plans when progress or feasibility changes, enabling cross-task retrieval and conditional task resumption. MR0 achieves 93.6% success on RoboTwin 2.0 and ranks fifth in the RoboDojo VLA track. Under matched HG-DAgger post-training, MR0 achieves higher average success rate and progress score than $π_{0.5}$ across three real-robot tasks. On Ethernet insertion, CFG-DAgger trained with Rollback data reaches 70% success and a progress score of 0.90. Qualitative agent deployments demonstrate cross-task event retrieval and recovery from temporarily unsatisfied task conditions.


## 精读解读（中文）
### 一、研究动机
通用桌面操作要求具身系统同时具备跨异构数据的广泛行为先验、跨本体迁移能力、闭环执行中的错误恢复能力，以及在长时程中保留任务相关状态的能力。仅扩大VLA动作模型难以解决机器人数据格式/动作空间/本体不一致、成功示范缺乏错误恢复监督、反应式策略离开观测窗口后丢失任务信息等问题。因此需要把对齐后的异构数据、鲁棒的真实世界策略学习和持久任务级记忆连接起来。

### 二、技术方案（Method）
MR0首先构建147M视觉语言样本与15,060小时、覆盖12种本体的桌面机器人轨迹，经静态边界过滤、运动学一致性检查、视频缺陷过滤、跨本体动作规范化和分层任务标注形成训练数据；动作统一为肩部中心坐标系下的末端执行器绝对位置、6D旋转和归一化夹爪开度，单臂10维、双臂20维。策略采用三阶段训练：离散动作token预训练对齐多模态表征与机器人行为，MMDiT动作头通过flow matching进行连续跨本体中训练，再用成功示范SFT、HG-DAgger人类纠正、RECAP结果标签自主 rollout 和Rollback增强的CFG-DAgger做真实世界后训练。部署时异步动作块合并将新预测与正在执行的命令融合以保持平滑控制；事件驱动智能体由Monitor把短视觉窗口总结为任务事件，Memory Manager维护持久事件记录，Planner仅在进度或可行性变化时重评估和恢复任务。

### 三、结果（Result）
作为独立策略，MR0在RoboTwin 2.0上达到93.6%成功率，并在RoboDojo VLA赛道排名第五。在匹配HG-DAgger后训练条件下，MR0在三个真实机器人任务上的平均成功率和进度分数均高于π0.5。在Ethernet insertion任务上，使用Rollback数据训练的CFG-DAgger达到70%成功率和0.90进度分数；定性部署还展示了跨任务事件检索以及任务条件暂时不满足后的恢复能力。

### 四、结论（Conclusion）
结果表明，对齐的异构数据、分阶段VLA训练、真实世界后训练与事件级记忆分别补充了通用桌面操作对先验、连续控制、错误恢复和长时程状态保持的需求。MR0提供了一条可迁移、可长时程执行的桌面操作具身系统路线，但其范围限于固定基座桌面操作，低层策略本身仍是反应式的，任务记忆依赖上层事件驱动智能体。

### 五、方法论与关键技术细节
数据侧关键点包括约13.6k小时具身训练数据、RoboDesk 3,235小时、授权真实机器人7,530小时和仿真4,295小时，以及S1-S3过滤和A1-A2对齐流程；CALVIN ABC-to-D消融支持优先构建2D目标可供性接地、场景描述和2D接地监督，其中2D接地用SAM候选区域加VLM身份分配。动作侧使用连续6D旋转、绝对末端位置和夹爪闭合并通过URDF校验运动学一致性，MMDiT以flow matching去噪动作块。Rollback通过回到历史锚点采集人类替换段并保留原策略段，为CFG-DAgger提供正负监督而无需价值学习或优势标注；异步动作块合并不阻塞策略推理。局限性包括仅面向固定基座桌面操作、排除基座运动、低层策略无显式历史，以及智能体仅在事件触发时进行任务级重规划。
