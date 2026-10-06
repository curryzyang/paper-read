# Retrieval-Centric Deep Learning in Growing Nonparametric Neural Networks

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Maximilian Schlegel, Rajai Nasser, Seijin Kobayashi, Yanick Schimpf, Oliver Sieberling, Robert Obryk, Kazuki Irie, João Sacramento, Johannes von Oswald
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03858v1) · [PDF](https://arxiv.org/pdf/2610.03858v1)

## TLDR
The paper develops Retrieval-Centric Deep Learning (RCDL), a growing nonparametric neural-network paradigm that stores key-value representations per data point and retrieves them via kernelized attention, derives principled functional-gradient learning rules for RBF/softmax-like kernels, and shows promising performance and efficiency while connecting advanced attention variants to conventional neural-network optimizers.

## Abstract
We investigate a general-purpose layer for deep learning that, instead of compressing arbitrary-size training data into fixed-size weight matrices, stores a new pair of key-value representations for every data point during training, and retrieves and recombines these representations through an attention mechanism at inference time - resulting in a growing neural net (NN). While Irie et al. (arXiv:2202.05798) have put forward this perspective from the classic duality expressing any linear layer in a deep NN trained by gradient descent as linear attention (LA) over the training data points, replacing LA by more powerful attention functions, as they suggest, turns out to be non-trivial: we show that naively applying learning rules from the LA case to advanced kernels does not lead to principled optimization. Here we fill this gap and develop functional gradient-based learning rules for kernelized attention layers, based on radial basis function (RBF) and softmax-like kernels - establishing the principled "retrieval-centric deep learning" (RCDL) paradigm. Empirically, we demonstrate the promising performance and learning-efficiency of RCDL on image classification and synthetic teacher-student learning tasks. Moreover, we show that replacing LA in the dual form of NNs by advanced LA variants, namely MesaNet/DeltaNet, yields a formal connection to recently proposed optimizers for conventional fixed-size NNs, offering a novel perspective on deep learning optimization.


## 精读解读（中文）
### 一、研究动机
传统深度网络将任意规模训练数据压缩进固定尺寸权重矩阵，既难以随数据增长而扩展，也削弱了样本级检索与重组能力。Irie 等从线性层与线性注意力的对偶出发提出 growing neural net，但把线性注意力替换为更强核注意力时，直接套用原学习规则并不构成有原则的优化。本文旨在填补这一缺口，建立面向核化注意力层的 functional gradient 学习规则，形成检索中心深度学习（RCDL）范式。

### 二、技术方案（Method）
RCDL 将每个训练样本存储为一对 key-value 表示，而不是压缩到固定权重中；推理时通过注意力机制检索并重组这些表示，使网络随训练数据增长而扩展。方法从梯度下降训练的线性层可写成对训练点的线性注意力这一对偶形式出发，针对基于 RBF 和 softmax-like 核的核化注意力层，用 functional gradient 推导学习规则。训练阶段更新样本键值与值表示，推理阶段执行查询、检索和加权组合；关键模块包括核化注意力检索层、非参数键值记忆和泛函梯度更新。实验在图像分类和合成 teacher-student 学习任务上验证该流程。

### 三、结果（Result）
作者表明，RCDL 在图像分类和合成 teacher-student 任务上展现出有前景的性能与学习效率，并说明朴素地把线性注意力学习规则迁移到高级核上并非有原则的优化。进一步地，将神经网络对偶形式中的线性注意力替换为 MesaNet/DeltaNet 等高级线性注意力变体后，可与近期针对常规固定尺寸神经网络的优化器建立形式联系。这为 growing nonparametric neural networks 的有效训练提供了可操作的学习规则。

### 四、结论（Conclusion）
本文提出并确立了 RCDL 这一有原则的检索中心深度学习范式，用核化注意力和泛函梯度规则替代传统的固定尺寸权重压缩。该视角既支持随数据增长的非参数神经网络，也通过 MesaNet/DeltaNet 等变体把注意力对偶与深度学习优化器联系起来。因此，RCDL 为深度学习的表示、检索和优化提供了一个新的统一视角。

### 五、方法论与关键技术细节
关键实现点包括：以每个数据点的 key-value 对构成随样本增长的非参数记忆，用 RBF 或 softmax-like 核化注意力进行检索与重组，并用 functional gradient 推导训练规则；从线性层对训练点的线性注意力对偶出发，将高级线性注意力变体 MesaNet/DeltaNet 与固定尺寸网络优化器形式关联。实验覆盖图像分类与合成 teacher-student 学习，但摘要未给出具体数据集规模、网络深度、准确率、学习率或核带宽等超参。局限在于非参数记忆和检索开销通常随训练点数增长，可能限制大规模部署，且核选择、泛函梯度实现和超参设置会影响稳定性与效率。
