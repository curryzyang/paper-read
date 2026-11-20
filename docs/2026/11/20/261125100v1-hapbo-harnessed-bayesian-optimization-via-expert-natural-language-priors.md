# HapBO: Harnessed $α$-$π$ Bayesian Optimization via Expert Natural Language Priors

- 区域：精读区
- 排名：6
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Jean-Sébastien Giroux, Rose Guay Hottin, Marco Bonizzato
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25100v1) · [PDF](https://arxiv.org/pdf/2611.25100v1)

## TLDR
HapBO converts one-time natural-language expert and/or LLM priors into a reusable, non-Gaussian belief function that multiplicatively reweights any nonnegative acquisition function, enabling robust, sample-efficient Bayesian optimization without in-loop LLM calls while preserving standard regret-rate guarantees under adversarial beliefs.

## Abstract
Bayesian Optimization (BO) can be substantially more sample-efficient when informed by prior knowledge about the problem. In practice, however, such knowledge is often available only in natural language, e.g., expert intuitions or documentation, rather than as the explicit probability distribution landscape that prior-guided BO methods may require. Leveraging it effectively demands both an expressive mapping from language to priors and robustness to information that may be misleading. We propose HapBO (Harnessed $α$-$π$ Bayesian Optimization), which elicits beliefs once from a human expert, a large language model (LLM), or both, and deterministically compiles a structured specification into a reusable belief function ($π: \mathcal{X} \to[0,1]$), with a rich representation not restricted to a Gaussian family. Building on $α$-$π$BO, HapBO applies this belief function through a bounded positive multiplier on any nonnegative acquisition, preserving positive acquisition support and requiring no LLM calls during optimization. We prove that, for the Expected Improvement acquisition function (EI), HapBO preserves the standard simple-regret rate up to a bounded factor, even under adversarial beliefs. We evaluate HapBO on 40 HPOBench tasks, a synthetic suite in 6-15 dimensions and two real-world applications: cortical neurostimulation and constrained solar design. HapBO achieves the lowest aggregate HPOBench regret and strong real-world task performance, with zero in-loop token cost. In real-world applications it improves the optimization outcome even at budgets of 12-20 queries, and at a small fraction of the wall-clock and token costs of other LLM-based methods.


## 精读解读（中文）
### 一、研究动机
贝叶斯优化在有先验知识时能显著提升样本效率，但实际问题中的先验往往以专家直觉、文档等自然语言形式存在，并非先验引导型贝叶斯优化方法所需的显式概率分布或函数形态。要把这类知识有效用起来，既需要把语言映射为富有表达力的先验，又必须对可能误导的信息保持鲁棒性。

### 二、技术方案（Method）
HapBO 只向人类专家、大语言模型或两者同时一次性征询信念，将得到的结构化说明确定性地编译为可复用的信念函数 π:X→[0,1]，其表示不受高斯族限制。在 α-π 贝叶斯优化框架上，HapBO 用有界正乘子把该信念函数作用于任意非负采集函数，即采集值乘以一个有界正系数，从而保持采集函数的正支撑集。由于编译是离线的确定性过程，优化循环内不再调用大语言模型，整个优化过程只使用这一个固定信念函数做采集最大化与常规高斯过程更新。

### 三、结果（Result）
在 40 个 HPOBench 任务、6–15 维合成测试集以及皮质神经刺激与带约束太阳能设计两个真实应用上评估，HapBO 取得最低的 HPOBench 聚合遗憾，并在真实任务上表现强劲且循环内 token 成本为零。在真实应用中，即便预算仅 12–20 次查询也能改善优化结果，且实际耗时与 token 开销仅为其他基于大语言模型方法的很小一部分。

### 四、结论（Conclusion）
结果表明，自然语言先验可以被一次性编译为可复用的信念函数，并通过有界乘子安全地注入贝叶斯优化，从而在保持理论保证的同时获得显著的样本效率与计算效率收益。HapBO 为把专家知识与大模型知识低成本、可复现地用于黑箱优化提供了实用范式。

### 五、方法论与关键技术细节
关键实现点在于：信念函数取值归一化到 [0,1]，通过有界正乘子作用于采集函数，保证正支撑不被破坏；理论上证明对期望改进（EI）采集函数，即使信念是对抗性的，HapBO 仍保持标准简单遗憾率至多相差一个有界因子。实验覆盖 40 个 HPOBench 任务、6–15 维合成任务与两个真实场景（含带约束的太阳能设计），并考察 12–20 次查询的小预算情形；成本上仅在初始征询阶段消耗一次 token，循环内为零。局限包括信念只在开始时获取一次、不随观测在线更新，乘子的有界性限制了先验影响力，且最终效果依赖一次性征询与编译所得信念函数的质量。
