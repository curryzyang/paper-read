# A panoramic aerodynamic performance prediction method for turbomachinery cascades using transformer-enhanced neural operator

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Qineng Wang, Zhendong Guo, Liming Song, Tianyuan Liu
- 机构：Hebei Key Laboratory of Compact Fusion, ENN Science and Technology Development China Co., Ltd., Xi'an Jiaotong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16066v1) · [PDF](https://arxiv.org/pdf/2609.16066v1)

## TLDR
This paper proposes a transformer-enhanced neural operator (TNO)-based panoramic prediction framework that first predicts basic Navier–Stokes flow variables and then derives various turbomachinery performance parameters, achieving CFD-like accuracy and cutting downstream task costs by four orders of magnitude.

## Abstract
To enable flexible and rapid aerodynamic performance evaluation in turbomachinery design, this paper proposes a panoramic performance prediction framework. Unlike most previous prediction models that directly predict the objective functions of interest, our approach first predicts the basic parameters of the Navier-Stokes equations, such as temperature, pressure, and density. Utilizing these basic physical quantities, it subsequently predicts key performance parameters of the turbine stage meridian plane. By adopting this methodology, our proposed panoramic performance prediction framework functions similarly to a CFD simulator, capable of predicting various objective of interest to the designers. To enhance prediction accuracy, a transformer-enhanced neural operator (TNO) is introduced within this framework. Using the Rotor 37 blades as a reference, the proposed TNO is trained to predict the performance of a transonic compressor blade in the meridian plane. The TNO can accurately predict total quantities such as isentropic efficiency, mass flow, and distributions of total pressure ratio. Remarkably, the prediction error of TNO is observed to be smaller than that of state-of-the-art deep learning operators such as the FNO and DeepONet. Furthermore, the TNO is applied to downstream tasks, including sensitivity analysis and optimization of various objective functions. The results confirm that the TNO can operate almost like a CFD simulator, while reducing the computational cost of downstream tasks by four orders of magnitude. The effectiveness and reliability of the proposed TNO for solving different kinds of downstream tasks have been well demonstrated.


## 精读解读（中文）
### 一、研究动机
在涡轮机械气动设计中，CFD仿真精度高但单次计算昂贵，优化、敏感性分析和不确定性量化等下游任务需要大量重复计算，难以在有限时间与预算内完成。传统代理模型虽快却忽略丰富流场数据且呈黑箱特性，已有深度学习流场预测模型又常局限于特定物理场或特定目标，复用性差。为此，本文希望构建一种类似CFD模拟器的全景式性能预测框架，可复用于多种下游任务。

### 二、技术方案（Method）
本文提出全景性能预测框架，其映射逻辑为几何设计变量与状态参数先经TNO预测Navier-Stokes基本物理量（如温度、压力、密度、速度），再由这些基本场推导叶栅子午面关键性能参数。TNO采用分支-主干神经算子结构：分支网络用多层感知机编码28个Rotor 37叶片几何设计变量，主干网络用多个Galerkin注意力块和FFN编码查询坐标(r,z)，共享输出网络融合分支与主干特征。训练数据由拉丁超立方采样生成2900个Rotor 37样本，CFD采用Numeca FINE/TURBO求解RANS，Spalart-Allmaras湍流模型，Autogrid5生成H-O-I网格，单通道稳态计算。

### 三、结果（Result）
以Rotor 37跨声速压气机叶片为对象，TNO能准确预测等熵效率、质量流量和总压比分布等总体与分布量，且预测误差小于FNO、DeepONet等先进深度学习算子。将该模型用于敏感性分析和多目标优化等下游任务时，其表现接近CFD模拟器，同时把下游任务计算成本降低约四个数量级。CFD与实验对比中，压比曲线吻合良好，效率曲线平均偏差约2%，验证了数值模拟基准的可靠性。

### 四、结论（Conclusion）
所提出的全景式TNO预测框架能够以近实时方式给出流场与性能，并可作为CFD代理用于多种气动设计下游任务，兼顾精度、灵活性与复用性。结果表明该方法对跨声速压气机叶栅性能评估和优化具有有效性与可靠性，可显著缩短涡轮机械设计迭代周期并降低计算成本。

### 五、方法论与关键技术细节
数据与先验方面，研究对象为Rotor 37，28个几何变量通过NURBS参数化叶片吸力面与堆叠线，2900个样本用LHS在设计空间采样；CFD为单通道稳态RANS，SA湍流模型，绝热光滑壁面，入口给定总温总压，出口给定平均静压115000 Pa，网格约4e6节点，近壁首层厚度3e-6 m，单样本约800 s。模型方面，TNO沿用分支-主干算子思想，分支用MLP编码设计变量，主干用Galerkin注意力块编码非结构查询坐标并接FFN，最后共享输出网络融合p维特征；输出先为基本NS物理量，性能参数由预测场后处理得到。实现上无需像素化采样，可处理非结构坐标输入；局限在于方法验证集中于Rotor 37单通道与特定工况范围，跨几何/工况泛化仍需更多数据或重训练。
