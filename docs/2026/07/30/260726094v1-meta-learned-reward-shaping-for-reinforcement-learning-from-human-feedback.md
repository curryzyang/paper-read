# Meta-Learned Reward Shaping for Reinforcement Learning from Human Feedback

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Yunpeng Chu
- 机构：Stony Brook University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26094v1) · [PDF](https://arxiv.org/pdf/2607.26094v1)

## TLDR
MeRLa introduces a meta-learned reward shaping framework for RLHF that learns a task-aware shaping function across auxiliary tasks to improve reward signals, policy optimality, and training stability, achieving consistent gains over PPO, DPO, GRPO, and DAPO on LLaMA-3-8B.

## Abstract
Reinforcement Learning from Human Feedback (RLHF) is the standard approach for aligning large language models with human preferences, but its quality is limited by static, task-agnostic reward models. This mismatch leads to sparse learning signals and suboptimal alignment. We introduce MeRLa (Meta-Learned Reward Shaping), a principled framework that meta-learns a task-aware shaping function $Φ(x,y;φ)$ across auxiliary tasks before RLHF training. The learned shaping produces a composite reward that preserves policy optimality while providing task-specific learning signals. Our meta-objective combines task discrimination, entropy regularization, and potential-based conservation for stable convergence. We provide theoretical guarantees for policy invariance, analyze representation drift sensitivity, and formally address incentive misalignment from entropy maximization. Experiments on LLaMA-3-8B across four benchmarks show consistent improvements over PPO, DPO, GRPO, and DAPO, achieving a 90.8% length-controlled win rate on AlpacaEval 2.0 and a score of 9.14 on MT-Bench, with 41% less training instability. MeRLa retains its benefits when combined with process-based and rubric-based enhanced rewards.


## 精读解读（中文）
### 一、研究动机
标准RLHF使用静态且任务无关的奖励模型，导致学习信号稀疏和对齐效果次优。静态奖励无法适应多样化提示下的细微质量差异，引发奖励稀疏、过度优化和对齐税等问题。

### 二、技术方案（Method）
方法包括两阶段：元学习阶段和部署阶段。元学习阶段利用辅助任务分布，学习一个轻量级MLP塑形函数Φ(x,y;φ)，输入为冻结参考模型提取的提示嵌入和响应嵌入及其差值的拼接。元学习目标结合任务区分损失（对比偏好/非偏好响应）、熵正则化（鼓励奖励值分散）和守恒损失（迫使Φ接近潜在基础形式以保证策略不变性）。部署阶段冻结Φ，与基础奖励组成复合奖励（带强度参数α），用于GRPO、PPO等在线RLHF算法，算法流程见Algorithm 1。

### 三、结果（Result）
在LLaMA-3-8B上四个基准测试中，MeRLa一致超越PPO、DPO、GRPO和DAPO：AlpacaEval 2.0长度控制胜率达90.8%，MT-Bench得分9.14，训练不稳定性降低41%。当与过程奖励或基于规则的增强奖励结合时，MeRLa仍保持优势。

### 四、结论（Conclusion）
MeRLa通过元学习任务感知的奖励塑形函数，在不改变最优策略的前提下提供了密集型任务特定学习信号，显著改善了RLHF的对齐质量和训练稳定性。其理论保证了策略不变性并分析了表示漂移与激励对齐问题，且与多种基奖励兼容。

### 五、方法论与关键技术细节
关键细节：数据来自辅助任务分布中的偏好对；先验采用潜在基础塑形以保证策略不变性；损失包含任务区分、熵正则和守恒损失；超参α控制塑形强度，λ1,λ2平衡各项；模型为低于1M参数的2层MLP；使用冻结编码器避免表示漂移，并通过谱归一化控制Lipschitz常数；局限性包括依赖辅助任务分布质量和残余守恒误差引入的微小偏差。
