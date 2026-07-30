# Early Verdicts, Better Budgets: Sequential Adaptive Rollout Allocation for Compute-Efficient RLVR

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26253v1) · [PDF](https://arxiv.org/pdf/2607.26253v1)

## TLDR
SARA (Sequential Adaptive Rollout Allocation) is a budget-constrained optimal stopping method for RLVR that uses Beta posteriors and SPRT-style thresholds to early detect and abandon saturated prompts, reallocating their rollout budget to fresh prompts, achieving comparable or better accuracy with 22–67% fewer rollouts.

## Abstract
Reinforcement learning with verifiable rewards (RLVR) is bottlenecked by rollout generation, yet many sampled prompts produce saturated groups (all responses correct or all incorrect) whose zero reward variance yields no policy-gradient signal. Existing remedies either oversample a larger candidate pool and discard saturated prompts (dynamic sampling), paying heavy extra rollouts, or predict prompt difficulty before sampling, which is fragile under a shifting policy. We observe that a group's effectiveness is usually decided early, within the first few of its rollouts, so spending a full group on an already-decided prompt is wasteful. We cast per-step rollout collection as a budget-constrained sequential allocation (optimal stopping) problem and introduce SARA (Sequential Adaptive Rollout Allocation). SARA maintains a Beta posterior over each prompt's success rate, evaluates a closed-form predictor of group effectiveness, and applies a two-threshold, SPRT-style rule that commits effective groups, abandons saturated ones after a short probe, and reallocates the freed budget to fresh prompts, without any extra prediction rollouts. We prove abandonment reliability, expected rollout savings, fixed-budget yield dominance, and a link between effective-group yield and the GRPO gradient norm. On mathematical reasoning and planning with 1.5B/3B models on a single GPU, SARA matches DPS (both below the DS oracle) while using 22% fewer rollouts than DS; composing SARA with DPS yields the best accuracy, slightly above DS, at 67% fewer rollouts (near-uniform cost).


## 精读解读（中文）
### 一、研究动机
现有RLVR中rollout生成是计算瓶颈，许多prompt产生饱和组（所有响应正确或全部错误），这些组零奖励方差，无策略梯度信号，浪费计算。现有方法如动态采样需额外rollouts，预测难度法在策略动态变化下脆弱，亟需更高效的预算分配方案。

### 二、技术方案（Method）
SARA将每个prompt的rollout收集建模为预算约束的序列分配问题。对每个prompt维护一个Beta后验估计成功率，训练中按顺序生成rollout，每步根据闭式预测器（基于后验概率计算组有效性的期望）判断当前组是否有效。应用双阈值SPRT风格规则：当后验低于低阈值时判定饱和并提前终止该组，当后验高于高阈值时判定有效并继续收集至满；释放的预算用于采样新prompt。整个过程无需额外预测rollouts，仅依赖在线生成的rollout结果。

### 三、结果（Result）
在数学推理和规划任务上，使用1.5B和3B模型在单GPU上，SARA匹配了DPS的性能（两者略低于DS oracle），但SARA使用的rollouts比DPS少22%。当SARA与DPS组合时，达到最佳准确率，略高于DS，且rollouts减少67%（接近均匀成本）。理论证明了SARA的放弃可靠性、期望rollout节省、固定预算收益优势以及与GRPO梯度范数的线性关系。

### 四、结论（Conclusion）
SARA通过早期判断组的有效性，自适应分配rollout预算，在不牺牲性能的前提下显著降低计算成本。与DPS组合可进一步提升效率，理论分析支持其可靠性。该方法为RLVR提供了一种高效、可扩展的预算分配策略。

### 五、方法论与关键技术细节
关键细节：使用Beta后验（初始α0=β0=1均匀先验）建模成功率；闭式预测器基于Beta分布计算组有效性的后验概率；双阈值（低阈值和高阈值）采用SPRT风格，探针长度设为前K个rollouts（实验中K=4）；理论证明包括错误放弃概率的上界、期望rollout节省的下界以及固定预算下收益优势的保证。局限性：假设prompt独立同分布，并假设rollout间条件独立；超参数（阈值、探针长度）需根据任务调整；目前未考虑非独立rollout或策略动态变化带来的先验漂移。
