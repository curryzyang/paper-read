# Learning Implicit Causal World Models from Multi-Agent Demonstrations

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Jasorsi Ghosh
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26336v1) · [PDF](https://arxiv.org/pdf/2607.26336v1)

## TLDR
Implicit Causal World Models learn causal environmental dynamics from multi-agent demonstrations without pre-defined graphs by leveraging policy variance and the sequential backdoor condition to achieve interpretable representations.

## Abstract
In model-based reinforcement learning, world models exist as internal simulators, but their training often conflates statistical correlations with causal mechanisms. This problem is exacerbated in multi-agent systems where physical transitions are intertwined with strategic agent intents, causing world models to fail under distribution shift. We introduce Implicit Causal World Models to recover environmental dynamics from offline demonstrations without requiring pre-defined causal graphs. By incorporating policy variance, we render world models discoverable via the sequential backdoor condition. Evaluations across coordination tasks (Two-Door, Navigation, and Giveway) demonstrate that these models provide interpretable causal representations under both full and partial observability, with model accuracy scaling directly with interventional strength.


## 精读解读（中文）
### 一、研究动机
在多智能体系统中，基于模型强化学习的世界模型常混淆统计相关与因果机制，导致分布偏移下失效。

### 二、技术方案（Method）
提出隐式因果世界模型，利用离线演示数据，通过整合策略方差并应用顺序后门条件来发现隐式因果图，无需预定义因果结构，从而恢复环境动态。

### 三、结果（Result）
在Two-Door、Navigation和Giveway等协调任务中，该模型在完全和部分观测条件下均可提供可解释的因果表示，且模型准确性随干预强度的增加而线性提升。

### 四、结论（Conclusion）
隐式因果世界模型能够从多智能体演示中有效学习因果机制，提升世界模型在分布外场景的泛化能力和可解释性。

### 五、方法论与关键技术细节
关键细节包括：利用策略方差作为后门调整变量实现因果发现；采用顺序后门条件处理时序依赖；模型基于变分推断框架学习隐式因果图；无需先验因果图，适用于部分观测；准确性受干预强度影响，强干预下因果识别更准确。
