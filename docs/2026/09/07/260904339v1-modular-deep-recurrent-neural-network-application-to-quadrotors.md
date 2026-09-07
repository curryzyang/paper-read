# Modular Deep Recurrent Neural Network: Application to Quadrotors

- 区域：精读区
- 排名：6
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Nima Mohajerin, Steven L. Waslander
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04339v1) · [PDF](https://arxiv.org/pdf/2609.04339v1)

## TLDR
A modular deep recurrent neural network (MODERNN) with feedforward inter-layer connections is introduced to improve learning of high-order nonlinear dynamics and alleviate vanishing/exploding gradients, as demonstrated by modeling quadrotor altitude dynamics.

## Abstract
A modular deep Recurrent Neural Network (RNN) is introduced to facilitate the process of deploying various architectures of RNNs, and to automatically compute derivatives for gradient-based learning methods. The modularity leads to a set of new architectures, one of which includes feedforward inter-layer connections. By adding feedforward inter-layer connections in a multi-layer RNN, it is observed that the capability of the RNN to learn and model high-order dynamics and nonlinearities is significantly improved. The problem of vanishing/exploding gradient in space for a multilayer RNN is also alleviated using feedforward connections. These results are demonstrated using a quadrotor case study, for which a model of the altitude dynamics is learned with our particular network structure, while existing methods are unable to generalize as quickly or at all.


## 精读解读（中文）
### 一、研究动机
现有RNN（如NARX/RMLP）在加深层数时会遭遇时间和空间维度上的梯度消失/爆炸问题，难以学习高阶段动力学与复杂非线性；同时四旋翼这类小型无人机的精确动力学难以仅靠物理建模获得，需要一种既能利用经验飞行数据、又支持多层RNN灵活构造与自动求导的建模框架。为此提出模块化深度递归神经网络（MODERNN），通过统一连接矩阵降低架构部署与导数计算成本，并利用前馈层间连接缓解空间梯度病态，实现对四旋翼高度动力学的有效学习。

### 二、技术方案（Method）
所提MODERNN以多个局部循环层G_i为模块组成深度网络，每个模块的动态为x_i(k)=A_i y_i(k-1)+B_i u_i(k)+b_i，并经激活函数得到y_i(k)=f_i(x_i(k))；其中u_i(k)可包含外部输入u(k)及其他层前一时刻输出y_j(k-1)。为统一不同深度RNN结构，使用(L+2)×L连接矩阵C的0/1元素控制输入注入、层间连接和输出选取，因此RMLP、NARX、带前馈跨层连接的新架构都可在同一框架内实例化。MODERNN采用多层全互连结构，输入为四旋翼飞行实验所得离散时间序列数据，输出为高度动力学模型预测；训练时通过模块化方法在时间展开图上自动计算输出对各层权重p_i的Jacobian，再使用Levenberg-Marquardt等梯度下降法更新权重。推理时给定整个输入序列U，沿各层状态方程和连接矩阵前向计算Y=Omega_L(U)，得到网络的动态输出。

### 三、结果（Result）
在四旋翼高度动力学建模案例中，MODERNN能利用带前馈层间连接的多层循环结构成功学到高度动态模型，并表现出明显更强的泛化能力；相比之下，NARX和常规多层RNN（RMLP/MRNN）等已有方法要么收敛很慢，要么完全无法泛化。作者还观察到，加入前馈层间连接显著提升了多层RNN学习高阶段动态和非线性的能力，同时缓解了多层RNN在空间上的梯度消失/爆炸，使输出Jacobian不再因层数增加而严重病态。

### 四、结论（Conclusion）
带有全互连和前馈层间连接的MODERNN能够在不依赖复杂物理建模的情况下，用普通梯度训练方法学习四旋翼高度这类高阶非线性动态系统，并且相比NARX与常规多层RNN具有更快的泛化优势。该模块化设计提供了统一而灵活的深度RNN架构框架，使增加层数以提升表达能力变得可行，适用于无人机等数据的经验动态建模。

### 五、方法论与关键技术细节
关键细节包括：每个局部循环层G_i的参数向量p_i包含B_i、A_i和偏置b_i，其长度q_i=n_i(m_i+n_i+1)，反馈通过A_i y_i(k-1)实现；连接矩阵C为(L+2)×L，取0/1值，其中最后两行分别表示外部输入u(k)与网络输出信号的连接来源，通过该矩阵可以配置标准RMLP、带跨层前馈连接或从中间层输出等不同结构。MODERNN的梯度计算采用模块化链式展开，避免手工推导不同拓扑的导数，使梯度类优化器可直接使用。该框架减弱了空间维度梯度消失/爆炸问题，也避免像NARX那样需要先验指定输入输出延迟数；但现有公开文本中未给出具体网络层数、神经元数、训练轮次与定量精度指标，其时间维度梯度问题和最优拓扑选择仍然是实际应用中的约束。
