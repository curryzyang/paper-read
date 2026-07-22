# SechKAN: Kolmogorov-Arnold Networks with Hyperbolic Secant Functions

- 区域：精读区
- 排名：3
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Hoang-Thang Ta
- 机构：University of Information Technology, Vietnam National University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18290v1) · [PDF](https://arxiv.org/pdf/2607.18290v1)

## TLDR
SechKAN proposes a Kolmogorov-Arnold Network using hyperbolic secant functions with parameter-efficient linear transformations, achieving superior performance on function fitting, PDE problems, and image classification compared to MLPs and other KAN variants while maintaining a similar number of parameters.

## Abstract
In recent years, Kolmogorov-Arnold Networks (KANs) have attracted increasing attention due to their effectiveness in machine learning and scientific computing tasks, offering a new paradigm for neural network design. In this paper, we present SechKAN, a KAN architecture based on hyperbolic secant (sech) functions. The hyperbolic secant basis is used for its smooth bell-shaped form, localized responses, and stable gradients. We employ 1D linear transformations to reduce the number of parameters, allowing SechKAN to remain comparable to multilayer perceptrons (MLPs) in model size. Experimental results indicate the effectiveness of SechKAN in function fitting, PDE problems, and image classification tasks on benchmark datasets, including MNIST, Fashion-MNIST, CIFAR-10, and CIFAR-100. SechKAN achieves superior performance compared to MLPs and other KAN variants while maintaining a similar number of parameters. However, its running time, while better than that of other KAN variants, is slightly longer than that of MLPs.


## 精读解读（中文）
### 一、研究动机
现有KANs参数过多、训练时间长，且B-spline等基函数在GPU上效率不高，亟需一种参数高效、GPU友好的新架构，在保持模型大小与MLP相当的同时提升性能。

### 二、技术方案（Method）
提出SechKAN架构，核心是使用双曲正割(sech)函数作为基函数，其光滑钟形、局部响应和稳定梯度特性有利于训练。每层先进行可选数据归一化（Norm1），再应用G个sech基函数得到含网格维度的表示，随后通过1D线性变换（网格投影）将最后一维从G压缩至1以大幅减少参数量。之后经过可选归一化（Norm2）、激活函数（如SiLU）和特征投影得到输出，同时采用跳跃连接将归一化后的输入直接加至输出。整个模型保持与MLP相当的参数量。

### 三、结果（Result）
在函数拟合、PDE问题（Navier-Stokes和浅水方程）以及图像分类（MNIST、Fashion-MNIST、CIFAR-10、CIFAR-100）基准测试上，SechKAN在参数量相当的情况下取得了优于MLP及其他KAN变体的性能。运行时间虽优于其他KAN变体，但略长于MLP。

### 四、结论（Conclusion）
SechKAN通过sech基函数和1D线性变换实现了参数高效、性能优越的KAN架构，验证了其在多项任务中的有效性，但仍存在训练时间略慢于MLP的局限。

### 五、方法论与关键技术细节
关键设计包括：sech函数光滑、有界且无穷可微，有助于稳定梯度但可能引发梯度消失；网格大小G控制基函数数量，影响模型容量；使用两步归一化（Norm1和Norm2）和跳跃连接提升训练稳定性；参数量减少策略为1D网格投影，使每层参数量与MLP相当；实验中对网格大小、激活函数和归一化策略进行了消融分析，提供了配置指南；局限性在于推理时间仍稍长于MLP，且对sech基函数的梯度行为需谨慎调参。
