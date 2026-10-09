# Recurrent Self-Improvement: Dynamic Cross-Loop On-Policy Distillation for Looped Language Models

- 区域：精读区
- 排名：6
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Yi Wang, Rui Qian, Yu Li, Haoyang Yao, Wenjie Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10623v1) · [PDF](https://arxiv.org/pdf/2610.10623v1)

## TLDR
LoopOPD uses a LoopLM’s own terminal loop as a frozen compute-privileged teacher to distill an intermediate loop on student rollouts, and D-LoopOPD dynamically refreshes that teacher for recurrent self-improvement, yielding better math, general reasoning, and code performance without external teachers or privileged information.

## Abstract
Looped Language Models (LoopLMs) offer a parameter efficient approach to scaling reasoning by reusing shared parameters across recurrent computation steps. Despite their promise, effective post-training of LoopLMs remains challenging. Existing approaches either provide reward based supervision that is sparse or costly to extend across loops, or rely on external teachers or privileged information, leading to limited teacher availability or teacher-student context mismatch. To address these limitations, we introduce LoopOPD, a cross-loop on-policy distillation framework that uses additional recurrent computation within a LoopLM as its own source of supervision. LoopOPD uses a frozen terminal loop policy as a compute privileged teacher for an intermediate loop student on student generated rollouts, providing dense supervision without an external teacher or privileged information. We further propose Dynamic LoopOPD (D-LoopOPD), which continually refreshes the terminal loop teacher as the shared model parameters are updated, enabling recurrent self-improvement. We characterize how distillation updates propagate across loop depths and derive sufficient conditions under which a single update yields simultaneous local improvement at both loop depths. Experiments on Ouro-Thinking models show that LoopOPD improves mathematical reasoning, while D-LoopOPD yields further gains through dynamic teacher updates. Despite being trained only on mathematical data, the resulting models also improve on general reasoning and code generation benchmarks, demonstrating that recurrent computation can serve as an effective source of supervision for LoopLMs. Our code and model checkpoints will be released upon acceptance.


## 精读解读（中文）
### 一、研究动机
Looped Language Models 通过循环复用共享参数来参数高效地扩展推理，但其后训练仍很困难；既有方法要么依赖稀疏且难以跨循环扩展的奖励监督，要么依赖外部教师或特权信息，导致教师可用性受限或师生上下文不匹配。为此，作者希望让 LoopLM 利用自身额外的循环计算作为监督来源。

### 二、技术方案（Method）
论文提出 LoopOPD，一种跨循环 on-policy 蒸馏框架：以 LoopLM 的冻结终末循环策略作为具备额外计算优势的教师，对中间循环学生模型在自身生成的 rollout 上进行稠密蒸馏，从而无需外部教师或特权信息。进一步提出 Dynamic LoopOPD，在共享模型参数更新后持续刷新终末循环教师，实现循环式自改进。作者还分析蒸馏更新如何跨循环深度传播，并推导单次更新可同时改善两个循环深度局部性能的充分条件。

### 三、结果（Result）
在 Ouro-Thinking 模型上的实验表明，LoopOPD 能提升数学推理表现，而 D-LoopOPD 通过动态教师更新带来进一步提升。尽管仅在数学数据上训练，所得模型在通用推理和代码生成基准上也获得改善，说明循环计算可作为 LoopLM 的有效监督来源；摘要未给出具体指标数值。

### 四、结论（Conclusion）
该工作表明，LoopLM 无需外部教师或特权信息，可利用自身不同循环深度的计算差异进行 on-policy 蒸馏与动态自改进，并且数学训练带来的收益可泛化到数学以外任务。这为 LoopLM 的后训练提供了可扩展的新范式。

### 五、方法论与关键技术细节
关键实现要点是教师与学生来自同一 LoopLM 的不同循环深度：教师为冻结的终末循环，学生为中间循环，监督发生在学生生成的 on-policy rollout 上，属于稠密蒸馏而非稀疏奖励。D-LoopOPD 随共享参数更新持续刷新终末循环教师，以缓解师生上下文或能力不匹配。理论部分刻画蒸馏更新跨循环深度的传播，并给出单次更新同时局部改善两个深度的充分条件。实验使用 Ouro-Thinking 模型且仅用数学数据训练；具体蒸馏损失形式、超参、刷新频率、复杂度约束及理论条件的实际局限在摘要中未展开。
