# Exact SO(3)-Equivariant Isotropic Kernels for Rotation-Robust Neural Dynamics

- 区域：精读区
- 排名：1
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Ridham Patel
- 机构：Indian Institute of Technology Gandhinagar
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10626v1) · [PDF](https://arxiv.org/pdf/2610.10626v1)

## TLDR
The paper introduces IKNO, an exactly SO(3)-equivariant isotropic-kernel graph neural operator for 3D Navier–Stokes dynamics that removes coordinate-frame dependence while matching a much larger Tensor Field Network and outperforming a parameter-matched graph simulator.

## Abstract
Neural surrogates for vector-valued partial differential equations can fit training data yet change their predictions when the same physical state is expressed in a rotated coordinate frame. We study this failure on three-dimensional Navier--Stokes dynamics observed at irregularly placed points. We introduce the Invariant-Conditioned Isotropic Kernel Neural Operator (IKNO), a compact graph model that builds local interactions from scalar quantities unchanged by rotation and vector directions that rotate with the data. Consequently, rotating the positions and velocities rotates the predicted velocity change in exactly the same way. On a held-out test set fixed after model design, training unconstrained graph models on randomly rotated examples reduces but does not eliminate their coordinate dependence. In contrast, IKNO is consistent to numerical precision, matches the forecasting accuracy of a general rotation-aware Tensor Field Network with $5.6$ times fewer parameters, and outperforms a parameter-matched graph simulator. These results show that a compact, PDE-specialized model can remove coordinate dependence without sacrificing forecasting accuracy.


## 精读解读（中文）
### 一、研究动机
向量值偏微分方程的神经代理能在训练坐标下拟合，却会在同一物理状态被旋转到新坐标系时改变预测，而图模型通常只保证置换等变、不保证空间旋转等变。作者在三维Navier-Stokes不规则采样点上研究这一失效，并检验精确SO(3)等变架构是否比旋转数据增强更能消除坐标依赖且不损失原坐标预测精度。

### 二、技术方案（Method）
提出Invariant-Conditioned Isotropic Kernel Neural Operator（IKNO）：输入为不规则点坐标X与速度U，边连接半径0.4内至多64个邻居；每条边计算单位相对方向rhat与速度差δu，并构造6个旋转不变量（距离、速度模、δu模、u_i·rhat、δu·rhat、u_i·δu），经两层64单元SiLU的多层感知机输出四个标量系数a,b,c,d；消息为aδu + b rhat(rhat^Tδu)+c u_i+d(u_i×rhat)，对邻居取均值后加λu_i得到导数预测，再用显式欧拉以Δt自回归积分。训练用监督目标(U(t+Δt)-U(t))/Δt，Adam、余弦学习率、3个种子、100轮，按验证误差选检查点；最终层和λ零初始化，理论上对SO(3)联合旋转严格等变且对平移不变。

### 三、结果（Result）
在模型设计后固定的held-out测试集上，IKNO在1000个Haar随机旋转下与数值精度一致；旋转增强的GNS和component-EGNN仅降低但未消除坐标依赖。IKNO以4,869个参数匹配Tensor Field Network（27,297参数，少5.6倍）的预测精度，并优于参数匹配GNS（5,352参数）。评估用一步和十步相对Frobenius误差、旋转相对原坐标的一步退化Δ1的均值/95分位/最大，以及归一化算子等变诊断e_eq。

### 四、结论（Conclusion）
精确SO(3)等变的各向同性核可在低参数成本下消除坐标依赖并保持预测精度，表明紧凑的PDE专用等变模型可优于通用旋转感知TFN、参数匹配图模拟器和旋转增强基线。但该构造仍只是紧凑的PDE导向子集而非完备参数化，最大旋转退化是有限样本压力测试而非认证最坏界。

### 五、方法论与关键技术细节
数据为[0,2π]^3三维不可压Navier-Stokes，16^3伪谱求解器，2/3去混叠、Leray投影、Strang分裂扩散；固定轴大尺度力预热50步制造方向偏置，20个快照Δt=0.02，谱速度三线性插值到500个不规则点，训练随机128点子采样、评估固定128点。开发集25条轨迹种子342–366，测试集5条轨迹种子367–371；监督目标为有限差分导数，无观测噪声。优化用Adam、余弦衰减、3种子、100轮，IKNO学习率3e-3，对照2e-3；TFN承载偶标量与奇向量、距离条件张量积且至一阶球谐，为O(3)等变。局限包括边图半径0.4与至多64邻居、系数网络仅两隐层64、四基非完备、最大旋转为有限样本压力测试以及仅单帧一步预测实验。
