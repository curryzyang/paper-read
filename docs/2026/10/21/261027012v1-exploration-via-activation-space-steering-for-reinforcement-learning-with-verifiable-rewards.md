# Exploration via Activation-Space Steering for Reinforcement Learning with Verifiable Rewards

- 区域：精读区
- 排名：2
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Yunan Zeng, Jinhao Jing, Xi Cheng, Yuwang Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.27012v1) · [PDF](https://arxiv.org/pdf/2610.27012v1)

## TLDR
**TLDR:** The paper introduces Activation-Space Exploration (ASE), an online RLVR method that clusters activation differences between correct and incorrect responses to build a bank of latent steering vectors and applies them to diversify training rollouts, improving mathematical reasoning over GRPO under the same rollout budget.

## Abstract
Reinforcement learning with verifiable rewards (RLVR) trains a language model by sampling responses, scoring them with an automatic verifier, and updating the policy from the resulting rewards. The policy therefore receives direct learning signals only from trajectories that appear in its rollouts. Yet repeated sampling from the same policy can concentrate on similar reasoning paths, leaving useful alternatives unexplored under a fixed rollout budget. We introduce Activation-Space Exploration (ASE), an online method for diversifying training rollouts. By clustering activation differences between correct and incorrect responses to the same problem, ASE builds a structured bank of latent exploration vectors. Different vectors are then applied to subsequent rollouts to explore alternative reasoning paths. On Qwen3-1.7B-Base and Qwen3-8B-Base trained on DAPO-Math-17k, ASE improves average Mean@8 across six mathematical reasoning benchmarks over GRPO by 4.87 and 1.87 percentage points, respectively, under the same rollout budget.


## 精读解读（中文）
### 一、研究动机
RLVR 的训练信号只来自策略实际采样到的轨迹，固定 rollout 预算下重复采样容易集中在相似推理路径，导致有用替代解探索不足。ASE 旨在不增加采样成本的前提下，通过干预模型内部激活来提升训练 rollout 的多样性。

### 二、技术方案（Method）
ASE 是面向 RLVR 的在线探索方法：训练时对同一问题采样多个回答并用自动验证器判分，收集正确与错误回答对应的激活差异，对这些差异做聚类形成结构化的潜在探索向量库；后续 rollout 时选择不同探索向量注入/作用于模型激活，引导策略探索不同推理路径，再按常规 RLVR 流程用验证奖励更新策略。

### 三、结果（Result）
在 DAPO-Math-17k 上训练 Qwen3-1.7B-Base 与 Qwen3-8B-Base，并在六个数学推理基准上评估，ASE 在相同 rollout 预算下相对 GRPO 将平均 Mean@8 分别提升 4.87 和 1.87 个百分点。

### 四、结论（Conclusion）
结果表明，直接利用正确/错误回答间的激活差异构造探索方向，可在不增加 rollout 预算的情况下缓解 RLVR 的路径同质化，提升数学推理的平均表现，说明激活空间 steering 是增强 RLVR 探索的有效补充手段。

### 五、方法论与关键技术细节
关键实现依赖同题多回答的验证器判分、正确-错误激活差收集、差异聚类与探索向量库，以及在线 rollout 时的向量选择与激活干预；实验使用 DAPO-Math-17k 和 Qwen3-1.7B/8B-Base，并以 Mean@8 和相同 rollout 预算对比 GRPO。摘要未披露具体干预层、聚类数、向量库规模、选择策略、损失形式与额外计算开销，且结论主要限于数学推理任务，跨任务泛化与实现复杂度仍需进一步验证。
