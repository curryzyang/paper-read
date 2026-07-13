# Reward Transport: Property Control in Flow Matching via Noise-Space Alignment

- 区域：精读区
- 排名：6
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Kehan Guo, Yili Shen, Yujun Zhou, Yue Huang, Chujie Gao, Shiyi Du, Xiangliang Zhang
- 机构：University of Notre Dame, Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08781v1) · [PDF](https://arxiv.org/pdf/2607.08781v1)

## TLDR
Reward Transport reframes the noise-data coupling in flow matching as a property-alignment interface, enabling inference-time distribution control via a single scalar coordinate without oracles or extra computation.

## Abstract
The coupling in flow matching -- the rule pairing noise vectors with data points -- is typically treated as a computational choice. We show that this coupling can instead serve as an alignment interface: by matching noise and data according to a target molecular property, it embeds controllable structure directly into the learned flow field. Building on this view, we introduce Reward Transport, which uses optimal transport coupling at training time to align a scalar noise-space coordinate with molecular rewards; at inference, varying this coordinate steers the generated distribution without requiring an oracle, reward model, gradient guidance, or additional computation. In the coupling-preserving limit, thresholding this coordinate recovers the Cross-Entropy Method's truncated reward distribution, providing a principled, continuously adjustable distribution-level control knob. Empirically, on ZINC-250K and GuacaMol, sweeping the scalar induces monotone control of logP and consistent QED control over its operating range; most tellingly, the same knob produces opposite structural responses for different targets, growing molecules for logP but shrinking them for QED, which rules out a generic size bias. The interface is complementary to classifier-free guidance and conditional flow matching, while a negative result under epsilon-prediction diffusion clarifies where coupling-level alignment is structurally absent. Code: https://github.com/KehanGuo2/reward-transport


## 精读解读（中文）
### 一、研究动机
流匹配中的噪声-数据耦合通常仅被视为计算选择，但本研究将其重新定义为对齐接口：通过根据目标分子属性匹配噪声与数据，可控结构可直接嵌入学习到的流场，无需推理时额外计算或模型修改。

### 二、技术方案（Method）
使用单调最优运输耦合，将噪声向量按均值池化后的L2范数排序，分子按目标属性（logP或QED）排序，然后秩匹配配对，形成1D最优运输方案。方向嵌入MLP将排序键（归一化后的s）作为额外输入注入网络。训练时每个epoch重采样噪声并构建耦合，采用插值路径上的MSE和交叉熵联合损失。推理时用户指定标量s值，从相应噪声积分得到生成分子。

### 三、结果（Result）
在ZINC-250K和GuacaMol上，调整单个标量s可实现logP的单调控制（范围3.14 logP单位，增加137%）和QED的一致控制。相同旋钮对logP和QED产生相反的结构响应：logP对应分子原子数从12增至23，QED对应原子数从23减至16，排除了通用大小偏差。Spearman秩相关分别为logP 0.57、QED 0.22。

### 四、结论（Conclusion）
流匹配中的耦合可作为对齐接口，通过最优运输以训练仅用属性信息的方式实现推理时分布级别的可控生成。该方法与无分类器引导和条件流匹配互补，提供了一个原理清晰、连续可调的分布控制旋钮。

### 五、方法论与关键技术细节
数据采用SELFIES表示的分子序列，属性为logP和QED。排序键为噪声平均池化的L2范数，方向嵌入为两层的GELU MLP。损失函数为MSE加交叉熵（λ=1），且对包含填充位的位置均计算。每epoch需对全部数据排序，但计算成本在分子数据集上可接受。局限性：控制质量依赖于耦合保持度（ρ_per），QED的ρ较低（0.22）导致控制不如logP精确；在ε-prediction扩散设置中，因缺乏耦合级对齐而无法工作。
