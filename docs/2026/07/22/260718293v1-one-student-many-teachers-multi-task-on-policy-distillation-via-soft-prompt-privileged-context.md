# One Student, Many Teachers: Multi-Task On-Policy Distillation via Soft-Prompt Privileged Context

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Yingzi Ma, Zichen Zhu, Ming Jiang, Chaowei Xiao
- 机构：University of Wisconsin--Madison, Johns Hopkins University, Nanyang Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18293v1) · [PDF](https://arxiv.org/pdf/2607.18293v1)

## TLDR
PromptSD introduces a soft-prompt-tuned teacher for on-policy distillation that preserves the student's representational geometry, enabling a single student to absorb knowledge from multiple tasks in parallel without catastrophic forgetting, achieving state-of-the-art results on four tasks while training orders of magnitude fewer parameters than full fine-tuning.

## Abstract
On-policy self-distillation (OPSD) teaches large language models new skills through a teacher that shares the student's backbone and supervises its own rollouts. Existing teachers either inject privileged context at the input -- inducing post-hoc rationalization -- or fine-tune weights, accumulating drift and forgetting across tasks. We propose \method, whose teacher differs from the student only by a learnable soft prompt: trained on $(x, y_\text{gold})$ pairs with the backbone frozen, the prompt yields a task-specific teacher that preserves the student's exact representational geometry. \method\ extends naturally to multi-task settings by routing each example in a merged corpus to its corresponding soft-prompt teacher, allowing a single student to absorb knowledge from $K$ teachers in parallel; at inference, all prompts are discarded. On Qwen3-1.7B-Base and Phi-4-mini-instruct across four tasks (Science, Tool Use, Biology, Math), the single-task variant (OPD with a PT teacher) matches or exceeds full fine-tuning while training orders of magnitude fewer parameters, and the multi-task variant achieves the best overall average ($56.2$ on Qwen3-1.7B-Base) while preserving general-capability benchmarks -- in contrast to sequential SFT, which degrades both.


## 精读解读（中文）
### 一、研究动机
现有在线策略自蒸馏方法中，教师模型要么在输入中注入特权上下文导致事后合理化，要么微调权重导致多任务间漂移和遗忘。为了在保持学生表示几何不变的前提下提供可吸收的监督信号并支持多任务并行蒸馏，本文提出基于软提示的教师构建方案。

### 二、技术方案（Method）
提出PromptSD框架。对于每个任务k，冻结学生模型πθ的骨干参数，训练一组可学习的连续软提示P_k，在(x, y_gold)对上通过标准监督微调优化，得到任务特定教师π_{θ+P_k*}，其与学生共享所有Transformer参数仅输入端不同。多任务蒸馏时，合并所有任务数据集并保留任务标签k，每次学生更新时将样本路由到对应教师。学生通过在线策略逆KL散度在其自身推演上更新，梯度来自教师分布。推理时丢弃所有软提示，仅使用学生模型。

### 三、结果（Result）
在Qwen3-1.7B-Base和Phi-4-mini-instruct上对Science、Tool Use、Biology、Math四个任务的实验表明：单任务变体匹配或超越全微调及LoRA，且是唯一教师准确率超过学生自身的配置；多任务变体取得最高平均分56.2（Qwen3-1.7B-Base），同时保持MMLU-Pro、HellaSwag、TruthfulQA等通用能力基准，而顺序SFT则导致训练任务能力和通用能力均退化。

### 四、结论（Conclusion）
软提示教师自然满足在线策略蒸馏的三个期望：中等初始重叠、可被学生吸收的能力差距、无事后合理化。多任务PromptSD通过并行路由有效避免灾难性遗忘，并推导出教师设计原则：教师家族应与任务类型匹配（SFT用于能力注入，RL用于激发），教师规模不如是否携带新知识重要。

### 五、方法论与关键技术细节
数据：四个任务（Science、Tool Use、Biology、Math）的(x, y_gold)对，来自标准基准或定制数据集。损失：教师用标准监督交叉熵训练软提示，学生用在线逆KL散度L(θ)=KL[π_s||π_t]更新。超参：软提示为可学习连续向量，长度默认？实验使用Qwen3-1.7B-Base和Phi-4-mini-instruct，提示长度未明确。复杂度：仅训练软提示参数（远少于全微调），推理无额外开销。约束：需任务标签路由，依赖标注数据训练教师。局限性：软提示数量随任务线性增长；方法假设冻结骨干足够表达不同任务，可能在任务差异极大时受限。
