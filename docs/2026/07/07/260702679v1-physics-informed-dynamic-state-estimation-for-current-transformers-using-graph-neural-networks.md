# Physics-Informed Dynamic State Estimation for Current Transformers Using Graph Neural Networks

- 区域：精读区
- 排名：2
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Michael A. Boateng, Gabriel Gauderman, Nathalie Uwamahoro
- 机构：Syracuse University, Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02679v1) · [PDF](https://arxiv.org/pdf/2607.02679v1)

## TLDR
This paper proposes a physics-informed graph neural network warm-start strategy for current transformer dynamic state estimation that improves robustness under noisy conditions by generating informed initial state estimates from the Jacobian sparsity pattern, achieving average gains of 25% in initialization distance and 38% in weighted objective value.

## Abstract
Current transformers are fundamental to power system protection and measurement, yet transient core saturation can severely distort the secondary current and degrade measurement accuracy. Existing dynamic state estimation methods rely mainly on numerical discretisation and iterative solvers, but their initialisation is not informed by the physical dependency structure of the estimation problem, which limits robustness under noisy conditions. This paper presents a physics-informed enhancement for current transformer dynamic state estimation using COMTRADE measurements generated in WinIGS-T. A structured benchmark of four discretisation schemes and three iterative solvers identifies Gauss-Newton with Quadratic discretisation as the strongest baseline. To address the limitation of conventional cold-start initialisation, a graph neural network is constructed from the Jacobian sparsity pattern to generate physics-informed initial state estimates. The proposed warm-start strategy improves estimator conditioning and achieves average gains of 25% in initialisation distance and 38% in initial weighted objective value across all tested SNR levels. The results demonstrate that embedding physical structure into the initialisation stage improves the robustness of CT saturation correction and supports more reliable measurement and protection performance in modern power grids.

## 精读解读（中文）

### 一、研究动机
电流互感器是电力系统保护与测量的基础，但暂态铁芯饱和会严重扭曲二次电流并降低测量精度。现有动态状态估计方法主要依赖数值离散和迭代求解器，但其初始化未利用估计问题的物理依赖结构，在噪声条件下鲁棒性受限。

### 二、技术方案（Method）
本文提出一种物理信息增强的电流互感器动态状态估计方法。首先，对四种离散方案（前向欧拉、后向欧拉、梯形、二次型）和三种迭代求解器（高斯-牛顿、列文伯格-马夸尔特、混合GN→LM）进行系统基准测试，确定高斯-牛顿结合二次离散为最强基线。然后，利用雅可比矩阵的稀疏模式构建图神经网络，将噪声测量映射为物理信息初始状态估计。图神经网络通过消息传递层在物理依赖节点间传播信息，训练时最小化与高信噪比参考状态的均方误差并加入L2正则化。热启动阶段，GNN输出替代零初始化作为迭代求解器的初始猜测。

### 三、结果（Result）
基准测试表明，高斯-牛顿与二次离散组合在准确性和鲁棒性上最优。所提GNN热启动策略显著改善了估计器条件数，在所有测试信噪比水平下，初始化距离平均提升25%，初始加权目标值平均提升38%。与冷启动相比，热启动在噪声条件下收敛更稳定，且收敛后精度相当。

### 四、结论（Conclusion）
将物理结构嵌入初始化阶段能够提高电流互感器饱和校正的鲁棒性，为现代电网提供更可靠的测量和保护性能。本文的GNN热启动框架有效结合了物理建模与图学习，为动态状态估计的初始化问题提供了新的解决思路。

### 五、方法论与关键技术细节
关键细节包括：离散方案中二次离散（Simpson变体）达到O(h^3)局部精度，梯形规则为O(h^2)；迭代求解器中高斯-牛顿在高信噪比下收敛快，列文伯格-马夸尔特在低信噪比下更鲁棒，混合策略自动切换以平衡速度与鲁棒性；GNN图结构来源于CT状态估计问题的雅可比稀疏模式，节点对应状态变量，边表示物理耦合；训练数据来自WinIGS-T生成的COMTRADE测量，共2000样本，参考状态由高信噪比（+20 dB）高斯-牛顿收敛得到；损失函数为MSE加L2正则化（权重0.001），使用Adam优化器（学习率0.01，批大小32，训练20轮）；该方法局限性在于GNN依赖训练数据的代表性，在未见过的故障场景或不同CT参数下可能泛化不足，且GNN推理引入额外计算开销。

