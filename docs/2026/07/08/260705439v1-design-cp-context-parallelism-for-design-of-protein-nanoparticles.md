# Design-CP: Context Parallelism for Design of Protein Nanoparticles

- 区域：精读区
- 排名：8
- 匹配度：2.0/10
- 来源：arxiv
- 作者：Lorenzo Tarricone, Helen E. Eisenach, Aiko Muraishi, Charlotte M. Deane
- 机构：Ellison Institute of Technology Oxford, University of Oxford, University of Washington
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.05439v1) · [PDF](https://arxiv.org/pdf/2607.05439v1)

## TLDR
Design-CP introduces two context-parallel inference strategies for RFdiffusion 3 that distribute quadratic memory across GPUs, enabling end-to-end all-atom design of large symmetric protein nanoparticles without retraining.

## Abstract
Many all-atom generative protein models can in principle design large multimeric complexes by jointly modelling all chains, but their quadratic token- and atom-pair representations quickly exceed single-GPU memory as the number of chains and residues modelled grows. We introduce Design-CP, two context-parallel (CP) inference strategies for RFdiffusion 3 (1D row-sharding and 2D grid sharding with ring attention) that distribute the quadratic activations across a multi-GPU mesh while preserving pretrained weights. We characterise their scaling when sampling icosahedral assemblies, showing that the maximum feasible asymmetric subunit (ASU) size grows with the expected square-root trend in GPU count and that 2D sharding achieves better wall-clock scaling. Moreover, we show how strong point-group symmetry constraints make CP usable out of the box for end-to-end, all-atom design of icosahedral nanoparticles, yielding favourable in silico structural and interface metrics. Finally, we demonstrate octahedral nanoparticle design on a small cluster of workstation-grade 16GB GPUs, illustrating how Design-CP can be a practical path towards democratising large-assembly protein design.


## 精读解读（中文）
### 一、研究动机
许多全原子生成蛋白模型原则上可以联合建模所有链来设计大型多聚体复合物，但其二次的token对和原子对表示随着链数和残基数增长会迅速超出单GPU内存，限制了端到端设计大型对称蛋白组装的能力。因此需要一种多GPU上下文并行策略来扩展模型的可设计规模。

### 二、技术方案（Method）
提出Design-CP，为RFDiffusion 3设计了两种上下文并行推理策略：1D行分片和2D网格分片（使用环注意力）。1D行分片将每层的查询维度在P个GPU上分割，每个GPU仅持有行条带的pair表示（Z和P），键和值全量复制，注意力计算转为交叉注意力；2D网格分片将pair表示在√P×√P设备网格上分片，通过环注意力逐块计算，三角更新等操作仅在行列子组内通信。输入为蛋白质序列和原子坐标，使用预训练RFD3权重，在扩散采样过程中施加点群对称性约束（如二十面体），每步在多个GPU上并行计算注意力，仅交换必要的键/值分片。

### 三、结果（Result）
在采样二十面体组装时，最大可行不对称亚基（ASU）大小随GPU数量呈平方根趋势增长，2D分片方案的壁钟缩放优于1D方案。强点群对称性约束使得CP可以直接用于端到端二十面体纳米颗粒设计，产生优越的计算机内结构和界面指标；在小型16GB GPU集群上成功演示了八面体纳米颗粒设计，表明该方法可普及大型组装蛋白设计。

### 四、结论（Conclusion）
Design-CP通过多GPU上下文并行显著扩展了全原子生成模型RFDiffusion 3的设计能力，无需额外训练或微调即可端到端生成大型对称蛋白纳米颗粒，为大型组装蛋白设计的民主化提供了一条实用路径。

### 五、方法论与关键技术细节
关键实现细节包括：1D分片使用AllGather通信以复制键和值，2D分片使用环注意力仅在子组内通信，降低了通信量和临时内存开销；利用点群对称性约束（默认90%扩散步施加对称噪声）弥补因超过原生训练裁剪尺寸导致的质量下降；模型权重完全保持预训练值无重新训练；复杂性方面，pair表示内存被P台GPU分担（O(I^2/P)），但1D方案中三角运算需要全量收集，2D方案将收集限制在√P大小；局限性在于对称约束仅适用于具有强对称性的组装，对非对称或弱对称复杂体可能效果有限，且目前仅实现推理，未支持训练。
