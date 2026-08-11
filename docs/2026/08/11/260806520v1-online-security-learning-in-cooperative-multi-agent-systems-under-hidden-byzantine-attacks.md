# Online Security Learning in Cooperative Multi-Agent Systems under Hidden Byzantine Attacks

- 区域：精读区
- 排名：5
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Ximing Sun, Yue Wang
- 机构：University of Central Florida
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06520v1) · [PDF](https://arxiv.org/pdf/2608.06520v1)

## TLDR
TLDR: This paper formalizes online security learning in cooperative multi-agent systems under hidden Byzantine action overwrites, showing that the attack’s information structure yields exact rectangular robust MDP formulations, that the security regret decomposes into return regret plus an unavoidable cumulative response gap, and that a stage-tied robust estimation-to-decisions algorithm achieves $\widetilde{O}(H^2 S \sqrt{AK}) + \mathbb{E}[D_K]$ security regret.

## Abstract
We study online cooperative control of a multi-agent system under Byzantine attacks. Namely, an unknown, fixed subset of agents are Byzantine comprised and can stealthily overwrite its own coordinates of the team's planned joint action after observing that plan. The learner observes planned actions, public rewards, and public states, but neither the overwrite nor the executed joint action. Our objective is security: to optimize the team performance against the worst overwrites and achieve the optimal security value. We first show that the attacker's information determines the geometry. An attacker that observes the planned action induces an exact $(s,a)$-rectangular robust Markov decision process (MDP) whose rows are convex hulls of overwrite-induced public-outcome laws, whereas a blind attacker induces an $s$-rectangular model. We then identify the information-theoretic limit of security learning, showing that the security regret decomposes exactly into return regret against the response generating the data and a cumulative response gap $D_K$. Two indistinguishable horizon-one instances force $Ω(K)$ expected security regret while return regret is zero, showing that dependence on $D_K$ is unavoidable. Finally, we develop a stage-tied robust estimation-to-decisions learner and prove a regret bound of $\widetilde{\mathcal O}\!\left(H^2S\sqrt{AK}\right)+\mathbb E[D_K]$. Our studies thus provide comprehensive theoretical and algorithmic foundations of reliable multi-agent systems under Byzantine attacks.


## 精读解读（中文）
### 一、研究动机
多智能体协同系统的价值依赖于每个智能体执行分配的动作，但部署中可能出现拜占庭故障：被入侵的智能体可能观察计划联合动作后静默覆盖自己的动作坐标，执行动作直接改变共享动态状态，传统过滤恶意消息的防御无法应对。现有工作缺乏在隐藏受损代理直接交互下的在线学习理解，因此本文研究如何在线学习最优安全策略以抵御最坏覆盖攻击。

### 二、技术方案（Method）
本文建立拜占庭团队MDP模型，其中未知固定子集B*为拜占庭代理，可观察计划联合动作并随机覆盖自身坐标。学习者仅观察计划动作、公共奖励和公共状态，不观察覆盖或执行动作。首先证明攻击者信息决定几何结构：知情攻击者诱导(s,a)-矩形鲁棒MDP，盲攻击者诱导s-矩形模型。随后将安全遗憾分解为返回遗憾与累积响应间隙D_K之和。最后基于鲁棒估计到决策框架设计阶段绑定学习器：每个阶段使用一个延续证书和一个占用校准见证，将累积估计预算从Õ(HS^2)降至Õ(HS)；在每个阶段，学习器基于历史数据构建置信集，调用近似决策oracle选择策略，并继续交互，无需估计拜占庭身份或覆盖动作。

### 三、结果（Result）
核心结果包括：安全遗憾逐路径地分解为返回遗憾与响应间隙D_K，且D_K非负；构造两个不可区分单阶段实例，使期望安全遗憾为Ω(K)而返回遗憾为零，证明依赖D_K不可避免；所提学习者达到期望返回遗憾Õ(H^2 S √(AK))，期望安全遗憾超过该值恰为期望响应间隙E[D_K]。与直接状态式构造相比，阶段绑定估计器带来√S的改进。

### 四、结论（Conclusion）
本文为拜占庭攻击下可靠多智能体系统提供了全面的理论和算法基础，揭示了公共反馈下安全学习的信息论极限，并给出了接近最优的安全遗憾界。研究显示，由于攻击者可自适应且身份隐藏，仅凭公共反馈无法完全消除响应间隙，但所设计的阶段绑定估计到决策学习器在无需识别受损代理的条件下实现了最优依赖K的遗憾。

### 五、方法论与关键技术细节
关键细节包括：模型假设无关于拜占庭类型或身份的先验；攻击者可在公共历史和计划动作上自适应随机化覆盖；证明确定性非平稳马尔可夫团队策略和确定性马尔可夫最坏响应足以达到最优安全值；阶段绑定估计器在标准近似决策oracle下使用每阶段一个延续证书和一个占用校准见证，累积估计预算为Õ(HS)；学习目标为最小化安全遗憾，安全遗憾界为Õ(H^2 S √(AK)) + E[D_K]，其中D_K为响应间隙；局限性在于安全学习者在公共反馈下无法识别实际最坏响应，响应间隙可能线性增长，因此安全遗憾的线性下界不可避免。
