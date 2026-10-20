# Web Agent Agentic Reinforcement Learning Decision Model Under Multi-Cost and Failure Risk

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Qianli Ma, Limengxi Yue, Shuyang Xu, Yanpei Shi, Hongrui Liu
- 机构：University of Massachusetts Amherst, Cornell University, University of Michigan – Ann Arbor, University of Massachusetts Boston, University of Southern California
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23857v1) · [PDF](https://arxiv.org/pdf/2610.23857v1)

## TLDR
The paper proposes a constrained agentic reinforcement learning model for web agents that integrates multi-dimensional request, latency, and failure costs with Lagrangian budget enforcement and CVaR tail-risk control, achieving a better balance among task completion, cost, and failure risk and empirically reducing cost-per-success and failure rates while improving completion under fixed budgets.

## Abstract
Intelligent agent interactions in real-world web environments are commonly constrained by request budgets, time delays, anti-crawling restrictions, and operational failure risks. Strategies solely optimizing task success rates often exhibit unusable phenomena such as "high success but high cost" or "low risk but conservative failure." This paper proposes a constrained agentic reinforcement learning model for web agents, unifying page access, search requests, and external API calls into a unified long-term decision-making framework with associated costs. It simultaneously incorporates cost budget constraints and tail risk control into the optimization objective: constructing a multidimensional cost vector comprising cumulative request count, total latency, and failure penalties to achieve budget compliance via Lagrange dual updates, while employing a CVaR risk term to suppress excessive exploration of high-failure-probability paths, thereby achieving an adaptive balance among "completion rate, cost, and risk."
  Experiments were conducted across 30-70 site/page templates and 800-1,500 end-to-end web tasks, including information extraction, price comparison, form submission, and cross-page navigation. Interaction sequences spanned 20-120 steps with tool scales of 30-200. Performance was benchmarked against unconstrained RL, budget-constrained RL, and rule-based/scripted web agents, quantifying task completion rates, cost-per-success, failure rates, and policy stability.
  Results demonstrate that at equivalent completion rates, our method reduces C-PS by 22%-31% and lowers failure rates by 18%-26% under high failure penalties. Under fixed budgets, task completion rates increase by 10%-16%, highlighting the necessity and effectiveness of constraint modeling for practical web agent deployment.


## 精读解读（中文）
### 一、研究动机
真实Web环境中的智能体常受请求预算、响应延迟、反爬限制和操作失败风险约束，仅优化任务成功率的策略容易出现高成功但高成本或低风险但保守失败的两极问题。论文旨在把完成率、成本与风险纳入统一决策目标，使Web Agent能够在实际预算和失败惩罚下稳定部署。

### 二、技术方案（Method）
将Web任务建模为带多维成本的约束马尔可夫决策过程，状态由页面DOM特征、历史动作嵌入和工具冷却向量组成，动作覆盖DOM操作、搜索请求、外部API调用与导航，成本向量包含累计请求数、总延迟和失败惩罚。用Lagrange对偶更新约束乘子以逼近请求数、延迟和失败成本预算，并引入CVaR尾部风险项及辅助变量η实现可微优化，形成奖励减去拉格朗日成本惩罚再减去风险惩罚的联合目标。策略网络采用参数共享双通道Actor-Critic，策略分支输出动作分布，价值分支估计成本加权Q值；训练中使用经验回放、Adam优化和软更新，推理时按约束策略选择动作并在预算与风险边界内完成长程交互。

### 三、结果（Result）
在30—70个站点/页面模板、800—1500个端到端任务、20—120步交互和30—200个工具的设定下，与无约束RL、仅预算约束RL及规则/脚本Web Agent对比，所提方法在同等完成率下将每次成功成本C-PS降低22%—31%，在高失败惩罚下将失败率降低18%—26%。固定预算下任务完成率提升10%—16%；表中完成率由无约束的72.30%提升到仅预算约束的74.80%、预算加失败风险约束的77.10%和CVaR约束的80.50%，C-PS由0.45降至0.32，失败率由18.20%降至12.50%。这些结果说明多维成本与尾部风险约束能同时改善成本效率和风险控制，并保持策略稳定性。

### 四、结论（Conclusion）
多成本与失败风险约束建模能够缓解传统RL在Web Agent高成本、高失败率任务中的不可部署问题，通过Lagrange预算控制和CVaR风险抑制实现完成率、资源成本与失败风险的自适应平衡。该框架在异构任务和页面模板上表现出较强泛化与稳定性，为真实Web场景的高维长程交互提供了约束感知的决策路径。局限在于稀疏奖励或超长路径任务下策略收敛较慢且风险估计存在偏差，未来可结合分层规划和动态风险调节改进。

### 五、方法论与关键技术细节
关键实现包括请求数、延迟和失败惩罚三类成本约束，训练设置给出请求上限b1=12、平均延迟上限b2=600ms、失败成本上限b3=0.3，而实验部分又报告35次请求、600ms平均延迟和7.0失败惩罚的上限，说明预算参数存在多组设定。CVaR使用风险置信水平约0.8—0.95、实验风险阈值α=0.1和0.2、风险抑制系数μ约0.1—1.0，成本与风险控制系数λ_c约0.1—1.5、β约0.1—1.0；状态维度配置为DOM特征128、历史动作嵌入64、工具冷却32，总状态维度120—320，折扣因子0.98，回放容量约10^5、批大小64、Adam学习率约3e-5、软更新系数0.005。损失由期望奖励、各成本约束的拉格朗日惩罚和CVaR风险项组成，每次交互采集请求数、响应延迟和失败标签以构造累计成本向量。局限是约束乘子和风险系数需调参，CVaR与拉格朗日耦合增加训练复杂度，且在稀疏奖励和超长路径上收敛与风险估计仍不稳定。
