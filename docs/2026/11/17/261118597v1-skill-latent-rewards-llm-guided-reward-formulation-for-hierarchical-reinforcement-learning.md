# Skill-Latent Rewards: LLM-Guided Reward Formulation for Hierarchical Reinforcement Learning

- 区域：精读区
- 排名：1
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Maryam Shoaeinaeini, Brent Harrison
- 机构：University of Kentucky
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18597v1) · [PDF](https://arxiv.org/pdf/2611.18597v1)

## TLDR
Skill-LR is a hierarchical reinforcement learning framework that uses a vision-language model to identify the current subgoal and an LLM to generate subgoal-conditioned latent rewards, enabling more stable, sample-efficient credit assignment for long-horizon sparse-reward tasks and outperforming baselines such as RUDDER and LaRe on MiniGrid and BabyAI benchmarks.

## Abstract
Long-horizon reinforcement learning under sparse and delayed feedback remains an open challenge. Existing return-decomposition methods redistribute episodic rewards to ease credit assignment, but they operate on raw state--action transitions and disregard the subgoal structure that governs meaningful progress in complex tasks. We propose Skill-LR, a hierarchical reinforcement learning framework in which a vision--language model identifies the agent's active subgoal at each timestep and a large language model generates a matching latent reward formulation through a two-stage prompting process. By conditioning reward signals on the currently active subgoal, Skill-LR produces stage-specific credit that evolves with the hierarchical plan, reducing temporal variance and improving sample efficiency. On multi-stage MiniGrid and BabyAI benchmarks, including DoorKey and Unlock-to-Unlock, Skill-LR converges faster and more reliably than sparse environmental rewards and strong credit-assignment baselines such as RUDDER and LaRe, demonstrating that subgoal-aligned latent rewards offer a principled path toward stable, interpretable credit assignment in long-horizon tasks.


## 精读解读（中文）
### 一、研究动机
长时程强化学习在稀疏或延迟反馈下难以完成时间信用分配，现有RUDDER、LaRe等回报分解方法主要基于原始状态—动作转移，忽视复杂任务中决定有效进展的子目标层级结构；而传统分层强化学习多依赖人工设计的内在奖励，只能提供粗粒度指导。因此，论文希望把LLM潜在奖励的语义可解释性与分层强化学习的子目标结构对齐，实现随层级计划演化的稳定信用分配。

### 二、技术方案（Method）
Skill-LR先用LLM作为层级规划器，根据环境描述和角色指令生成多个候选子目标序列，并通过实际RL训练评估平均回报来选择最优层级；随后用视觉—语言模型在每个时刻将图像状态与候选子目标文本编码到共享空间，以兼容度最大者预测当前活动子目标。奖励侧采用两阶段提示：第一阶段让LLM生成n个与子目标对齐的候选潜在奖励函数并在环境中验证，第二阶段让LLM比较候选并选出最符合子目标进展语义的奖励R*；训练时收集带子目标标签的轨迹并存入回放与奖励缓冲，用Phi(s_t,a_t,g_t;R*)生成语义潜变量，由LSTM回报预测器F_psi估计累计潜在回报，并以rhat_{t+1}=F_psi(z_{t+1})-F_psi(z_t)做RUDDER式奖励重分配，周期性用RD损失更新F_psi直至阈值以下，再用重分配奖励更新策略。

### 三、结果（Result）
在DoorKey、Unlock-to-Unlock等多阶段MiniGrid和BabyAI基准上，Skill-LR比稀疏环境奖励以及RUDDER、LaRe等强信用分配基线收敛更快、更稳定，论文还声称其优于基于真实环境奖励的信用分配方式。预览未给出具体回报曲线数值、样本效率倍数或置信区间，因此可复现结论主要是相对收敛速度和可靠性优势。

### 四、结论（Conclusion）
结果表明，将LLM生成的潜在奖励条件化到当前活动子目标，可以把语义奖励与层级计划的阶段结构同步起来，降低回报方差并改善长时程任务的样本效率和收敛稳定性。该方向为可解释、子目标一致的信用分配提供了有前景的框架，但其理论保证依赖较强假设，且当前证据主要来自离散网格类多阶段基准。

### 五、方法论与关键技术细节
关键实现包括LLM生成候选子目标层级并按实际RL平均回报筛选、VLM按图像—文本兼容度逐时刻预测活动子目标、两阶段提示生成并二次筛选奖励函数，以及LSTM回报预测器以F_psi差分产生密集潜在奖励；RD损失、候选数n、最大回合数、奖励更新频率、损失阈值和学习率alpha在预览中未给出具体值。理论分析假设不同子目标潜空间近似正交且重分配奖励时间近似独立，从而把回报方差量级从O(TD)降至O(TD_g)，并给出含子目标数|G|和子目标潜维D_g的遗憾界。限制在于LLM/VLM推理和候选奖励的环境验证带来额外计算开销，候选子目标需通过多次RL训练评估，且实验局限于MiniGrid/BabyAI类离散环境，对连续控制和开放任务的泛化性尚未验证。
