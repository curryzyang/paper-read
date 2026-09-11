# From Connectivity to Rewards: Dense Reward Learning with Directed State Graphs

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Shuyuan Zhang, Zihan Wang, Xiao-Wen Chang, Doina Precup
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10781v1) · [PDF](https://arxiv.org/pdf/2609.10781v1)

## TLDR
G2QDR learns pairwise state-connectivity strengths from a directed state graph and converts them into dense auxiliary rewards to improve Goal-Conditioned Hierarchical Reinforcement Learning in sparse-reward, asymmetric quasimetric environments.

## Abstract
The integration of graphs with Goal-Conditioned Hierarchical Reinforcement Learning (GCHRL) has received increasing attention, as graphs naturally encode task hierarchies for effective subgoal sampling. However, existing methods often overlook intrinsic connectivity information, failing to fully leverage the underlying topology for efficient learning. Most graph-based GCHRL methods use the graph as a stochastic sampling tool rather than as an environmental model that encodes connectivity and state-accessibility information. This limitation is particularly acute in quasimetric environments, where the inherent asymmetry of state transitions poses a fundamental challenge to stable policy learning and robust path planning. In this paper, we address these problems by introducing a state connectivity model designed to predict pairwise state connectivity strength in asymmetric environments. We transform these connectivity strengths into scalar auxiliary dense rewards, providing continuous guidance across multiple hierarchical levels. We demonstrate that our proposed framework, Graph-Guided Quasimetric Dense Reward (G2QDR), can theoretically be integrated into any existing GCHRL architecture, and the state connectivity model is efficiently implemented via a neural network trained on a directed state graph generated during exploration. Empirical results across a wide range of sparse reward environments indicate that, in general, G2QDR can enhance the performance of baseline GCHRL approaches with acceptable computational overhead.


## 精读解读（中文）
### 一、研究动机
现有将图与目标条件分层强化学习结合的方法多把图当作随机子目标采样工具，而未充分利用图中蕴含的状态连通性与可达性拓扑信息，尤其在准度量环境中状态转移天然不对称，会显著影响策略学习的稳定性和路径规划的鲁棒性。因此，作者希望把探索中形成的图从采样器提升为可编码环境连通结构的状态连通模型，并用其生成稠密奖励来缓解稀疏奖励与不对称转移带来的学习困难。

### 二、技术方案（Method）
G2QDR的核心方案是在探索过程中构建有向状态图，并训练一个神经网络来预测任意状态对之间的连通强度，从而在非对称/准度量环境中建模状态可达性。随后把预测出的成对连通强度转化为标量辅助稠密奖励，在多个分层层级上为GCHRL提供连续引导。该框架理论上可作为插件集成到任意现有GCHRL架构中，训练数据来自探索阶段生成的有向状态图，推理/训练时用连通模型输出辅助奖励并叠加到原有目标条件分层强化学习流程中。

### 三、结果（Result）
在多种稀疏奖励环境中，G2QDR总体上能够提升基线GCHRL方法的性能，同时仅带来可接受的计算开销。摘要还指出该框架具有理论上的通用集成性，可与任何现有GCHRL架构结合，但未给出具体数值指标或逐环境对比结果。

### 四、结论（Conclusion）
G2QDR通过有向状态图和连通强度预测，把图结构从随机采样工具转变为编码环境连通性的模型，并用准度量稠密奖励改善稀疏奖励和非对称转移下的分层强化学习。其价值在于通用、可插拔且计算开销可接受，但实际效果会受探索图覆盖度、连通模型近似精度和辅助奖励权重设计影响。

### 五、方法论与关键技术细节
关键实现细节包括：使用探索中生成的有向状态图作为训练数据；用神经网络学习成对状态连通强度；将连通强度转为标量辅助稠密奖励并注入分层GCHRL的多个层级；框架设计为与任意GCHRL兼容。摘要未提供具体网络结构、损失函数、超参数、奖励缩放系数与复杂度量级，复现时需查阅正文；潜在局限是图覆盖不足或连通预测偏差可能削弱引导效果，且额外模型会带来非零计算开销。
