# One Neural Operator for Re-planning Low-Thrust Cislunar Transfers after Thrust Outages, at the Original or a Later Arrival

- 区域：精读区
- 排名：8
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Selim Olgu Pilav
- 机构：Independent researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33188v1) · [PDF](https://arxiv.org/pdf/2611.33188v1)

## TLDR
The paper trains a Fourier neural operator ensemble to rapidly map nominal low-thrust NRHO-to-DRO cislunar transfers with thrust outages to re-planned trajectories and recovery probabilities—at the original arrival or with up to 10 days’ slip—enabling fast, accurate missed-thrust margin studies without thousands of exact re-optimizations.

## Abstract
Safe-mode events causing thrust outages are common in missions with electric propulsion. To demonstrate mission feasibility in such an event, missed-thrust margin studies are performed where thousands of outage scenarios need an exact re-plan solved. We train a neural operator that maps a nominal trajectory with an outage profile to a re-planned trajectory and to the probability that the recovery exists, for 270 low-thrust near-rectilinear halo orbit (NRHO) to distant retrograde orbit (DRO) transfers, at an allowed slip of up to 10 days. On unseen transfers and zero slip, its median control error on the severe half of outages is 1.20% compared to 14.0% for the best cheap re-planner benchmark. With the arrival slip as an input, the error is 1.67% against 23.2%. It also predicts the recoverability of an outage for a given arrival slip with an area under the receiver operating characteristic curve (AUC) of 0.997, while the minimum recoverable slip prediction is optimistic by more than half a day on only 6 of the 84 checked outages needing slip. At the original arrival, the ensemble spread of an operator variant with solver inputs has a rank correlation of 0.91 with the actual error, and performing exact solves on the 31% most uncertain severe outages reduces the 90th-percentile error from 8.5% to 2.3%. A query takes milliseconds without a solver, making this a useful tool for large outage studies where the cost of thousands of exact solves outweighs the time to train the operator.


## 精读解读（中文）
### 一、研究动机
电推进深空任务常因安全模式事件发生推力中断，任务可行性评估需要进行大量错过推力裕度研究，而每个中断场景都要精确重规划恢复轨迹，精确求解中位耗时约14.5 s、平均约71 s，数千次求解成本很高。因此需要一种快速工具，能同时给出重规划轨迹、Δv裕度、最近月面距离以及给定到达延迟下恢复是否存在，以加速大规模中断研究。

### 二、技术方案（Method）
作者构建了270条低推力NRHO到DRO转移族，在200节点网格上把可用推力历史、已飞行节点标志、标称控制与状态、时间分数、飞行时间和太阳相位等输入映射到重规划控制与状态，并用10个Fourier神经算子成员组成集成；混合算子分别校正单步凸优化R1和单步SQP R3，无求解器算子直接校正标称轨迹，联合算子额外输出恢复存在概率。训练损失为重新规划节点上的控制相对L2误差加λx=0.1的状态MSE，恢复概率用权重0.1的交叉熵训练，晚到达研究还输入到达延迟、有效性掩码并补齐到329节点。固定到达研究生成6750个精确重规划标签，晚到达研究生成13500个标签，并与R0至R3及带学习校正的R5至R7等廉价重规划器在未见过转移和严重中断上比较。

### 三、结果（Result）
在未见过转移且不允许到达延迟时，混合算子在严重中断半区的中位控制误差为1.20%，最佳廉价重规划基准为14.0%；允许最晚10天到达时，联合算子误差为1.67%，基准为23.2%。恢复存在性预测的AUC达0.997，在84个需要延迟的抽查中断中仅6个的最小可恢复延迟预测乐观超过半天；固定到达下集成离散度与实际误差的Spearman秩相关为0.91，对31%最不确定的严重中断做精确求解可把90分位误差从8.5%降至2.3%。无求解器查询为毫秒级且比带R1/R3输入的混合算子快16倍，Δv增量误差中位0.14 m/s、90分位7.2 m/s，而R3为2.2和58 m/s。

### 四、结论（Conclusion）
该工作表明，一个神经算子即可在原始或延迟到达条件下快速重规划低推力地月转移中断恢复，并以高精度预测恢复可行性和最小可恢复延迟。其毫秒级无求解器查询适合数千次中断场景筛查，而集成离散度可用于挑选少量最不确定案例做精确求解，从而在训练成本与大量精确求解成本之间取得实用折中。

### 五、方法论与关键技术细节
数据由Sobol序列采样270条最小控制能量转移，按210/30/30划分训练、验证和测试，测试转移限制在15.6至19.1天飞行时间包络内；中断按Weibull形状1.17、尺度2.41天再乘1.5生成0.5至10天全关机，至多三次并含推力下降。精确标签用IPOPT从标称轨迹和R1两个起点求解，控制相对L2差小于0.1%视为唯一；FNO每节点64特征、4个Fourier层、保留32个低阶模态、GELU激活，10成员集成输出均值与离散度。关键局限包括常质量与固定0.82 mm/s²推力加速度上界、无燃料上限、合成中断分布、仅30条测试转移，以及主要在严重中断子集上评估。
