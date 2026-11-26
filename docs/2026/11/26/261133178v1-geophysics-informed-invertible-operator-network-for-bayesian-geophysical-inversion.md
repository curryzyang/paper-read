# Geophysics-informed invertible operator network for Bayesian geophysical inversion

- 区域：精读区
- 排名：1
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Yangwen Zhang, Xintong Wang, Xiaofei Guan, Peng Yu
- 机构：Shanghai Normal University, Tongji University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33178v1) · [PDF](https://arxiv.org/pdf/2611.33178v1)

## TLDR
The paper proposes GI-ION, a geophysics-informed invertible operator network that integrates an invertible neural network into a DeepONet-style operator-learning framework with physics-informed and independence-oriented training to efficiently approximate Bayesian posteriors and enable uncertainty sampling for geophysical inversion under sparse, noisy observations.

## Abstract
Geophysical inverse problems are inherently ill-posed because of sparse observations and measurement noise. Classical sampling-based Bayesian inference methods, such as Markov chain Monte Carlo (MCMC), are computationally prohibitive because they require many forward simulations. Data-driven machine-learning methods often struggle to produce physically consistent solutions when training data are limited. To address these issues, we propose a geophysics-informed invertible operator network (GI-ION) that integrates an invertible neural network (INN) within a deep operator-learning framework for efficient Bayesian geophysical inversion. The INN serves as the branch network and transforms the model parameters into branch coefficients that represent the forward solution and a latent variable that captures uncertainty in the inverse problem. By learning the forward operator and enforcing statistical independence between the branch coefficients and the latent variable, GI-ION enables efficient sampling from a learned conditional approximation, even with sparse boundary observations. We validated GI-ION on three representative cases: 1D surface-wave dispersion and travel-time tomography for a 2D synthetic random-field model and a seismic-slice model. Numerical experiments demonstrate robust performance across diverse problem settings and efficient conditional sampling.


## 精读解读（中文）
### 一、研究动机
地球物理反演常因观测稀疏、含噪且间接而严重不适定，传统MCMC类贝叶斯采样需要大量正演模拟，计算代价高；纯数据驱动深度学习方法在训练数据有限时又难以保证物理一致性。为此，作者希望构建一个既能嵌入地球物理控制方程、又能在离线训练后高效进行条件后验采样的算子学习框架。

### 二、技术方案（Method）
GI-ION在DeepONet式算子学习框架中用可逆神经网络INN替换确定性branch网络：输入模型参数m被双射映射为前向解的分支系数b(m)和捕获反演非唯一性的潜变量z(m)，并满足维度平衡d_m=P+d_z；前向场由b(m)与trunk网络T(x)的内积表示。训练时联合数据损失与物理损失，数据项约束观测点处前向输出与观测d一致，物理项在整个域查询点上施加控制方程约束；同时引入面向独立性的训练目标，惩罚分支系数与潜变量之间的统计依赖，使给定b后z仍近似服从标准正态先验。反演时先用trunk在观测点形成的矩阵T_o的Moore–Penrose伪逆估计b*=T_o†d，再从z~N(0,I)采样并经INN逆映射m=B^{-1}(b*,z)生成条件样本，从而避免在线迭代MCMC采样。

### 三、结果（Result）
作者在三个代表性算例上验证了GI-ION：一维面波频散反演、二维合成随机场模型的走时层析以及地震切片模型的走时层析。数值实验表明，该方法在多种问题设置下具有稳健表现，并能在稀疏边界观测条件下进行高效条件采样；同时实验中传统INN常用的MMD损失表现出更强的残余依赖，而所提出的独立性导向目标改善了条件不确定性估计。

### 四、结论（Conclusion）
GI-ION将可逆网络、DeepONet算子学习、物理约束和独立性约束结合，能够在离线训练后同时学习前向算子并构造贝叶斯后验的条件近似，从而以较低在线成本实现地球物理反演的不确定性采样。该方法为观测稀疏、训练数据有限且需要物理一致性的贝叶斯地球物理反演提供了一条可行途径。

### 五、方法论与关键技术细节
关键实现包括：以模型参数样本和对应观测数据训练，trunk网络以空间查询坐标为输入并输出P维基函数，branch网络输出P维系数与d_z维潜变量；潜变量先验取标准正态N(0,I)，贝叶斯框架中模型参数另有先验p0(m)；观测系数通过T_o†d获得，矩阵满列秩时为唯一最小二乘解，否则为最小范数最小二乘解；损失由观测点L2数据项、全域物理残差项及分支系数—潜变量独立性惩罚组成，物理项含加权系数α、β。在线反演只需一次伪逆投影、潜变量采样和一次可逆映射，避免重复正演；主要约束是d_m=P+d_z的维度平衡以及T_o的秩条件，且qθ(m|d)只是学习到的条件后验近似而非精确闭式后验，高维地球物理场景中MMD类正则可能不稳定，这也是作者改用独立性目标的原因之一。
