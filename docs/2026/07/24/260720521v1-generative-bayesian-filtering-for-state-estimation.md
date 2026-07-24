# Generative Bayesian Filtering for State Estimation

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Lei Cao, Sihang Feng, Jixin Yan, Tao Sun, Naichen Shi
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20521v1) · [PDF](https://arxiv.org/pdf/2607.20521v1)

## TLDR
Generative Bayesian Filtering (GBF) replaces restrictive linear-Gaussian observation models with pretrained conditional variational autoencoders and uses score-based posterior sampling for flexible, robust state estimation from high-dimensional streaming data.

## Abstract
The state of a dynamic system evolves over time, switching among several latent modes that govern its observable behavior. Filtering methods infer the latent state from observations. Classical filtering approaches, including Kalman filters, typically rely on simple observation models, such as linear-Gaussian models, that are incapable of characterizing the increasingly nonlinear and heterogeneous patterns in high-dimensional sensor signals. To tackle the challenge, we propose Generative Bayesian Filtering (GBF), a filtering framework that replaces restrictive observation models with pretrained conditional generative models parametrized by conditional variational autoencoders (CVAE). For online inference, GBF performs a Bayesian prediction-update recursion in which the measurement update is formulated as a posterior sampling problem that combines the dynamical prior with the CVAE-induced likelihood. The resulting filtering problem is then transformed into a score-based sampling problem, which naturally inherits the flexibility from generative models and the uncertainty quantification capabilities from ensembling. Experiments on synthetic datasets and real-world applications involving manufacturing system monitoring and arrhythmia diagnosis demonstrate that GBF improves state estimation accuracy and robustness relative to baseline approaches.


## 精读解读（中文）
### 一、研究动机
经典滤波方法如卡尔曼滤波依赖于线性高斯观测模型，无法刻画高维传感器信号中日益非线性和异质的模式。为了在保持贝叶斯滤波框架的同时利用生成模型的灵活性，本文提出生成贝叶斯滤波（GBF）方法。

### 二、技术方案（Method）
GBF使用预训练的条件变分自编码器（CVAE）作为观测模型，取代线性高斯假设。在线推理时，执行贝叶斯预测-更新递归：预测步骤基于状态转移模型得到先验分布，更新步骤将测量更新转化为后验采样问题，结合动态先验与CVAE诱导的似然。该后验采样通过基于分数的采样方法（随机梯度Langevin动力学，SGLD）实现，利用CVAE的可微性通过反向传播优化潜在状态。输入为高维观测序列和低维状态转移模型，输出为状态的后验分布样本。

### 三、结果（Result）
在合成数据集、制造系统监测和心律失常诊断三项任务上，GBF相比卡尔曼滤波及其变体、深度状态空间模型等基线方法，在状态估计准确性和鲁棒性上有显著提升，尤其在观测噪声较大和存在分布偏移的场景下优势明显。具体指标包括均方根误差和负对数似然等，实验表明GBF能有效处理非线性、非高斯观测。

### 四、结论（Conclusion）
GBF将生成模型的灵活性与贝叶斯滤波的不确定性量化能力相结合，为高维观测下的低维状态估计提供了一种模块化框架。该方法无需重新训练完整模型即可利用预训练生成模型，适用于实时监测和诊断等应用，未来可扩展至更复杂的状态转移模型和多模态数据。

### 五、方法论与关键技术细节
关键方法细节：使用CVAE作为观测模型，其编码器将观测映射到潜在空间，解码器生成条件分布，似然通过重构误差隐式定义。后验采样采用SGLD，每次迭代对状态进行梯度更新并注入噪声，通过多次采样得到样本集合以量化不确定性。预训练阶段独立于在线滤波，降低计算负担。实验使用合成数据（切换线性动态系统）和真实数据（制造传感器、心电图），超参数包括SGLD步长和迭代次数。局限性：对生成模型质量敏感，若CVAE不能准确捕捉观测分布则滤波性能下降；采样过程可能计算耗时，需平衡精度与实时性。
