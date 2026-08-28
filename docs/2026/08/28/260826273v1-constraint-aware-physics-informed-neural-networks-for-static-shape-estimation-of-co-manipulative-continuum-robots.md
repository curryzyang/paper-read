# Constraint-Aware Physics-Informed Neural Networks for Static Shape Estimation of Co-Manipulative Continuum Robots

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Rana Danesh, Pari Qarehdaghi, Farrokh Janabi-Sharifi
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26273v1) · [PDF](https://arxiv.org/pdf/2608.26273v1)

## TLDR
A constraint-aware physics-informed neural network that enforces static equilibrium and loop-closure constraints enables accurate, physically consistent, and computationally efficient static shape estimation for closed-chain co-manipulative continuum robots.

## Abstract
Static shape estimation of co-manipulative continuum robots (CCRs) is challenging because the continuum arms and manipulated flexible object form a closed chain that must satisfy both static equilibrium and geometric loop-closure constraints. This paper presents a constraint-aware physics-informed neural network (PINN) for static shape estimation of a tendon-driven CCR modeled using the geometric variable strain formulation. The proposed method incorporates a projected static equilibrium residual and a configuration-level geometric residual to enforce the governing mechanics and closed-chain geometry. In simulation, the PINN is compared with a purely data-driven artificial neural network (ANN) under limited and noisy training data. With 140 samples and 50% label noise, the PINN reduces the relative configuration error, equilibrium residual, and closed-chain residual by 67.88%, 67.35%, and 88.06%, respectively. Using the full dataset, the PINN achieves 0.1597% relative configuration error with an inference time of 0.1773 ms, compared with 17.97 s for an iterative nonlinear solver. Experimental fine-tuning reduces the marker RMSE from 2.657 mm to 0.497 mm and increases R2 from -0.788 to 0.937. These results demonstrate accurate, physically consistent, and computationally efficient static shape estimation of closed-chain CCRs.


## 精读解读（中文）
### 一、研究动机
协操作连续体机器人（CCR）中，连续体臂与受操作柔性对象构成闭合链，其静态形状估计需同时满足静力平衡和几何闭环约束，而传统迭代非线性求解器计算昂贵，纯数据驱动网络又无法保证物理一致性与约束满足，尤其在训练数据有限或带噪声时。为此，本文提出一种约束感知的物理信息神经网络（PINN），在统一建模中融合力学残差和几何闭环残差，以实现快速、准确且物理一致的静态形状估计。

### 二、技术方案（Method）
采用几何变量应变（GVS）公式对肌腱驱动的CCR进行建模，将连续应变场用基函数展开为广义坐标q，并通过Magnus指数映射从应变重构位形。系统包含两个连续体臂和一个柔性对象，通过闭环连接形成闭链。网络输入为肌腱驱动向量u，输出为广义坐标q（即预测的静态构型）。训练时，除了数据拟合损失外，还引入两个物理约束残差：一是投影静力平衡残差，将静态平衡方程Kq = B_q(u) + F_g投影到约束兼容子空间（利用约束雅可比A(q)的零空间投影），以保证在闭链约束下满足力平衡；二是配置级几何闭环残差，即闭环连接处的位形误差e(q)（由SE(3)相对变换的对数映射得到），用于强制闭合链的几何一致性。网络通过最小化数据损失、平衡残差和几何残差的加权组合进行训练。训练流程为先使用仿真数据预训练，再使用实验测量的肌腱位移和标记点位置进行微调。推理时仅需前向传播即可快速得到静态形状。

### 三、结果（Result）
在仿真中，与纯数据驱动ANN比较，在140个样本且50%标签噪声条件下，PINN将相对配置误差降低67.88%，平衡残差降低67.35%，闭环残差降低88.06%。使用完整数据集时，PINN达到0.1597%的相对配置误差，推理时间0.1773 ms，而迭代非线性求解器需17.97 s。实验微调后，标记点RMSE从2.657 mm降至0.497 mm，R2从-0.788提升至0.937。结果表明PINN在精度、物理一致性和计算效率上均显著优于基线。

### 四、结论（Conclusion）
约束感知PINN能够有效融合数据与力学模型，同时满足静力平衡和闭环几何约束，在有限、带噪数据下仍保持高精度和物理一致性，并比迭代求解器快数个数量级。实验微调进一步验证了从仿真到实验的可迁移性，为CCR实时静态形状估计提供了高效且可靠的方案。

### 五、方法论与关键技术细节
关键细节包括：使用GVS公式减少参数维度，并采用四阶Zanna配点方案和两点Gauss积分实现高精度位形重建；约束处理采用配置级闭环误差e(q)与约束雅可比A(q)，其中A(q)的零空间用于投影静力平衡残差，避免直接求解约束方程；损失函数为数据损失、投影平衡残差和闭环残差的加权和，超参数需平衡三者的贡献；训练数据仅使用140个样本就能获得鲁棒性，但依赖仿真数据的物理真实性，且闭链约束的m_i（约束方向数）和偏移变换需精确标定；模型局限性包括仅考虑静态情况，未含惯性/阻尼项，且假设线性弹性本构关系和已知材料参数，对模型误差敏感，但实验微调可部分补偿。推理时间0.1773 ms可实现实时应用，但训练本身仍需离线完成。
