# Diffusion-corrected Autoregressive Fourier Neural Operator for Droplet Evolution Prediction

- 区域：精读区
- 排名：5
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Jinghao Cao, Minsung Kang, Hongyue Sun, Chi Zhou, Jihoon Chung, Xubo Yue, Sanchoy Das, Bo Shen
- 机构：University of Georgia, University at Buffalo, Northeastern University, Hanyang University, New Jersey Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16238v1) · [PDF](https://arxiv.org/pdf/2607.16238v1)

## TLDR
The paper introduces the Diffusion-corrected Autoregressive Fourier Neural Operator (DiffARFNO), a two-stage framework that combines an autoregressive Fourier-MIONet for coarse prediction with a conditional Denoising Diffusion Implicit Model (DDIM) corrector to refine fine details, achieving state-of-the-art long-horizon droplet evolution prediction in inkjet printing.

## Abstract
Predicting droplet evolution in material jetting, or Inkjet Printing (IJP), is essential for maintaining printing quality. However, long-horizon forecasts remain challenging due to error accumulation and the complex coupling of process variables. In this work, we introduce the Diffusion-corrected Auto-Regressive Fourier Neural Operator (DiffARFNO), a two-stage framework that combines an autoregressive Fourier-MIONet with a conditional Denoising Diffusion Implicit Model (DDIM) corrector. Fourier-MIONet is trained as a coarse predictor and deployed autoregressively for long-horizon forecasting. In the second stage, a DDIM-based conditional corrector refines the coarse prediction within each sliding window through efficient iterative denoising. By combining coarse predictions from Fourier-MIONet with a DDIM corrector that restores fine details, DiffARFNO aims to provide high-fidelity predictions for long-horizon forecasts. Extensive experiments on droplet datasets from ANSYS Fluent demonstrate that DiffARFNO significantly outperforms existing state-of-the-art models.


## 精读解读（中文）
### 一、研究动机
喷墨打印中液滴演化预测对于保持打印质量至关重要，但长期预测因误差累积和过程变量复杂耦合而极具挑战。现有数据驱动方法难以实现高保真长期预测。

### 二、技术方案（Method）
提出DiffARFNO两阶段框架。第一阶段，使用Fourier-MIONet作为粗预测器，以初始50帧图像序列和材料属性（密度、粘度、表面张力）为输入，通过分支-主干结构（视频编码器、属性编码器、坐标网格投影）和UFNO解码器，自回归地生成粗预测序列。第二阶段，在滑动窗口内使用条件DDIM修正器对粗预测进行迭代去噪修正，恢复高频细节并校正累积误差。最终得到高保真长期预测。

### 三、结果（Result）
在ANSYS Fluent生成的液滴演化数据集上，涵盖韧带变薄、夹断动力学和卫星液滴形成三种典型场景。DiffARFNO相比FNO基准模型，在MAE、MSE、R²、IoU、PSNR、SSIM等指标上均获得更优结果，同时保持速度预测的准确性，证明其能有效减少误差累积并恢复精细结构。

### 四、结论（Conclusion）
DiffARFNO通过结合Fourier神经算子的高效粗预测和扩散模型的高分辨率修正，实现了对液滴演化长期高保真预测，优于现有SOTA方法。该框架有望提升喷墨打印过程监控与质量控制能力。

### 五、方法论与关键技术细节
数据来自ANSYS Fluent CFD模拟，包含不同材料属性的液滴演化图像序列。训练损失采用二元掩码加权的MSE损失，增强对液滴边界的关注。超参数包括滑动窗口大小、扩散步数等（文中未明确数字），但整体采用两阶段设计平衡效率与保真度。局限性可能包括对训练数据多样性依赖，以及极端物理条件下的泛化能力待验证。
