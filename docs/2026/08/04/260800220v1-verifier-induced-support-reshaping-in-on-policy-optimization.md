# Verifier-Induced Support Reshaping in On-Policy Optimization

- 区域：精读区
- 排名：3
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Shaohang Wei, Zikun Su, Feifan Song, Wen Luo, Wei Li, Guangyue Peng, Houfeng Wang
- 机构：Peking University, BUPT
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00220v1) · [PDF](https://arxiv.org/pdf/2608.00220v1)

## TLDR
On-policy RL with verifiable rewards improves the current objective but reshapes the policy’s support, making successful behaviors for later objectives too rare to sample and reinforce, thereby limiting future trainability and joint capability.

## Abstract
We show that on-policy reinforcement learning with verifiable rewards (RLVR) can improve the current objective while making successful behaviors for later objectives too rare to sample and reinforce. We call this verifier-induced support reshaping and define effective rewardable support as successful trajectories reachable within a fixed rollout budget. Across two model families, we study this effect through repeated verifier-scored sampling and bidirectional training on mathematical reasoning and constrained instruction following, including sequential training with the opposite verifier. Math-RLVR raises average instruction-following success but reduces the number of prompts with any successful response under repeated sampling. On IFEval with Qwen3-8B-Base, pass@1 rises by 6.5 percentage points while best@32 falls by 9.8 percentage points, and the same divergence appears across both models and IF benchmarks. Conversely, IF-RLVR shifts math responses from step-by-step openings toward direct answers, lowers best@k across sampling budgets, and reduces reward variation for later Math-RLVR. Token-distribution analyses and controlled opening interventions show that these changes concentrate in the first few response tokens. RLVR mainly reranks openings already available in the base policy, and the selected opening causally affects math searchability. The tested reference-policy constraints, routing priors, and on-policy distillation preserve cross-task support only partially; MathIF and ReasonIF show that marginal gains translate only partly into responses that are both correct and constraint-following. Therefore, endpoint improvements do not guarantee future trainability or joint capability under on-policy optimization. Code is available at https://github.com/sylvain-wei/verifier-induced-support-reshaping


## 精读解读（中文）
### 一、研究动机
在线策略优化中，使用可验证奖励的强化学习（RLVR）虽然能改善当前目标，但可能使后续目标所依赖的成功行为在固定采样预算内变得过于稀有而无法被采样和强化。现有研究多关注事后的性能保持（灾难性遗忘），缺乏对未来可训练性的前瞻性度量。本文提出验证器诱导的支持重塑，研究当前验证器优化后，后续目标的有效奖励支持如何被改变。

### 二、技术方案（Method）
以Qwen3-8B-Base和Qwen2.5-Math-7B为基座，分别进行数学推理RLVR（Math-RLVR，在7.5k MATH子集上使用精确最终答案验证）和约束指令跟随RLVR（IF-RLVR，在IFTrain上使用确定性全约束检查器），并执行双向顺序训练（IF→Math和Math→IF）。评估时对每个提示做k=32次随机采样，用对应验证器评分，计算均值（pass@1）、best@k和通过次数，并按通过数将提示分为全部错误、混合、全部正确三组，以混合组作为可提供组内奖励变化的信号。此外，将响应按可见开头分类为DRI（逐步推导）、DAI（直接答案）和Other，结合受控开头干预和逐token分布分析，检验跨任务支持变化的机制。最后测试参考策略约束、路由先验和在线策略蒸馏（OPD）等保留策略的效果。

### 三、结果（Result）
在IFEval上，Math-RLVR使Qwen3-8B-Base的pass@1提升6.5个百分点，但best@32下降9.8个百分点；Qwen2.5-Math-7B上同样出现+7.9和-11.4的分歧，IFBench亦有一致趋势，表明平均成功率上升而可采样覆盖下降。IF-RLVR使AIME的best@k在k=4到32的所有预算下持续下降，且响应开头从DRI转向DAI，DAI比例与best@32呈负相关。顺序训练中，IF→Math虽然使全错比例从65.6%下降，但混合组从33.6%持续下降至step 20时几乎消失，导致后续Math-RLVR缺少组内奖励变异；MathIF和ReasonIF的联合得分也仅小幅提升，未成比例转化为既正确又满足约束的响应。

### 四、结论（Conclusion）
端点指标上的改进并不保证后续目标的可训练性或联合能力：验证器诱导的支持重塑会改变未来成功轨迹的可采样性，当前目标的提升可能以牺牲另一目标的奖励支持为代价。因此，持续RLVR评估应不仅看当前验证器得分，还应监测有效奖励支持的变化；参考策略约束、路由先验和在线策略蒸馏只能部分保留跨任务支持，并可能与目标收益形成权衡。

### 五、方法论与关键技术细节
关键细节包括：训练数据采用7.5k MATH、IFTrain，评估集为AIME24/AIME25/MATH-500-128、IFEval/IFBench及MathIF/ReasonIF；数学验证器为最终答案精确匹配，IF验证器要求全部显式约束通过；核心支持分析使用k=32的采样预算，并定义了all-wrong/mixed/all-correct三组；组相对更新使奖励信号仅来自混合组，因此混合组比例下降意味着训练信号匮乏；开头分类规则只依据可见前几token，不反映内部推理状态；受控干预证明开头选择因果影响数学可搜索性，且RLVR主要重排基础策略已有的开头，而非生成新能力；保留策略（参考策略约束、路由先验、OPD）只能部分保留支持或牺牲目标性能；训练配置为固定种子单次运行，重复rollout反映策略内采样变异；局限性包括行为证据不能排除部分能力变化、结果局限于两个模型族和特定基准、以及缓解方法未完全解决支持重塑问题。
