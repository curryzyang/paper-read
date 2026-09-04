# Kernel Reboot: Breaking the Boundaries of Neural Tangent Kernels for Neural Fields

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Amir Mallak, Alaa Maalouf, Lior Wolf, Daniela Rus, Dan Rosenbaum
- 机构：Massachusetts Institute of Technology, Tel Aviv University, University of Haifa
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03117v1) · [PDF](https://arxiv.org/pdf/2609.03117v1)

## TLDR
This paper introduces NTK-KIP, MetaQuill, and their fusion MetaQuill-KIP to overcome the linearity and non-learnability of standard NTK-based neural fields, enabling compact non-linear representations, reusable priors, and lightweight few-shot inpainting/reconstruction from sparse observations.

## Abstract
Neural fields (NFs) map continuous coordinates to signals such as color or density, but fast high-quality reconstruction from sparse observations remains difficult. Classical Neural Tangent Kernel (NTK) regression gives closed-form fits, yet it is fundamentally linear and cannot accumulate reusable task priors. We develop three algorithms that address these gaps. NTK-KIP learns a distilled support set of coordinates (and optional labels) so that a finite NTK can inpaint large missing regions from little observed data, yielding a compact non-linear representation instead of a raw kernel solve. MetaQuill meta-learns a shared initialization for an INR so that new scenes can be adapted by updating only a small task-specific weight offset, which provides true feature learning and a reusable prior. Finally, MetaQuill-KIP fuses both ideas: it seeds the task with a KIP-style non-linear warm start, then refines only that small offset around the meta-learned initialization. MetaQuill-KIP achieves high-PSNR reconstructions and semantically plausible inpainting under very sparse observations, while requiring only lightweight per-instance adaptation, whereas diffusion-style baselines typically depend on large pretrained generative priors and costly per-image tuning. This shows that NTK-driven neural fields can be made both non-linear and meta-learnable, narrowing the gap between analytic kernels and practical few-shot reconstruction.


## 精读解读（中文）
### 一、研究动机
神经场（NF）将连续坐标映射为颜色或密度等信号，但从稀疏观测进行快速高质量重建仍然困难。经典神经正切核（NTK）回归虽然提供闭式解，但本质是线性模型，无法在函数空间中表达丰富结构，也无法跨任务累积可复用的先验；同时标准NTK对噪声和掩膜敏感，且在大规模神经场网格上存在高内存和高求解开销。为此，本文旨在弥合解析核与实际少样本重建之间的鸿沟，使NTK驱动的神经场具备非线性和元学习能力，从而在不依赖大规模预训练扩散先验的前提下实现快速、可学习的单图像重建与修复。

### 二、技术方案（Method）
本文提出三种NTK驱动的算法。NTK-KIP：利用蒸馏支持集（一组可学习的空间坐标及可选标签）代替全像素核求解，通过核函数反向优化支持集，使有限NTK在稀疏观测下修复大块缺失区域，形成紧凑的非线性表示。MetaQuill：在多个任务上元学习一个共享初始化θ_S，并为每个任务学习低秩权重偏移Δθ_i，测试时仅沿该低维偏移做几十步或单步梯度更新，绕开MAML昂贵的内部循环，获得可迁移特征与快速适应能力。MetaQuill-KIP：融合上述两者，先对单张目标图像执行KIP式支持集优化，得到蒸馏支持集和初始任务更新方向Δθ_i，然后固定共享初始化θ_S，仅非线性地精调该低维偏移，实现少量轻量步内的结构感知重建与语义合理修复。输入均为2D坐标（经原始或傅里叶位置编码FPE，默认k=20频段）并通过5层宽度256的MLP输出RGB或标量；训练/推理以MSE损失和NTK闭式核回归为基础。

### 三、结果（Result）
在MNIST数字场上，MetaQuill-KIP仅需50步精调即可达到32 dB以上PSNR，显著优于普通核回归约11 dB和MetaQuill的切空间更新约18-19 dB；MetaQuill可在约50步内将新数字重建至约20 dB PSNR，而从头训练的Single-INR需更长的优化才能接近。在RGB Flowers图像上，MetaQuill-KIP在极稀疏掩膜下产生视觉连贯的修复结果，PSNR和感知质量均优于朴素单图像基线，且仅需几秒适配；与Stable Diffusion、StrDiffusion、DDPM和GSDM等扩散模型相比，扩散模型在大观测区域和预训练语义先验下PSNR更强，但本文方法在无需外部文本条件和大规模预训练的情况下，以秒级速度和单图像监督实现从零适配的重建和修复。

### 四、结论（Conclusion）
该工作证明NTK驱动的神经场可以被改造为非线性和可元学习的，通过NTK-KIP注入非线性表示能力、MetaQuill提供真正的特征学习与可复用初始化，两者的融合MetaQuill-KIP统一了这些优势，实现了无需大型预训练生成先验的快速、可适应、逐实例重建与分析修复。这缩小了理论NTK结构与实际少样本重建之间的差距，为设备端个性化或单场景重建提供了实用方案。

### 五、方法论与关键技术细节
方法默认采用傅里叶位置编码（FPE）并设置频带数k=20，该值由实验确定；NF架构为5层隐藏层、每层256个神经元、输出RGB或单值。NTK-KIP的可学习支持集实质是一种任务自适应非线性先验，可有效压缩监督信号；MetaQuill使用共享初始化加低秩任务偏移，避免内循环优化，测试时只需更新低维Δθ_i，支持几十步或单步适应；MetaQuill-KIP将KIP式非线性热启动与元初始化后的低维精调结合。关键限制包括有限宽度NTK在密集网格上需要构造或应用大雅可比块，导致高内存和非平凡求解成本；MetaQuill的切空间线性化在大孔修复下仍有困难；扩散基线依赖大规模预训练和昂贵逐图优化，本文方法仅在无外部先验、单图监督场景中展现互补优势。
