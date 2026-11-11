# Branch-and-Commit for Frozen RL Agents: When and Where to Spend Test-Time Compute

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Sahar Admoni, Assaf Hallak, Yftah Ziser, Ofra Amir
- 机构：Technion, Israel Institute of Technology, Nvidia Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13003v1) · [PDF](https://arxiv.org/pdf/2611.13003v1)

## TLDR
This paper shows that for frozen RL agents, branch-and-commit—sampling multiple continuations, scoring them, and continuing from the selected branch—improves return mainly in high-dispersion states and largely by selecting among stochastic realizations of the same action, so test-time compute is best allocated to states predicted to have useful dispersion rather than uniformly.

## Abstract
Reinforcement learning agents are often deployed with policies that cannot be retrained or modified. In digital environments whose states can be copied and resumed, an operator has another option: sample several continuations from the current state, evaluate them, and continue from the endpoint of the selected branch. We call this procedure branch-and-commit. We study when it improves return, what produces the improvement, and where its computational budget should be spent. Across four environments, two frozen policies, five continuation verifiers, and a model-free selection rule, we find that the benefit of branching depends on dispersion: the difference between the best candidate return and the mean candidate return. Branching provides no benefit in low-dispersion settings, while increasing return by 12.8% in our main Craftax-Medium setting. Most of this gain comes not from selecting better actions, but from selecting among different stochastic realizations of the same action. Several competent verifiers achieve similar episode returns, suggesting that verifier quality is not the main constraint at our operating budget. Instead, computation is better allocated to states where useful dispersion is likely. On held-out seeds, gating branching using predicted dispersion retains 69% of the improvement from uniform branching while using 48% as many branching calls. These results characterize when branch-and-commit is useful and clarify what its gains represent.


## 精读解读（中文）
### 一、研究动机
部署后的强化学习策略常常被冻结、不可重训，但在状态可复制和恢复的数字环境中，操作者可以在测试时从当前状态采样多条延续、评估并择优提交。论文研究这种branch-and-commit何时提升回报、提升由什么产生，以及测试时算力应分配到哪些状态，并试图用候选回报的离散度解释其收益边界。

### 二、技术方案（Method）
在可复制状态的决策点，用冻结策略采样K条长度为H的候选轨迹并计算各自回报，再用延续验证器对候选打分并选择一条提交，随后从选中分支继续执行，整个过程不更新策略。实验覆盖Craftax-Symbolic的Medium、Easy、Hard，Asterix-MinAtar，以及XLand-MiniGrid的DoorKey-8x8和R9-19x19等环境、两种冻结策略和五类验证器（包括价值头、仅评论家、仅奖励的无模型选择规则和LLM选择等），并与无分支、随机选择等基线比较；对每个决策点记录离散度Δ(s)=最优候选回报减候选平均回报，按单元拟合ℓ_c≈β_{v,e}Δ_c，并进一步用预测离散度做门控，仅在可能产生有用离散度的状态执行分支。

### 三、结果（Result）
低离散度设置中分支没有收益，而在主设置Craftax-Medium中回报提升12.8%；大部分增益并非来自选择更好的动作，而是来自在同一动作的不同随机实现之间选择。多个有能力的验证器取得相近的回合回报，说明在当前操作预算下验证器质量不是主要约束；在留出种子上，用预测离散度门控分支保留了均匀分支69%的改进，同时只使用48%的分支调用。

### 四、结论（Conclusion）
Branch-and-commit的有效性主要取决于状态处候选回报的离散度，而不是普遍适用；测试时算力应优先投入可预测高离散度的状态。该结果澄清了分支收益的本质是测试时对随机性的重采样与选择，并为冻结策略部署提供了状态级的算力分配原则。

### 五、方法论与关键技术细节
关键实现包括候选分支长度约H=15到20步、从记录回报直接测量离散度、采用比例模型ℓ_c≈βΔ_c和顺序统计量启发κ(K)，其理论解释依赖选择非对抗以及分支回报近似可交换或高斯的假设，但零离散度处的点质量会违背高斯理想化。短回合环境存在奖励记账伪影：DoorKey回合约23步而H=15，需用alive-step掩码移除自动重置后的奖励，否则离散度会从约0.02被夸大到2.19；近零离散度时commit成本会使分支收益略负，过度分支在高触发率下可低于基线。LLM验证器只接收候选分支的自然语言渲染，不接收价值头、策略logits或符号状态向量，种子与超参在复现附录中给出。
