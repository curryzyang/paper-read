# Active Curriculum Refinement for Reinforcement Learning

- 区域：精读区
- 排名：2
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Zhenya Liu, Yuxin Chen
- 机构：The University of Chicago
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26469v1) · [PDF](https://arxiv.org/pdf/2608.26469v1)

## TLDR
PATH is a curriculum-learning framework that performs active learning over a directed acyclic curriculum graph by combining random path sampling for broad coverage with regret-driven allocation to unmastered regions, improving robustness and generalization in reinforcement learning.

## Abstract
In many reinforcement learning (RL) domains, environments are connected by prerequisite relations, such as difficulty-increasing edits or parameter increments, which induce a directed acyclic curriculum graph (DAG). Although this structure is often exploited only implicitly, explicitly modeling it can improve training. We introduce PATH, a curriculum-learning framework that performs active learning over the curriculum graph. PATH first expands coverage by sampling diverse curriculum paths and then reallocates training toward regions that remain unmastered. Experiments across diverse environments show that PATH explicitly leverages the graph structure to achieve strong robustness and generalization.


## 精读解读（中文）
### 一、研究动机
在众多强化学习场景中，环境实例间存在先决关系（如难度递进编辑或参数增量），可构成有向无环课程图DAG；现有方法往往仅隐式利用该结构。本文提出显式建模课程图并进行主动学习的框架，以解决如何用少量课程路径高效掌握整个可达环境空间的问题。

### 二、技术方案（Method）
PATH以课程DAG为输入，节点为环境实例、边为先决关系；维护N个路径指针构成的动态缓冲区B。第一阶段PATH:Random从源节点均匀采样完整路径，在每个当前环境上训练策略，当平均回合回报达到早停阈值eps_es则沿出边推进，达到采样耐心eps_p则终止并重新初始化路径。第二阶段PATH:Active用基于TD误差的positive value loss（PLR式S(theta)）作为后悔代理更新权重w(theta)，按权重采样训练，并在掌握节点后把多个后继指针插入缓冲区以扩张高学习潜力区域；同时以概率p注入随机源节点并驱逐低权重指针以保持缓冲区大小N。当终止路径数n达到T_switch后由随机阶段切换至主动阶段，从而完成从广泛覆盖到重点分配的课程训练。

### 三、结果（Result）
在MiniGrid离散控制与BipedalWalker连续控制等基准上，PATH相比已有课程学习与基于后悔的UED方法，显式利用课程DAG结构取得了显著更优的鲁棒性与泛化性能，能够更高效地覆盖并掌握可达环境空间。

### 四、结论（Conclusion）
显式将课程学习建模为课程DAG上的主动路径获取，能有效平衡探索与利用：先随机路径探索扩大覆盖面，再根据后悔信号重分配训练预算到未掌握区域。该框架验证了显式结构利用对提升RL泛化与鲁棒性的价值，并可用于带先决关系的结构化环境族。

### 五、方法论与关键技术细节
关键细节包括：早停阈值eps_es与采样耐心eps_p控制路径推进和终止，T_switch决定两阶段切换点；PATH:Active使用GAE的lambda/gamma计算TD误差序列，以正价值损失S(theta)作为后悔代理；缓冲区大小N、重放率p、低权重淘汰机制共同维持对高后悔区域的聚焦；算法无需显式枚举整张图，只要能从当前节点通过参数增量或局部编辑构造后继即可在线生成路径。当前局限是依赖显式或可构造的课程DAG，且超参数（尤其eps_es和eps_p）需要在不同任务上调整，论文通过附录敏感性分析说明其影响。
