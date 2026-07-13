# How are linear representations learned? Exact solutions to the dynamics of abstraction

- 区域：精读区
- 排名：3
- 匹配度：2.9/10
- 来源：arxiv
- 作者：William W. Yang, Andrew M. Saxe, Peter E. Latham
- 机构：University College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08843v1) · [PDF](https://arxiv.org/pdf/2607.08843v1)

## TLDR
This paper provides an exact dynamical theory of how linear concept representations (abstraction) emerge during training, revealing key principles in linear and nonlinear networks including the roles of data/target geometry, depth, initialization, and an attenuation law whereby nonlinearities weaken abstraction in activations relative to preactivations.

## Abstract
In artificial and biological neural networks, concepts are often encoded as consistent linear directions in representation space. In deep learning, this idea is known as the linear representation hypothesis and underpins many interpretability and control methods based on linear probes, from concept detection to activation steering. Yet while prior work has studied whether such directions should exist $\textit{after}$ training, the dynamics of how they emerge $\textit{during}$ training remain poorly understood. Here, we develop a framework to study the alignment of concept directions during training - a process we call "abstraction". In a minimal linear network setting, we obtain exact solutions for the full trajectory of abstraction. These solutions reveal key analytic principles governing abstraction: (i) data and target geometry jointly determine abstraction at the end-of-learning, (ii) abstraction improves with network depth, and (iii) initialization scale controls the maximum abstraction reached during training. Extending our theory to nonlinear networks, we analyze how the choice of nonlinearity affects abstraction dynamics: erf networks approximate the linear theory, while abstraction in ReLU networks depends less on target geometry and more on input geometry. Across both, we prove a striking attenuation law: both nonlinearities weaken abstraction in activations relative to preactivations. We find evidence for this law in open models (DINOv3, Gemma 4) and apply our theory to improve linear probe generalization in LLMs. Together, our results provide a dynamical theory of abstraction with implications for interpretability and control.


## 精读解读（中文）
### 一、研究动机
尽管线性表示假说在深度学习中广泛用于可解释性与控制，但概念方向在训练过程中如何涌现（即“抽象”过程）的动力学尚不清楚。现有理论仅关注训练收敛后的存在性，而真实网络的抽象轨迹往往呈现非单调、未能达到完美的特性，亟需一个动力理论进行解释。

### 二、技术方案（Method）
以最小二乘线性网络为解析原型，假设输入与目标由两个二元潜变量（形状与颜色）生成，并遵循2FS块结构核。通过可变投影读出假设（即读出权重始终最优）简化损失，推导隐层表示核的矩阵Riccati方程，获得抽象余弦相似度的精确轨迹解析解。随后推广到任意深度线性网络及无限宽非线性网络（erf与ReLU），利用神经切线核分析非线性对抽象动力学的影响。

### 三、结果（Result）
精确解揭示：数据与目标几何联合决定学习结束时的抽象水平；网络深度增加可提升抽象；初始化尺度控制训练中能达到的最大抽象。在非线性网络中，erf网络近似线性理论，而ReLU网络降低目标几何影响、更依赖输入几何；且两类非线性均导致激活中的抽象弱于预激活（衰减定律）。该定律在DINOv3和Gemma 4等开放模型中得到验证，并用于改进大语言模型线性探针的泛化。

### 四、结论（Conclusion）
本研究建立了抽象训练动力学的理论框架，为理解神经网络中线性表示的形成提供了基本规律（深度正效应、初始化和非线性衰减等），对可解释性方法（如线性探针）和控制策略（如激活操控）具有直接指导意义。

### 五、方法论与关键技术细节
关键简化：假设数据核满足2FS块结构（仅五个参数），并采用变量投影读出（快速最优读出）。求解时利用矩阵Riccati方法，将两层线性网络的隐核动力学封闭。关键发现：深度线性网络中抽象随层数单调提升；非线性衰减定律源于激活函数对特征方向的扰动；局限性包括仅考虑两个二元概念、线性读出正则化假设、以及无限宽非线性近似可能偏离有限宽度行为。
