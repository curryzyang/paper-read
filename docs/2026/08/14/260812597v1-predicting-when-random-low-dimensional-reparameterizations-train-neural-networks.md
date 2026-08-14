# Predicting When Random Low-Dimensional Reparameterizations Train Neural Networks

- 区域：精读区
- 排名：2
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Andrew Cheng, Ali Eslamian, Jie Cheng, Mehdi Zargham, Qiang Cheng
- 机构：University of Kentucky, University of Manchester, Miami University, University of Dayton, Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12597v1) · [PDF](https://arxiv.org/pdf/2608.12597v1)

## TLDR
The paper derives an orientation-resolved quadratic predictor for the latent dimension at which random low-dimensional reparameterizations can train neural networks, and introduces RaMaN, a memory-efficient framework that instantiates this predicted dimension using structured Hadamard or seed-regenerated Gaussian maps.

## Abstract
Neural networks can often be trained or fine-tuned through random low-dimensional reparameterization, where a small latent vector is mapped into a full parameter update by a frozen random map. This raises a practical question: how large must the latent search space be to reach a low-loss region? We first express the known accessibility transition in an equivalent conic form, centered for compact convex targets at the statistical dimension of the polar cone. Our main theoretical contribution is an orientation-resolved quadratic master formula that predicts the random-slice residual from both the curvature spectrum and the reference-to-solution displacement profile. It yields a self-consistent isotropic-orientation predictor and, in a conservative radius-only specialization, recovers the earlier Gaussian-width quadratic bound. Building on this analysis, we introduce Random Mapping Networks (RaMaN), which instantiate the predicted latent dimension using structured Hadamard or seed-regenerated Gaussian maps. These constructions avoid the O(dP) storage of dense random maps and reduce optimizer-state memory from O(P) to O(d). We also develop matrix-free curvature approximations and sweep-free dimension selection. Across controlled quadratic and neural-curvature experiments, the orientation-resolved predictor closely tracks measured transition locations and outperforms orientation-agnostic approximations when displacement direction matters. End-to-end experiments further show sharp, protocol-dependent training transitions across image and language models.


## 精读解读（中文）
### 一、研究动机
神经网络常可通过随机低维重参数化来训练或微调，即用一个小的隐向量经冻结随机映射生成完整参数更新。核心实际问题是：隐搜索空间需要多大才能到达低损失区域？已有的几何刻画依赖难以预先获取的高斯宽度，且半径近似未显式考虑位移相对于曲率特征方向的方向性，存在操作层面的空白。本文旨在发展一个可计算的、能根据局部曲率谱和参考点到解的位移轮廓预测所需隐维度的框架，从而避免逐维穷举。

### 二、技术方案（Method）
本文提出两类贡献。理论上，先将已知的可达性相变等价表述为锥形式：对紧凸目标，相变中心由极锥的统计维度刻画；随后推导方向分辨的二次主公式，输入为局部曲率谱（Hessian特征值）和参考点到解的完整位移轮廓，输出为随机切片残余的预测值，从而得到自洽的各向同性方向预测器，并在忽略方向的半径特例中恢复Larsen等人的高斯宽度二次界。方法上，提出Random Mapping Networks (RaMaN)：用结构化Hadamard映射（SHM，基于crop(H D I_Omega)的嵌套Hadamard基方向选择）或种子再生成高斯映射实例化预测的隐维度d，避免存储O(dP)稠密随机映射，并将优化器状态内存从O(P)降至O(d)。还开发了无矩阵曲率近似（基于主曲率方向和随机谱质量估计）与免扫描维度选择流程；支持方向解析选择（有位移估计时）、半径选择（仅有位移尺度时）和嵌套自适应扩展。训练时仅优化低维z，通过冻结映射生成完整参数θ，执行标准前向/反向传播。

### 三、结果（Result）
在受控二次型和神经曲率实验中，方向分辨预测器能紧密跟踪实测相变位置，并在位移方向重要时显著优于忽略方向的近似；端到端实验在图像和语言模型上展示了清晰且依赖训练协议的相变。方法上，RaMaN的Hadamard和种子高斯映射相比稠密随机映射大幅降低存储和优化器状态开销。整体结果表明，随机低维重参数化的可达性相变位置可以基于可测的局部曲率和位移信息预先预测，而非仅靠经验扫描。

### 四、结论（Conclusion）
随机低维重参数化能否成功取决于低损失区域的有效余维数，本文给出的方向分辨主公式将相变位置与曲率谱和位移方向联系起来，提供了可操作的隐维度选择准则。RaMaN框架在保持理论固定切片解释的同时，通过结构化或种子映射避免了稠密映射存储，使大规模应用成为可能。作者不声称所有大网络都能用极低维隐变量训练，而是明确了何时几何上可行、如何预测所需维度，以及映射结构、优化器和训练协议如何影响相变。

### 五、方法论与关键技术细节
数据/输入：目标网络参数θ∈R^P，隐变量z∈R^d，d<<P；使用冻结随机映射θ=g_ω(z)。建模：二次局部曲率模型，Hessian正半定，包含曲率谱与位移轮廓；主公式同时依赖位移方向与曲率特征方向，两个具有相同谱和相同位移范数的问题可能因方向不同而需要不同隐维度。实现关键：SHM用Hadamard基的嵌套裁剪选择，种子高斯映射的活动列形成固定虚拟高斯矩阵的前缀；均避免O(dP)存储。训练/推理流程：仅优化z，θ由映射生成；支持无矩阵曲率近似（用主方向加随机谱估计），免扫描维度选择，以及保持先前随机子空间的嵌套扩展。损失与协议：相变对训练协议（如优化器、学习率、重采样策略）敏感，基准需记录可训练参数、冻结映射存储、优化器状态、检查点大小和运行时间。局限性：精确谱信息在大规模无法获得，需近似；理论对紧凸目标严格，神经损失非凸，预测为启发式；层间高斯构造基于独立层假设，实际网络未必满足。
