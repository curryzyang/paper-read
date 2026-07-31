# RLPF: Reinforcement Learning from Performance Feedback for Code Generation

- 区域：精读区
- 排名：4
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Huihao Jing, Haozhe Cui, Wenbin Hu, Shaojin Chen, Haochen Shi, Changxuan Fan, Yuxuan Liu, Hanyu Yang, Sirui Zhang, Ziyi Chen, Haoran Li, Yangqiu Song
- 机构：New York University, Southwest University of Political Science and Law, MODEIO.AI, The Hong Kong University of Science and Technology, Hong Kong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27271v1) · [PDF](https://arxiv.org/pdf/2607.27271v1)

## TLDR
RLPF introduces a staged reinforcement-learning reward for code generation that orders failed programs by execution progress and correct programs by relative efficiency against baseline and expert references, enabling code agents to optimize runtime as well as pass tests, as shown by large gains on PerfCodeBench.

## Abstract
Code models are increasingly trained with execution feedback, but most training signals still stop at correctness. This leaves an important gap for systems code: two programs can pass the same tests while differing greatly in runtime. We study how to train code agents to prefer faster correct implementations, rather than treating efficiency only as an evaluation metric. The key difficulty is that runtime is a fragile reward. It is meaningful only after a program is correct, varies across tasks, and gives little guidance when most sampled programs fail to compile or run. We propose \textbf{RLPF}, reinforcement learning from performance feedback, which turns execution outcomes into a staged reward. Failed programs are ordered by execution progress, while correct programs are ranked by their relative improvement from the baseline toward the expert reference. This gives useful feedback before correctness and performance-sensitive feedback after correctness. Fine-tuning Qwen3-32B with RLPF on PerfCodeBench raises correct-and-runnable solutions from $11.1\%$ to $54.6\%$ and improves relative efficiency from $8.1\%$ to $38.6\%$. The trained model becomes competitive with stronger open-weight systems, and its optimization behavior transfers modestly to EffiBench-X. Additional studies show that model-generated references provide useful but weaker supervision, and that the full composite reward is more reliable than correctness-only or runtime-only baselines. These results suggest that code agents can be trained not only to pass tests, but also to optimize the programs they write.


## 精读解读（中文）
### 一、研究动机
现有代码模型训练主要依赖执行正确性反馈，但正确性不足以衡量系统代码质量，因为通过相同测试的程序在运行时可能存在巨大差异。运行时作为奖励信号具有脆弱性：仅在程序正确后才有意义、跨任务尺度不一致，且在大多数采样程序无法编译或运行时几乎无法提供学习信号。因此需要一种训练方法，让代码智能体不仅学会通过测试，还能学会偏好更快的正确实现。

### 二、技术方案（Method）
RLPF将执行结果转化为分级奖励。对于失败的程序，按照执行进度排序：无可提取代码、无法编译、无法运行、输出错误，分别赋予-0.05、0.00、0.05、0.10的塑造奖励。对于正确的程序，采用相对于任务基线和专家参考的相对效率奖励：核心指标CGRE为裁剪后的基线到参考差距闭合比例，并辅以FBR（快于基线）和RBR（达到或超越参考）两个小奖励（权重分别为0.16和0.10）。最终奖励为阶梯式：失败状态按进度排序，正确程序取成功奖励与正确性下限（0.15）的最大值，确保正确与失败之间有严格间隔。训练采用GRPO算法，使用Qwen3-32B作为策略模型，通过LoRA微调，每组采样8个候选程序，使用与评估相同的可执行测试框架进行评分，训练5个epoch。

### 三、结果（Result）
在PerfCodeBench家族不相交测试集上，RLPF将Qwen3-32B的correct-and-runnable解决方案从11.1%提升至54.6%，相对效率从8.1%提升至38.6%。训练后的模型在PerfCodeBench上与更强的开源模型竞争，并适度迁移到EffiBench-X。对照实验表明，模型生成的参考提供有用但较弱的监督，完整的复合奖励比仅正确性奖励或仅运行时奖励更可靠。

### 四、结论（Conclusion）
代码智能体可以通过强化学习不仅学会通过测试，还能学会优化其编写的程序。RLPF通过分级奖励结构有效利用了正确性前后的反馈信号，表明性能可以作为一种可训练的目标，而不仅仅是评估指标。

### 五、方法论与关键技术细节
关键细节包括：任务输入包含问题描述、函数签名、基线实现、专家参考和可执行测试框架；成功模式奖励中CGRE是主要连续项，FBR和RBR是阈值奖励；失败模式有四种状态（NX、NC、NR、WO）及其对应分数；最终奖励中正确性下限为0.15（0.10+0.05），保证正确程序始终优于错误程序；训练时每个prompt采样8个候选，运行时测量一次，评估时取3次中位数；超参数包括alpha_F=0.16，alpha_R=0.10，训练5个epoch。局限性包括：模型生成的参考监督较弱，且RLPF的迁移到其他基准（如EffiBench-X）是适度的，性能提升受限于任务特定的基线和参考设置。
