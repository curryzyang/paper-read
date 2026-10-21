# Latent Projection for Latent Planning

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Yoo Sung Jang, Michael Ryoo
- 机构：Stony Brook University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26979v1) · [PDF](https://arxiv.org/pdf/2610.26979v1)

## TLDR
The paper proposes a post hoc latent projection that fits a constrained normal state-dynamics matrix under SIGReg’s Gaussian Gauss–Markov assumptions and restricts the ℓ2 planning cost to the lowest-uncertainty eigen-subspace, improving latent planning success by up to 54.7 points on 2D navigation tasks without modifying the encoder, predictor, rollout, or planner.

## Abstract
Latent world models let an agent plan in latent space. The planner searches for an action sequence that minimizes a cost, and that cost is often the $\ell_2$ distance between the predicted terminal latent and the goal latent. The latent, however, is partly noise: the regularizer that prevents collapse during world model training promotes variance in the directions carrying no signal. We show that the same regularizer also supplies the structure to prune that noise in the latent. SIGReg drives the latent marginal to a standard Gaussian at every step, and assuming further that the latent sequence is a Gauss-Markov process, the transition is linear with its covariance pinned by the map itself, $z' \mid z \sim \mathcal{N}(Az,\, I - AA^\top)$. Fitting the state dynamics $A$ therefore yields the covariance at no additional cost, and in its eigenbasis each latent direction carries its own uncertainty. Furthermore, constraining $A$ to be a normal matrix fixes that basis across timesteps, so one eigenbasis measures the uncertainty over an arbitrary number of steps and serves as a stable basis to compute the planning cost on. We then restrict the $\ell_2$ cost to the $k$-dimensional subspace the state dynamics carry forward with the least uncertainty. The correction is post hoc: the encoder, the predictor, the rollout, and the planner are all left untouched, and only a single constrained matrix, $A$, is fit. We evaluate across six environments and show large gains on the 2D navigation tasks, TwoRoom and PointMaze, raising success rate over the plain $\ell_2$ cost by up to $+54.7$ points under a harder planning setting. Code is available at https://github.com/yjang43/lp2.


## 精读解读（中文）
### 一、研究动机
潜在世界模型常用终端潜在与目标潜在之间的ℓ2距离作为规划代价，但SIGReg等正则项在防止坍缩的同时会在无信号方向注入方差，编码器也保留与任务无关的内容，导致代价部分沿无信息方向计算。作者希望在不改动编码器、预测器和规划器的前提下，利用正则项诱导的分布结构剪除噪声方向，得到更可靠的规划信号。

### 二、技术方案（Method）
在LeWM框架中冻结编码器f和预测器g，先把轨迹观测编码为潜在序列，再以最小二乘拟合动作无关的线性状态动力学A；拟合同时约束I−AA^T为半正定协方差且A为正规矩阵AA^T=A^TA，并对H步未来帧联合最小化∑_{t=1}^H E||A^t z−z^(t)||^2。由Gauss–Markov与标准高斯边际假设得到z'|z∼N(Az,I−AA^T)，对协方差做特征分解，取最小k个特征值对应特征向量U_k构成低不确定性子空间；规划时仍用冻结预测器rollout候选动作序列，但把终端潜在与目标潜在先投影到U_k，再用||U_k^T(ẑ_T−z_g)||_2排序候选。

### 三、结果（Result）
在六个环境中评估，投影代价在二维导航任务TwoRoom和PointMaze上相对原始ℓ2代价取得大幅提升，较难规划设置下成功率最高提高54.7个百分点；摘要强调编码器、预测器、rollout和规划器均不变，仅拟合一个受约束矩阵A即可获得该收益。

### 四、结论（Conclusion）
论文表明SIGReg带来的标准高斯结构不仅能稳定世界模型训练，还能把潜在噪声与状态动力学协方差绑定，从而为规划提供可解释的不确定性度量。将ℓ2代价限制在状态动力学最确定的方向上是一种低成本、后处理式的规划改进，尤其有利于存在大量无关或噪声潜在方向的导航任务。

### 五、方法论与关键技术细节
关键实现点包括：A在冻结编码器产生的潜在转移上一次性拟合，训练目标为多步平方误差且动作无关；正规性约束使协方差特征基跨时间步共享，因为A^t(A^t)^T=(AA^T)^t，从而可用同一U_k计算任意horizon的投影代价；A可按实正规矩阵分解为1×1静态块和2×2运动块，默认采用全平面布局P=floor(n/2)，并需选择保留维数k与拟合步长H。局限在于依赖Gauss–Markov、线性转移和正规矩阵假设，A只描述数据生成策略下的动力学，且收益主要在二维导航环境中验证。
