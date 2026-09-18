# Learning-Induced Dynamical Transition in Recurrent Neural Networks

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Varun Vaidya
- 机构：University of South Dakota
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19288v1) · [PDF](https://arxiv.org/pdf/2609.19288v1)

## TLDR
This paper develops a non-equilibrium dynamical mean-field theory showing that slow feedback-driven learning in recurrent neural networks generates an evolving effective feedback strength that drives a bifurcation from chaotic to stable task-dependent dynamics, predicting a learning-rate-dependent critical time and quantitatively matching simulations.

## Abstract
Learning in recurrent neural networks can fundamentally reshape their underlying dynamics, transforming initially chaotic activity into stable task-dependent behavior. We develop a non-equilibrium dynamical mean-field theory(DMFT) to describe this transition during learning. We show that a slow feedback-driven learning process generates an evolving effective feedback strength that drives the network through a transition from chaotic to stable dynamics defined by a bifurcation of the DMFT solution. By deriving the two-time correlation function throughout learning, we identify a critical feedback strength and a corresponding learning rate dependent critical time separating these regimes. The transition arises from the progressive deformation of an effective dynamical landscape by the growing learned feedback structure. Starting from the untrained state, the theory predicts the time evolution of the network output during training and shows quantitative agreement with numerical simulations.


## 精读解读（中文）
### 一、研究动机
循环神经网络在学习后可从混沌活动转变为稳定任务行为，但既有理论多关注最终训练态或静态相图，缺乏描述学习过程中非平衡动力学如何连续驱动这一转变的理论。本文旨在建立学习过程中的动态平均场理论，把学习本身视为产生有效反馈控制参数并重塑动力学景观的过程。

### 二、技术方案（Method）
模型为连续时间率型RNN：τ_c dx_i/dt=-x_i+g^2ΣJ_ij φ(x_j)+ΣW_i^fb y(t)，输出y=Σw_i^out φ(x_i)，J与W^fb为高斯随机耦合，φ=tanh，目标为常数y*=A~O(√N)，读出自适应遵守误差驱动的慢学习规则dw_i^out/dt=α/N (y*-y)φ(x_i)，且α≪1/τ_c。作者用MSRJD路径积分引入响应场并对J、W^fb做无序平均，在大N极限下得到单神经元有效方程、输出方程⟨y(t)⟩=α∫ds(y*(s)-⟨y(s)⟩)C(t,s)、两时自相关Δ(t,s)的演化方程以及由Δ决定C(t,s)的自洽闭合系统。随后利用慢学习时间尺度分离，在中心时间T=(t+s)/2与相对时间τ=t-s的近对角区域忽略慢导数，将问题化为SCS型方程(1-∂τ^2)Δ=g^2∫Dz[∫Dx φ(...)]^2+ŷ^2，从而用有效势的形变和分岔分析学习轨迹，并与数值模拟对比输出演化。

### 三、结果（Result）
理论表明，慢反馈学习会生成随时间增长的有效反馈强度，使DMFT解发生分岔，网络从混沌动力学转变到稳定动力学；两时相关函数给出临界反馈强度及依赖学习率α的临界时间，临界前后分别对应快速混沌弛豫与慢变相关平台。该转变源于学习形成的反馈结构逐步形变有效动力学景观。作者从初始未训练态预测训练中网络输出的时间演化，并与数值模拟取得定量一致。

### 四、结论（Conclusion）
本文把稳定计算不是看作固定训练结构的静态属性，而是慢塑性适应动态诱导的动力学相变结果，为理解RNN如何从内部混沌走向可靠任务动力学提供了非平衡DMFT框架。结论强调学习轨迹本身可作为有效控制参量，并提示该框架可推广到不同目标强度与学习规则。

### 五、方法论与关键技术细节
关键实现细节包括：大N极限、J_ij与W_i^fb零均值高斯分布（方差分别为g^2/N与σ_fb^2/N）、tanh激活、常数目标A~O(√N)以令反馈与内部混沌同阶，并取σ_fb=1作归一化；损失/误差为e=y*-y，学习率为α且满足α≪1/τ_c。DMFT中利用MSRJD响应场、无序平均和跨神经元关联在大N下被抑制，得到由C(t,s)、Δ(t,s)和⟨y⟩构成的自洽方程；解析部分采用中心时间-相对时间分离、忽略∂_T、假设输出在τ上近似常数，并化为SCS有效势与分岔条件。局限性是三重积分闭式求解代价高且直接数值解缺少直觉，SCS近对角近似牺牲部分定量精度，主要针对大N、慢学习、常数目标和σ_fb=1设定，未包含有限N修正及更一般动态目标的完整处理。
