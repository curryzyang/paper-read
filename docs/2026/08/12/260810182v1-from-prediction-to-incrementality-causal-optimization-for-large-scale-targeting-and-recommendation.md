# From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Changshuai Wei, John Bencina, Phuc Nguyen, Andre Assuncao Silva T Ribeiro, Benjamin Zelditch
- 机构：LinkedIn
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10182v1) · [PDF](https://arxiv.org/pdf/2608.10182v1)

## TLDR
TLDR: This paper proposes a decision-centric causal optimization framework that jointly models individual treatment effects with a Transformer-augmented DragonNet, uncertainty-aware neural bandit exploration, and dual-based large-scale constrained allocation, demonstrating production feasibility and a statistically significant +7.20% lift in long-term value in a LinkedIn Feed marketing A/B test.

## Abstract
Large-scale targeting and recommendation systems are typically built around predictive scores fed into heuristic or local allocation. When the business goal is incremental impact, as in marketing campaigns, incentives, and notifications, this paradigm systematically misallocates resources toward users who would have acted anyway. We present a decision-centric framework that instead optimizes causal effects under global constraints, aligning three components under a single objective: a causal neural network with a Transformer backbone for individual treatment-effect estimation, a Bayesian neural-bandit layer for uncertainty-aware exploration, and a dual-based large-scale linear-programming layer for constrained allocation. The framework also supports sequential context and multi-outcome, attribute-conditioned scoring through a Transformer encoder and outcome embeddings. We evaluate it with offline simulations on a public bandit dataset, targeted architectural ablations, and an online A/B test on LinkedIn Feed marketing traffic. We also distill production lessons on causal training-data construction and cost and delivery control, which were critical to successful deployment. The end-to-end treatment policy delivered a statistically significant $+7.20\%$ lift in the primary long-term-value metric, demonstrating the feasibility of production-scale causal optimization under business constraints.


## 精读解读（中文）
### 一、研究动机
大规模定向与推荐系统通常基于预测分数进行启发式或局部资源分配，当业务目标是增量影响（如营销活动、激励、通知）时，这种范式会将资源系统性错配给那些即使不干预也会行动的用户，导致投资回报率下降。现有因果建模或优化方法往往只关注局部决策或使用非因果信号，缺乏将因果效应、探索和全局约束联合优化的决策中心框架。

### 二、技术方案（Method）
提出一个决策中心的因果优化框架，包含三个协同组件：1) 因果神经网络：基于DragonNet架构，使用Transformer编码用户触达序列（含时间位置嵌入与多头注意力）和多结果产品嵌入，联合估计潜在结果μ1(X)、μ0(X)和倾向性得分e(X)，并采用EIF正则化；2) 贝叶斯神经Bandit层：通过线性化拉普拉斯近似（LLA）对预训练DragonNet参数后验进行高斯近似，对增量logit采样实现神经Thompson采样，保证探索正性和因果识别；3) 大规模线性规划层：将分配问题建模为带全局约束（预算、频控等）的0-1整数规划，松弛为概率变量后用smoothed dual-decomposition方法求解，通过Nesterov加速对偶上升，每个用户子问题用O(|I|log|I|)投影求解。训练流程为先用观测日志预训练因果模型，部署时每轮从后验采样增量分数输入LP求解器，观测反馈后更新Bandit。

### 三、结果（Result）
在公开bandit数据集上的离线仿真、针对性架构消融和LinkedIn Feed营销流量的在线A/B测试中，端到端处理策略在主要长期价值指标上取得了统计显著的+7.20%提升，验证了生产级规模下因果优化在业务约束下的可行性。

### 四、结论（Conclusion）
从预测转向增量因果优化，并将因果效应估计、不确定性探索和全局约束分配统一到单一目标下，能够显著改善大规模定向与推荐系统的业务效果，尤其适用于营销激励等增量目标场景。该框架在生产和在线实验中均表现有效，且可推广到其他有限干预能力分配问题。

### 五、方法论与关键技术细节
关键细节包括：使用营销触达序列（渠道-动作交互，含AD/IMPRESSION、EMAIL/OPEN等）及[CLS]标记池化，融合天数、星期和正弦位置编码；多结果损失采用逆频率权重c_k的BCE，按T=1和T=0分支分别计算并仅用观测对应头；EIF正则项为Neyman正交的一步修正；LLA采用last-layer变体以降低训练/服务开销，也可用Bayes by Backprop离线评估；LP求解器对双变量K维对偶使用Nesterov加速，每轮线性复杂度O(|U||I|)，γ选取保证ridge扰动<0.1%；实施约束包括每轮预算、频控x_{u,i,t}≤C_fcap，以及guardrail指标约束；探索保证对可行动作的正性概率；局限性包括需要未混淆性和重叠假设，且依赖观测日志构建训练数据，生产部署需注意成本与投放控制。
