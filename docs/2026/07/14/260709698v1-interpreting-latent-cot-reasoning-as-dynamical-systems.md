# Interpreting Latent CoT Reasoning as Dynamical Systems

- 区域：精读区
- 排名：2
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Sabari Iyyappan Duraipandian, Shreya Sanjay Boyane, Manju Nagesh, Jerome Francis, Archana Vaidheeswaran, Kevin Zhu
- 机构：Worcester Polytechnic Institute, Algoverse AI Research, George Mason University, San Jose State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09698v1) · [PDF](https://arxiv.org/pdf/2607.09698v1)

## TLDR
This paper models latent chain-of-thought reasoning as a dynamical system, revealing that CODI exhibits stable attractor dynamics while COCONUT behaves as an unstable expanding system, with SIM-CoT supervision tightening but not altering these underlying behaviors.

## Abstract
Recent latent reasoning methods, such as CODI and COCONUT, face a fundamental interpretability problem: they maintain multiple superimposed candidate traces in the hidden space at each step, unlike explicit- CoT, which follows a single transparent reasoning trace. Existing mechanistic methods show compression, shortcuts, and superposition without explaining how reasoning evolves across latent steps. To address this gap, we model latent token sequences as trajectories in representation space and apply dynamical systems analysis to characterize the evolution of reasoning. Using quantitative measures, such as step-to-step change, direction consistency, and Lyapunov sensitivity, alongside qualitative projections, such as UMAP and DMD/PHATE, we show that latent CoT exhibits structured, non-random dynamics with two distinct stability classes. CODI behaves as a stable attractor, while COCONUT behaves as an unstable expanding system, and SIM-CoT supervision tightens both behaviors without changing the underlying dynamics. This framework advances the interpretability of latent CoT reasoning dynamics and provides actionable insights for improving latent reasoning performance. Code1 and Project page2 available online.


## 精读解读（中文）
### 一、研究动机
现有潜在推理方法（如CODI和COCONUT）面临根本的可解释性问题：它们在隐藏空间中维护多个叠加的候选轨迹，这与显式CoT跟随单一透明推理轨迹不同。现有的机械解释方法揭示了压缩、捷径和叠加现象，但未能解释推理如何在潜在步骤间演化。为填补这一空白，我们将潜在token序列建模为表示空间中的轨迹，并应用动力系统分析来刻画推理的演化过程。

### 二、技术方案（Method）
基于GSM8K数据集（8,792个数学应用题），使用CODI和COCONUT两种潜在CoT模型（均基于GPT-2-small骨干，124M参数，隐藏维度768），生成固定6步的潜在推理轨迹。提取每步的隐藏状态z_t ∈ R^768作为轨迹点。定量分析包括步间变化（L2距离）、方向一致性（余弦相似度）、弧长（累积位移）和Lyapunov敏感性（步长比值）。稳定性分析通过注入高斯噪声的扰动稳定性评估。定性分析使用UMAP、t-SNE、DMD和PHATE将高维轨迹投影到2D/3D空间。所有定量指标在原始表示上计算，不依赖降维。

### 三、结果（Result）
潜在CoT表现出结构化、非随机的动力学，存在两类不同的稳定性：CODI表现为稳定吸引子（Lyapunov敏感性为负，步间变化单调递减），COCONUT表现为不稳定扩张系统（Lyapunov敏感性为正，步间变化较大）。SIM-CoT监督使两类行为更紧凑（CODI的收敛更深入负值区域，COCONUT的波动更平稳），但不改变底层动力学类型。

### 四、结论（Conclusion）
该框架将动力系统分析引入潜在CoT可解释性，揭示了两种不同的推理演化模式，并为改进潜在推理性能（如通过调控稳定性）提供了可操作见解。

### 五、方法论与关键技术细节
数据：GSM8K全量（8792样本），按7个数学概念分层抽样，每类最多500样本。模型：GPT-2-small（12层，12头，隐藏768，词表扩展至50260含3个潜在特殊token），检查点来自公开仓库。潜在步数T固定为6。所有实验使用随机种子42，文本生成采用贪心解码。定量指标直接在高维原始表示上计算（不降维）。局限性：未在大规模模型（如7B）上验证；Lyapunov敏感性为代理指标，缺乏因果验证；仅分析GSM8K单一数据集。
