# EvoAD: Self-Evolving Autonomous Driving via Latent World-Model Guided Post-hoc Reflection

- 区域：精读区
- 排名：1
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Junjie Yang, Qiming Zhang, Yuyan Li, Shuqi Shen, Yusong Huang, Yanggang Sheng, Wenpeng Xu, Ziyi Shi, Tianshun Li, Yijie Chen, Yujia Wang, Jun Ma, Xinhu Zheng, Hongliang Lu, Hai Yang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23886v1) · [PDF](https://arxiv.org/pdf/2610.23886v1)

## TLDR
EvoAD enables post-deployment self-evolution of autonomous driving policies by storing BEV driving experiences, retrieving similar precedents, and using a latent world model to reflect on executed trajectories and refine future decisions without retraining, achieving state-of-the-art results on NAVSIM.

## Abstract
End-to-end autonomous driving systems have achieved rapid progress by learning unified policies that map sensor observations directly to driving trajectories. However, once deployed, these systems typically remain frozen: they may repeat similar decisions in similar scenes, and failures can only be addressed through costly data collection and retraining. This sharply contrasts with human drivers, who improve lifelong through experience, memory, and reflection. In this work, we ask whether autonomous driving systems can achieve similar post-deployment self-evolution to human drivers. We propose EvoAD, a self-evolving autonomous driving framework via latent world-model guided post-hoc reflection. EvoAD stores driving experiences in a bird's-eye-view feature memory pool, retrieves scene-relevant precedents according to geometric and semantic similarity, and uses a latent world model to evaluate the future consequences of candidate trajectories in a compact planning-oriented space. Instead of treating memory as external textual contexts or using world models only for pre-action simulation, EvoAD transforms executed driving outcomes into reusable improvement signals for future decisions. This enables the system to diagnose how prior trajectories could have been improved and to refine behavior in similar future scenarios without retraining the base driving policy. Experiments on NAVSIM v1 and v2 show consistent improvements across reflection rounds and state-of-the-art performance, demonstrating the potential of world models as reflective mechanisms for post-deployment self-evolution in autonomous driving.


## 精读解读（中文）
### 一、研究动机
端到端自动驾驶策略部署后通常保持冻结，容易在相似场景重复相似决策，失败只能依赖昂贵的数据采集与重训练来修正，缺乏人类驾驶员通过经验、记忆和反思实现终身改进的能力。论文因此提出后部署自演化问题：能否在不重训练基础驾驶策略的前提下，让系统利用已执行经验持续诊断并改进未来决策。

### 二、技术方案（Method）
EvoAD将驾驶经验存入鸟瞰图特征记忆池，依据几何与语义相似度检索与当前场景相关的前例，并利用潜在世界模型在面向规划的紧凑空间中评估候选轨迹的未来后果。系统把已执行驾驶结果转化为可复用的改进信号，通过事后反思诊断先前轨迹可改进之处，并在相似未来场景中细化行为；基础驾驶策略保持冻结，不进行重训练。

### 三、结果（Result）
在NAVSIM v1和v2上的实验显示，EvoAD随反思轮次增加取得一致性能提升，并达到当前最优性能。结果支持将世界模型作为反思机制，使端到端自动驾驶系统在部署后利用经验记忆实现自演化，而无需重新训练基础策略。

### 四、结论（Conclusion）
EvoAD表明，基于潜在世界模型引导的事后反思与BEV经验记忆，可以为自动驾驶系统提供部署后的持续改进路径。其核心价值在于把记忆从外部文本上下文转变为可复用改进信号，并把世界模型从仅用于行动前模拟扩展为行动后反思与策略细化机制。

### 五、方法论与关键技术细节
关键实现包括BEV特征记忆池、基于几何与语义相似度的场景前例检索、规划导向紧凑空间中的潜在世界模型后果评估，以及将执行结果回写为反思信号的事后改进闭环；基础策略冻结以控制部署后更新成本。局限在于摘要未给出记忆容量、检索阈值、世界模型训练细节、反思轮次与具体指标数值，且验证局限于NAVSIM v1/v2，真实部署中的记忆漂移、世界模型偏差与在线安全约束仍需进一步评估。
