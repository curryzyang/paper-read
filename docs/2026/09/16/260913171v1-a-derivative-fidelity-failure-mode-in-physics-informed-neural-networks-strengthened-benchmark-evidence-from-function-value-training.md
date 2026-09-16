# A derivative-fidelity failure mode in physics-informed neural networks: strengthened benchmark evidence from function-value training

- 区域：精读区
- 排名：2
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Koji Koyamada
- 机构：Osaka-seikei University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13171v1) · [PDF](https://arxiv.org/pdf/2609.13171v1)

## TLDR
This paper shows that physics-informed neural networks trained only on function values can fit smooth target functions accurately while their automatic-differentiated second derivatives remain substantially inaccurate—especially near high-curvature boundaries—revealing a derivative-fidelity failure mode and arguing that PINN validation must separately assess derivative and residual reliability.

## Abstract
Physics-informed neural networks (PINNs) use automatic differentiation to impose differential-equation residuals, but good agreement in function values does not necessarily imply accurate derivatives. This paper formulates derivative fidelity as a failure mode of PINNs and tests it with one-dimensional benchmarks. Multilayer perceptrons are trained only on function values for sin(x) and exp(x), while second derivatives obtained by automatic differentiation are evaluated separately. The hypothesis is strengthened by additional tests over training-point density, activation functions, endpoint-dense evaluation, and both L2 and maximum-error diagnostics. The results show that visually accurate function approximation can coexist with substantially larger second-derivative errors, especially near high-curvature boundary regions. The experiment provides a diagnostic protocol for distinguishing value accuracy from physics-residual reliability.


## 精读解读（中文）
### 一、研究动机
PINN通过自动微分把微分方程残差纳入训练，但函数值拟合好并不保证导数准确，而已有失败模式讨论多集中在优化和损失平衡。本文把导数保真度明确表述为PINN的一种失败模式，并在一维基准中隔离函数值精度与二阶导数精度，以检验其是否可能解释残差不可靠或结构保持失败。

### 二、技术方案（Method）
实验选取sin(x)于[-2π,2π]和exp(x)于[-2,2]两个一维光滑目标，其解析二阶导数已知；使用全连接MLP，3个隐层、宽度64、Adam优化、2500轮，仅用函数值均方误差损失训练，基线训练点128、tanh激活。训练后在均匀密集网格上评估函数误差和由自动微分得到的二阶导数误差，并加强验证训练点密度32、64、128、256、512，激活函数tanh、sine、gelu，exp(x)的端点密集评估及区域误差，以及统一报告RMSE和最大绝对误差。

### 三、结果（Result）
基线中sin(x)函数值误差约在1e-3或以下，但二阶导数误差在局部达到约1e-2至1e-1；exp(x)函数曲线视觉上仍接近真值，但二阶导数在x=1.6以后尤其x=2附近高曲率右边界显著劣化，误差比内部多数区域大若干数量级。加强验证显示，增加训练点不能单调消除exp(x)二阶导数误差，其二阶导数RMSE约1量级、最大绝对误差约1e1；sine激活在sin(x)上取得最低二阶导数RMSE约0.023，而exp(x)最大二阶导数误差仍达约3.93，tanh约6.21；端点密集评估把主要失败定位在右高曲率边界，最大误差指标揭示平均指标掩盖的局部失败。

### 四、结论（Conclusion）
结果表明，在仅做函数值训练、有限采样和固定架构/优化条件下，函数值精度不能作为导数精度或物理残差可靠性的替代指标；即使函数图看起来准确，含二阶导的PDE残差仍可能在高曲率或边界区域不可靠。因此PINN验证应把导数误差剖面、端点/高曲率诊断以及最大绝对残差/误差当作一等诊断，与函数值精度分开报告；该研究是诊断性证据而非通用不可能定理，更强训练目标或架构可能改善导数保真度。

### 五、方法论与关键技术细节
数据为解析已知的sin与exp一维函数，评价包含均匀密集网格和exp靠近x=2的端点密集网格；网络为3隐层宽64的MLP，Adam，2500轮，损失仅函数值MSE，二阶导数由自动微分获得而非直接拟合，基线128训练点与tanh激活。强化实验覆盖训练点密度扫描、tanh/sine/gelu激活比较、端点区域误差和L2与最大绝对误差诊断，核心指标为函数RMSE/最大误差与二阶导数RMSE/最大误差。局限在于任务为标量一维、网络族较小，未构成通用定理，也未测试导数增强损失、Sobolev训练、高曲率区重采样以及Poisson或热方程等PDE基准。
