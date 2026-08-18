# SAGE: Surrogate-gradient Adaptation via Attention-Guided Entropy for Spiking Transformers

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Kiran Nair, Rodrigue Rizk, KC Santosh
- 机构：University of South Dakota
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13702v1) · [PDF](https://arxiv.org/pdf/2608.13702v1)

## TLDR
SAGE adapts the surrogate-gradient slope during training of Transformer-based spiking neural networks by using attention-entropy-derived block-level uncertainty, improving accuracy on CIFAR benchmarks without changing the inference architecture.

## Abstract
Spiking neural networks (SNNs) offer an energy-efficient alternative to conventional deep neural networks by exploiting sparse event-driven computation, but their training remains challenging because the non-differentiable spike function requires surrogate gradients whose fixed shape may be suboptimal across layers and training stages. In this work, we introduce SAGE, an uncertainty-modulated surrogate-gradient mechanism for Transformer-based SNNs. SAGE estimates block-level uncertainty from normalized self-attention entropy and uses this signal to adapt the surrogate-gradient slope during training while leaving the inference model unchanged. By modulating only the training-time surrogate parameter, the proposed method preserves the original architecture and deployment cost while improving optimization flexibility. Experiments on CIFAR-10/100 demonstrate that SAGE achieves improved accuracy over fixed-surrogate baselines, with results up to 1-2\% consistent gains across multiple simulation time steps. These results highlight the potential of attention-derived uncertainty as a lightweight training signal for adaptive surrogate-gradient learning in transformer-based SNNs.


## 精读解读（中文）
### 一、研究动机
脉冲神经网络（SNN）以稀疏事件驱动计算提供高能效，但训练中因脉冲函数不可微而依赖代理梯度，固定形状的代理梯度在不同层和训练阶段可能次优。现有方法对所有token使用统一梯度窗口，忽略了视觉token间的不确定性差异，导致深层梯度消失和注意力头死亡。因此需要一种能根据局部token不确定性动态调整代理梯度、同时保持推理模型不变的方法。

### 二、技术方案（Method）
SAGE基于Spikformer架构，仅修改训练时的反向传播。输入为CIFAR-10/100等图像，经脉冲分块和SSA模块得到注意力分数。对每个注意力头，使用温度T=0.25的softmax从detach的注意力分数构造辅助分布，计算归一化Shannon熵，再取跨头标准差作为不确定性信号D。随后对D做EMA平滑，维护运行均值/标准差，计算归一化并跨层中心化得到z，经死区控制器得到自适应代理梯度斜率alpha=alpha0+β*tanh(z)（或alpha0）。训练中BPTT使用该动态斜率计算代理梯度，前向推理完全不改变架构和参数。

### 三、结果（Result）
在CIFAR-10和CIFAR-100上，SAGE相比固定代理梯度基线持续提升精度约1-2%。具体地，Spikformer-4-384在时间步4下，CIFAR-10准确率从95.51%提升到96.32%，CIFAR-100从78.21%提升到78.69%，参数量保持9.32M不变。

### 四、结论（Conclusion）
SAGE通过注意力熵离散度作为轻量级不确定性信号，动态调制代理梯度斜率，仅训练时生效，不改变推理图、复杂度和延迟。实验验证了注意力导出的不确定性可用于适应性代理梯度学习，为深度脉冲Transformer提供更有效的优化灵活性，同时保持部署成本。

### 五、方法论与关键技术细节
关键细节：辅助概率分布使用detach的注意力分数和温度T_ent=0.25，确保不确定性估计不影响前向计算；熵采用归一化Shannon熵，跨头标准差比均值更具备判别性；使用EMA平滑和运行统计进行z-score归一化，并跨层中心化，死区抑制小波动；代理斜率函数为分段函数：|z|<δ时alpha=alpha0，否则alpha=alpha0+βtanh(z)；超参alpha0>0, β>0, δ>0；方法仅增加训练计算开销，推理零额外成本；局限性包括主要验证于CIFAR，ImageNet-200结果未在预览中给出，且需要根据数据集调整温度/死区等超参。
