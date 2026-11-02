# Learning Stabilizing Latent Feedback Controllers via Multi-Step Backward Losses

- 区域：精读区
- 排名：1
- 匹配度：5.6/10
- 来源：arxiv
- 作者：Paul Lutkus, Lars Lindemann, Stephen Tu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40931v1) · [PDF](https://arxiv.org/pdf/2610.40931v1)

## TLDR
The paper proves that training latent linear dynamics models with sufficiently long multi-step reconstruction (“backward”) losses—rather than forward-prediction or single-step losses—provably yields latent models whose \(H_\infty\) output-feedback controllers, applied through the encoder, stabilize the original LTI system when the latent dimension captures all unstable modes, and illustrates the implications on a nonlinear flexible-arm system.

## Abstract
Can learned latent dynamics models support the design of feedback controllers that provably stabilize the original system? For linear time-invariant systems, we show that learning linear autoencoders and latent dynamics with multi-step prediction-reconstruction losses $\unicode{x2014}$ which we term "backward losses" as they encourage latent trajectories to reconstruct full state trajectories $\unicode{x2014}$ provably recovers the structure needed for stabilization. Specifically, a sufficiently long reconstruction horizon ensures that a minimum ${H}_\infty$-norm controller designed using the learned latent model stabilizes the original system through output-feedback via the corresponding encoder, provided the latent dimension is large enough to capture all non-stable modes of the underlying system. We also show why both reconstruction and a multi-step horizon are essential: forward prediction losses that require only low prediction error along latent trajectories admit global loss minimizers that discard unstable modes regardless of horizon length, while single-step reconstruction losses can yield latent models whose stabilizing controllers fail to stabilize the original system. Finally, experiments on a non-linear flexible-arm system illustrate the practical implications of our results for learning non-linear autoencoders and latent dynamics.


## 精读解读（中文）
### 一、研究动机
潜动力学模型/世界模型能从轨迹数据中以无模型、统一算法方式学习低维替代模型，但其用于反馈控制时缺乏闭环稳定性保证；传统降阶方法往往依赖真实动力学，且可能因截断或输出映射选择产生不稳定零动态。本文因此追问：用机器学习方法学到的潜动力学与编码器，能否设计出可证明稳定原系统的反馈控制器。

### 二、技术方案（Method）
针对线性时不变系统，论文学习线性自编码器（编码器E与解码器）及潜在线性动力学，并用多步预测-重构损失训练：在长度为H的滚动窗口内，要求潜轨迹不仅能预测，还能重构完整状态轨迹，作者称之为“backward losses”。随后在学到的潜模型上设计最小H∞范数控制器K(z)，再通过编码器构成输出反馈u=K(E(x))作用于原系统；理论分析给出充分条件：潜维数足以捕获原系统全部非稳定模态，且重构时域足够长，则该潜控制器可稳定原系统。非线性柔性臂实验用非线性自编码器和潜动力学比较不同损失，验证多步预测-重构损失的实际作用。

### 三、结果（Result）
理论上证明，多步预测-重构损失能可证明地恢复稳定化所需结构：只要潜维数覆盖所有非稳定模态且重构时域足够长，基于学习潜模型设计的最小H∞范数输出反馈控制器即可稳定原系统。论文还给出反例说明两个要素缺一不可：仅要求潜轨迹低预测误差的前向预测损失，无论时域多长都存在丢弃不稳定模态的全局最小解；单步重构损失则可能得到其稳定化控制器无法稳定原系统的潜模型。柔性臂实验中，只有多步预测-重构损失L_bwd使潜输出反馈控制器实现稳定。

### 四、结论（Conclusion）
多步预测-重构的“backward loss”为从数据学习潜动力学并设计可证明稳定的输出反馈控制器提供了理论基础，表明重构完整状态轨迹与多步时域对保留非稳定模态至关重要。该工作把世界模型式学习与闭环稳定性保证连接起来，并为非线性系统的经验表现提供启示；但严格保证目前限于线性时不变情形，非线性实验主要说明实践含义。

### 五、方法论与关键技术细节
关键实现与理论要点包括：对象为线性时不变系统，使用线性自编码器与潜在线性动力学，从轨迹片段学习而非依赖已知模型；损失为多步预测-重构损失，重构时域H需足够长，潜维数需至少覆盖全部非稳定模态；控制器为潜空间最小H∞范数控制器并经编码器做输出反馈。分析强调前向预测损失只约束潜预测误差会允许丢弃不稳定模态，单步重构也不充分，因此重构和多步缺一不可。假设可获得全状态以隔离降阶问题，未处理部分可观测与滤波；有限样本统计保证与非线性理论保证未给出，柔性臂实验为非线性实践验证。
