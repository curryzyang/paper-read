# PIKFNO: An Interpretable Neural Operator Based on Physics Informed Kernel Function

- 区域：精读区
- 排名：1
- 匹配度：6.5/10
- 来源：arxiv
- 作者：Yuan Guo, Hanshu Chen, Zhuojia Fu
- 机构：Hohai University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14619v1) · [PDF](https://arxiv.org/pdf/2608.14619v1)

## TLDR
PIKFNO introduces an interpretable neural operator that explicitly embeds physics-informed kernel functions derived from governing equations into its architecture, achieving high accuracy, physical consistency, and improved generalization under limited training data.

## Abstract
This work proposes a new interpretable neural operator framework, termed the Physics Informed Kernel Function Neural Operator (PIKFNO), which explicitly incorporates physics informed kernel functions derived from governing equations into the neural operator architecture. Unlike traditional neural operators such as DeepONet, which rely on deep networks to implicitly learn basis functions, PIKFNO constrains the trunk network through physics informed kernel functions, thereby aligning its operator structure with the kernel expansions used in meshless collocation methods. Two construction strategies are introduced: one learns kernel functions directly from data, where the learned kernel can be regarded as a nonsingular fundamental solution, while the other builds them through transformations of analytical fundamental solutions. Numerical experiments demonstrate that PIKFNO achieves high predictive accuracy with substantially improved interpretability and superior generalization under limited training data. The proposed framework offers a new pathway for developing efficient, physically consistent, and interpretable neural operators.


## 精读解读（中文）
### 一、研究动机
传统神经算子如DeepONet虽在PDE求解中表现优异，但内部结构缺乏显式物理意义，可解释性差，且通常需要大量训练数据，外推能力和物理一致性不足。现有物理信息方法多通过损失项施加软约束，无法在算子层面保证物理一致性。受无网格配点法中核函数由控制方程决定这一思想启发，本文提出将物理信息核函数显式嵌入神经算子架构，以构建兼具可解释性、物理一致性与数据驱动表达力的算子学习框架。

### 二、技术方案（Method）
提出PIKFNO框架，在DeepONet基础上修改trunk网络：将trunk网络约束为径向基函数形式，核函数中心与边界配点对齐，使算子结构等同于无网格配点法中的核展开。两种核函数构造策略：PIKFNO_v1在难以获得解析基本解时，用一维神经网络直接学习核函数ψ(r)，训练后可视为非奇异数值基本解；PIKFNO_v2在已知基本解φ(r)时，将其线性变换为ψ(r)=k*φ(β*r)+b，其中k、β、b为可学习参数且β>0以避免r=0处的奇异性。框架输入为边界离散采样值（每边40点共160特征），trunk输入空间坐标(x,y)，输出为PDE解。训练采用与DeepONet相同的监督学习流程，损失为预测解与数值参考解之间的误差。

### 三、结果（Result）
在二维Laplace方程从边界条件到解的算子学习实验中，DeepONet测试误差为8.32e-4，PIKFNO_v1为8.90e-4，PIKFNO_v2为1.65e-3。PIKFNO_v1精度接近DeepONet但参数更少，PIKFNO_v2收敛最快。训练数据量减少时，PIKFNO_v2优势显著：训练集仅50个样本时误差1.58e-2，优于DeepONet的8.18e-2；500个样本时误差4.87e-3，优于DeepONet的3.57e-3。PIKFNO_v1学习到的核函数可直接作为基本解用于MFS，在解析解u=x^3-3xy^2的测试中相对误差极小，验证了数据驱动发现基本解的能力。

### 四、结论（Conclusion）
PIKFNO通过将物理信息核函数嵌入神经算子结构，实现了物理先验与数据驱动学习的有机融合。相比传统神经算子，PIKFNO具有更强的可解释性、在有限训练数据下保持高精度，且收敛更快；PIKFNO_v1还能为无网格方法提供数值基本解，为发展高效、物理一致且可解释的神经算子提供了新途径。

### 五、方法论与关键技术细节
关键细节包括：PIKFNO_v1的核函数由1D神经网络参数化，输入为径向距离r，输出为非奇异数值基本解，训练后可与PIKFNO框架解耦独立使用；PIKFNO_v2的核函数仅含3个可学习参数（k,β,b），β>0消除奇异性，线性变换保持物理一致性同时改善系数数值范围；branch网络采用[160,160,160,160]结构，trunk网络DeepONet为[2,160,160,160]，PIKFNO_v1为[1,160,160,1]（输入r），PIKFNO_v2无隐藏层；训练数据由传统数值求解器在40×40网格上生成，训练/测试各5000样本；PIKFNO_v1的核函数在r=0处无奇异性但值与PIKFNO_v2几乎一致，符合奇异边界法中源点位置决定ψ(0)的规律；局限性包括PIKFNO_v2因表达空间受限导致精度低于DeepONet，且依赖基本解先验。
