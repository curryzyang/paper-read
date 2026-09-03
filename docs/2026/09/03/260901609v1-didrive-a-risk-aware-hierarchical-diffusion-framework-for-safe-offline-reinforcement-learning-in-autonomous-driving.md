# DiDrive: A Risk-Aware Hierarchical Diffusion Framework for Safe Offline Reinforcement Learning in Autonomous Driving

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Qisong Guo, Jingtang Chen, Zhilin Chen, Pei Xu, Mingjian Fu, Wenxi Liu, Yuanlong Yu
- 机构：Fuzhou University, Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01609v1) · [PDF](https://arxiv.org/pdf/2609.01609v1)

## TLDR
DiDrive introduces a risk-aware hierarchical diffusion framework for safe offline reinforcement learning in autonomous driving, combining a Risk-Aware Hierarchical Diffusion architecture and 3DICE policy optimization to reduce distribution shift, OOD actions, and heavy-tailed risks, achieving superior success rates and rewards in complex CARLA traffic scenarios.

## Abstract
While diffusion models effectively capture multimodal behavioral priors for autonomous driving, offline reinforcement learning (RL) policies remain susceptible to distribution shift, heavy-tailed risk signals, out-of-distribution (OOD) action generation, and high-dimensional state redundancy. To address these challenges, we propose DiDrive, a distribution-guided offline diffusion framework featuring two synergistic components: the Risk-Aware Hierarchical Diffusion (RHDif) architecture and the 3DICE policy optimization paradigm. In the state space, RHDif utilizes a low-level risk-gated encoder and a high-level contextual modulator to filter environmental redundancy and focus on safety-critical threats. In the action space, 3DICE mitigates OOD overestimation and gradient oscillation through in-sample calibrated guidance, spatiotemporal optimization, and ensemble-based candidate ranking. Evaluations on the CARLA benchmark demonstrate DiDrive's superiority over baselines like IQL, CQL, and Diffusion-QL, particularly in complex, high-density traffic scenarios with 60 vehicles, where it achieves an 85% success rate and a 4295.68 average reward, providing a robust pathway for safe autonomous driving decision-making.


## 精读解读（中文）
### 一、研究动机
自动驾驶中的离线强化学习面临分布偏移、重尾风险信号、OOD动作生成以及高维状态冗余等挑战。现有扩散模型虽能捕捉多模态行为先验，但在复杂交通场景中易受噪声干扰，生成危险或分布外动作；而传统策略约束和价值正则化方法受限于单峰高斯假设，难以刻画驾驶行为的多模态性。此外，高维状态输入中的冗余环境信息会掩盖局部风险，误导动作生成。因此需要一种能同时实现风险感知状态表征与支持集内稳定策略优化的离线扩散框架。

### 二、技术方案（Method）
提出DiDrive框架，包含两个协同组件：风险感知分层扩散（RHDif）架构和3DICE策略优化范式。在状态空间，RHDif采用低层风险门控时空编码器（RGSE）增强局部危险特征，并通过高层跨模态上下文调制器（CMCM）对齐全局语义、抑制背景冗余；融合后的特征作为联合条件注入反向去噪过程。在动作空间，3DICE构建表征-引导-优化-选择四阶段机制：先由RHDif构建风险过滤后的行为先验，再基于密度比w*(s,a)进行样本内校准引导，通过渐进参数整合（PPI）实现时空协同优化，最后采用集成候选排序筛选动作。训练时利用静态数据集，通过重尾奖励下的稳定性设计避免OOD过估计和梯度振荡。在CARLA基准上进行评估。

### 三、结果（Result）
在CARLA仿真基准上，DiDrive在不同交通密度下均优于IQL、CQL和Diffusion-QL等基线。特别在60辆背景车辆的高密度复杂场景中，DiDrive实现了85%的成功率和4295.68的平均奖励，同时在成功率、平均奖励和车道偏离指标上均表现更优，证明了其在复杂高密度交通场景下的鲁棒性和安全性。

### 四、结论（Conclusion）
DiDrive通过RHDif与3DICE的协同设计，有效解决了离线强化学习在自动驾驶中的分布偏移、OOD动作生成、重尾风险信号不稳定以及高维状态冗余等问题，为安全自动驾驶决策提供了可靠路径。其成功表明，风险感知的状态表征与支持集内约束的分布校正优化相结合，能够显著提升复杂交通环境下的决策安全性和任务性能。

### 五、方法论与关键技术细节
关键点包括：奖励函数综合速度保持、车道保持、平滑性、停止惩罚以及碰撞/偏离道路各-100的硬惩罚，从而自然形成重尾分布；3DICE使用密度比w*(s,a)=d*(s,a)/d^D(s,a)对行为策略进行样本内加权，目标策略表示为π*(a|s)∝w*(s,a)π^D(a|s)；RHDif采用RGSE进行自底向上的局部风险感知，CMCM进行自顶向下的上下文过滤，融合特征作为扩散模型的条件；利用样本内引导避免了显式查询OOD动作，PPI渐进参数整合增强训练稳定性，集成候选排序减少过估计。实验在CARLA模拟器中进行，高密度场景为60辆背景车辆。局限性可能包括依赖仿真环境，尚未在真实道路数据中验证，且扩散模型的采样计算开销需考虑。
