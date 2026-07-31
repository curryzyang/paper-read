# Recursive transformers for semiconductor thermo-mechanical reliability

- 区域：精读区
- 排名：6
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Kart-leong Lim
- 机构：Agency for Science, Technology and Research (A*STAR)
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27251v1) · [PDF](https://arxiv.org/pdf/2607.27251v1)

## TLDR
Recursive weight-sharing transformers offer an accurate, parameter-efficient, and compute-scalable surrogate modeling alternative to over-parameterized transformers for small, low-dimensional engineering datasets, as demonstrated on semiconductor thermo-mechanical reliability and electrostatic field prediction tasks.

## Abstract
Transformer-based surrogate models are increasingly used to replace expensive first-principles simulation in engineering design. But conventional transformer architectures are often over parameterized for the small, low-dimensional datasets typical of engineering design spaces, where large simulation data is expensive to generate. Under these conditions, excess parameter capacity leads to overfitting rather than improved accuracy, while also incurring unnecessary memory and compute overhead. This motivates a shift towards architectures that focus on additional compute rather than additional learnable parameters. This paper presents a hardware-aware evaluation of three recursive transformer paradigms for surrogate thermo-mechanical analysis of advanced packages: a)Tiny Recursive Model, b) our proposed Depth Recursive transformer, c) and a simple recursive transformer. We systematically compare their predictive performance (Recall, Mean Reciprocal Rank), parameter count, computational complexity (FLOPs), providing practical design guidelines for selecting recursive transformer architectures under resource-constrained scenarios. We validate this principle on two low-dimensional engineering prediction tasks: 1) thermo-mechanical reliability analysis of advanced semiconductor packages, where stress and warpage from thermal cycling must be evaluated repeatedly across a design-of-experiments sweep under costly finite element analysis (FEA). 2) Laplace PDE iterative numerical solver for capacitance field. Overall, recursive weight-sharing transformers provide an effective and generalizable trade-off between prediction accuracy, parameter efficiency, and computational cost for small data engineering surrogate modeling.


## 精读解读（中文）
### 一、研究动机
传统Transformer架构在小规模、低维的工程数据集上往往参数过多，容易过拟合且带来不必要的存储和计算开销；而工程设计中大规模仿真数据获取昂贵，因此需要转向更注重增加计算量而非增加可学习参数的架构。

### 二、技术方案（Method）
本文提出并评估三种递归权重共享Transformer范式：Tiny Recursive Model (TRM)、Depth Recursive Transformer (DEPTH)和Simple Recursive Transformer (SIMPLE)。所有模型共享一个可重复使用的Transformer模块RECUR（含自注意力、归一化、前馈网络及残差连接），通过不同递归策略在保持参数不变的情况下增加计算深度。TRM使用联合潜在状态（Z和Y）的耦合更新，内循环N=3次、外循环T=5次；DEPTH类似RNN，将顺序深度状态S^(t)经线性变换后作为递归输入，深度T=16；SIMPLE则将RECUR简单重复T次。输入为低维设计变量（如EMC热膨胀系数、弹性模量、芯片尺寸、间距等）及深度位置，输出为13×13×16或13×13×15的场图。训练采用BPTT，每个递归输出贡献损失项，评估指标为Recall@K和MRR。

### 三、结果（Result）
实验在三个数据集（FEA生成的Stress10k、Warpage10k以及PINN生成的电容器静电场数据集）上进行。Pareto分析表明：在MRR对FLOPs维度，不同数据集前沿不同，Stress10K为M1→M2→M3→M7，PINN为M1→M2→M6→M7，Warpage10K为M2→M7；TRM变体（M4-M5）不在任何前沿上。在MRR对参数维度，所有数据集的前沿完全由DEPTH模型（M6-M7）占据。DEPTH模型以最少参数和最低FLOPs之一获得最强或接近最强的检索精度；SIMPLE FLOP高效但精度受限，TRM则参数和计算均昂贵且精度无增益。

### 四、结论（Conclusion）
提出以深度作为递归注入输入的Depth Recursive Transformer（DEPTH）在准确率-参数和准确率-FLOPs权衡上表现最佳，验证了在小数据工程代理建模中，递归权重共享Transformer相比传统大参数Transformer更有效，特别是DEPTH的深度状态递归设计是取得优异权衡的关键因素。

### 五、方法论与关键技术细节
数据集与输入：Stress10k和Warpage10k由FEA生成，N=5^4×16=10000对，输入特征为[EMC_CTE, EMC_E, Size_dies, Gap_dies, S^(t)]，输出为13×13×16应力/翘曲场图；PINN数据集N=22^2×15=7265对，输入为[a,b,d^(t)]，输出13×13×15电场图。模型配置：M1为VANILLA 1-block LN；M2/M3为SIMPLE（1/3步）；M4/M5为TRM（1-Block RMS/LN，T=5,N=3）；M6/M7为DEPTH（1/2-block RMS，T=16）。训练细节：递归展开时使用BPTT，每个递归输出有单独损失项。评估指标：Recall和MRR。Pareto分析中，高FLOPs意味着GPU单请求耗时更长，且模型必须整体装入VRAM才能推理。局限性：TRM的额外参数和计算未带来相应精度提升，DEPTH在参数维度上独占前沿。
