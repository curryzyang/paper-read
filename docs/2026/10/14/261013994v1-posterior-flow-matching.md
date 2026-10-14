# Posterior Flow Matching

- 区域：精读区
- 排名：1
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Chenrui Ma, Xi Xiao, Lin Zhao, Xinru Jiang, Tianyang Wang, Yanning Shen, Ferdinando Fioretto
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.13994v1) · [PDF](https://arxiv.org/pdf/2610.13994v1)

## TLDR
Posterior Flow Matching (PFM) extends flow matching by learning Gaussian posterior means and componentwise variances, enabling simultaneous transport prediction and endpoint-uncertainty diagnostics for improved generation across images, point clouds, molecules, and actions.

## Abstract
Flow matching learns how to transport noise toward data, but its mean prediction does not directly report the endpoint uncertainty remaining at an intermediate state. This paper introduces Posterior Flow Matching (PFM), a general generative modeling framework that learns conditional velocity means and componentwise variances with a Gaussian posterior model. The same model evaluation supplies both a transport prediction and endpoint uncertainty, making posterior diagnostics available throughout generation. These learned moments support a mean-driven ordinary differential equation (ODE) and a posterior-driven stochastic differential equation (SDE), whose local noise scales adapt to the predicted uncertainty. Across image, point-cloud, molecular, and action generation, PFM improves generation quality and provides endpoint-posterior readouts throughout generation.


## 精读解读（中文）
### 一、研究动机
流匹配能够学习将噪声输运到数据，但其均值预测并不直接报告中间状态处剩余的端点不确定性。该工作试图在生成模型中同时获得输运预测与端点后验诊断，使不确定性可在整个生成过程中被读取。

### 二、技术方案（Method）
PFM 以噪声到数据的流匹配为输入与训练场景，将条件速度分布建模为高斯后验，并由同一网络同时学习条件速度均值和逐分量方差。训练时拟合这些条件矩，推理时每次模型评估即可输出输运预测和端点不确定性；基于学到的矩可构造均值驱动的 ODE 采样器，以及由后验驱动、局部噪声尺度随预测不确定性自适应的 SDE 采样器。该框架覆盖图像、点云、分子和动作生成等多类数据模态。

### 三、结果（Result）
在图像、点云、分子和动作生成任务上，PFM 均提升了生成质量，并在生成全程提供端点后验读数。摘要未给出具体数值指标，但可复现结论是：同一模型评估即可同时支持高质量输运与不确定性诊断。

### 四、结论（Conclusion）
PFM 是一个通用生成建模框架，把端点不确定性直接嵌入流匹配的矩学习与采样过程。通过均值驱动 ODE 和后验驱动 SDE，它兼顾生成质量与生成过程的可诊断性。

### 五、方法论与关键技术细节
关键实现点包括：用高斯后验建模条件速度，学习均值和逐分量方差；同一次前向评估同时给出输运预测与端点不确定性；均值驱动 ODE 用于确定性输运，后验驱动 SDE 将局部噪声尺度与预测不确定性耦合；实验覆盖图像、点云、分子和动作生成。局限在于摘要未披露损失函数、方差参数化、噪声调度、额外计算开销与不确定性校准指标，SDE 采样还可能引入随机性及对步长和噪声尺度的敏感性。
