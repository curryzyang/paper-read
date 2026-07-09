# Empirical Minimal-Realisation Compression of Deep Neural Networks via Controllability-Observability Tests

- 区域：精读区
- 排名：3
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Anis Hamadouche, Amir Hussain
- 机构：Heriot-Watt University, King Fahd University of Petroleum and Minerals
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.05457v1) · [PDF](https://arxiv.org/pdf/2607.05457v1)

## TLDR
This paper proposes a controllability-observability framework for compressing deep neural networks by viewing them as dynamical systems, using empirical Gramians to estimate and retain only the jointly reachable-observable hidden-state directions, achieving significant state and parameter reductions with minimal accuracy loss.

## Abstract
Deep neural networks often contain substantial hidden-state redundancy, but most compression methods operate directly on weights, neurons, or quantised representations without explicitly characterising the dynamical role of internal states. This paper proposes a controllability-observability framework for empirical state-order reduction of deep neural networks. By viewing a trained network as a depth-indexed nonlinear dynamical system, we construct data-driven reachability, observability, and balanced Gramians from hidden-state snapshots and output Jacobians. The resulting A/B/C tests estimate layer-wise reachable, observable, and jointly reachable--observable ranks. These ranks are then used not only as diagnostic measures of hidden-state redundancy, but also as actual compressed layer widths for realised reduced networks. Experiments on MNIST and CIFAR-10 compare the proposed balanced realisation against projection-based reduction, unstructured pruning, structured pruning, low-rank SVD, dynamic INT8 quantisation, and linear baselines. On MNIST, a four-layer SiLU DNN is reduced from state order 1024 to 277, giving 72.95% state compression and 73.48% parameter compression, while maintaining 95.45% accuracy compared with 96.60% for the full model. On CIFAR-10, a larger SiLU DNN is reduced from state order 4608 to 1339, giving 70.94% state compression and 83.09% parameter compression, while preserving accuracy from 54.45% to 54.44% and reducing CUDA inference latency by approximately 3X. The results show that balanced reachable-observable ranks provide a principled empirical minimal-realisation criterion for designing compact neural architectures with little or no loss in accuracy.


## 精读解读（中文）
### 一、研究动机
深度神经网络常含有大量隐藏状态冗余，但现有压缩方法多直接作用于权重、神经元或量化表示，未明确表征内部状态的动态角色。本文提出可控可观性框架，通过经验状态阶降来实现网络压缩。

### 二、技术方案（Method）
将训练后的前馈网络视为深度索引的非线性动态系统，隐藏状态快照用于构建数据驱动的可达Gramian（隐藏状态协方差），输出logits对隐藏状态的雅可比矩阵用于构建可观Gramian。通过A（可达性）、B（可观性）、C（平衡）测试估计每层的可达、可观及联合可达-可观秩，并将C平衡秩直接作为压缩后网络的层宽度。压缩后的紧凑网络从随机初始化训练，可选知识蒸馏辅助。

### 三、结果（Result）
在MNIST上，4层SiLU全连接网络状态阶从1024降至277，状态压缩72.95%，参数压缩73.48%，准确率从96.60%略降至95.45%。在CIFAR-10上，更大网络状态阶从4608降至1339，状态压缩70.94%，参数压缩83.09%，准确率保持54.44%（原54.45%），CUDA推理延迟减少约3倍。与投影降阶、非结构化剪枝、结构化剪枝、低秩SVD、动态INT8量化等方法相比，C平衡方法在精度保持和压缩率上表现最佳。

### 四、结论（Conclusion）
平衡可达-可观秩提供了原则性的经验最小实现准则，可用于设计紧凑神经架构，在显著降低状态阶和参数量的同时几乎不损失准确率。

### 五、方法论与关键技术细节
方法基于数据驱动的经验Gramians，依赖代表性数据集前向传播收集隐藏状态快照和反向传播计算雅可比矩阵，计算复杂度随网络宽度和数据集规模增加。采用SiLU激活函数，压缩网络从随机初始化训练，可选知识蒸馏损失。超参数如学习率（默认0.01）、优化器（SGD）等遵循常规设置。当前仅验证全连接网络，对卷积网络需通过全局平均池化定义状态；平衡秩选取需设定累积能量阈值（如保留99%方差）。
