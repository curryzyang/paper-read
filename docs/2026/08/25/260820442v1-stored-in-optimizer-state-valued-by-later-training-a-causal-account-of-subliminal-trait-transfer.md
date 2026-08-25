# Stored in Optimizer State, Valued by Later Training: A Causal Account of Subliminal Trait Transfer

- 区域：精读区
- 排名：8
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Qinyang Xu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20442v1) · [PDF](https://arxiv.org/pdf/2608.20442v1)

## TLDR
Subliminal trait transfer is causally explained by a two-stage mechanism in which source perturbations are carried through the optimizer's first moment and only later assigned their behavioral value by subsequent training.

## Abstract
Subliminal trait transfer allows a student model to acquire behavioral dispositions from teacher-generated data in which the trait is not semantically expressed. Recent work explains how such signals enter gradients, but not how they survive source removal or acquire different signs under later training. We treat parameters and optimizer moments as a single trainer state and derive an exact transport-valuation identity separating observer-independent propagation of the source perturbation from the value assigned by a future continuation and behavioral readout. State surgery identifies the first moment as a causal carrier. Transplanting it alone leaves parameters, hidden states, and outputs unchanged at the cut, yet source-free updates generate growing parameter and hidden-state differences; transplanting parameters with the first moment recovers the terminal behavioral response. Sending the same source-induced difference through matched futures produces negative, near-zero, and positive Qwen effects (-0.658, +0.008, and +0.658 seed means). This ordering recurs in all 12 Llama-3.2-1B seeds after eight updates, while state-difference norms remain nearly equal across routes. Both contrasts grow in every paired seed when the continuation extends to sixteen updates. A full-horizon costate predicts all 42 Qwen route-mean signs and all 21 resolved Llama ordinary-route signs. Observer-independent transport also replicates across Qwen, SmolLM2, and Llama, while the complete-state recurrence predicts physical, hidden, and fixed-head responses in non-LoRA MNIST systems, including CNNs trained with AdamW and momentum SGD. Together, these results identify a two-stage mechanism for subliminal trait transfer: optimizer state transports the source perturbation, and later training determines its behavioral value.


## 精读解读（中文）
### 一、研究动机
已有工作只能解释亚阈值特质如何进入梯度，却无法解释在教师数据源被移除后该信号如何继续存留，以及后续训练中为何会获得不同符号。本文从因果角度研究亚阈值特质迁移，将优化器状态视为关键载体，并分离源扰动的传播过程与后续训练对行为价值的赋值过程。

### 二、技术方案（Method）
将模型参数与优化器动量（一阶矩等）共同视为一个训练器状态，推导出精确的传输-估值恒等式：源扰动以观察者无关的方式传播，未来继续训练与行为读出为其赋值。采用状态手术：在切割点仅移植一阶矩，保持参数、隐藏状态和输出不变，再进行无源更新；同时对比移植参数与一阶矩的完整状态。通过匹配的未来轨迹将同一源差异送入不同继续训练路径，并用全时域共态预测最终行为效应的符号。实验在Qwen、SmolLM2、Llama-3.2-1B以及非LoRA MNIST CNN（AdamW与动量SGD）上进行。

### 三、结果（Result）
同一源诱导差异经三种匹配未来路径分别产生负、近零和正的Qwen行为效应（种子均值 -0.658、+0.008、+0.658），该排序在全部12个Llama-3.2-1B种子中于8次更新后复现，且各路径状态差异范数几乎相等；当延续至16次更新时两个对比在每个配对种子中均增长。全时域共态预测了全部42个Qwen路径均值的符号以及全部21个已解析的Llama普通路径符号。传输机制在Qwen、SmolLM2和Llama间复现，完整状态递推也预测了MNIST CNN的物理、隐藏与固定头响应。

### 四、结论（Conclusion）
亚阈值特质迁移由两阶段机制构成：优化器状态（尤其一阶矩）负责携带并传播源扰动，而后续训练决定该扰动的行为价值与符号。该因果解释统一了参数与优化器状态，为理解和控制隐式行为特质迁移提供了新视角。

### 五、方法论与关键技术细节
关键点包括：状态手术中单独移植一阶矩在切割点不改变参数、隐藏状态与输出，但无源更新后产生持续增大的参数和隐藏状态差异；同时移植参数与一阶矩可恢复终端行为响应。不同未来路径的状态差异范数接近，说明符号反转并非来自扰动幅度差异，而是后续训练赋予的价值。方法涉及LoRA与非LoRA设置、AdamW和动量SGD优化器，并在多模型多种子下验证。摘要未提供完整超参与损失函数细节，也未报告计算复杂度或明确局限性。
