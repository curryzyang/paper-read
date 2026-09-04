# GPU-Accelerated Astrodynamics World Models for Spacecraft Rendezvous and Proximity Operations

- 区域：精读区
- 排名：7
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Duncan Eddy, Isaac R. Ward, Grace Ra Kim, Mykel J. Kochenderfer
- 机构：Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03067v1) · [PDF](https://arxiv.org/pdf/2609.03067v1)

## TLDR
This paper introduces the first world model-based approach to spacecraft rendezvous and proximity operations, combining a GPU-accelerated JAX docking simulator with a transformer-based "Out-of-this-World-Model" that predicts future observations via flow matching, demonstrating improved docking success, sample efficiency, out-of-distribution generalization, and anomaly detection over reinforcement learning baselines.

## Abstract
World models are an emerging paradigm in representation learning in which an agent jointly learns state-action dynamics and observation models from offline trajectory data, enabling multi-step planning and trajectory prediction with uncertainty estimates. They have shown strong results in robotics and game environments, but, to the best of our knowledge, have not previously been applied to the space domain. This paper introduces a world model-based approach to cooperative and non-cooperative spacecraft rendezvous and proximity operations. First, we introduce an open-source, JAX-based International Space Station (ISS) docking environment supporting parallel GPU simulation of spacecraft orbit and attitude dynamics, generating the thousands of state-action transitions that world model training requires. Second, we introduce Out-of-this-World-Model, a transformer-based world model that encodes relative kinematic states and body-fixed camera imagery into a latent state and predicts its evolution under commanded thrusts and torques using one-step flow matching. It produces a distribution over future observations, capturing stochastic dynamics and per-timestep uncertainty, and outperforms DreamerV3-style posterior-correction baselines with fewer trainable parameters and hyperparameters. Third, we apply the approach to a capsule autonomously docking with the ISS under keep-out-zone constraints, demonstrating improved sample efficiency and task performance over reinforcement learning baselines (53% versus 29% docking success across ports), better out-of-distribution generalization (on held-out ports the world model more than doubles baseline success, 40% versus 17%), and detection of anomalous objects encountered during approach with 98% classification accuracy. We open-source the simulation environment and model architecture to enable further study of this paradigm.


## 精读解读（中文）
### 一、研究动机
航天器交会与近距操作正从罕见的人控任务变为常规任务，但传统GNC分解依赖精确解析模型且难以直接融合相机等丰富观测；现有学习方法或只能回归状态动力学、或仅学策略而缺乏可复用系统模型。世界模型虽在机器人和游戏领域取得成功，却尚未应用于空间领域。本文首次将世界模型引入航天交会与抵近操作，以学习联合的状态-动作动力学与观测模型，从而支持多步规划、不确定性估计和异常检测。

### 二、技术方案（Method）
本文提出两大部分：(1) 开源JAX仿真环境AstroJAX及ISS对接环境，支持GPU大规模并行仿真轨道与姿态动力学，生成数千条状态-动作转移数据；(2) 世界模型Out-of-this-World-Model（OWM），采用模态参数化编码：MLP编码相对运动学状态，视觉Transformer（带注意力瓶颈的交叉注意力）编码本体相机图像，动作经MLP投影为条件token，与状态/图像token拼接成每时间步的潜在状态。主干为分解式时空Transformer：空间注意力在同一时间步token间双向融合，时间注意力在滑动窗口内因果跨时间步融合，并配合旋转位置编码与KV缓存实现线性自回归。预测头使用一步流匹配（flow matching）将高斯噪声输运到潜在残差分布的样本，加上当前潜在状态得到下一时刻潜在状态；通过多次采样生成未来观测分布。训练时从离线轨迹数据集学习条件分布p(o_{t+1}|h_t)，观测解码器将潜在状态映射回图像和状态预测。规划阶段将OWM与模型预测路径积分控制（MPPI）结合，在保持区约束下采样控制序列并评估未来后果。

### 三、结果（Result）
在自主对接国际空间站（ISS）任务中，OWM结合MPPI在所有八个对接端口的成功率达53%，而强化学习基线为29%；在未见过的保留端口上，世界模型使基线成功率翻倍以上（40%对17%），展现出更好的分布外泛化。在接近路径异常物检测中，模型达到98%的分类准确率。相比DreamerV3式后验校正基线，OWM以更少可训练参数和超参数取得更高预测性能。

### 四、结论（Conclusion）
本文首次将世界模型应用于航天器交会与抵近操作，证明了联合学习动力学与观测模型的空间任务范式可行。OWM不仅能生成对未来观测的分布预测、量化每步不确定性，还能与采样式规划结合提升对接成功率与样本效率，并在分布外端口泛化和异常检测上优于强化学习基线。作者开源了仿真环境、模型架构与训练数据集，供后续研究该范式在空间领域的应用。

### 五、方法论与关键技术细节
关键实现细节：输入包括相对运动学状态（带传感器噪声）和本体相机图像，动作由推力与力矩命令组成，模型对奖励不可知。OWM的训练不使用观测重构损失，而采用潜在空间一步流匹配预测残差，结合防坍缩正则化策略（如方差/协方差惩罚或各向同性高斯正则器）。时空分解注意力将计算复杂度从全序列二次降为各轴分别二次，KV缓存令自回归推理随视界线性。仿真与训练数据由GPU并行生成，可覆盖合作与非合作目标。局限性包括：世界模型缺乏Kalman滤波器的最优性保证，长时预测误差累积仍需关注，且当前实验基于仿真环境，迁移到真实航天器需处理传感器噪声与实际动力学偏差。超参数与复杂度方面，OWM比DreamerV3基线更少参数量和超参数，具体数值见论文正文。开源地址包括模型库、环境库与HuggingFace数据集。
