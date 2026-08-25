# Bern2Edge: A Neurosymbolic Compiler for Edge Deployment via Bernstein Polynomial Networks

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Malak Gamal El-Din, Yifan Zhang, Yasser Shoukry, Sitao Huang, Salma Elmalaki
- 机构：University of California, Irvine
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20497v1) · [PDF](https://arxiv.org/pdf/2608.20497v1)

## TLDR
Bern2Edge is an end-to-end neurosymbolic compiler that distills pretrained feed-forward networks into Bernstein polynomial activations, enabling both high-fidelity LUT-based FPGA deployment and interpretable symbolic rule-based inference with large latency, BRAM, and DSP reductions on resource-constrained edge devices.

## Abstract
Deploying high-accuracy neural networks on resource-constrained edge devices remains challenging, as existing approaches treat training, compression, and hardware synthesis as separate stages, leaving a gap between software-trained models and efficient end-to-end deployment with limited support for interpretability. We propose Bern2Edge, an end-to-end framework that uses knowledge distillation to convert a pretrained teacher feed-forward network into hardware-efficient representations via Bernstein polynomial activations. This representation enables two deployment paths: (i) a high-fidelity LUT-based realization that preserves model fidelity under compression, and (ii) a symbolic rule-based representation derived from Bernstein activation geometry, enabling interpretable inference with explicit input-space constraints. The resulting BNNs achieve up to 2.12 percentage-point (pp) accuracy improvement over ReLU under identical compression constraints. At the system level, Bern2Edge achieves up to 99.8% latency reduction and 95.2% BRAM reduction relative to a W8A8 quantized teacher on an AMD Xilinx KV260 FPGA, while maintaining accuracy within 0.5 pp, and further deploys on a low-power Spartan-7 XC7S15 FPGA. The rule-based path reduces DSP usage by up to 89.0% at a cost of 1.5 pp in total accuracy.


## 精读解读（中文）
### 一、研究动机
高精度神经网络在资源受限的边缘设备上部署仍具挑战，现有方法将训练、压缩和硬件综合分离，导致软件训练模型与高效端到端部署之间存在鸿沟，且可解释性支持有限。因此需要一种端到端框架，从训练表示层面协同设计硬件高效与可解释的模型。

### 二、技术方案（Method）
提出Bern2Edge框架，通过知识蒸馏将预训练的前馈网络教师转换为采用Bernstein多项式激活的硬件高效学生网络（BNN）。训练过程使用蒸馏损失（交叉熵与KL散度加权）并加入越界惩罚，通过预热后逐层固定每神经元激活边界，使输入归一化到[0,1]。训练好的BNN支持两条部署路径：一是高保真LUT实现，将每个神经元的Bernstein激活离线预计算并存储为查找表，运行时仅需一次存储访问以消除激活计算；二是从Bernstein激活几何结构推导符号规则表示的路径，实现可解释推理并具有显式输入空间约束。最终通过硬件综合部署到FPGA。

### 三、结果（Result）
在相同压缩约束下，BNN相比ReLU学生网络精度最高提升2.12个百分点。系统级实现中，相对于W8A8量化教师在AMD Xilinx KV260 FPGA上，延迟最高降低99.8%，BRAM减少95.2%，同时精度保持在0.5个百分点以内，并可在低功耗Spartan-7 XC7S15 FPGA上部署。规则路径在总精度损失1.5个百分点的情况下，DSP使用量最高减少89.0%。

### 四、结论（Conclusion）
Bern2Edge首次联合利用Bernstein多项式激活的结构特性实现高效硬件综合与符号规则提取，验证了从教师模型到硬件部署的端到端统一流水线可行性，在精度、资源开销和可解释性之间取得了有利权衡，为边缘ML提供了一种新的神经符号编译范式。

### 五、方法论与关键技术细节
关键细节包括：Bernstein激活定义在固定归一化域[0,1]上，系数直接控制形状，具有单位划分性质；训练时先预热再逐层固定激活边界以避免持续漂移，并对越界输入施加惩罚（lambda_ob）且前向传播中截断归一化输入；LUT实现中每个激活函数在E个均匀网格点上离线预计算并存入BRAM，存储随神经元数和E线性增长；与PolyLUT等需限制扇入的方法不同，本方法保留密集MLP层；符号规则路径利用Bernstein几何结构提取规则，支持低比特量化且精度损失可忽略；实验覆盖多个表格数据集和Transformer FFN子层，并验证了规则网络对输入噪声和分布偏移的鲁棒性。局限性方面，论文正文未完整展开，但可推断规则路径存在一定精度成本（1.5 pp）。
