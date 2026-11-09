# Q-OIL: Optimistic Exploration in Learning from Human Interventions

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Pranav Teegavarapu, Sriyash Poddar, Rico Qi, Cleah Winston, Krisha Khandelwal, Aykut Onyol, Natasha Jaques, Abhishek Gupta
- 机构：Toyota Research Institute, University of Washington
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08576v1) · [PDF](https://arxiv.org/pdf/2611.08576v1)

## TLDR
TLDR: The paper shows that real humans intervene when robot progress stalls and give suboptimal corrections, then proposes Q-OIL, which treats interventions as optimistic exploration bonuses with decoupled critics to learn faster and more robustly from human interventions in simulation and on real robots.

## Abstract
As robots are deployed in the real world, they will inevitably make mistakes. Human interventions provide valuable feedback for improving their behavior, enabling them to adapt online to new scenarios. However, studying human-in-the-loop robot learning is difficult: real-world experiments are slow and expensive, so most algorithm development relies on simulated human models. We show that common human modeling assumptions do not match how real people intervene in practice. Through analyzing intervention data from human participants, we find that humans tend to intervene when agent progress stalls, and that their corrective actions are often suboptimal. Motivated by these findings, we introduce a progress-based model of human intervention that achieves higher rank correlation with real-user algorithm rankings, enabling realistic algorithm benchmarking and development in simulation. Building on these insights, we propose Q-OIL, a method that adds optimistic bonuses to intervention transitions in reinforcement learning and softly guides exploration toward human corrections. We find that decoupled critics are critical for stability because they prevent the bonuses from backing up to pre-intervention states. As a result, Q-OIL learns more efficiently than competitive baselines, achieving 10-50% higher success in simulation and on real robots, and improving pretrained VLAs on two bimanual manipulation tasks. As we ground both evaluation and algorithms in realistic human behavior, this work provides a practical path toward scalable robot learning from interventions.


## 精读解读（中文）
### 一、研究动机
真实机器人部署中不可避免会犯错，人类干预能提供有价值的在线反馈，但真实人类实验慢且昂贵，现有研究多依赖模拟人类模型；论文发现常见假设（如按即时次优触发干预、纠正接近最优）与真实干预数据不符，导致模拟评估和算法设计偏离真实用户表现，因此需要先理解人类何时、如何干预，再据此设计鲁棒的干预学习算法。

### 二、技术方案（Method）
论文先收集8名参与者、3个操作任务、24次运行约20万转移的真实干预数据，并用RLPD稀疏奖励训练参考策略和价值函数来分析干预触发与纠正质量，进而提出基于短时程进展的干预模型。Q-OIL在在线离策略强化学习中给干预转移加入乐观奖励/探索bonus，并采用解耦critic：乐观critic驱动探索与策略更新，仅任务critic提供TD目标，防止bonus回传到干预前状态；该方法不绑定具体离策略RL算法，并可扩展到改进预训练VLA策略。

### 三、结果（Result）
真实数据表明，人类干预触发是非马尔可夫的，更符合短时程进展停滞或价值下降，而非单步动作次优；人类纠正动作往往次优、噪声大，甚至偏离学习者策略。基于进展的模拟人类模型与真实用户算法排名的秩相关更高；Q-OIL在仿真和真实机器人上比竞争基线学习更高效，成功率提高10-50%，降低人类负担，并在两个双臂操作任务上改进预训练VLA，且对次优和多样干预保持稳健。

### 四、结论（Conclusion）
该工作主张把人类干预视为乐观探索引导而非最优监督目标，并用真实人类行为校准模拟评估与算法设计，从而缩小模拟到真实的差距，为可扩展的机器人从干预中学习提供实用路径。

### 五、方法论与关键技术细节
关键细节包括：干预模型由触发函数g和人类策略π_h组成，二者可依赖历史τ_{t-L:t}，并用k步价值进展V*(s_t)-V*(s_{t-k})刻画非马尔可夫触发，纠正以次优/噪声策略近似；Q-OIL的核心实现是干预转移上的乐观奖励和解耦critic，任务critic生成TD目标、乐观critic只用于探索与策略更新，以避免乐观项传播到非干预状态；数据来自带IRB批准的模拟机器人用户研究，参考π*、Q*、V*由RLPD稀疏奖励训练获得。局限在于真实实验仍慢且贵、人类模型只是近似，且具体损失权重与超参需参考原文，方法稳定性依赖解耦critic和对干预分布的合理处理。
