# Lecture notes on Physics Informed Neural Networks, Neural Operators, and their applications

- 区域：精读区
- 排名：2
- 匹配度：5.8/10
- 来源：arxiv
- 作者：Alessandro Bombini
- 机构：Istituto Nazionale di Fisica Nucleare
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17638v1) · [PDF](https://arxiv.org/pdf/2609.17638v1)

## TLDR
These lecture notes provide a PhD-level introduction to Physics-Informed Neural Networks and Neural Operators, covering their implementation in PyTorch and NVIDIA PhysicsNeMo as well as applications in engineering, physics, and petroleum reservoirs, with recent topics such as Mixture-of-Models, Fourier Neural Operators, and Physics-Informed Kolmogorov-Arnold Networks.

## Abstract
This is the set of lecture notes for the PhD course \href{https://www.unibz.it/en/faculties/engineering/phd-computer-science/study-course-offering/2025/36967}{\textit{Physics Informed Neural Network}, held at the University of Bozen/Bolzano} in the academic year 2025/2026.
  The goal of the course was to introduce the concept of Physics Informed Deep Neural Networks (PINN) and Neural Operators (NOs), discuss their implementation from scratch in PyTorch and using advanced ad-hoc developed open-source libraries such as NVIDia PhysicsNeMo to address real-world problems in various fields (engineering, physics, petroleum reservoir). We discuss recent topics such as Mixture-of-Models, Fourier Neural Operators, Physics-Informed Kolmogorov-Arnold Networks (PIKANs) and Fourier Neural Operators.


## 精读解读（中文）
### 一、研究动机
该材料的动机是服务于博岑/博尔扎诺自由大学2025/2026学年博士课程，向研究者介绍物理信息深度神经网络（PINN）与神经算子（NOs）的概念及实现。课程强调从零用PyTorch和NVIDIA PhysicsNeMo等开源库构建模型，以处理工程、物理和石油储层等现实问题。

### 二、技术方案（Method）
讲义以课程讲授和代码实践形式组织，输入/数据未在给定摘要与前言中展开；关键模块包括PINN、NOs、Mixture-of-Models、Fourier Neural Operators和Physics-Informed Kolmogorov-Arnold Networks（PIKANs）。实现路径同时覆盖从零PyTorch实现与使用NVIDIA PhysicsNeMo等专用开源库，目标是在多领域实际问题上应用这些方法；但具体建模、训练/推理流程与超参未在所给材料中给出。

### 三、结果（Result）
给定材料未报告实验指标、数据集、基准对比或可复现数值结果；其可见结果是形成一套博士课程讲义，并列出涵盖PINN、NOs、FNO、PIKANs等主题及PyTorch、PhysicsNeMo工具链的教学内容。LaTeX前言显示正文由lecture1至lecture5及附录A等章节组成。

### 四、结论（Conclusion）
该讲义定位为PINN与神经算子的教学与实现入门材料，强调从概念到开源库实践并面向工程、物理和石油储层应用。由于提供的是摘要和前言而非完整正文，无法据此得出具体科学结论或性能结论。

### 五、方法论与关键技术细节
关键细节包括课程于University of Bozen/Bolzano 2025/2026学年开设，标题为Physics Informed Neural Networks, Neural Operators, and their applications，作者为Alessandro Bombini（INFN Firenze）。文档使用memoir等LaTeX宏包并配置Python listings，include章节为abstract、acknowledgements、lecture1-5和appendixA，主题含Mixture-of-Models、FNO、PIKANs和PhysicsNeMo。主要局限性是全文预览仅含导言区，未提供数据、先验、损失函数、超参、复杂度约束及实验结果。
