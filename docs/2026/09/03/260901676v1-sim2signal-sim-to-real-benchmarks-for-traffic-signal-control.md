# Sim2Signal: Sim-to-Real Benchmarks for Traffic Signal Control

- 区域：精读区
- 排名：4
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Ferdous Al Rafi, Susrik Mukherjee, Latika Liladhar Dekate, Jennifer Yawa Lavoe, Huaiyuan Yao, Shlok Mohanty, Longchao Da, Xuesong Zhou, Hua Wei
- 机构：Arizona State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01676v1) · [PDF](https://arxiv.org/pdf/2609.01676v1)

## TLDR
Sim2Signal is a benchmark that systematically decomposes the sim-to-real gap in traffic signal control into observation, action, transition, and reward gaps, and its evaluation of 18 mitigation methods shows that no single method reliably closes these gaps—except for the action gap—and that the most effective approaches work by estimating what the gap changes rather than making policies insensitive to it.

## Abstract
Reinforcement learning achieves strong traffic signal control performance in simulation, yet policies trained in simulators often fail once deployed in the real world, a failure known as the Sim-to-Real gap. When RL is applied to traffic signal control, this gap arises from several sources: sensing, action execution, traffic dynamics, and the control objective. Their relative impact and the reliability of existing Sim-to-Real mitigation methods remain insufficiently understood, and the field lacks a standard benchmark for systematically measuring the gap and evaluating mitigation methods. We present Sim2Signal, a benchmark that decomposes the Sim-to-Real gap into observation, action, transition, and reward gaps, corresponding to mismatches in the four components of the underlying MDP, and induces each gap in isolation under a shared protocol. We evaluate 18 mitigation methods on 2 base controllers, across 33 gap settings and 10 calibrated networks built from 5 real-world locations. We find that direct transfer consistently degrades performance across all four gap sources, but the severity of the degradation does not predict the effectiveness of mitigation. Instead, mitigation effectiveness depends strongly on the network and gap setting: outside the action gap, a method that helps in one case may fail in another. The most effective methods generally estimate what the gap changes, rather than make the policy insensitive through domain randomization or invariant representations. Our code is available at https://github.com/Red-Pheonix/Sim2RealTSCBenchMark


## 精读解读（中文）
### 一、研究动机
强化学习在交通信号控制模拟中表现优异，但策略部署到真实世界时常因Sim-to-Real gap而失效，且该gap源自观测、动作执行、交通动态和控制目标等多个环节。领域缺乏统一基准来分解并量化这些gap源，也缺少在共享协议下系统比较缓解方法的平台，导致各来源的相对影响和现有Sim-to-Real方法在不同设定下的可靠性仍不清楚。

### 二、技术方案（Method）
Sim2Signal基于sim2sim协议，将Sim-to-Real gap按MDP四要素分解为observation、action、transition和reward四种gap：在不改变路网与需求的前提下，以第二个受控环境扮演E_real，并在E_sim/E_real校准到ATT和吞吐量匹配后单独注入每种gap。基准使用DQN与PressLight两种基座控制器，覆盖5个真实地点的10个校准路网（含Tempe和Bullhead两个新NEMA数据），共33个gap settings，并统一遵循pretrain-train-deploy流程：所有缓解方法从同一预训练checkpoint出发，最多300 episode、其中至多100 episode在E_real中执行。主要指标是平均旅行时间ATT，用Δ=m_real-m_sim量化性能下降；reward gap下因真实奖励无法在E_sim计算，改为计算相对真实奖励oracle的regret。缓解方法按gap族组织：观测gap包括域随机化、潜在空间域自适应（LUSR/DARLA/ATC/VAE）和重建方法；动作延迟gap包括Delayed-Q、PRLight及其消融；动作相变gap在NEMA路网上测试规则约束恢复；transition和reward gap则使用对应估计量或oracle式方法，以Direct-Transfer作为无缓解基线。

### 三、结果（Result）
直接迁移（Direct-Transfer）在全部四类gap源下都稳定造成性能下降，但gap造成的退化幅度并不能预测缓解方法能恢复多少。动作gap上有相对跨网络和设置稳健的方法；其余三类gap中，方法有效性高度依赖路网与具体gap设置，同一方法在一种情况下有效、在另一种情况下可能失败，甚至所有缓解方法都不如不做缓解。最有效的缓解方法通常显式估计gap改变的量（如预测动作延迟后策略实际到达的状态、从噪声传感器估计真实车辆数），而不是通过域随机化或不变表征使策略对gap不敏感。

### 四、结论（Conclusion）
Sim2Signal说明Sim-to-Real缺口不能作为单一问题对待，需要按观测、动作、transition和reward四类来源分别测量与评估；缓解方法的选择应结合具体gap和路网进行，不能依赖“退化越严重则某种缓解越有效”的假设。该基准提供了可复现的共享协议、校准路网和18种方法的系统对比，为研究社区提供了一个比较Sim-to-Real缓解方法的标准平台，也为交通信号控制真实部署时选择可靠策略提供了依据。

### 五、方法论与关键技术细节
观测gap的具体设置包括高斯噪声σ∈{3,5,10,20}、每车道检测器故障概率∈{0.05,0.2,0.5,0.7}、检测区长度∈{10,20,50,100}米以及C1-C4组合；动作延迟gap设置20、30、40、60秒固定延迟，而缓解方法只假设20秒，从而同时检验延迟低估；动作相变gap只在带NEMA双环相位配置的Tempe和Bullhead路网上施加，包括Flexible、Barrier若干变体和Cyclic等规则。E_sim与E_real在注入gap前先校准到ATT和吞吐量残差范围内，因此后续Δ可归因于gap；所有方法共享预训练权重并受300 episode预算约束，reward oracle例外地直接在真实目标上训练且不受预算限制。该基准是sim2sim受控环境而非物理实地部署，且仅考虑车辆、未含行人；phase-transition类设置不适用于没有NEMA信号方案的路网。
