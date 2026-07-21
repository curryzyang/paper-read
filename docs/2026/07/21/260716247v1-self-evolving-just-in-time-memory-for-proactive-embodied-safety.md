# Self-Evolving Just-In-Time Memory for Proactive Embodied Safety

- 区域：精读区
- 排名：1
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Bingrui Sima, Lizhong Wang, Xiaoya Lu, Kun He, Xiao Yang
- 机构：Tsinghua University, Shanghai Jiao Tong University, Huazhong University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16247v1) · [PDF](https://arxiv.org/pdf/2607.16247v1)

## TLDR
The paper introduces the Self-Evolving Just-In-Time Memory framework, which uses a Risk-Sufficient Topological Belief Graph, Agency-Grounded Factual Memory, and Experience Memory with a Test-Verify-Write loop to enable embodied agents to proactively mitigate dynamically emerging hazards without stalling task progress.

## Abstract
While Vision-Language Models (VLMs) have empowered embodied agents to execute complex household tasks, they struggle to proactively handle dynamically emerging hazards during closed-loop interactions. Existing safety approaches often rely on runtime guardrails to block unsafe actions or induce excessive caution, which severely stalls task progress instead of actively resolving the underlying risks. To break this safety-progress trade-off, we introduce the Self-Evolving Just-In-Time Memory framework, which reframes embodied safety from progress-stalling guardrails to proactive hazard mitigation. The framework consists of a Risk-Sufficient Topological Belief Graph (RSG) for persistent safety-relevant state tracking under partial observability, an Agency-Grounded Factual Memory for precise hazard anticipation, and an Experience Memory that injects procedural Meta-Skills to guide executable, progress-preserving mitigation. Furthermore, we propose an automated Test-Verify-Write loop, allowing agents to continually refine their mitigation Meta-Skills from execution traces at test time. Experiments on IS-Bench demonstrate that our framework substantially boosts the Safe-Success rate across multiple VLM backbones (e.g., +30.3% on Qwen3-VL-8B), enabling agents to proactively mitigate hazards without stalling task progress. Code is available at https://github.com/DyMessi/JIT-Memory.


## 精读解读（中文）
### 一、研究动机
现有VLM驱动的具身代理在执行复杂家庭任务时，难以主动处理闭环交互中动态出现的危险。现有安全方法要么依赖运行时护栏阻止不安全动作，要么引发过度谨慎，严重阻碍任务进展而非主动解决潜在风险。为了打破这种安全-进展权衡，本文提出了Self-Evolving Just-In-Time Memory框架。

### 二、技术方案（Method）
框架包含三个核心模块：Risk-Sufficient Topological Belief Graph (RSG)作为工作记忆，采用动作条件patch更新在部分可观测下持续跟踪安全相关状态；Agency-Grounded Factual Memory将抽象人类安全规范编译为可触发、可验证的规则，映射到代理动作空间，实现精确的意图条件危险预测；Experience Memory注入过程性Meta-Skills，提供可执行的缓解指导和时机。此外，提出自动化的Test-Verify-Write循环，在测试时通过程序化验证执行轨迹并挖掘成功案例，不断优化Meta-Skills。每步中，规划器先产生动作和预测意图，RSG更新后，事实记忆检查是否存在情境风险或时间风险，触发时注入相应Meta-Skill指导下一步动作。

### 三、结果（Result）
在IS-Bench基准上，该框架在多个VLM骨干上显著提升了安全成功率（Safe-Success rate），例如在Qwen3-VL-8B上提升30.3%。代理能够主动缓解危险而不停滞任务进展，有效打破了安全与进展的权衡。

### 四、结论（Conclusion）
该框架将具身安全从阻碍进展的护栏重构为主动危险缓解，通过协调三个专门记忆模块和自演化循环，实现了持续提升的主动安全能力，同时保持任务进展。实验证明该方法能显著提升安全成功率，且对多种VLM骨干有效。

### 五、方法论与关键技术细节
RSG使用有限但充分的语义词汇表（如SAFETY_FLAMMABLE标签、动态状态、拓扑关系），确保风险足够性并支持零样本泛化。事实规则通过离线编译有限安全原则得到，实例解耦并与RSG词汇对齐，通过精确子图匹配触发，避免过度谨慎。Test-Verify-Write循环利用RSG历史快照自动验证执行轨迹，无需人工标注。动作条件patch更新仅处理局部子图，避免全场景重解析，降低计算开销。框架依赖于预定义规则集，对未见危险场景的泛化可能受限。
