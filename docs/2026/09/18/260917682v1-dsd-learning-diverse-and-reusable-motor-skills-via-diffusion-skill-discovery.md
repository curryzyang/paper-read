# DSD: Learning Diverse and Reusable Motor Skills via Diffusion Skill Discovery

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Sun Woo Kim, Xue Bin Peng
- 机构：Simon Fraser University, NVIDIA
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17682v1) · [PDF](https://arxiv.org/pdf/2609.17682v1)

## TLDR
DSD is a diffusion-based skill discovery method that approximates the state-entropy gradient via score matching to learn a broader repertoire of diverse, reusable motor skills for high-dimensional humanoid control, enabling effective downstream reuse through hierarchical control and zero-shot latent selection.

## Abstract
Humans efficiently learn new tasks by reusing a rich repertoire of motor skills across different goals and contexts. A similar strategy can also be used to enable simulated characters to efficiently perform new tasks by leveraging reusable motor skills. To support a wide range of downstream tasks, the learned repertoire should be diverse, consisting of distinct behaviors as well as spatial and temporal variation within each behavior. A commonly used method for learning diverse skills is by maximizing the mutual information between skill latents and the states produced by a policy. The marginal state entropy promotes broad behavioral coverage, while the conditional entropy encourages consistent behaviors from each latent. However, directly estimating the marginal state entropy is intractable in high-dimensional control problems. Prior methods therefore rely on indirect latent-space approximations or coarse estimators of the state distribution. These approximations may not effectively promote broad coverage of the state space, resulting in skills with limited behavioral diversity and reduced utility for downstream tasks. In this work, we propose Diffusion Skill Discovery (DSD), a skill discovery method that uses a diffusion model to approximate the entropy gradient of the policy-induced state distribution through score matching. The resulting objective encourages the discovery of skills that produce a broader range of behaviors for high-dimensional humanoid control. The learned skills are reused in two downstream control settings: hierarchical control with a task-specific high-level policy and zero-shot control through latent selection from offline trajectories. Our experiments show that DSD discovers a broader repertoire of reusable motor skills than prior skill discovery methods, leading to the emergence of complex and agile behaviors that can be reused across downstream tasks.


## 精读解读（中文）
### 一、研究动机
模拟人形角色若要像人类一样高效完成新任务，就需要一个可复用的多样化运动技能库，而非针对每个任务从零训练。主流方法通过学习技能隐变量与状态之间的互信息来获得多样化技能，但其中最大化策略诱导状态分布边缘熵的一项在高维人形控制中不可解。现有工作因此退而使用潜空间变分近似或粒子最近邻、技能条件动力学等粗糙估计器，这些近似无法有效促进状态空间的广泛覆盖，学到的技能往往只是同一行为的微小变体，功能多样性有限、下游可用性差。

### 二、技术方案（Method）
DSD 训练一个以技能隐变量 z 为条件的低层策略 π(a|s,z)，并让扩散模型 ε_θ 与策略在 rollout 状态上联合训练，通过去噪分数匹配（DDPM/SDS 式的加权噪声预测目标）在线逼近策略诱导状态分布的熵梯度，再把该梯度转化为内在奖励，激励策略访问更广泛的新颖状态。为把行为组织成可区分的技能，方法引入技能编码器 q(z|s) 构造互信息目标，使不同隐变量产生不同行为；同时用 GAN 式判别器（动作先验）鼓励动作接近参考动作分布，三部分奖励合成后用于策略的强化学习优化。训练完成后技能库以两种方式复用：一是分层控制，由任务特定的高层策略输出隐变量驱动冻结的低层策略；二是零样本控制，从离线轨迹中依据适应度函数 F 选择最优隐变量 z*，无需任何再训练。

### 三、结果（Result）
在多个运动数据集上的实验表明，DSD 学到的技能库比先前技能发现方法覆盖更广的行为范围，能够涌现出复杂且敏捷的运动（如行走、跑跳、击打等行为及其空间与时间变体），并捕捉到同一技能内部的变化。在分层控制和零样本隐变量选择两类下游控制设定中，复用该技能库均取得更好表现，验证了更宽的状态分布覆盖确实转化为更强的下游任务效用。

### 四、结论（Conclusion）
研究表明，用扩散模型近似策略诱导状态分布的熵梯度，是替代不可解边缘熵估计、提升高维人形控制技能多样性的可行途径。DSD 是首个面向物理仿真人形、以扩散模型近似状态熵梯度的无监督技能发现框架，学到的多样化技能库可同时支持基于高层策略的分层控制与无需训练的零样本潜在选择。

### 五、方法论与关键技术细节
数据侧使用无标注的参考运动数据集，扩散模型在策略 rollout 产生的状态上在线联合训练，目标为分数匹配加权的噪声预测损失 w(k)‖ε_θ(x^k)−ε‖²，其梯度充当状态熵最大化的替代信号；技能一致性由隐变量条件编码器 q 的互信息项保证，运动自然性由 GAN 式判别器（类似 AMP 的动作先验）保证；论文针对高维人形控制提出了一系列实践性设计以提高训练稳定性与运动质量，并隐含了扩散模型评估的额外计算开销；下游复用分为高层策略分层控制与离线轨迹零样本隐变量选择两条路径；主要局限在于依赖参考动作分布作为先验、且熵梯度估计在高维状态下的可靠性仍是关键约束，具体超参与复杂度指标未在摘要层面给出。
