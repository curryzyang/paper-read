# A Study of Conditional Diffusion Models for Open-Loop Control under Dry Friction and Stiction

- 区域：精读区
- 排名：5
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Eric Aislan Antonelo
- 机构：Federal University of Santa Catarina
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01756v1) · [PDF](https://arxiv.org/pdf/2609.01756v1)

## TLDR
Conditional action-sequence diffusion models trained on state-to-state control data provide an effective, sample-efficient proposal distribution for open-loop control under dry friction and stiction, reducing terminal error and stuck steps compared to uniform/structured random shooting and CEM.

## Abstract
Diffusion models have recently emerged as expressive generative priors for planning and control. This paper studies Action Diffusion, an action-sequence diffusion formulation used as an open-loop proposal distribution for a point-mass system with dry friction and stiction. In this benchmark, motion starts only when the applied input exceeds a static-friction threshold, so effective controls occupy a small and temporally structured subset of the action-sequence space. A compact conditional 1D U-Net generates bounded control sequences conditioned on initial and target states. We compare it with uniform random shooting, random shooting from the same structured dataset prior, and the Cross-Entropy Method (CEM). Results show that Action Diffusion reduces terminal error and stuck steps, especially in low-sample regimes. These results indicate that conditional diffusion provides an effective mechanism for generating temporally coherent control sequences that overcome stiction by conditioning and recombining structured control primitives from the training prior for state-to-state open-loop control.


## 精读解读（中文）
### 一、研究动机
干摩擦与静摩擦使质点系统只有在控制输入超过静摩擦阈值时才开始运动，因此有效的开环控制序列在整个动作序列空间中只占很小的、具有较强时序结构的子集；均匀随机采样或无目标条件的结构化先验难以稳定给出符号、幅值和时机都合适的控制。论文旨在研究一种动作序列扩散模型作为状态到状态开环控制的采样提议分布，利用初末状态条件化提升低样本量下的控制质量，并作为高维扩散控制研究之外的一个可解释低维基准。

### 二、技术方案（Method）
方法是在H=64的离散控制序列上构建条件扩散模型p_theta(u_0:H-1|x0,x*)，其中x0和x*为初始与目标状态，条件向量为c=[x0^T,x*^T]^T，通过MLP注入去噪网络。数据由合成方式得到：先从包含高幅kick、中幅和近零三类分段并经一阶滤波和裁剪的结构化控制先验中采样候选序列，再利用已知的干摩擦/静摩擦动力学前向rollout得到对应终端状态，形成训练集和验证集。去噪网络是紧凑的条件1D U-Net，由Conv1D、ResBlock1D、下采样/上采样和跳跃连接组成，使用GroupNorm、SiLU、时间正弦嵌入和条件嵌入。训练采用标准噪声预测MSE损失、余弦噪声调度，并以p_drop=0.2随机丢弃条件来实现classifier-free guidance。推理时用DDIM进行50步采样，combined conditional/unconditional预测并采用guidance scale=2.0。对每个目标状态生成K条候选控制序列，用已知动力学rollout后按终端误差||x_H-x*||_2选最优；多段参考目标则按状态序列分段进行开环组合规划。对比基线包括均匀随机shooting、同一数据集先验的无条件随机shooting以及CEM。

### 三、结果（Result）
在小位移目标如x*=(0.2,0)的任务上，Action Diffusion可以生成大量靠近目标轨迹的候选，并选出先超过静摩擦阈值启动运动、随后调节接近目标的控制序列。与均匀随机shooting和数据集先验随机shooting相比，Action Diffusion显著降低终端误差和卡滞步数，在低样本量K下优势尤为明显；数据集先验因未按目标条件化，常产生符号、时长或时机不合适的kick序列，而均匀随机shooting在多数样本预算下基本无效。在与CEM的误差-计算时间对比中，论文给出了K=32和K=512等代表性预算下Action Diffusion与CEM的终端精度和墙钟耗时关系，说明条件扩散在低样本预算下能提供更高效的候选控制分布。

### 四、结论（Conclusion）
条件扩散模型可以有效作为干摩擦/静摩擦系统中开环采样控制的学习式提议分布：通过以初始和目标状态条件化结构化控制先验，模型能够对已有控制基元进行选择、排序与时序重组，形成越过阈值、调节运动、停靠等可解释阶段，从而克服静摩擦造成的输入死区问题。该模型适合作为采样型开环规划的提议分布，但不是对摩擦建模、补偿算法或反馈控制的替代，其贡献在于为低维非光滑物理控制提供了一种可检查、可复现的生成式方法。

### 五、方法论与关键技术细节
动力学采用分段模型：当|v|<epsilon_v且|u|<=f_s时系统保持静止，即stiction；当|v|<epsilon_v但|u|>f_s时运动启动并受库仑摩擦项影响；当速度足够大时还需考虑库仑摩擦和粘性阻尼。关键超参包括H=64、dt=0.05、u_max=0.9、f_s=0.7、f_c=0.6、b=0.05、epsilon_v=1e-3、p0范围[-1,1]、v0范围[-0.5,0.5]；扩散训练使用50k训练样本和10k验证样本，Adam训练15000步、学习率2e-3、批大小256、EMA衰减0.995、扩散步数200、DDIM步数50、条件丢弃概率0.2、guidance scale=2。数据集的控制先验由八段常数构成，每段按三类幅度模式采样，并经alpha=0.3的一阶滤波和裁剪，因此模型学到的是条件化组合已有结构模式，而非从零发现模式。评测指标包括终端误差、控制能量、控制平滑度，以及满足|v_k|<epsilon_v、|u_k|<f_s且位置偏离目标delta>0.01时的卡滞步数。局限性包括系统为低维理想化质点、无测量噪声和过程噪声，且评测基于确定性已知动力学的开环选择，不涉及在线闭环反馈或复杂的摩擦辨识问题。
