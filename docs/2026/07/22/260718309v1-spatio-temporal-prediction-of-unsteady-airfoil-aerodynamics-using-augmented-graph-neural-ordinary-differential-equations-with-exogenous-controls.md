# Spatio-Temporal Prediction of Unsteady Airfoil Aerodynamics Using Augmented Graph Neural Ordinary Differential Equations with Exogenous Controls

- 区域：精读区
- 排名：2
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Henrik Lange, Reik Thormann, Philipp Bekemeyer
- 机构：Airbus Operations, German Aerospace Center (DLR)
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18309v1) · [PDF](https://arxiv.org/pdf/2607.18309v1)

## TLDR
This paper introduces GNODE, an augmented graph neural ordinary differential equation framework that achieves temporally stable and accurate spatio-temporal predictions of unsteady airfoil aerodynamics under exogenous control inputs.

## Abstract
Unsteady aerodynamic phenomena, such as gusts, turbulence, and fluid-structure interactions affect an aircraft during flight. For design, optimisation and certification, it is indispensable to quantify such unsteady aerodynamic effects. Industry-standard computational fluid dynamics methods, such as solving the unsteady Reynolds-averaged Navier-Stokes equations or the linearized frequency domain method, are either computationally expensive or restricted by assumptions like linearity. Once trained, machine learning methods are capable of computing non-linear relationships very fast, making them suitable as surrogate models. By autoregressively applying graph neural networks (GNNs), operating on a discretised spatial domain, spatio-temporal predictions can be made. However, autoregressive GNNs suffer from error accumulation leading to unstable rollouts over time. Here we show that combining GNNs with augmented Neural Ordinary Differential Equations yields temporally stable predictions of the surface forces on a pitching airfoil. We found that our approach, called GNODE, based on Graph Neural Ordinary Differential Equations, provides temporally more stable, spatially smoother, and overall more accurate results than an autoregressive GNN baseline. Tests are conducted on a dataset consisting of a simulations of a pitching airfoil, including transonic shocks, transient behaviour and dynamic non-linearities. Augmenting GNODEs with additional latent dimensions improves the expressivity and accuracy by capturing underlying history effects. The developed method demonstrates an approach that is suitable to model non-linear spatio-temporal systems with exogenous inputs.


## 精读解读（中文）
### 一、研究动机
非定常气动力预测对飞行器设计、优化与认证至关重要，但高保真URANS方法计算成本极高，线性化方法仅适用于小扰动，而自回归图神经网络存在误差累积导致长时间预测不稳定的缺陷。因此需要一种能够稳定、准确预测非定常时空气动场的替代模型。

### 二、技术方案（Method）
本方法提出GNODE框架，将图神经网络（GNN）与神经常微分方程（Neural ODE）结合。数据来源于URANS模拟的二维俯仰翼型表面网格节点上的流场变量（如压力系数）及控制输入（俯仰角、角速度）。空间域构建为图结构（节点为网格点，边基于邻接关系），编码器将节点特征映射到潜在空间，处理器采用多层消息传递机制更新节点表示，解码器映射回物理量。时间演化通过神经常微分方程建模，使用ODE求解器从初始状态积分至目标时刻，并引入额外潜在维度（状态增强）以捕捉历史效应。训练过程以监督方式最小化预测与参考数据之间的均方误差。

### 三、结果（Result）
在包含跨声速激波、瞬态行为和非线性的俯仰翼型数据集上，GNODE相较于自回归GNS基线在长时间稳定性、空间平滑性和总体预测精度上表现更优。增强维度有效减少了预测与参考数据之间的相位滞后，并提升了激波位置和幅值的捕捉能力，表明该方法在复杂非定常流动建模中具有优势。

### 四、结论（Conclusion）
GNODE框架成功实现了对具有外源输入的非线性时空系统（如非定常气动力）的高效替代建模，克服了自回归方法的误差累积问题，为快速、准确的气动力预测提供了新途径，有望应用于工程设计优化与认证分析。

### 五、方法论与关键技术细节
数据基于URANS模拟（NACA 64A010翼型正弦俯仰运动，多种减缩频率与振幅）。损失函数为预测与真实节点值的均方误差。关键超参数包括潜在维度（如4维）、消息传递层数（6层）及学习率。状态增强通过添加冗余潜在变量提升表达力，但增加模型复杂度。局限性：模型泛化至未见运动参数或三维构型的能力尚未验证，且依赖于网格拓扑结构。
