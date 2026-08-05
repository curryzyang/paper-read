# Neural Networks with Local Converging Inputs for Efficient Options Pricing Models

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Harris Cobb, Wenbo Hao, Yingjie Liu
- 机构：Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02778v1) · [PDF](https://arxiv.org/pdf/2608.02778v1)

## TLDR
NNLCI uses small neural networks to locally correct coarse- and refined-mesh numerical solutions, reducing pricing error by 4–12× for multi-asset Black–Scholes and Heston barrier options with minimal high-fidelity training data.

## Abstract
We present a novel application of Neural Networks with Local Converging Inputs (NNLCI) to improve the efficiency of existing numerical methods for pricing multi-asset options. The most concise input format for NNLCI has been introduced, offering substantial convenience and efficiency. NNLCI uses a neural network to locally correct solutions from a coarse mesh and a refined mesh (relative to the coarse one), requiring only a minimal amount of high-fidelity training data. We demonstrate this approach on cash-or-nothing options under the Black-Scholes equation in one, two, and three spatial dimensions, and on single-asset down-and-out barrier call options under the Heston stochastic-volatility model (whose pricing PDE is two-dimensional in the spot price $S$ and the instantaneous variance $v$). In each case, NNLCI reduces the root-mean-square error (RMSE) of the refined-mesh numerical solution by a factor of approximately 4-12 on test sets, even when the neural network is trained on only a small subset of parameter combinations. These results demonstrate that NNLCI significantly reduces computational requirements for high-dimensional problems in real-time options trading and risk management, offering low training costs and strong generalization ability.


## 精读解读（中文）
### 一、研究动机
多资产期权定价面临高维PDE求解的维数灾难，传统隐式差分或有限元方法在实时交易与风险管理中计算代价极高；同时现有神经PDE求解器（如PINN、算子学习）常需大量高保真数据或直接编码参数，泛化能力受限。本文首次将局部收敛输入神经网络（NNLCI）引入期权定价，利用粗网格与加密网格的局部解修正，以极少量高保真训练数据提升现有数值方法效率，并实现对不同PDE参数、几何与边界的强泛化。

### 二、技术方案（Method）
构建嵌套的粗网格（如每方向21节点）、加密网格（每方向41节点，为粗网格加倍且粗节点重合）与参考网格（此处采用闭式解或最高分辨率解）。在每个时空配准点，取该点在粗网格与加密网格上的重合节点解值作为网络输入（2个输入）；对非均匀网格（Heston模型）再加入局部网格尺寸度量h_local作为第三输入。网络为两层ReLU前馈网络（1D用15神经元、2D用20神经元），以参考网格解为监督目标，用Adam学习率1e-3训练1500-2000轮。训练集按参数网格等间隔子采样（训练间隔g）生成，测试集为其余参数组合；推理时仅需粗网格与加密网格解，无需坐标、PDE参数或边界信息。

### 三、结果（Result）
在Black–Scholes下的现金或无期权（1D/2D/3D）与Heston随机波动率下的向下敲出障碍看涨期权（2D）四类案例中，NNLCI将加密网格数值解的均方根误差（RMSE）在测试集上降低约4至12倍。即使仅用少量参数组合子集训练，网络仍能在未见的参数上保持显著精度提升，且训练成本低，推理速度快。

### 四、结论（Conclusion）
NNLCI通过局部收敛输入对粗网格与加密网格解进行神经校正，能以极低训练数据和高泛化能力显著提升多资产及障碍期权定价的精度与效率，为实时交易和高维风险管理提供了一种轻量级替代方案；未来可探索更大局部patch及更多金融PDE场景。

### 五、方法论与关键技术细节
关键细节包括：输入仅为局部配准点处的粗/细网格解值，不显式编码时空坐标、PDE参数（σ、r、κ等）或边界条件，信息由局部收敛输入隐式携带；该方法依赖非混沌抛物型PDE的局部解唯一性近似，对混沌系统无效；粗网格与加密网格必须嵌套以保证节点重合，加密网格分辨率是粗网格两倍；训练数据按参数网格等间隔子采样（gap）构造，训练集远小于全网格；1D/2D参数网格分别含289和6561组，训练集在gap=2时仅为81和625组；网络架构极简，参数量小；局限在于局部patch信息可能无法唯一决定参考解，且在Heston非均匀网格上需额外输入局部网格尺寸度量以补偿网格非均匀性。
