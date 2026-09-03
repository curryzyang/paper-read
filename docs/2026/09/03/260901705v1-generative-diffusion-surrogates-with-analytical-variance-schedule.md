# Generative Diffusion Surrogates with Analytical Variance Schedule

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Patrick Reichherzer, Gianluca Gregori, David N. Hosking, Subir Sarkar
- 机构：Max Planck Institute for Security and Privacy, University of Cambridge, University of Oxford, Gonville & Caius College, Princeton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01705v1) · [PDF](https://arxiv.org/pdf/2609.01705v1)

## TLDR
This paper proposes physics-anchored diffusion surrogates for stochastic transport by setting the forward noise schedule from an analytically or empirically known variance law, so that generative time becomes a calibrated physical clock and the learned score models only non-Gaussian structure, enabling accurate, entrance-only emulation of transport distributions.

## Abstract
Stochastic transport describes physical systems in which an initially structured distribution spreads under unresolved forcing, scattering, or heterogeneous media. Useful surrogates for such systems should be probabilistic, time-resolved, and able to represent non-Gaussian distributional structure. Generative diffusion models, which corrupt data with Gaussian noise and learn a reverse flow back to structured states, have these properties. Their noise schedules, however, are usually chosen heuristically: image and audio generation---the canonical use cases---provide no physical clock. In transport, by contrast, the variance, or mean-square displacement, is often known from macroscopic theory or empirical scaling even when the full distribution is not. Here we prescribe the forward noising rate as the time derivative of this variance, turning generative time into a calibrated transport clock. The variance path is enforced by construction, while the learned score field represents how non-Gaussian structure inherited from entrance data is smoothed along that path, requiring no intermediate-time physical transport data. For ballistic-to-diffusive transport in turbulent plasmas, the surrogate matches test-particle distributions, reproduces the laboratory-measured variance scale, and tracks the simulated kurtosis evolution without schedule tuning, enabling calibrated emulation and likelihood-based inference.


## 精读解读（中文）
### 一、研究动机
随机输运系统（如湍流等离子体中的粒子输运）需要能够表示非高斯分布结构、随时间演化的概率代理模型。生成扩散模型具备这些性质，但其噪声调度通常按图像生成等场景的经验规则选择，缺乏物理时钟。在输运问题中，方差（均方位移）常可由宏观理论或经验标度已知，即使完整分布未知。因此，将前向噪声率设为该方差的时间导数，使生成时间成为校准的输运时钟，从而实现物理锚定的代理建模。

### 二、技术方案（Method）
采用方差爆炸（VE）随机微分方程框架，前向过程为 dx = g(τ)dW，其中噪声调度 g^2(τ) = dσ^2(τ)/dτ，σ^2(τ) 为解析给定的宏观方差律（如弹道-扩散过渡的方差公式 σ^2(τ) = C^{-1}[τ - τ_c(1 - e^{-τ/τ_c})]）。初始分布 x0 取入口分布 P0，训练时仅使用入口样本及其按该方差路径合成的高斯扰动，无需中间时刻物理输运数据。用神经网络学习score函数 sθ(x,τ) 逼近真实score，训练后通过概率流ODE或反向SDE采样，在指定读出时间 τ* 生成代理边际分布。方差路径由调度解析强制执行，网络只学习沿该路径非高斯结构（继承自P0）被平滑的形状。

### 三、结果（Result）
针对湍流等离子体中的弹道-扩散输运，所提物理锚定调度（VE-Telegraph）无需调度调优即可匹配测试粒子分布，复现实验室测量的方差尺度，并跟踪模拟的峰度演化。与线性、余弦、Karras/EDM等启发式调度相比，只有锚定调度的生成时间对应物理时钟，方差和峰度路径符合理论预测。反向SDE和概率流ODE采样均能实现预期的高斯卷积边缘路径，峰度松弛与解析式 K_M(τ)=K0(σ0^2/(σ0^2+σ^2(τ)))^2 一致。

### 四、结论（Conclusion）
将扩散模型的噪声调度锚定到宏观方差律，可把生成时间转化为校准的输运时钟，从而构建物理上可信的概率代理模型。该方法在仅需入口分布训练的条件下，能够准确再现从弹道到扩散过渡的方差尺度和高阶级非高斯结构演化，适用于科学仿真与似然推断。

### 五、方法论与关键技术细节
关键点：1) 方差锚定通过构造保证二阶矩路径，score网络只需学习残余形状，避免学习方差演化；2) 边际分布为入口分布与高斯核的卷积，峰度弛豫有闭式解；3) 与Kac/telegraph核对比说明相同方差律可对应不同输运机制，高斯代理核与有界支撑核会存在高阶矩差异；4) 训练数据仅需入口样本及其合成噪声，无需中间时刻物理数据；5) 限制包括高斯核假设无法表示有限传播速度、记忆效应或轨迹相关性，且马尔可夫近似忽略了相关尺度以上的记忆；6) 方法保持VE-SDE框架，仅修改标量调度，兼容现有扩散模型基础设施，计算开销低。
