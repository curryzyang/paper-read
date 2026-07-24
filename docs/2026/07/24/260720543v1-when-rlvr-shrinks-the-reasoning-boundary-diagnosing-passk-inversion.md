# When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion

- 区域：精读区
- 排名：5
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Todd Zhou
- 机构：Harvard University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20543v1) · [PDF](https://arxiv.org/pdf/2607.20543v1)

## TLDR
Reinforcement learning with verifiable rewards can improve one-sample accuracy but cause pass@k inversion by destroying rare correct trajectories in boundary prompts, and this paper provides a diagnostic framing and a simple proof-of-concept intervention (Per-Problem Base Anchoring) to preserve coverage under repeated sampling.

## Abstract
Reinforcement learning with verifiable rewards (RLVR) can improve one-sample accuracy while making a model worse under repeated sampling. We study this pass@k inversion: after training, the policy may solve fewer distinct problems than its base model at large $k$. The failure concentrates on boundary prompts, where the base model contains rare correct trajectories that are recoverable by sampling but too sparse to reliably appear in finite RLVR rollout groups. We argue that a two-mode account explains this as an absence-of-evidence failure: rare correct trajectories may disappear before RLVR samples and reinforces them often enough. The main contribution is this diagnostic and mechanistic framing. Per-Problem Base Anchoring (PBA) is a deliberately simple proof-of-concept: sharpen prompts with sufficient frozen-base correct evidence, and anchor risky prompts to the base distribution. Across three training seeds on Omni-MATH-Test, with MATH500 as a secondary high-coverage validation benchmark, PBA improves both \PassK{1} and high-budget coverage over matched GRPO. A 3000-prompt regime-controlled diagnostic study is consistent across seeds with the expected signature: ordinary GRPO loses base-solvable boundary prompts, while PBA preserves rare verifier-positive trajectories. We use mathematical verifiers as a controlled testbed for verifier-guided optimization; the same pass@k inversion risk applies to ECCV-relevant vision-language agents when repeated visual, spatial, or chart-reasoning attempts are checked by external tools or verifiers. Reasoning post-training should decide not only how strongly to optimize, but which prompts are safe to optimize.


## 精读解读（中文）
### 一、研究动机
强化学习可验证奖励（RLVR）在提升单样本准确率的同时，可能导致重复采样下覆盖率下降的pass@k反转现象。该问题集中于边界提示（基础模型存在稀有正确轨迹但采样不足），现有方法缺乏诊断和干预机制。

### 二、技术方案（Method）
本文提出Per-Problem Base Anchoring (PBA)方法，基于数学验证器作为可控实验平台。输入为问题x和基础模型π₀，通过冻结基础模型采样估计每个问题的正确模式质量w(x)（正例比例）。建模上，将训练策略分布与基础分布通过混合模型关联。关键模块包括：对于w(x)高（>0.6）的提示，直接使用基础模型正确轨迹进行监督锐化；对于w(x)低但高预算可恢复（边界提示，定义为p(π₀)<0.1且pass@256>0.4），在GRPO训练目标中加入KL散度约束锚定到基础分布；其余提示保持常规GRPO。训练流程为：预计算每个提示的w(x)，然后在GRPO更新中根据提示类型调整目标函数。与匹配的GRPO对比评估。

### 三、结果（Result）
在Omni-MATH-Test数据集上，PBA在三个独立训练种子下均改善了pass@1和高预算覆盖率（pass@256），相对于匹配的GRPO，表明PBA减轻了pass@k反转。3000提示的诊断研究显示：普通GRPO丢失了基础模型可解的边界提示的覆盖率，而PBA保留了这些稀有正确轨迹。数学验证器的结论可推广到视觉语言代理的类似场景。

### 四、结论（Conclusion）
pass@k反转是有限样本RLVR中边界提示的模式承诺失败：训练在稀有正确轨迹被充分采样强化之前就向错误模式承诺，导致覆盖率损失。PBA作为概念验证，表明通过诊断提示的风险程度并采取自适应优化（锐化安全提示、锚定边界提示）可以避免这种破坏。推理后训练不仅应关注优化强度，还应选择哪些提示安全优化。

### 五、方法论与关键技术细节
数据：Omni-MATH-Test（主）和MATH500（辅助验证）。验证器为0/1结果奖励。边界定义基于基础模型的单样本成功率p(x)<0.1且256次采样覆盖率>0.4。PBA的核心是估计每个提示的正确模式质量w(x)（通过冻结基础模型有限采样），并据此决定优化策略。超参：训练种子×3，评估采样n=256。局限性：PBA不能发现新解，不替代蒸馏或搜索，仅防止已有覆盖率被破坏，且依赖基础模型预训练质量。
