# Teaching a Robot Dog New Tricks: Diverse Quadruped Skills via Combined Reinforcement and Imitation Learning with Adversarial Task Selection

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Lemon Foxmere, Anthony Furman, Yizheng Du, Oliver Chang, Leilani Gilpin, Steve McGuire
- 机构：University of California at Santa Cruz
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10601v1) · [PDF](https://arxiv.org/pdf/2610.10601v1)

## TLDR
The paper presents a three-stage reinforcement and imitation learning method with adversarial task selection that trains a single quadruped policy to perform and compose 22 diverse skills from 8 teacher policies, achieving better command tracking and real-world robustness on a Unitree B1.

## Abstract
Reinforcement Learning (RL) has enabled legged robots to perform a range of skills in single-task settings. However, applications such as farm robotics or space exploration require diverse skills such as locomotion, digging, or close-range surveying. Training an end-to-end policy to address this problem remains difficult due to challenges such as sample inefficiency and gradient conflict between tasks in multi-task learning. We propose a three-stage method that trains a single policy to perform distinct tasks such as walking, digging, and hopping, and compose them into novel behaviors such as crawling. First, multiple teacher policies are trained using RL on narrowly defined tasks. Then, two additional stages train a student policy with a multi-teacher distillation setup that uses a combined RL and Imitation Learning (IL) objective under an adversarial task selection process that focuses training on the worst-performing task. With this method, we train a student policy that performs 22 tasks using 8 teachers. Evaluations show our method preserves motion quality and tracks commands more accurately than PPO and distill-then-finetune baselines, and in some cases generalizes to new tasks without explicit training. Finally, we demonstrate real-world robustness by deploying the resulting policy on a Unitree B1 quadruped. Video: https://youtu.be/V9yX04EBcFA


## 精读解读（中文）
### 一、研究动机
腿足机器人单任务强化学习已能实现多种复杂技能，但农业机器人或太空探索等应用需要行走、挖掘、近距离勘察等多技能，端到端多任务策略训练仍受样本效率低、奖励游戏化、梯度冲突和灾难性遗忘制约。模仿学习可提供训练稳定性和行为保真度，强化学习可提供对分布外状态的鲁棒性，因此将二者结合有望训练单一策略执行、切换并组合多种技能。本文特别关注多任务训练中不同难度任务训练资源分配不均以及运动质量退化的问题。

### 二、技术方案（Method）
提出三阶段方法：第一阶段为每个窄定义单任务用PPO训练专用教师策略，教师可访问足端接触力等特权信息，并以自然运动为主要目标，训练后冻结。第二阶段为学生策略的ILP阶段，在单任务上以高λ优化PPO与行为克隆BC的联合目标L=L_PPO-λL_BC，BC示范通过DAgger在学生自身状态分布下在线查询教师获得，且MSE仅作用于策略均值，ILP中向学生动作加入零均值高斯噪声以保持探索。第三阶段为RLP阶段，加入单任务和复合任务，降低λ，先冻结actor并固定策略标准差预训练新critic，再联合优化PPO与IL锚定，同时采用对抗式任务选择，按各任务相对教师的误差赤字重加权采样，使训练更集中于当前表现最差任务。

### 三、结果（Result）
用8个教师策略训练出可执行22个任务的单一学生策略，其中8个为教师直接教授的单任务，14个为组合两个教师任务得到的复合任务，例如组合身高跟踪与全向行走形成低姿态爬行。评估表明该方法在运动质量和命令跟踪精度上优于PPO与distill-then-finetune基线，奖励游戏化影响较小，并能在未显式训练的情况下泛化到三个及以上任务的组合。最终策略部署在Unitree B1四足机器人上，实现爬行、galloping、跳跃、挖掘、倾斜和抬腿按按钮等真实世界行为。

### 四、结论（Conclusion）
结果表明，结合多教师蒸馏、联合RL与IL目标、对抗任务选择和critic预训练，可以训练单一策略掌握多种四足技能，并通过组合已有单任务产生新行为。该方法在保持自然运动质量和命令响应性的同时，展现出从仿真到Unitree B1实机部署的鲁棒性，为需要多技能按命令切换与组合的腿足机器人提供了一条可扩展路径。局限包括复合任务没有教师示范而依赖组合泛化，对抗采样权重受教师基线误差影响，且当前预览未展示完整消融、网络结构与全部超参数。

### 五、方法论与关键技术细节
关键设定是将任务分为单任务集合X与单/复合任务集合Y，学生策略为πθ(a|s,c_Y)，命令向量c_Y含共享的标量跟踪目标和二值标志，可指定任意任务。教师用PPO在任务特定奖励和特权信息下训练并冻结；学生联合损失为L=L_PPO-λL_BC，BC为MSE且不更新动作分布标准差；ILP仅训练单任务、高λ、奖励只含身体稳定与运动平滑项，RLP训练单任务和复合任务、低λ、奖励扩展到跟踪误差最小化和行为微调，并在RLP前冻结actor、固定σ0预训练critic。DAgger每步若命令对应单任务则查询对应教师并将(s,c_Y,a*)加入D，复合任务无教师则不采样；对抗任务选择用误差通道e、教师名义误差τ_e定义CNorm(e)=tanh(a v_e/τ_e)，a=tanh^-1(0.2)，任务赤字为相关通道均值，采样概率为p_i=κ deficit_i^β/Σdeficit_j^β+(1-κ)/|Y|，其中κ混合对抗分量与均匀先验，β控制锐度。实现细节还涉及教师训练优先自然运动而非完美跟踪、ILP噪声防止动作标准差坍缩、critic预训练缓解RLP初期值估计不可靠；但预览未给出完整网络结构、PPO超参、sim-to-real随机化和消融结果。
