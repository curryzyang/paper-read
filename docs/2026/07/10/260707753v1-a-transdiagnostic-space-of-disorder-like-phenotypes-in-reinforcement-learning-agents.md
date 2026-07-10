# A Transdiagnostic Space of Disorder Like Phenotypes in Reinforcement Learning Agents

- 区域：精读区
- 排名：9
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Hari Prasad
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07753v1) · [PDF](https://arxiv.org/pdf/2607.07753v1)

## TLDR
This paper introduces a dose-controllable appraisal-guided reinforcement learning framework that induces seven psychological disorders in agents, revealing emergent transdiagnostic structure (a two-dimensional affective space), treatment dissociations between reward-distortion and avoidance disorders, and nonadditive comorbidity interactions.

## Abstract
Modelling psychological disorders in artificial agents offers both a testbed for computational psychiatry and a lens on the failure modes of affective control. Prior work induces one or two disorders in a reinforcement learning (RL) agent by hand-tuned reward shaping, labels the behaviour post hoc, and reports single runs. We recast disorder modelling as dose-controllable manipulation of cognitive appraisal signals in an appraisal-guided PPO agent, expressing seven disorders (anxiety, mania, obsessive-compulsive checking, depression, impulsivity, addiction, and post-traumatic stress) each as a single knob grounded in a computational psychiatry account, with each symptom measured by a preregistered assay mapped to a recognised paradigm. Across more than a thousand runs (10 seeds, four controls, 95% confidence intervals) every disorder shows a graded, monotone dose-response that no control reproduces. Beyond these induced effects, three findings emerge that were not written into the reward: the disorders self-organise into a two-dimensional affective space in which mania mirrors anxiety; removing a knob remits reward distortion disorders (mania, checking, addiction) but not avoidance disorders (anxiety, PTSD), which instead recover under a graded exposure curriculum; and two simultaneous knobs interact nonadditively, yielding testable comorbidity predictions. Appraisal weights thus parameterise a controllable space of affective phenotypes in which the same knobs that induce a disorder can model its treatment. We also show that three disorder knobs (depression, addiction, anxiety) transfer to a three-dimensional pixel environment (MiniWorld) with a standard convolutional agent and no appraisal critic, with cross-assay dissociation confirmed across both domains, indicating the framework is not specific to grid worlds or to PPO's appraisal critic.


## 精读解读（中文）
### 一、研究动机
现有强化学习障碍模型存在三个缺陷：手动调参而非基于机制、事后标签而非预先注册测量、单次运行缺乏方差和对照。本文提出通过认知评估引导的PPO代理进行剂量可控的障碍建模，以克服这些局限，并探索跨诊断的涌现结构。

### 二、技术方案（Method）
采用AG-PPO架构，包括卷积编码器、Actor、Critic和Next-Reward Estimator。每步计算六个评估维度（动机相关性、目标一致性、确定性、新颖性、应对潜力、预期），输入Critic并塑造奖励。七种障碍各对应一个可调参数（焦虑/狂躁操作应对潜力，强迫症检查奖励，抑郁移动代价，冲动降低折扣因子，成瘾非习惯化奖励，PTSD创伤电击），奖励函数为r'_t = r_t - sum w_i g(ζ) - 移动代价 + 检查奖励 + 药物奖励 - 电击奖励。训练使用PPO剪辑损失和值损失，Next-Reward网络最小化预测误差。在多个网格世界（动态障碍、熔岩间隙、趋避冲突、时间选择、成瘾、创伤）和MiniWorld像素环境中进行1000+次运行（10种子、4对照、95%置信区间）。

### 三、结果（Result）
七种障碍均呈现梯度单调的剂量-响应曲线，且无对照复现。涌现结果包括：障碍自组织成二维情感空间（狂躁与焦虑镜像）；移除障碍旋钮消除奖励扭曲障碍（狂躁、强迫症、成瘾）但无法消除回避障碍（焦虑、PTSD），后者需分级暴露课程恢复；双旋钮组合产生非加性交互，提供可检验的共病预测。三个障碍旋钮（抑郁、成瘾、焦虑）成功迁移至MiniWorld像素环境，并在两个领域间维持跨测定分离。

### 四、结论（Conclusion）
评估权重参数化了一个可控的情感表型空间，同一旋钮既可诱导障碍也可模拟治疗。框架具有跨领域迁移性，不限于网格世界或AG-PPO的评估评价器，为计算精神病学提供可剂量控制的测试平台。

### 五、方法论与关键技术细节
数据：使用四个威胁/空间网格世界和三个专用环境（趋避冲突、时间选择、成瘾、创伤），以及MiniWorld三维像素环境；先验：每个障碍旋钮基于计算精神病学文献（如Rachman强迫症、Redish成瘾、Treadway抑郁）；损失：PPO剪辑代理损失 + 值函数MSE + Next-Reward预测MSE；超参：10随机种子，4对照条件（标准PPO、Critic噪声随机评估、PPO+RND内在动机、无塑造的评估Critic），95%置信区间；复杂度/约束：AG-PPO包含额外评估评价器和Next-Reward网络，增加计算开销；局限性：环境为简化的网格世界和人工任务，评估维度手工设计，可能限制复杂场景泛化。
