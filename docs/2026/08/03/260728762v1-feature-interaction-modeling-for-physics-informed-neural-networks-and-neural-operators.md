# Feature Interaction Modeling for Physics-Informed Neural Networks and Neural Operators

- 区域：精读区
- 排名：1
- 匹配度：6.3/10
- 来源：arxiv
- 作者：Quan Gu, Hongxia Liu
- 机构：Taiyuan University of Technology, Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28762v1) · [PDF](https://arxiv.org/pdf/2607.28762v1)

## TLDR
The paper introduces factorization-machine-inspired feature interaction modules into PINNs and neural operators to explicitly model pairwise couplings among coordinates, time, and parameters, yielding significant accuracy gains for shock-dominated PDEs while remaining competitive on smooth benchmarks.

## Abstract
This work embeds feature interaction modules derived from factorization machines (FMs) into physics-informed neural networks (PINNs) and neural operator learning, to enhance model expressiveness for solution manifolds of parameterized partial differential equations (PDEs). Motivated by the second-order Taylor expansion of multivariate functions to characterize variable couplings, we first propose FM-PINN. It explicitly captures spatio-temporal variable interactions and improves the approximation accuracy for smooth high-order PDEs. We further group spatial coordinates, time, physical parameters, and initial and boundary conditions into independent feature sets and model their cross-group interactions. Based on this strategy, we develop FM-Operator and FM-DeepONet, which are particularly effective for nonlinear conservation laws and problems with sharp gradients or discontinuities, while offering no consistent advantage on smooth operator learning benchmarks. Numerical tests demonstrate that the proposed mechanism delivers substantial accuracy gains on challenging shock-dominated equations, indicating a promising direction for physics-consistent modeling of parameterized PDEs with strong cross-field dependencies.


## 精读解读（中文）
### 一、研究动机
现有PINN和神经算子研究多聚焦于域分解、谱分解、多模态融合和输入编码，却较少关注输入特征之间的交互；而参数化PDE解流形常依赖坐标、时间、物理参数与初边条件之间的强耦合。受多元函数二阶泰勒展开中交叉项的启发，论文将因子分解机的高效双线性交互机制引入PINN与神经算子，以增强对强跨场依赖问题的表达能力。

### 二、技术方案（Method）
构建连续场特征交互块：将输入划分为M个语义场F_i，每个场经仿射投影W_iF_i+β_i得到r维嵌入e_i，再用NFM的双交互池化z_BI=Σ_{i<j} e_i⊙e_j=1/2[(Σe_i)^{⊙2}-Σe_i^{⊙2}]聚合两两交互。基于该模块提出三种架构：FM-PINN将每个坐标作为独立场，经嵌入与交互后由MLP解码输出，损失仍为PDE残差、初边条件的加权MSE；FM-Operator直接以F=(s,y,q(s),η)为输入，q(s)=[mean(s),std(s),max|s|]，预测为MLP(z_BI)+Linear([F_1;...;F_M])以保留一阶线性项；FM-DeepONet将基干与trunk特征及辅助统计量组成场集，用MLP解码交互向量并生成修正量Δb和Δφ，最终以归一化内积形式输出。训练采用AdamW，PINN任务30k步、学习率1e-3、权重衰减1e-6，拉丁超立方采样内点10000个、边界/初始点400个，每步用1024个内点与全部边界/初始点。

### 三、结果（Result）
FM-PINN在多个高维光滑问题上的精度优于vanilla PINN；FM-Operator在更少参数条件下对sharp-gradient问题取得更优精度；FM-DeepONet显著改善含间断或强梯度问题的解精度。数值测试表明，在冲击主导的守恒律方程上，所提机制带来大幅精度提升；但在光滑算子学习基准上无一致优势。

### 四、结论（Conclusion）
特征交互建模为具有强跨场依赖的参数化PDE提供了一种物理一致的建模方向，尤其适用于非线性守恒律和激波/间断问题。该机制不是普适的万能近似增强，而是一种紧凑归纳偏置：显式建模交叉特征可提升表达效率，但共享秩约束也可能导致负迁移，因此在实际任务中需根据问题是否具有显著交叉项来选用。

### 五、方法论与关键技术细节
关键实现细节：特征交互块要求M≥2，单场输入需额外的一阶路径或不同场划分；FM-PINN中每个坐标映射为64维嵌入后做交互；FM-Operator需要同时提供传感器向量s、查询坐标y、统计量q(s)和物理参数η（若已包含在s中则省略）；理论动机来自分块二阶泰勒展开，交互项对应交叉Hessian项δF_i^T H_{ij} δF_j；双交互池化通过共享r维隐向量将交叉双线性形式限制为秩至多r，因此是紧凑归纳偏置，可能无法联合表示任意秩r交叉矩阵并造成负迁移；训练设置包括AdamW优化器、学习率1e-3、权重衰减1e-6、30k步、内点1024个/批、边界初始点400个全部使用。
