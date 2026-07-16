# Uncertainty-Aware Sequential Decision Rules for Event-Triggered LLM Invocation in Streaming Systems

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Zhaohui Wang
- 机构：University of Southern California
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13048v1) · [PDF](https://arxiv.org/pdf/2607.13048v1)

## TLDR
This paper proposes a risk-based sequential decision framework for triggering Large Language Model (LLM) invocations in streaming systems, proving theoretical guarantees (including regret bounds, calibration transfer, and avoidance of trigger chattering) and unifying classical trigger families (event-triggered, optimal stopping, SPRT, CUSUM, Bayesian) under a threshold policy on a risk functional, with empirical validation on turbofan degradation data.

## Abstract
Streaming inference pipelines increasingly pair lightweight fast models with Large Language Models (LLMs) that provide rich semantic understanding at substantial cost. The central question of when to invoke the LLM has received limited formal treatment. We cast this as a risk-based sequential stopping problem, where a trigger policy fires when a risk functional over the observation history exceeds a threshold. Within this framework, we prove six results: a minimum inter-event time bound excluding trigger chattering; optimality of threshold policies via smooth pasting; approximate SPRT guarantees under estimated parameters; O(sqrt(T log T)) regret for stationary streams, extending to O(sqrt((C_T + 1) T log T)) under C_T changepoints; O(1/sqrt(T)) convergence of online gradient descent for adaptive thresholds; and a calibration-to-miss-rate transfer inequality. Several classical trigger families, including event-triggered, optimal stopping, SPRT, CUSUM, and Bayesian triggers, can be expressed as special cases of this framework. On turbofan degradation data (CMAPSS) with real LLM calls, we empirically verify the theoretical assumptions, ablate the risk function design, compare against six baselines including a RouteLLM-style router and contextual bandits, and analyze cost sensitivity and LLM failure modes. The results confirm sublinear regret, with alpha < 1 for all principled triggers; high diagnostic quality, with 92.9 percent of 1600 LLM diagnoses reaching grounding score >= 0.75 under our rubric; and that anomaly-score-driven risk functions dominate alternatives by roughly an order of magnitude on the Pareto AUC.


## 精读解读（中文）
### 一、研究动机
流式推理系统需要在轻量级快速模型和昂贵大型语言模型（LLM）之间取得平衡，LLM虽能提供丰富的语义理解但成本高昂。现有工作对何时调用LLM这一核心问题缺乏正式处理。本文将此问题形式化为基于风险的序列停止问题，旨在为LLM在流式系统中的调用提供理论框架。

### 二、技术方案（Method）
本文提出一个统一的风险函数阈值策略框架，其中触发策略π在风险函数R(历史)超过阈值θ时调用LLM。快速模型采用GRU双头网络，分别输出预测和异方差不确定性估计。风险函数通过聚合异常分数、预测不确定性和时间上下文构建。阈值可通过在线梯度下降（OGD）或LinUCB自适应更新，并支持事件触发、最优停止、SPRT、CUSUM及贝叶斯触发等经典触发器作为特例。在CMAPSS涡轮风扇退化数据集和CIC-IDS2017网络入侵数据集上评估，算法流程为每步：快速模型处理输入生成预测与不确定性，更新风险，若风险超过阈值则调用LLM获取诊断并自适应调整阈值。

### 三、结果（Result）
理论结果包括最小事件间隔（排除颤振）、阈值策略的最优性、近似SPRT保证、静态流下次线性后悔界O(√(T log T))、非静态流下扩展为O(√((C_T+1)T log T))、在线梯度下降的O(1/√T)收敛率，以及校准到遗漏率的转移不等式。实验证实所有原则性触发器的后悔值均为次线性（α<1），LLM诊断质量高（1600次诊断中92.9%达到接地分数≥0.75），异常分数驱动的风险函数在Pareto AUC上优于其他方案约一个数量级，并与六个基线（包括RouteLLM风格路由器和上下文老虎机）比较，验证了成本敏感性和LLM故障模式。

### 四、结论（Conclusion）
本文提出的统一风险框架为流式系统中何时调用LLM提供了形式化的决策理论基础，理论结果和经验验证共同确认了该框架在后悔下界、诊断质量和自适应阈值方面的有效性。该框架能够将多种经典触发机制作为特例统一，并支持在线自适应调整阈值以适应非平稳流。

### 五、方法论与关键技术细节
快速模型通过最小化异方差损失训练，不确定性估计方法包括方差头、MC Dropout（20次前向）、深度集成（5个模型）和温度缩放。阈值自适应采用OGD（步长η/√t，有界次梯度G，域直径D）或LinUCB。理论结果基于有界增量、风险下鞅、单调性等假设，并经过CMAPSS数据验证。校准到遗漏率转移不等式表明，对于ε-校准的不确定性估计u_t∈[0,1]，触发阈值为θ_u时遗漏关键事件的联合概率≤θ_u+ε。工作局限性包括未考虑硬实时调度、最坏情况执行时间和队列响应时间等系统级时序问题。
