# Physics-Informed Dynamic State Estimation for Current Transformers Using Graph Neural Networks

- 区域：精读区
- 排名：2
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Michael A. Boateng, Gabriel Gauderman, Nathalie Uwamahoro
- 机构：Georgia Institute of Technology, Syracuse University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02679v1) · [PDF](https://arxiv.org/pdf/2607.02679v1)

## TLDR
This paper presents a physics-informed graph neural network warm-start strategy for current transformer dynamic state estimation that leverages the Jacobian sparsity pattern to improve initialization robustness, achieving average gains of 25% in initialization distance and 38% in weighted objective value across all tested SNR levels.

## Abstract
Current transformers are fundamental to power system protection and measurement, yet transient core saturation can severely distort the secondary current and degrade measurement accuracy. Existing dynamic state estimation methods rely mainly on numerical discretisation and iterative solvers, but their initialisation is not informed by the physical dependency structure of the estimation problem, which limits robustness under noisy conditions. This paper presents a physics-informed enhancement for current transformer dynamic state estimation using COMTRADE measurements generated in WinIGS-T. A structured benchmark of four discretisation schemes and three iterative solvers identifies Gauss-Newton with Quadratic discretisation as the strongest baseline. To address the limitation of conventional cold-start initialisation, a graph neural network is constructed from the Jacobian sparsity pattern to generate physics-informed initial state estimates. The proposed warm-start strategy improves estimator conditioning and achieves average gains of 25% in initialisation distance and 38% in initial weighted objective value across all tested SNR levels. The results demonstrate that embedding physical structure into the initialisation stage improves the robustness of CT saturation correction and supports more reliable measurement and protection performance in modern power grids.


## 精读解读（中文）
### 一、研究动机
现有电流互感器动态状态估计方法依赖数值离散和迭代求解器，但初始化未利用估计问题的物理依赖结构，在噪声条件下鲁棒性有限。

### 二、技术方案（Method）
使用WinIGS-T生成的COMTRADE测量数据；将CT动态状态估计问题建模为非线性加权最小二乘，对比四种离散化方案（前向欧拉、后向欧拉、梯形法、二次型）和三种迭代求解器（Gauss-Newton、Levenberg-Marquardt、混合GN→LM）后，选择Gauss-Newton与二次型离散化作为最强基线；针对冷启动初始化的局限，从Jacobian稀疏模式构建有向图，设计图神经网络通过消息传递层学习状态耦合，以生成物理信息初始状态估计；训练使用2000个高SNR（+20 dB）参考样本，损失函数为MSE加L2正则化（权重0.001），Adam优化器（学习率0.01），批量大小32，训练20轮；推理时，将GNN输出作为Gauss-Newton求解器的暖启动，替代零初始化。

### 三、结果（Result）
提出的暖启动策略改善了估计器条件，在所有测试信噪比水平上，平均初始化距离提升25%，初始化加权目标值提升38%。

### 四、结论（Conclusion）
将物理结构嵌入初始化阶段能够提高电流互感器饱和校正的鲁棒性，支持现代电网中更可靠的测量和保护性能。

### 五、方法论与关键技术细节
数据来源为WinIGS-T生成的COMTRADE测量；图神经网络基于Jacobian稀疏模式构建有向图以表征物理依赖结构；损失函数为MSE加L2正则化（权重0.001），训练超参数包括2000样本、20轮、学习率0.01、批量32；该暖启动方法仅在初始化阶段引入GNN，收敛后精度与冷启动相当；局限性包括GNN训练依赖高SNR参考状态，且在极低SNR场景下可能仍需进一步验证。
