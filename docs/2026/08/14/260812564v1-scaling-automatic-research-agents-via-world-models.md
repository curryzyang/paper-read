# Scaling Automatic Research Agents via World Models

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Xiyuan Yang, Sheikh Sarwar, Jingru Cheng, Zhan Shi, Duanshun Li, Huiyuan Chen, Haiyang Zhang, Chenlei Guo, Jingrui He, Zhenyu Liao
- 机构：Amazon, University of Illinois Urbana-Champaign
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12564v1) · [PDF](https://arxiv.org/pdf/2608.12564v1)

## TLDR
This paper introduces World Model RL (WMRL), which replaces expensive real-environment execution with a learned world model during RL training of automatic research agents, removing the scaling bottleneck and, with bias/noise corrections, achieving 3–4× faster training and stronger performance than standard RL baselines.

## Abstract
Automating empirical research is a long-standing direction of AI. Recent automatic research (AutoResearch) agents bring this goal within reach, as modern LLMs show the capability to independently implement solutions and learn from the execution outcomes. Behind these gains, post-training (especially RL) plays a central role. In this paper, we identify a fundamental tension when scaling RL for these agents: the two components of every AutoResearch trajectory (agent generation and environment execution) scale in very different manners, since all generation shares compute through batching, while each execution occupies its exclusive sandbox and real machine time. As a result, the environment execution dominates the training cost and becomes the bottleneck as trajectories grow. To resolve this tension, we propose World Model RL (WMRL), which replaces environment execution with a world model to remove this bottleneck. Additionally, the world model can be imperfect, as its rewards are corrupted by bias and noise. Therefore, we further equip WMRL with two mitigations, Online Debiasing and Inverse-Variance Denoising, which offset the bias and suppress the noise respectively. Theoretically, we prove that both mitigations of WMRL strictly improve the convergence guarantee. Empirically, WMRL accelerates training by 3-4x on various tasks at different agent scales, while exceeding the performance of standard RL baselines. Moreover, our post-trained 4B and 9B agents outperform much larger open-weight agents of 48B and 120B on held-out benchmarks. Beyond AutoResearch, WMRL also transfers to post-training embodied VLA policies, which demonstrates the generalizability of our method.


## 精读解读（中文）
### 一、研究动机
自动化实证研究是AI长期目标，AutoResearch代理结合LLM后训练（尤其是RL）已能独立实现解决方案并从执行结果中学习。但扩展RL时存在根本张力：轨迹的生成部分通过批处理共享计算，而每次环境执行需独占沙箱和真实机器时间，导致执行成本随轨迹增长线性上升并成为训练瓶颈。因此需要一种像生成一样可扩展的快速环境信号来替代昂贵执行，同时处理这种替代带来的预测误差。

### 二、技术方案（Method）
提出世界模型强化学习（WMRL）：用与代理同骨干的通用语言模型作为世界模型，输入任务上下文和代理的解决方案，预测执行结果并从中读取估计奖励，替代真实环境执行。训练流程基于GRPO，每批任务中采样多个组，所有组先用世界模型评分；同时选一部分锚组用真实环境执行获取真实分数。通过Online Debiasing在锚组上拟合单调映射来校正世界模型分数的系统偏差，再用Inverse-Variance Denoising将真实分数与校正后预测分数按方差反比加权融合，抑制随机噪声，得到修正奖励后计算组内优势并更新策略。由于世界模型前向传播可像生成一样批处理，执行瓶颈被消除。

### 三、结果（Result）
在多种AutoResearch任务和不同agent规模上，WMRL将训练加速3到4倍，同时超过标准RL基线；训练后的4B和9B agents在保留基准上优于48B和120B的开放权重模型；该方法还迁移到具身VLA策略后训练，证明了泛化性。

### 四、结论（Conclusion）
WMRL通过世界模型替代环境执行，解决了AutoResearch代理RL扩展中的执行瓶颈，并设计在线去偏与逆方差去噪来补偿世界模型的偏差和噪声，理论上严格改善收敛保证，实验上加速训练并提升性能，且可泛化到VLA等其他后训练场景。

### 五、方法论与关键技术细节
关键细节：世界模型是与代理相同骨干的通用语言模型，输入任务上下文与解决方案，输出执行结果预测；RL目标采用GRPO，每n个轨迹为一组，更新步长为γ；世界模型误差被分解为偏差b与零均值噪声ξ，其上界B和σ分别引入收敛界中的O(B²)和O(σ²)项；训练循环内保留少量真实执行流作为锚组，在线拟合单调映射去偏，并逆方差加权融合以去噪；限制是仍需少量锚组真实执行，世界模型不完美需要在线校正，无法完全免费；具体超参数如锚组比例、融合权重等依赖实现与任务。
