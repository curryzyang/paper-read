# Regularized Least Squares Training of Quadratic Neural Networks with Applications to System Identification

- 区域：精读区
- 排名：8
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Luis Rodrigues, Zachary Yetman Van Egmond, Mohammad R. Amiri Fard
- 机构：Concordia University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17654v1) · [PDF](https://arxiv.org/pdf/2609.17654v1)

## TLDR
This paper proposes a regularized least-squares training method for quadratic neural networks that provides closed-form weight and sensitivity expressions along with a tight lower bound on the training cost, and demonstrates its effectiveness in nonlinear system identification.

## Abstract
This paper proposes a least squares approach for the training of quadratic neural networks with regularization. The proposed methodology yields a lower bound on the solution of the training optimization problem for the case where the regularization coefficient is positive. Moreover, it yields closed-form expressions for the approximate solution and its sensitivity The lower bound is tight and the approximate solution is the optimal solution when the regularization coefficient is zero. Having a closed-form expression for the weights reduces considerably the computational time when compared with iterative numerical methods such as backpropagation that can get stuck in local minima. The proposed approach has three main contributions, namely, (i) it yields an analytical expression for the weights, (ii) an analytical expression for the sensitivity of the weights to errors in the data is also provided, (iii) it establishes a connection between the optimization to compute a lower bound and nuclear norm minimization. The proposed least squares training is successfully applied to a nonlinear system identification example where the proposed lower bound is compared with the optimal value.


## 精读解读（中文）
### 一、研究动机
两层二次神经网络在系统辨识等任务中具有良好表达能力和可解释性，但其训练通常是非凸优化，反向传播只能收敛到局部极小且计算迭代成本高。已有凸重构方法可求全局最优，却缺少闭式权重表达式；前期工作表明无正则QNN可用最小二乘闭式求解。本文旨在将这一思路推广到带1范数正则的QNN训练，给出训练代价下界、闭式近似权重及其灵敏度，并建立与核范数最小化的联系，从而降低计算量并增强可解释性。

### 二、技术方案（Method）
以N组输入x_i和标签y_i为数据（多输出可拆分为单输出，故不失一般性取单输出），采用两层二次网络，隐藏激活为σ(z)=a z^2+bz+c，输出为yhat_i=Σ_j σ(x_i^T w^j)α_j，隐藏权重w^j满足单位范数，训练目标为凸损失加βΣ|α_j|。利用单项式提升xbar_i=[x_i^T,1]把输出写成二次型yhat_i=xbar_i^T Z xbar_i，并令Z具有[[aZ1,(b/2)Z2],[(b/2)Z2^T,c Tr(Z1)]]的块结构；先证明该结构矩阵可分解为同结构半正定矩阵之差，再去掉原凸重构中的LMI/PSD约束，构造关于Z的正则最小二乘，用β惩罚与1范数对应的核范数/迹项。求解时把xbar_i^T Z xbar_i视为Z元素的线性模型，β=0时用标准最小二乘得到闭式解，β>0时用核范数正则最小二乘的SVD软阈值形式得到闭式近似解，并推导其对数据误差的灵敏度；最后将解分解回隐藏层权重并用于推理。

### 三、结果（Result）
理论上得到正则系数β≥0时原QNN训练最优代价的下界；当β=0时该下界是紧的，近似解即全局最优解；β>0时给出闭式近似权重及其对数据误差的灵敏度。权重解析表达避免了反向传播的迭代搜索和局部极小，计算时间显著减少，并揭示下界优化与核范数最小化之间的联系。在非线性系统辨识示例中方法成功应用，并将所提下界与最优值进行了对比，验证了理论下界的有效性，其中β=0时与最优值一致。

### 四、结论（Conclusion）
本文为正则化二次神经网络训练提供了一种最小二乘与核范数正则化相结合的凸近似框架，可给出闭式权重、训练代价下界和数据误差灵敏度，适用于非线性系统辨识，并可通过单项式提升推广到深层QNN。其核心价值在于用解析计算替代易陷入局部极小的反向传播，同时保持与凸QNN重构及核范数最小化的理论联系；局限是β>0时通常只保证下界和近似解，网络恢复效果与正则强度、数据噪声及分解条件有关。

### 五、方法论与关键技术细节
关键实现点包括：激活参数a,b,c需预先固定，常通过区间内ReLU的最小二乘拟合得到；隐藏层权重w^j单位范数；正则系数β≥0；单输出处理因多输出可拆分为独立QNN。核心数学工具是结构保持的PSD分解引理和去除LMI约束的松弛，下界紧性仅在β=0时保证。核范数/迹正则来自原L1惩罚，闭式解依赖最小二乘或SVD软阈值，灵敏度由解析导数给出；复杂度主要来自矩阵求逆或SVD而非迭代反向传播。局限性在于β>0时得到的是下界与近似解而非原非凸问题的精确全局最优，结果针对两层QNN，深层情形需输入单项式提升，且对数据误差的鲁棒性由所推导的灵敏度刻画。
