# Architecture Generalization with MetaNCA

- 区域：精读区
- 排名：5
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Meet Barot, Daniel Berenberg, Sina Khajehabdollahi
- 机构：Independent Scholar, Mythos Scientific
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07743v1) · [PDF](https://arxiv.org/pdf/2607.07743v1)

## TLDR
MetaNCA introduces a neural cellular automaton that learns local weight update rules via a Weight Transformer with linear attention, enabling it to generate weights for diverse neural network architectures without backpropagation and generalize to architectures unseen during meta-training.

## Abstract
Self-organization is an emergent property of life, driven by the collective behavior of individual components acting on local information. Biological neurons, through local interactions transmitted through synapses, are able to learn efficiently and can adapt their connections over an organism's lifespan. Motivated by these desirable properties of adaptability and local interaction, neural cellular automata (NCA) models have been successful at learning morphogenesis solely through local update rules, demonstrating stability over many updates and robustness to perturbations. In this work, we introduce Meta Neural Cellular Automata (MetaNCA), a framework that learns local rules which self-organize the weights of artificial neural networks. A learned rule network iteratively updates the weights of a task network using only local interactions on the computation graph. We propose a novel Weight Transformer architecture for the local rule network, which uses linear attention to aggregate signals from neighboring weights and hidden states. Once trained, the rule network generates task networks of diverse architectures without backpropagation. We show that MetaNCA generates weights for feedforward MLPs, CNNs, and ResNets on MNIST and CIFAR-100, scaling to networks of 2 million parameters. We further show that MetaNCA generalizes to architectures not seen during meta-training, and that architectural diversity in the training phase strengthens this generalization.


## 精读解读（中文）
### 一、研究动机
反向传播训练神经网络存在内存消耗大、需要固定架构和大量样本等缺陷，而生物神经元通过局部交互和突触自适应实现高效学习。受神经细胞自动机（NCA）通过局部规则展现稳定和鲁棒性的启发，本文提出MetaNCA框架，旨在学习一种纯粹基于局部交互的规则，能够自组织生成任意架构人工神经网络的权重，并实现对未见架构的泛化，从而突破传统全局权重生成方法对特定架构的依赖。

### 二、技术方案（Method）
输入为MNIST和CIFAR-100数据集，任务网络包括MLP、CNN和ResNet等架构。MetaNCA由一个局部规则网络（Weight Transformer）构成：对于任务网络中的每个权重w及其隐藏状态h，定义其在前向（后突触）和后向（前突触）方向上的邻域权重和隐藏状态；使用两个独立的线性注意力模块（ELU特征映射+旋转位置编码）分别聚合前向和后向邻域信息，得到前向信号a_f和后向信号a_b；将[w, h, a_f, a_b]拼接为感知向量，输入一个MLP头，输出增量Δw和Δh，用于更新当前权重和隐藏状态。训练时，对任务网络进行T=10次局部规则迭代更新，每次随机更新80%的权重（模拟异步更新），计算任务网络在分类任务上的交叉熵损失，通过反向传播经过任务网络和局部规则网络的更新轨迹来更新局部规则网络参数φ（使用Muon优化器）；任务网络自身不通过反向传播更新，仅由局部规则网络生成。

### 三、结果（Result）
在MNIST和CIFAR-100上，MetaNCA生成了MLP、CNN和ResNet的权重，可扩展至200万参数。对于MLP，在三种训练架构（不同隐藏层宽度）下，生成的网络在未见过的宽度组合上取得与训练架构相近的测试准确率（例如热力图中(30,0)和(0,30)接近80%）。对于CNN，在两个训练架构（核大小3和5）下，生成的网络在核心小4（未见）上也表现出良好性能，平均准确率与训练架构相当。实验表明，训练时包含更多架构多样性（从3种增加到5种MLP）能提升对更广未见过架构的泛化能力。

### 四、结论（Conclusion）
MetaNCA是第一个能够学习单一局部更新规则、并在未见于训练阶段的多样化任务网络架构（MLP、CNN、ResNet）上自组织生成权重（达百万级参数）的方法。该方法通过纯粹基于计算图邻域的局部交互实现跨架构泛化，为克服反向传播的架构固定性和高内存消耗提供了一条新路径。

### 五、方法论与关键技术细节
局部规则网络仅依赖于计算图的局部拓扑（前向和后向邻域），不关心全局架构，因此天然支持跨架构泛化。使用线性注意力（ELU特征映射+旋转位置编码）实现邻域聚合，复杂度与邻域大小线性关系。隐藏状态初始化为正弦位置编码（包含层索引、前/后神经元索引、卷积核位置等），为规则提供架构先验。训练时随机dropout部分邻域向量，以减少对特定邻居的依赖，增强鲁棒性。每次迭代随机更新80%权重，模拟异步更新，提升稳定性。局限性：每个权重均需维护隐藏状态，对于极大网络（如数亿参数）内存开销较高；当前仅在分类任务（MNIST、CIFAR-100）上验证，未在更大规模数据集或更复杂架构（如Transformer）上测试；跨架构泛化的边界尚不明确，可能受限于训练架构的多样性。超参数方面，更新步数T=10，优化器Muon，具体学习率等未详细给出。
