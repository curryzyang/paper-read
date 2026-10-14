# Splicing Hints into Reasoning Traces: Learning from Demonstrator Failures

- 区域：精读区
- 排名：4
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Hamed Mahdavi, Pouria Mahdavinia, Majid Farhadi, Vasant Honavar
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.13996v1) · [PDF](https://arxiv.org/pdf/2610.13996v1)

## TLDR
TLDR: SPLICE improves mathematical reasoning by using a reference-solution-guided second model offline to truncate failed traces at the last verified step and splice in adaptively strengthened hints, yielding finetuning data that outperforms distilling unedited traces on AIME and olympiad proofs.

## Abstract
Reinforcement learning with verifiable rewards improves mathematical reasoning when a final answer can be checked, but a correct answer does not certify the derivation behind it, and proof problems offer no answer to check. Replacing the check with a reasoning model as an in-loop verifier faces a fundamental obstacle: the policy must already produce occasional correct attempts for any reward to exist, which it may never do at olympiad level. We instead move verification and repair out of the training loop and into offline data generation with SPLICE, a workflow in which a second model, given only a reference solution, edits a reasoning model's traces as they are generated: it verifies progress, truncates a failed trace at its last verified step, and splices in an adaptively strengthened hint until progress resumes. The resulting dataset includes repaired examples whose sampled unaided trajectory failed, with failed continuations removed and progress repeatedly checked against the reference solution. A model finetuned on SPLICE traces outperforms the same model distilled from the reasoning model's unedited traces on AIME and, under a grading protocol validated against human grades, on olympiad proofs. The trained model's own traces show a corresponding behavioral signature: at difficult points it announces a branch in the style of the spliced hints and takes riskier steps, with predictive entropy rising there and just after, a pattern absent from the model trained on unedited traces.


## 精读解读（中文）
### 一、研究动机
可验证奖励强化学习依赖最终答案检查，但正确答案并不保证推导正确，证明题又没有答案可查；若把推理模型作为训练循环中的验证器，又要求策略已经能偶尔产生正确尝试，而在奥林匹克难度下这可能永远不会发生。因此需要将验证与修复移出训练循环，转而从失败示范中学习。

### 二、技术方案（Method）
提出 SPLICE 离线数据生成流程：给定参考解答，第二个模型在推理模型生成轨迹时逐步验证进展；一旦失败，就在最后一个已验证步骤处截断，并拼接自适应增强的提示，直到进展恢复。收集这些修复轨迹以及未编辑轨迹，对同一策略模型进行微调/蒸馏。关键模块包括进展验证、失败截断、自适应提示拼接、参考解对齐与离线数据构建。

### 三、结果（Result）
在 AIME 和奥林匹克证明题上，用 SPLICE 修复轨迹微调的模型优于用同一推理模型未编辑轨迹蒸馏的模型；证明题评估采用了与人工评分验证过的评分协议。训练后模型自身的轨迹还出现行为特征：在困难点以拼接提示的风格宣布分支并采取更高风险步骤，预测熵在该处及之后上升，而未编辑轨迹训练的模型没有这种模式。

### 四、结论（Conclusion）
将验证与修复从在线训练循环移到离线数据生成，可以绕过可验证奖励对“已有正确尝试”的依赖，使模型能从失败示范中的部分正确步骤学习，并提升数学推理与证明表现。行为证据表明模型学会了在困难点主动分支和探索，而不是仅模仿未编辑的成功路径。

### 五、方法论与关键技术细节
数据来自推理模型在数学题（含证明）上的采样轨迹；第二个模型仅依据参考解进行逐步验证、失败截断和自适应提示拼接；训练目标是对 SPLICE 修复轨迹进行微调，对比基线为未编辑轨迹蒸馏。评估包含 AIME 和奥林匹克证明，后者使用经人工评分验证的评分协议；行为分析使用预测熵。局限包括依赖参考解与外部编辑器、离线流程成本、提示拼接可能引入人工先验，且摘要未给出模型规模、超参、损失细节及对无参考解或不可验证领域的泛化验证。
