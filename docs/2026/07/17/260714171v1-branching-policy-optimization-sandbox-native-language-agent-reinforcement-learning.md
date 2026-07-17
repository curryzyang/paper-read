# Branching Policy Optimization: Sandbox-Native Language Agent Reinforcement Learning

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Bowei He, Yankai Chen, Xiaokun Zhang, Xue Liu
- 机构：City University of Hong Kong, McGill Univeristy, Mohamed bin Zayed University of Artificial Intelligence
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14171v1) · [PDF](https://arxiv.org/pdf/2607.14171v1)

## TLDR
Branching Policy Optimization (BPO) is a sandbox-native reinforcement learning algorithm that leverages the deterministic, snapshottable properties of agent environments to construct a tree of rollouts with shared prefixes, yielding unbiased, lower-variance advantage estimates that improve training efficiency and success rates on benchmarks like WebShop, ALFWorld, and SWE-bench.

## Abstract
Reinforcement learning has emerged as the dominant paradigm for training large language model (LLM) agents that interact with executable sandboxes. State-of-the-art algorithms such as PPO, RLOO, and GRPO inherit their rollout topology from RLHF: for each prompt, N independent trajectories are sampled from the initial state, and an advantage is computed by subtracting a group baseline. This design ignores a defining property of agent sandboxes. They are deterministic, snapshottable, and resumable from any intermediate state. We argue that this property enables a fundamentally different rollout topology: rather than N independent trees of depth T, one can construct a single tree of N leaves whose siblings share prefixes, and therefore share variance. We instantiate this idea as Branching Policy Optimization (BPO), a sandbox-native RL algorithm that (i) adaptively snapshots the sandbox at high-entropy decision points along a backbone trajectory, (ii) forks K alternative actions per branch point and rolls out each to termination, and (iii) computes per-step advantages from sibling returns rather than from independent prompts. We prove this estimator is unbiased and has strictly lower variance than the trajectory-level baseline, with the reduction equal to the prefix-explained portion of return variance. On WebShop, ALFWorld, and SWE-bench Verified with Qwen2.5-7B and Llama-3.1-8B backbones, BPO improves success by 3.6--6.1 absolute points over GRPO and RLOO at matched compute, halves gradient-norm variance, and matches the best baseline using 38% fewer policy updates.


## 精读解读（中文）
### 一、研究动机
现有的强化学习算法如PPO、RLOO和GRPO在训练语言智能体时，继承自RLHF的独立轨迹采样拓扑结构，忽略了沙盒环境具有确定性、可快照和从任意中间状态恢复的关键属性。这种设计导致优势估计方差主要由仅条件于初始状态的回报方差主导，对于长程智能体任务而言方差过大，限制了学习效率和效果。

### 二、技术方案（Method）
BPO算法首先为每个提示从策略采样一条主干轨迹；然后依据每一步的熵值选择M个决策点作为分支点，在每个分支点对沙盒进行快照并分叉出K个替代动作，每个分叉展开到终止，构建一棵总节点数为N（K×M）的轨迹树；接着在分支点处使用留一兄弟基线计算局部优势，并通过折扣因子λ=0.95沿共享前缀向前传播；最后使用标准PPO-clip目标函数优化策略，并包含KL正则项。训练过程中不依赖值函数，分支预算由熵驱动调度器分配并限制最小间距64步以避免聚集。

### 三、结果（Result）
在WebShop、ALFWorld和SWE-bench Verified基准上，使用Qwen2.5-7B和Llama-3.1-8B骨干网络，BPO在等计算量下比GRPO和RLOO绝对提升3.6–6.1个成功率百分点；梯度范数方差减半；以38%更少的策略更新步数即可达到最佳基线同等性能。

### 四、结论（Conclusion）
通过利用沙盒的快照-恢复原语构建轨迹树并引入兄弟基线优势估计，BPO实现了比独立轨迹基线显著更低的方差，且在多个智能体任务上取得一致改进，证明了沙盒原生RL算法在减少方差和提升样本效率方面的有效性，为训练语言智能体提供了新范式。

### 五、方法论与关键技术细节
关键方法细节包括：(1) 分支点选择基于当前策略的熵值，避免使用值函数置信度，以保证不依赖值网络；(2) 每个分支点分叉K个动作，K和分支点数量M是超参数，总样本N=K×M与GRPO匹配；(3) 沙盒快照操作假设具有保真性（Assumption 1），快照开销远小于完整展开，且在实际沙盒（如Docker、解释器）中可行；(4) 优势估计理论证明无偏且方差严格小于轨迹级基线，方差缩减量等于由前缀解释的回报方差部分（Theorem 2）；(5) 折扣因子λ=0.95控制下游信号对上游的传播强度，熵分支调度设有最小间距64步以避免聚集；(6) 局限：可能受限于非确定性沙盒或快照开销过大的环境。
