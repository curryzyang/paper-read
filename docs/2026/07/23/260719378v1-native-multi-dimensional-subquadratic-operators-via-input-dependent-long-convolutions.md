# Native Multi-Dimensional Subquadratic Operators via Input Dependent Long Convolutions

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：David R. Wessels, Farhad Ramezanghorbani, David W. Romero, Alireza Moradzadeh, Olivia Viessmann, Maksim Zhdanov, John St. John, Ken Janik, David M Knigge, Yucheng Tang, Erik J Bekkers, Saee Gopal Paliwal
- 机构：University of Amsterdam, NVIDIA, Cartesia AI, New Theory AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19378v1) · [PDF](https://arxiv.org/pdf/2607.19378v1)

## TLDR
HyenaND introduces a subquadratic, global, input-dependent operator that processes multi-dimensional data natively via long convolutions with implicitly parametrized kernels, achieving wall-clock speedups and matching or surpassing attention and recurrence-based models across genomics, vision, medical imaging, and PDE tasks.

## Abstract
Subquadratic alternatives to attention require compromises when applied to multi-dimensional data: standard convolutions lack global receptive fields and input dependency, while recurrent models require rasterizing data such as images, volumes, and partial differential equation (PDE) into an ad-hoc $1\rm D$ scan order that violates their spatial structure. We introduce \textit{HyenaND}, a subquadratic, global, input-dependent operator that acts directly on the native geometry of multidimensional data through convolutions with implicitly parametrized global, input-dependent multi-dimensional convolutional kernels. Our CUDA implementation, \texttt{nSubQ}, fuses the FFT-convolution path to turn HyenaND's $\mathcal{O}(L \log L)$ scaling into wall-clock speedups. Across long-context genomics, computer vision, medical imaging, and PDE modeling, pure HyenaND stacks match the accuracy of strong attention baselines, while hybrid configurations that interleave HyenaND and attention layers outperform both pure attention and strong recurrence-based hybrids.


## 精读解读（中文）
### 一、研究动机
次二次替代注意力在处理多维数据时需妥协：标准卷积缺乏全局感受野和输入依赖性，递归模型如Mamba需将图像、体积、PDE等光栅化为一维扫描顺序，破坏空间结构。同时，注意力的二次复杂度限制了高分辨率图像、3D医学扫描、长基因组序列等大尺度多维数据的处理，而缩小patch尺寸虽能提升精度却使token数回升，再次受限于二次复杂度。

### 二、技术方案（Method）
HyenaND将输入直接视为ND张量，通过隐式参数化的全局、输入相关多维卷积核进行ND卷积。核由可学习的寄存器嵌入经FiLM层调制得到，实现样本级输入依赖性同时保持线性时不变性。卷积通过ND FFT在频域计算，复杂度O(L log L)。CUDA实现nSubQ融合FFT卷积路径，采用IO感知、混合精度优化，将理论加速转化为实际墙钟加速。

### 三、结果（Result）
在长上下文基因组学、计算机视觉、医学成像和PDE建模上，纯HyenaND堆叠匹配强注意力基线（如ViT、Swin Transformer）；混合HyenaND与注意力层的配置在准确性上超过纯注意力和强递归混合（如Vision Mamba）。在1M token序列上，HyenaND前向时间比flash-attention快339倍，而Mamba在1M token时内存溢出。

### 四、结论（Conclusion）
HyenaND是首个同时满足次二次、原生多维、全局、输入依赖的算子，通过输入相关长卷积在多维数据中实现高效全局交互，可替代注意力作为多维视觉和物理建模的基本模块，且混合配置进一步提升了性能。

### 五、方法论与关键技术细节
使用ND卷积保持原生几何结构，无需光栅化；核基于FiLM调制的学习寄存器实现样本级输入依赖性，维持LTI归纳偏置以匹配自然信号的近似平稳性；训练采用ND FFT实现O(L log L)复杂度，nSubQ库通过融合FFT、谱调制和混合精度实现实际加速；局限性在于HyenaND专为LTI数据设计，对于非LTI的因果序列（如文本）不如Mamba，但混合注意力层可弥补。
