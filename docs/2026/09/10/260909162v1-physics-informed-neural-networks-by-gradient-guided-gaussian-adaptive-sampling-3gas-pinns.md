# Physics-informed neural networks by Gradient-Guided Gaussian Adaptive Sampling (3GAS-PINNs)

- 区域：精读区
- 排名：1
- 匹配度：6.1/10
- 来源：arxiv
- 作者：Yousen Wang, Wei Zhao
- 机构：Northwest University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09162v1) · [PDF](https://arxiv.org/pdf/2609.09162v1)

## TLDR
The paper introduces Gradient-Guided Gaussian Adaptive Sampling Physics-Informed Neural Networks (3GAS-PINNs), which adaptively blend uniform and gradient-derived Gaussian collocation sampling to resolve high-gradient intermittent structures, improving nonlinear PDE simulation accuracy by up to 14× over baseline PINNs.

## Abstract
Physics-informed neural networks (PINNs) provide a mesh-free framework for solving partial differential equations, yet their performance in nonlinear problems is often limited by slow convergence, gradient imbalance, and insufficient resolution to capture localized intermittent structures such as shock waves[1]. These issues arise primarily from the use of fixed weights of loss and uniform collocation point distributions, which cannot adapt to the evolving complexity of the solution field during training. To address these challenges, Gradient-Guided Gaussian Adaptive Sampling Physics-Informed Neural Networks (3GAS-PINNs) is proposed in this paper, which combines uniform probability distribution and Gaussian-smoothed probability distribution derived from the spatial gradients of solution, to maintain global constraint satisfaction as well as concentrating collocation points in regions of high gradient. Thus, intermittency structures like shock wave and solitons can be accurately captured. The method is evaluated on three benchmark nonlinear problems, including one-dimensional forced Burgers equation, Korteweg-de Vries (KdV) equation and nonlinear Schrodinger equation, all of which exhibit steep gradients or strong nonlinearity. In comparison with baseline PINNs, 3GAS-PINNs can effectively promote the physical consistency in intermittent regions. The accuracy of the numerical simulation can be improved by a factor of up to 14.


## 精读解读（中文）
### 一、研究动机
标准 PINN 在非线性 PDE 中常因固定损失权重和均匀/随机配点导致收敛慢、梯度不平衡，并难以分辨激波、孤子等局部间歇结构；这些问题源于训练中解场复杂度演化而采样不能自适应。为此，作者希望在不破坏全局约束的前提下，将计算资源动态集中到高梯度区域。

### 二、技术方案（Method）
提出 3GAS-PINNs，以神经网络 u(x,t;θ) 为代理，用自动微分计算 PDE 残差及空间梯度，损失由 PDE 残差、初始条件和边界条件的 MSE 加权组成并用 Adam 优化。核心是在 warmup 后每隔 K 个 epoch 重采样：先由当前预测解计算梯度场 g_k(x)，再用高斯核卷积得到平滑强度场 G_k(x)，归一化为概率密度 ρ_k(x)，并按混合策略抽取 ⌊ηN⌋ 个自适应点和 N−⌊ηN⌋ 个均匀点组成下一轮配点集。高斯核宽度 σ 根据平均梯度和解的标准差自适应确定，以平衡高梯度集中采样与空间连续性。

### 三、结果（Result）
在 1D 强迫 Burgers 方程、KdV 方程和非线性 Schrödinger 方程三个具有陡梯度或强非线性的基准上，3GAS-PINNs 相比基线 PINNs 更能捕捉激波/孤子等间歇结构，并提升间歇区域物理一致性。以绝对解误差和绝对梯度误差衡量，数值模拟精度最高可提升 14 倍。

### 四、结论（Conclusion）
梯度引导高斯自适应采样通过混合均匀分布与梯度平滑概率分布，使配点动态集中到高梯度区域，同时保留全局约束，从而缓解标准 PINNs 在非线性问题中的收敛慢、梯度不平衡和局部结构抹平问题。三个非线性基准验证表明该方法可显著提高 PINNs 的求解精度和物理一致性，最高约 14 倍。

### 五、方法论与关键技术细节
关键实现包括网络输入为时空坐标 (x,t)、输出预测解，自动微分计算 PDE 所需导数，损失由 PDE 残差、IC 和 BC 的 MSE 构成，并用 Adam 迭代优化。采样算法需设置总配点数 N、自适应比例 η、重采样频率 K、warmup 阶段和经验缩放常数 A；概率密度满足非负且积分为 1，均匀子集用于维持全局 PDE 约束。高斯核宽 σ 过宽会使采样过均匀，过窄会造成配点过度聚集，因此其选择对稳定性和精度至关重要；参考点上的高斯卷积和周期性重采样会带来额外计算开销，且 A、η、K 等超参可能需要针对问题调节。评估使用绝对解误差 e_u 和绝对梯度误差，测试覆盖 Burgers、KdV 和 NLS。
