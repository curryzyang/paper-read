# PF-Exec: Large-Scale UAV Relay Load Balancing with an Anchored Potential Direction Decider and a Per-Dimension Gain-Learning Executor

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Liheng Zeng, Hanzhang Jia, Yiran Li, Yi Gao, Bo Ma
- 机构：Zhejiang Gongshang University, University of Sussex, Shanghai Shuyuan Information Technology Co., Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17492v1) · [PDF](https://arxiv.org/pdf/2611.17492v1)

## TLDR
PF-Exec is a two-layer UAV relay load-balancing method that combines a closed-form anchored potential-direction decider with a per-dimension gain-learning executor to achieve scalable, robust fairness across large fleets and demanding crowd/load conditions.

## Abstract
Relay load balancing in large-scale UAV networks requires joint decisions on association, bandwidth, power and hovering position, while the dimension grows with the number of UAVs and each UAV sees only its local state. This paper splits the decision into two layers. An anchored potential direction decider emits a closed-form target at every instant and returns its direction only. A gain-learning executor maps a local observation into a positive gain per dimension, composes gain and target, and clips the action against the physical single-step bound; the two layers form PF-Exec. The unit gain is the default start, so the executor reduces to the pure potential policy before training. The load is first-order homogeneous in bandwidth, making the bandwidth target closed form, and the position target is the demand-weighted centroid of the served users. The system uses a two-hop access and millimetre-wave backhaul link with soft association, a 3GPP UMa-AV channel with two shadowing layers, an OU-type social-force crowd and a quadrotor physical layer. Evaluation spans all fleet sizes, two crowd scenarios, independent seeds, the published baselines in their own settings and a degraded-information line. In the highest-pressure burst setting the fixed-step comparison breaks down on part of the seeds, losing fairness and mean load at once, while PF-Exec holds fairness near one. Among the ten comparison methods only the greedy heuristic survives that setting; its load variance stays far higher. Under stale global state and position noise the fairness index stays high at both largest-scale scenarios. Flight energy is nearly identical between the learned and the fixed-step executor, and three constants are fixed once across all settings. The convergence properties of both layers, from the truncated gain iteration to the perturbed tracking bound, are proved in the companion analysis.


## 精读解读（中文）
### 一、研究动机
大规模无人机中继负载均衡需联合决定关联、带宽、功率和悬停位置，决策维度随无人机数量增长，且每架无人机只能看到局部状态；同时人群移动会造成负载严重偏斜，少数无人机过载而整体均值掩盖偏斜，且负载超过5意味着无法服务用户，因此平衡是独立的一等目标。现有集中式非凸重解随规模增长，端到端学习又缺乏可解释方向且中心评估成本随编队增长，系统需在线秒级运行并具备与编队规模无关的运行时保证。

### 二、技术方案（Method）
PF-Exec把决策拆成两层：锚定势方向决策器在每个时刻输出闭式目标并只返回方向，利用负载对带宽的一阶齐次性给出闭式带宽目标，利用位置目标可分离性给出被服务用户的需求加权质心位置目标；增益学习执行器把22维局部观测经投影残差块映射为五个逐维正增益，增益硬约束在[0.50,2.01]，用TD3训练，将增益与目标组合后按物理单步界裁剪动作。初始单位增益使执行器在训练前严格退化为纯势策略，因此学习只改进速度而不经过不安全中间策略。系统采用两跳接入与毫米波回传、阻尼softmax软关联、3GPP UMa-AV信道与双层阴影、OU型社会力人群和四旋翼物理层；环境步长0.1 s、回合2000步，评估扩展到4000步。

### 三、结果（Result）
在最高压力突发设置中，固定步长对比方法在部分随机种子上失效，同时损失公平性和平均负载，而PF-Exec把Jain公平指数保持在接近1；十种对比方法中仅贪心启发式在该设置下存活，但其负载方差仍远高于PF-Exec。在过期全局状态和位置噪声下，两个最大规模场景的公平指数仍保持较高。学习执行器与固定步长执行器的飞行能耗几乎相同，且三个常数在所有设置中固定一次；评估覆盖3、12、30、60、100架无人机、flow与burst场景、三个种子、十种比较方法、四种已发表基线原生设置及信息退化线，共602次运行。

### 四、结论（Conclusion）
论文表明可将负载均衡中的闭式势方向与学习到的逐维速度分离：方向由锚定势闭式给出，执行器仅学习每维增益，从而在保持可解释性和安全初始化的同时提升高压力下的公平性与鲁棒性。该方法以局部观测和逐无人机小网络实现在线运行，运行时保证不随编队规模增长，且不带来额外飞行能耗；收敛性由伴随分析中的截断增益迭代和扰动跟踪界证明，本文侧重行为测量。

### 五、方法论与关键技术细节
负载在接入受限区对带宽一阶齐次，需求尺度c_i=u_i b_i相对带宽漂移约1e-16，带宽目标为需求尺度除以负载锚点；方向势采用对数拐点视图的等权完全图势，保持全负载域排序并在深度过载时梯度严格为正，价格信号通过被视负载差分的次梯度一步更新。关联阻尼softmax取τ_u=5、α=1.0、κ=0.5、ε=0.1，功率24 dBm且乘子[0.5,2]，带宽预算B且单机下限1e-3；回传28 GHz、100 MHz、43 dBm，接入2 GHz、高度50 m，路损离线10 m网格烘焙，运行时阴影标准差每回合从[0,13.2] dB抽取并每100步刷新。执行器输入22维局部观测、输出5个正增益，硬界[0.50,2.01]，TD3训练，单位增益初始化等价纯势策略；局限性包括收敛依赖增益界与截断而非谱证书，伴随分析报告60/60个实测状态的谱充分条件失败，且策略仅依赖局部状态。
