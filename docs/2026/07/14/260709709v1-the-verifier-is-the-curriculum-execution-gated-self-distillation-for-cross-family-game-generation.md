# The Verifier is the Curriculum: Execution-Gated Self-Distillation for Cross-Family Game Generation

- 区域：精读区
- 排名：9
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Chenyu Zhou, Qiliang Jiang, Shuning Wu, Xu Zhou
- 机构：Institute of Science Tokyo, Zhejiang University, National University of Singapore
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09709v1) · [PDF](https://arxiv.org/pdf/2607.09709v1)

## TLDR
Using a deterministic, ungameable launch-check verifier as the training filter in rejection-sampling self-distillation compounds out-of-family generalization for cross-family game generation, demonstrating that the verifier is the curriculum.

## Abstract
Post-training a code generator against a learned judge can optimize proxy features that raise the score without improving the artifact. We study the opposite signal: a deterministic, judge-free, ungameable filter -- whether a generated project launches cleanly under a headless engine (strict-launch). Under this gate, rejection-sampling self-distillation compounds out-of-family generalization. On GameCraft-Bench (mapping a natural-language brief to a complete Godot project), a 14B model (Qwen3-14B+LoRA) distilled under strict-launch raises clean generation on four unseen game families from 8.8% to 42.2% per-candidate and best-of-K coverage from 18/25 to 25/25 (the gold ceiling) over three rounds, each a significant gain (p=0.0019, p<1e-4, p<1e-4). The gain is not from merely adding data: an exactly-matched gold-duplication control regresses below the base model (5.6% vs. 8.8%, p=0.019), while a count-matched decomposition splits the round-1-to-2 jump into comparable quality (+8.8pp) and quantity (+8.5pp) channels. Most directly, rerunning the loop with only the filter swapped -- the lenient BUILD check, which passes 99.9% of generations, in place of the launch gate -- erases the gain entirely (back to base, p=1e-3 vs. the launch-gated round), isolating verifier precision rather than the optimizer. A second ungameable signal, headless execution grounding, rises monotonically across rounds and yields far more grounded candidates than gold-duplication at a matched budget (16 vs. 5), confirming the gains are functional, not launch-but-empty. Game generation is a verifiable testbed for one lesson: the verifier is the curriculum -- what it certifies is what the model learns.


## 精读解读（中文）
### 一、研究动机
针对代码生成模型的后训练，使用学习型评判器（learned judge）可能导致模型优化代理特征（如表面得分）而不真正改进工件。本文研究相反的信号：确定性、无评判、不可欺骗的过滤器——即生成的项目是否能在无头引擎下干净启动（strict-launch），在这种门槛下，拒绝采样自蒸馏可以复合跨家族泛化。

### 二、技术方案（Method）
使用GameCraft-Bench任务（将自然语言简短描述映射到完整的Godot项目），模型为Qwen3-14B + LoRA。采用迭代的拒绝采样自蒸馏：每一轮用当前模型在训练家族brief上采样K=8个候选项目，通过strict-launch过滤器（启动干净且至少三个文件）接受，去重后每个brief最多保留2个，累计到训练池；然后基于基础模型用LoRA微调（r=16, alpha=32, lr=1e-4, 8 epochs），共进行三轮。控制实验包括：金标准重复（CTRL）、计数匹配、BUILD门控（替换过滤器为宽松的BUILD检查）。

### 三、结果（Result）
三轮后，对四个未见游戏家族的逐候选项干净启动率从8.8%提升到42.2%，best-of-K覆盖率从18/25提升到25/25（金标准上限）。控制实验显示：金标准重复回归到低于基础模型（5.6% vs 8.8%，p=0.019）；BUILD门控消除增益（回到基础，p=1e-3 vs 启动门控轮）；计数匹配隔离出质量和数量两个渠道（+8.8pp和+8.5pp）。功能审计确认增益是功能性的，不是启动但空洞。

### 四、结论（Conclusion）
游戏生成是一个可验证的测试平台，揭示一个教训：验证器就是课程——它所认证的就是模型所学的。确定性、不可欺骗的过滤器通过精确分离功能性和破坏性项目，使得自蒸馏的增益跨家族迁移。

### 五、方法论与关键技术细节
数据：GameCraft-Bench，10个训练家族（111个金标准项目），4个留出家族（25个任务），无泄露。先验：strict-launch过滤器是确定性、无需评判、不可欺骗的，仅要求启动干净和至少三个文件。损失/超参：LoRA（r=16, alpha=32），学习率1e-4，8 epochs，bfloat16，使用vLLM推理。复杂度：每轮采样K=8，每brief最多保留2个，燃料大小逐轮增长（67->123->186）。约束：仅Godot引擎，14B模型规模，需验证到其他领域。局限性：未测试其他引擎或跨模态任务，未分析长尾失败模式。
