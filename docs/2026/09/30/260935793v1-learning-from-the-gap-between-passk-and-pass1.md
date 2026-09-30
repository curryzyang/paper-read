# Learning from the Gap Between Pass@K and Pass@1

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Xuan Liu, Jingbin Qian, Haosheng Chen
- 机构：William Marsh Rice University, East China Normal University, Shanghai Jiao Tong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35793v1) · [PDF](https://arxiv.org/pdf/2609.35793v1)

## TLDR
GapFT improves single-sample LLM performance by fine-tuning on the Pass@K–Pass@1 gap—problems the source policy fails on one sample but solves within K samples—rather than uniformly on verified responses, yielding large Pass@1 gains over budget-matched verified RFT.

## Abstract
Large language models (LLMs) are increasingly trained with reinforcement learning from verifiable rewards (RLVR). An exact verifier can also support test-time scaling by selecting a passing response from multiple samples, while other deployments use beam search, adaptive sampling, or tools. We study single-sample decoding, where each query receives one response without search, to ask whether search-exposed behavior can be absorbed into the model. Existing verified-response post-training recipes do not generally distinguish problems already solved on the first decode from failures recovered within K samples. Under a fixed budget, this can spend examples repeating behavior the deployed policy already has. We introduce GapFT, which selects training evidence by the source checkpoint's single-sample outcome and fine-tunes on the Pass@K-Pass@1 gap: problems the policy fails on one sample but solves within K samples. We match training examples, processed tokens, and optimizer steps while keeping the objective unchanged. GapFT fills the matched budget with recovered failures and uses an exact decomposition to distinguish corrections of recovered and missed failures from regressions on first-decode successes. On LogiQA 2.0 and ReClor with Llama-3.1-8B, GapFT improves Pass@1 by 14.4 and 13.9 points over the source model, outperforms budget-matched uniform verified RFT at the same learning rate, and matches fine-tuning on the full verified pool using one third of the data. A single decode matches the source model's verifier-selected Pass@4 accuracy. A randomized control attributes gains to covering distinct failures, and our analysis relates available gains to transferable failure support. A three-seed Qwen2.5-7B replication retains positive gains over uniform RFT on both logic tasks.


## 精读解读（中文）
### 一、研究动机
大语言模型 increasingly 用可验证奖励强化学习（RLVR）训练，同一验证器也可支持测试时扩展（多次采样后选一个通过的回答）。但在单样本解码部署时每个查询只有一个回答、没有搜索，因此需要把搜索暴露的行为吸收进模型。现有基于验证响应的后训练配方通常不区分“首次解码就成功”的问题与“K 次采样中恢复的失败”问题，在固定预算下会重复已掌握行为、挤占可恢复失败的学习名额。

### 二、技术方案（Method）
GapFT 先用冻结的源策略和精确验证器把发现问题分成三类：G_K（单样本成功）、S_K（单样本失败但 K 个样本内至少一个通过验证）、U_K（K 个样本都失败）。在匹配预算 (N,L,J) 下，即固定训练例数 N、处理 token 数 L 和优化步数 J，GapFT 用 S_K 中每个问题的一个验证通过回答（逻辑与代码取最短通过回答，MATH 取冻结生成顺序）填满数据槽位，保持最大似然 RFT 目标不变；uniform verified RFT 从 G_K∪S_K 无视状态抽样，solved replay 只从 G_K 抽样作为无搜索对照。评测在同一单样本解码流程下进行，审计集与发现集不相交，并用恒等式 ΔPass@1 = p_S κ_S + p_U κ_U − p_G ρ_G 把 Pass@1 变化精确分解为 S_K 与 U_K 上的纠正率和 G_K 上的回退率，其中 κ 为单样本错误在训练后变为正确的比例，ρ_G 为源成功变为错误的比例。

### 三、结果（Result）
在 Llama-3.1-8B 上，GapFT 在 LogiQA 2.0 和 ReClor 上分别把 Pass@1 相对源模型提升 14.4 和 13.9 个百分点，优于同学习率、预算匹配的 uniform verified RFT，并用约三分之一数据达到在全量验证池上微调的水平。单次解码即可达到源模型经验证器选择的 Pass@4 准确率；随机对照把增益归因于覆盖不同的失败问题。在 Qwen2.5-7B 上三个随机种子的复现实验在两个逻辑任务上均保持优于 uniform RFT 的正向增益，且分析表明可用增益与可迁移失败支持量相关。

### 四、结论（Conclusion）
按源 checkpoint 的单样本结果来分配验证证据，比只按正确性筛选更能把搜索收益转化为单样本部署能力；匹配预算下的状态感知选择可减少冗余、提高 Pass@1，并在不同模型家族上具有可复现性。该工作把放大已有行为（S_K 纠正）、获取观察支持外行为（U_K 纠正）与回退代价（G_K）统一在同一分解中，说明收益上限受审计集中可被搜索恢复的失败比例约束。

### 五、方法论与关键技术细节
设置与数据：离线 RFT，冻结源策略在发现集上采样，K 为搜索预算并与训练预算分开报告；G_K、S_K、U_K 只是有限搜索预算下的观测划分，U_K 不代表源策略对正确答案概率为零。选择规则在训练前冻结，S_K 每个问题只保留一个验证通过回答，即使多个样本通过也只取一个；replay 可对同一问题重复分配槽位。预算匹配要求 N=R|T|、R·Tok(T)≈L、Step(T;R)=J，并报告允许的 token 偏差；loss 只在响应 token 上计算，处理 token 含截断后的输入与响应但不含 padding。审计响应从不进入证据选择、训练或 checkpoint 选择；嵌套预算复用前 K 个样本作为前缀，审计划分在每个 K 重建；区间用 2000 次 bootstrap 重采样配对审计问题与耦合训练种子。分解是精确恒等式但不独立赋予因果，因果由匹配预算干预和随机对照承担；主要局限是收益受可迁移失败支持规模限制，且结论主要来自逻辑基准与两个 7B/8B 级模型。
