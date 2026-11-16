# Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Gongyue Teng, Yuqing Xie, Yixian Zhang, Feng Gao, Shu'ang Yu, Jiaji Rao, Sukai Wang, Guanghui Ren, Ya Zhang, Maoqing Yao, Yu Wang, Chao Yu, Xinlei Chen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17394v1) · [PDF](https://arxiv.org/pdf/2611.17394v1)

## TLDR
Agentic-Teacher is an autonomous failure-driven data engine that uses coding agents to generate, refine, and curate targeted demonstrations from a VLA model’s failed rollouts, enabling effective post-training that improves task success without requiring agent assistance at inference time.

## Abstract
Improving a pretrained vision-language-action (VLA) model requires demonstrations that address its weaknesses and provide effective supervision for learning. Coding agents can autonomously generate demonstrations through environment interaction, yet successful execution alone does not ensure effective supervision for VLA learning. We introduce Agentic-Teacher, an autonomous data engine for failure-driven VLA post-training. Given a VLA checkpoint, a task specification, and configured environment tools, the engine analyzes failed rollouts, selects intervention states, and iteratively develops closed-loop code policies through execution feedback. Validated policies become reusable demonstration generators that collect successful continuations from states where the VLA struggles. To make these demonstrations suitable for learning, Agentic-Teacher introduces temporally correlated action noise to broaden state-action coverage, removes idle frames while preserving gripper transitions, and filters trajectories using the frozen base model's flow-matching loss. The resulting demonstrations are combined with successful VLA rollouts for post-training, yielding an updated policy that operates without coding-agent assistance. Agentic-Teacher thus connects the weaknesses of a target VLA to both the generation and curation of its training data. In simulation, it improves $π_0$ success rates from 79.4% to 87.8% on LIBERO-10, from 80.4% to 90.6% on MetaWorld-10, and from 0% to 30.0% across three RoboCasa tasks.


## 精读解读（中文）
### 一、研究动机
提升预训练视觉-语言-动作（VLA）模型需要能够针对其薄弱环节提供有效监督的示范数据，但仅靠编码智能体与环境交互生成成功轨迹，并不保证这些数据对 VLA 学习有效。为此，作者提出面向失败驱动的 VLA 后训练数据引擎，将目标模型的失败模式同时连接到训练数据的生成与筛选。

### 二、技术方案（Method）
给定 VLA 检查点、任务说明和环境工具，Agentic-Teacher 先分析失败 rollout，选择需要干预的状态，再借助执行反馈迭代开发闭环代码策略；验证通过的策略作为可复用示范生成器，从 VLA 失败状态收集成功后续轨迹。为使示范适合学习，方法引入时间相关动作噪声扩大状态-动作覆盖，删除空闲帧但保留夹爪切换，并用冻结基模型的流匹配损失过滤轨迹，最后将筛选后的示范与成功 VLA rollout 合并用于后训练，部署时更新后的策略不再需要编码智能体辅助。

### 三、结果（Result）
在仿真中，该方法将 π0 的成功率从 79.4% 提升到 87.8%（LIBERO-10），从 80.4% 提升到 90.6%（MetaWorld-10），并在三个 RoboCasa 任务上从 0% 提升到 30.0%。这些结果说明失败驱动生成与筛选的数据能改善目标 VLA 的后训练效果，尤其在基模型完全失败的任务上带来非零成功。

### 四、结论（Conclusion）
Agentic-Teacher 将目标 VLA 的失败弱点与训练数据的生成、增强和筛选闭环连接起来，形成可自主运行的后训练数据引擎。后训练后的策略无需编码智能体参与即可执行任务，表明该方法有潜力把失败分析转化为可复用的监督数据；但当前证据主要来自仿真基准，RoboCasa 上 30.0% 的成功率也显示复杂任务仍有明显提升空间。

### 五、方法论与关键技术细节
关键实现包括基于失败 rollout 选择干预状态、用执行反馈迭代闭环代码策略、以时间相关动作噪声扩展覆盖、保留夹爪转换的空闲帧删除，以及用冻结基模型的流匹配损失进行轨迹过滤。方法依赖任务说明、可配置环境工具和可执行反馈，数据由验证策略生成的成功续接与原有成功 rollout 混合构成；摘要未披露噪声强度、过滤阈值、轨迹数量和后训练超参数。局限性在于目前仅报告仿真结果，缺少真实机器人验证，且对需要复杂长程操作的任务提升有限。
