# FedCausal-Dyn: A Causal-Dynamic Paradigm for Federated Learning under Dynamic Feature Drift

- 区域：精读区
- 排名：5
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Kaijie Chen, Alex Johnson, Maria Garcia, Wei Zhang, Daniel Kim
- 机构：Mindlab
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09695v1) · [PDF](https://arxiv.org/pdf/2607.09695v1)

## TLDR
FedCausal-Dyn introduces a causal-dynamic federated learning framework that disentangles invariant causal features from spurious domain-specific variations through adversarial training, enabling reliable prototype aggregation and collaborative regularization to achieve state-of-the-art performance under dynamic feature drift.

## Abstract
This paper addresses the challenging problem of dynamic feature drift in federated learning, where data distributions evolve across clients and over time -- a common scenario in real-world applications like financial technology. Existing approaches often assume static drift, limiting their effectiveness in non-stationary environments. To overcome this, we propose \textbf{FedCausal-Dyn}, a novel federated learning framework built on a causal-dynamic paradigm. Its key innovation is \textit{causal-domain feature separation}, which disentangles domain-invariant causal features from spurious, domain-specific variations via specialized projection heads and adversarial training. This enables \textit{reliable and dynamic prototype aggregation}, weighting local class prototypes by estimated reliability before global aggregation. We further introduce \textit{causal-feature guided collaborative regularization}, unifying prototype contrastive alignment and domain invariance into a cohesive objective. Extensive experiments on three federated domain generalization benchmarks demonstrate that FedCausal-Dyn consistently achieves state-of-the-art performance, with the highest average accuracy and the most stable results. Ablation studies confirm each component's critical contribution. Our work provides a robust and principled solution for federated learning under dynamic feature drift.


## 精读解读（中文）
### 一、研究动机
现有联邦学习方法通常假设静态的特征漂移，在金融科技等实际应用中数据分布随时间动态演化，导致模型泛化能力受限。本文旨在解决动态特征漂移这一挑战性问题，提出一种基于因果-动态范式的框架。

### 二、技术方案（Method）
提出FedCausal-Dyn框架，包含三个核心创新：(1) 因果-域特征分离：通过共享编码器G、因果特征提取器C和伪特征提取器S，结合对抗训练（梯度反转层GRL）和域判别器，将域不变因果特征与客户端特定的伪特征解耦；训练目标包括因果预测损失、域不变损失和域捕获损失。(2) 可靠动态原型聚合：每个客户端计算因果特征的类原型，并基于本地模型在验证集上的准确率或类内特征一致性分配可靠性权重，服务器按权重聚合全局原型。(3) 因果特征引导的协作正则化：统一原型对比对齐损失（InfoNCE形式）与域不变损失，平衡超参数λ。此外，采用隐私增强的因果特征混合机制，通过二进制掩码最大化域判别器的不确定性并保持语义相似性。整体本地训练总损失为L_Causal + γL_Reg + ηL_Spur。

### 三、结果（Result）
在三个联邦域泛化基准（Office-10、Digits、PACS）上，FedCausal-Dyn在所有数据集中达到最高平均准确率，并展现出最优的训练稳定性。消融实验验证了每个组件的关键贡献。

### 四、结论（Conclusion）
本文提供了一个鲁棒且原则性的解决方案，有效应对联邦学习中的动态特征漂移，通过因果特征分离和可靠性感知聚合显著提升了模型在非平稳环境下的泛化性能。

### 五、方法论与关键技术细节
数据分布被建模为动态域D_n^t；因果特征维度d_c和伪特征维度d_s为超参数；可靠性权重ω基于局部准确率或特征一致性计算；温度τ、平衡参数λ、γ、η为关键超参数；隐私混合采用二进制掩码优化满足sim(·)≥ε约束；全局分类器C_g通过混合特征更新；局限性包括可能的计算开销及超参数敏感性，有待进一步探索。
