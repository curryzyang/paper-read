# CAT-Flow: Curvature-Adaptive sTeps for Flow Matching

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Qinchan Li, Pedro Cisneros-Velarde, Keru Fu, Samuel Antunes Miranda, Sharan Vaswani, Hao Zhang
- 机构：Simon Fraser University, VMware Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01746v1) · [PDF](https://arxiv.org/pdf/2609.01746v1)

## TLDR
CAT-Flow proposes two lightweight, training-free adaptive step-size algorithms (CAT-OV and CAT-OT) that leverage a connection between Flow Matching sampling and gradient flow to adjust step-sizes based on trajectory curvature, reducing required generation steps by up to 40% while maintaining image quality.

## Abstract
Flow Matching has emerged as a leading framework for generative modeling, powering state-of-the-art systems such as FLUX and Stable Diffusion 3.5. However, the iterative nature of its ODE-based sampling process creates a fundamental efficiency bottleneck: the quality of generated samples is highly sensitive to the choice of step-sizes, and current models typically require 20 to 30 steps for good quality. In this work, we propose two lightweight, training-free algorithms, CAT-OV and CAT-OT that adapt step-sizes at inference time based on a novel connection between Flow Matching sampling and gradient flow. Our algorithms are computed efficiently by not requiring additional neural function evaluations. Specifically, CAT-OT estimates curvature over time via a finite-difference approximation of the time-derivative of the vector field, while CAT-OV approximates curvature over the state space via a gradient of the vector field. Under suitable conditions, both methods have truncation error bounds of constant order. Empirically, CAT-OV and CAT-OT outperform existing step-size heuristics in image quality metrics across four text- to-image Flow Matching models, reducing the number of generation steps required to reach comparable quality by up to 40%.


## 精读解读（中文）
### 一、研究动机
文本到图像的流匹配模型（如FLUX、Stable Diffusion 3.5）依赖ODE迭代采样，但采样质量对步长设置非常敏感，通常需要20到30步才能取得好效果；现有固定步长、启发式步长或需额外训练/额外神经函数评估的自适应方法均未直接考虑ODE轨迹的几何曲率。因此，本文基于流匹配与梯度流之间新的理论联系，提出推理时免训练、无额外NFE的曲率自适应步长算法，以提升采样效率。

### 二、技术方案（Method）
输入为训练好的流匹配向量场u(x,t;θ)与初始噪声x0。作者先证明在相同初始条件下，流匹配直线流与特定梯度流具有相同解，从而将采样过程视为沿势能面的梯度流，并借鉴RMSProp等自适应优化器的思想。CAT-OT通过前后两个时间步向量场的有限差分近似向量场对时间的导数，用该曲率估计的范数动态调整当前步长；CAT-OV则利用历史向量场或其加权值的运行平均（一阶与二阶矩）构建RMSProp式曲率估计，并在状态空间维度上对更新步长进行归一化。两种算法都在现有生成迭代中直接计算，不调用额外神经函数，无需训练，推理时按自适应步长执行欧拉更新至t=1。

### 三、结果（Result）
在DiffDB真实用户提示下，CAT-OV和CAT-OT在四个文生图流匹配模型上均优于现有步长启发式；达到可比图像质量所需的生成步数最多减少40%，且只增加可忽略的墙钟时间和FLOPs。相比同步数基线，两种方法在CLIP、AES和HPSv3等指标上表现更好，较小步数设置下优势更明显。

### 四、结论（Conclusion）
流匹配采样可以等价地解释为梯度流，基于这一连接设计的曲率自适应步长方法能有效减少生成所需步数、提升采样效率。该方法是轻量且免训练的，可直接用于现有流匹配模型，也验证了几何曲率信息对设计采样算法的实用价值。

### 五、方法论与关键技术细节
方法核心是不引入额外神经函数评估，只对每次已获得的向量场做O(d)量级的算术运算；CAT-OT依赖相邻两步向量场差的有限差分，故在第一步无法直接估计时间方向曲率，需额外处理；CAT-OV使用β∈[0,1]的指数移动平均估计向量场的一阶和二阶矩，采用entrywise的平方与开方，整体步长受超参λ控制；二者在满足一定光滑性条件时具有常数阶截断误差上界。实验数据来自DiffDB，评估指标包括CLIP、AES和HPSv3；局限性是一阶欧拉式更新的基础框架对极端弯曲区域仍需较小步长，且理论与实现的曲率定义存在差异。
