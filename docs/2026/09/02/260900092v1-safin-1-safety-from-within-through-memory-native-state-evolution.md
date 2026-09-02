# Safin-1: Safety from Within through Memory-Native State Evolution

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Ming Zhang, Kaisen Yang, Shu Yu, Ermo Hua, Zhekai Chen, Cheng Jin, Jingnan Zheng, Yi Zhang, Zhongtian Ma, Jiawei Zhou, Sirui Chen, Qiaosheng Zhang, Xiang Wang, Ning Ding, Xia Hu, Bowen Zhou, Youbang Sun, Chaochao Lu
- 机构：Shanghai AI Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00092v1) · [PDF](https://arxiv.org/pdf/2609.00092v1)

## TLDR
Safin-1 introduces a family of foundation models that embeds safety and capability adaptation directly into the model's native memory via Memory-Anchor Routing across Context History (MARCH), using persistent, selectively routed "state anchors" and a detachable Safety State to enable test-time safety specialization without modifying the backbone.

## Abstract
Long-horizon complex tasks require foundation models to accumulate information, maintain internal states, and adapt over extended interactions. Safety should be an intrinsic property of the model itself, rather than a behavioral constraint relying solely on external safeguards or post-hoc alignment such as supervised fine-tuning. This motivates Safety from Within, where safety-relevant capabilities are represented and invoked through the model's native computation. We present Safin-1, a family of foundation models realizing this principle through memory routing and state evolution. Safin-1 is built on Memory-Anchor Routing across Context History (MARCH), a network architecture that maintains structured memory states and selectively retrieves relevant historical information through content-conditioned routing. It supports test-time adaptation of persistent capability states without repeatedly modifying the backbone, enabling controlled specialization over a shared foundation. We investigate this interface on downstream safety tasks through a Safety State, demonstrating effective state-based adaptation with substantial safety improvements. More broadly, the routed-state interface unifies contextual memory and persistent capability adaptation within the model's native computation, reframing memory from a passive record of prior context into an active substrate for maintaining and evolving model behavior. Evaluations across general capabilities, long-context understanding, retrieval, and efficiency further validate Safin-1. These findings provide a path toward safety as a state-native and adaptively maintainable capability. This work is only an initial architectural exploration of Safety from Within, and substantial further work is needed to realize this broader vision.


## 精读解读（中文）
### 一、研究动机
长程复杂任务要求基础模型在长时间交互中持续积累信息、维持内部状态并动态适应，而现有方法将安全视为外部护栏或事后对齐（如监督微调）所施加的行为约束，未能使安全成为模型自身的内在属性。作者提出“由内而外的安全”（Safety from Within）理念，认为安全相关能力应通过模型原生计算被表征和调用，而非依赖外部防护或事后修正。

### 二、技术方案（Method）
Safin-1基于MARCH（Memory-Anchor Routing across Context History）架构实现状态路由与状态演化。其核心方案为：采用Gated DeltaNet、Kimi Delta Attention或Gated DeltaNet-2等循环骨干，在文本边界后插入共享可学习锚点嵌入，周期性检查点保存累积循环状态形成可寻址的状态锚点；每个锚点通过与状态对齐的读取操作和输出投影生成内容相关的紧凑路由键，每个token通过路由机制在因果可见的锚点键与可学习的空选项之间进行选择，并将检索到的历史状态读出与当前循环路径残差融合。此外，该路由接口还支持持久能力状态，即在不修改冻结的共享语言模型骨干的前提下，将层级的持久安全状态（Safety State）与上下文派生锚点一起放入同一状态库，由现有路由器决定每个token的贡献，从而实现测试时安全状态适应。训练流程涉及匹配的持续预训练和监督微调，并开发了稠密与稀疏路由实现以支持长序列。

### 三、结果（Result）
在受控0.8B预训练研究中，MARCH一致提升了通用语言建模、LongBench、真实世界上下文检索和RULER NIAH的表现，并支持超出训练长度的外推。在规模扩展中，4B和35B-A3B变体在十个能力基准上的宏平均值分别从66.79提升至69.20、从76.25提升至78.35，在挑战性推理和竞赛级数学上提升最显著。在安全方面，状态原生安全专用化使平均越狱攻击成功率相对训练匹配的rank-8 LoRA控制降低42.3%，且具有更优的安全-过度拒绝权衡。

### 四、结论（Conclusion）
Safin-1通过将循环计算的时间轨迹转化为可寻址状态锚点库，并用同一路由接口承载上下文记忆与持久能力状态，证明了“由内而外安全”的可行路径：安全可以作为模型原生状态的一部分被选择性调用，并在测试时通过状态演化进行自适应维护，同时保持共享通用基础模型不动。该工作只是初步架构探索，但为安全作为状态原生且可自适应维持的能力提供了具体方向。

### 五、方法论与关键技术细节
关键细节包括：锚点策略按文本边界二分插入共享锚点嵌入，锚点不修改循环状态而只读取对应检查点以构建路由元数据；状态锚点维度为d_v×d_k，代表累积前缀状态而非局部片段；路由键通过独立投影矩阵W_k压缩到d_r维，实现内容条件寻址；检索到的历史状态读出与当前状态路径残差融合，保持底层循环更新不变；持久安全状态从有害与良性示例中学习，支持可插拔增减而无需重写骨干；安全评估同时报告越狱成功率与过度拒绝指标，以刻画权衡；稀疏状态路由在长序列（至128K）中选择压缩循环记忆而非token级键，提供注意力的状态级类比；该工作为初始探索，全面落地仍需大量后续工作。
