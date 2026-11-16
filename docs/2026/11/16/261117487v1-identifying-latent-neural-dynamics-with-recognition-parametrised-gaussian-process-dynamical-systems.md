# Identifying Latent Neural Dynamics with Recognition-Parametrised Gaussian Process Dynamical Systems

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Arielle Rosinski, Qianqian Feng, Lior Fox, Maneesh Sahani
- 机构：University College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17487v1) · [PDF](https://arxiv.org/pdf/2611.17487v1)

## TLDR
The paper introduces RP-GPdyn, a generation-free latent dynamical systems model that combines a Gaussian-process transition function with recognition-parametrised inference to uncover meaningful, behaviorally relevant neural dynamics without relying on explicit generative observation models.

## Abstract
Neural circuits are densely interconnected systems, and many neural computations are thought to be mediated by the dynamical evolution of activity within these recurrent networks, a hypothesis often referred to as "computation through dynamics". Under this view, understanding computation within real neural populations depends on building models of the dynamical rules governing the temporal evolution of recorded high-dimensional neural activity. Most commonly, such models depend on explicit generative parameterisations of (i) the (nonlinear) intrinsic dynamical flow field and stochasticity, (ii) the (nonlinear) mapping from dynamical state to neuronal activity, and (iii) the variability of individual neural responses given that dynamical state. Misspecification of any of these components can bias estimates of dynamics and latent trajectories. In this paper, we circumvent generation-related issues by introducing the Recognition-Parametrised Gaussian Process dynamics (RP-GPdyn) model. RP-GPdyn models the dynamical flow field using a nonparametric Gaussian Process-defined transition function and models the relationship of dynamics to neural activity implicitly using the Recognition-Parametrised Model (RPM) framework. We show that this generation-free approach uncovers meaningful, behaviourally relevant latent variables and dynamics from both synthetic and experimental datasets.


## 精读解读（中文）
### 一、研究动机
神经计算常被认为由群体活动的低维动力学介导，因此需要从高维神经记录中估计潜在动力系统。现有潜变量动力模型通常显式参数化非线性流场、状态到神经活动的嵌入以及观测噪声，任一组件设定错误都会使动力学和潜在轨迹估计产生偏差。本文旨在构建一种无需显式生成观测模型、同时保留动力学可解释性的框架。

### 二、技术方案（Method）
RP-GPdyn将潜在马尔可夫动力学建模为非参数高斯过程定义的转移函数，并采用稀疏变分诱导点进行近似推断；GP先验进一步以学习到的固定点和局部雅可比矩阵为条件，使流场显式暴露固定点、局部稳定性和流几何。观测关系不通过参数化发射分布或噪声模型给出，而由Recognition-Parametrised Model框架隐式建模：联合分布为潜在先验乘以各时刻经验边际p0(x_t)与归一化识别因子g_phi(z_t|x_t)/G_phi(z_t)的乘积。训练时优化识别因子和GP变分后验，支持时间池化或时间特异的经验参考分布，并可自然纳入异质数据模态。

### 三、结果（Result）
作者在合成数据和实验神经数据上报告，RP-GPdyn能够恢复有意义且与行为相关的潜在变量和动力学。该生成无关方法避免了对观测噪声分布的显式假设，从而减轻噪声模型误设对潜在轨迹和动力学估计的影响。预览材料未给出具体定量指标或基线对比数值。

### 四、结论（Conclusion）
RP-GPdyn提供了一种兼具非线性随机动力学表达能力和机制可解释性的潜变量动力建模途径。它通过GP流场保留固定点与局部稳定性等可解释结构，并通过RPM避免 restrictive 的观测似然假设，适用于神经群体活动及异质观测数据的动力学分析。

### 五、方法论与关键技术细节
关键实现包括：GP核及其对输入的一阶、二阶导数构成联合协方差，以条件化固定点和雅可比矩阵；诱导点数量M固定计算成本；RPM用经验边际p0和归一化项G_phi保证联合分布归一化，因而不隐含Poisson观测假设；参考分布可选时间池化或时间特异，选择会影响模型行为。局限包括变分近似、核函数与参考分布选择、固定点/雅可比超参数优化及GP计算约束，且预览中缺少定量基准结果。
