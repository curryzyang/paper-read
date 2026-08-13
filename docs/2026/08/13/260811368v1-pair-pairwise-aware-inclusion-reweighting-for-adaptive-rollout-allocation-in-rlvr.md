# PAIR: Pairwise-Aware Inclusion Reweighting for Adaptive Rollout Allocation in RLVR

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes
- 机构：University of Washington, University of Wisconsin--Madison
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11368v1) · [PDF](https://arxiv.org/pdf/2608.11368v1)

## TLDR
PAIR introduces a pairwise-aware inclusion reweighting method for adaptive rollout allocation in RLVR that corrects for the U-statistic structure of group-relative gradients, improving accuracy while roughly halving token usage.

## Abstract
Reinforcement learning with verifiable rewards (RLVR) spends most of its compute generating groups of long reasoning trajectories. Recent allocators reduce this cost by assigning budgets to prompts, rollouts, or tokens according to a pointwise notion of difficulty or utility. We identify a statistical mismatch: the unclipped leave-one-out group-relative score gradient is not a sum of independent point contributions, but a second-order U-statistic over pairs of rollouts. Completing one rollout therefore reveals contrast with every other completed rollout, and adaptive endpoint selection changes which pair terms are observable. We introduce PAIR (Pairwise-Aware Inclusion Reweighting), which treats short rollout prefixes as vertices and pair-gradient terms as edges of a contrast graph. A prefix-only predictor estimates correctness and remaining token cost; a convex design chooses positive continuation probabilities under an expected suffix-token budget; and each edge induced by completed vertices is inverse-weighted by its logged joint inclusion probability. Under conditionally independent on-policy rollouts and an unclipped, unstandardized objective, the resulting estimator is design-unbiased for the complete candidate-pair gradient. Across compute-matched RLVR runs on Qwen3-1.7B/4B, PAIR improves average accuracy by +1.2 and +1.4 over the strongest pointwise allocator while using 51% and 52% fewer generated tokens than full-group GRPO. A frozen-population estimator audit confirms that unweighted adaptive selection is biased, whereas pair-inclusion correction recovers the complete-pair target at matched suffix cost.


## 精读解读（中文）
### 一、研究动机
现有RLVR计算主要消耗在生成长推理轨迹组上，近期分配器按点级难度或效用为提示、rollout或token分配预算，但未裁剪的留一法组相对分数梯度本质上是关于rollout对的二阶U统计量，而非独立点贡献之和；自适应端点选择会改变可观测的pair项，导致点级分配与成对估计统计不匹配。

### 二、技术方案（Method）
PAIR将短rollout前缀视为顶点、pair梯度项视为边构建对比图；首先为每个候选rollout独立生成短前缀，用轻量预测头基于前缀隐状态估计最终正确率与剩余token成本；随后在期望后缀token预算约束下求解凸优化问题，为每个顶点分配严格正的继续生成概率；按该概率随机决定是否完成rollout后，对已完成顶点诱导出的每条边，用其被记录的联合包含概率的倒数进行逆概率加权，从而对完整候选pair梯度构造设计无偏估计。

### 三、结果（Result）
在Qwen3-1.7B与Qwen3-4B上的计算量匹配RLVR实验中，PAIR相比最强点级分配器的平均准确率分别提升+1.2和+1.4，同时相比完整分组GRPO减少51%和52%的生成token；冻结总体的估计器审计表明未加权的自适应选择有偏，而pair包含校正能在匹配后缀成本下恢复完整pair目标。

### 四、结论（Conclusion）
PAIR表明RLVR自适应rollout分配必须考虑组相对梯度的成对结构：在顶点上付出后缀生成成本、在边上获得统计价值，通过正包含概率的随机化延续和pair逆包含加权，能同时提高优化精度与token效率，为未来RLVR分配器设计提供了可证明无偏的基准方案。

### 五、方法论与关键技术细节
关键点包括：目标精确对应未裁剪、未标准化的留一法/完整pair平均梯度；联合包含概率rho_ij=pi_i pi_j需严格为正并在终局奖励前记录；预测头使用逆概率加权损失（Brier与对数成本误差）并冻结在一个RL更新内；凸目标包含edge二阶矩项与共享顶点协方差代理项，并设pi_min下限约束逆权重；方法对标准GRPO的PPO裁剪与奖励标准化只是近似场景，需作为实践扩展单独研究；局限性包括依赖前缀预测质量、条件独立on-policy rollout假设、以及凸优化额外的迭代开销。
