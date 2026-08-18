# L-FNO: Lorentzian Fourier Neural Operator for Stochastic Event Dynamics

- 区域：精读区
- 排名：1
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Songhee Kang, Jihoon Kang
- 机构：Tech University of Korea
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13562v1) · [PDF](https://arxiv.org/pdf/2608.13562v1)

## TLDR
L-FNO introduces a likelihood-trained stochastic neural operator with Lorentzian spectral memory to model rare, self-exciting event dynamics, improving event likelihood, calibration, and rare-event detection over existing neural operator baselines.

## Abstract
Modern operational systems face uncertainty even in routine conditions, where rare, bursty, and self-exciting events emerge from both exogenous covariates and endogenous event dynamics. Standard neural operators are typically trained as regression-style function-to-function models rather than conditional-intensity estimators, limiting their suitability for sparse event regimes. We introduce the Lorentzian Fourier Neural Operator (L-FNO), a stochastic neural operator that combines an FNO-style covariate path, Lorentzian spectral kernels for history-dependent excitation, and a likelihood-based training objective. We evaluate L-FNO on eight synthetic point-process benchmarks and three real-world datasets covering disease outbreak prediction and semiconductor fault or defect detection. L-FNO improves event likelihood, calibration diagnostics, and rare-event detection over regression- and likelihood-based neural operator baselines. These results show that structured spectral memory and likelihood-based learning provide effective inductive biases for neural operator models of stochastic event dynamics.


## 精读解读（中文）
### 一、研究动机
现代运营系统在常规条件下也面临不确定性，罕见、突发且自激的事件由外生协变量和内生事件动态共同产生。标准神经算子通常训练为回归式函数到函数模型，而非条件强度估计器，难以处理稀疏事件场景，因此需要一种能建模随机事件动态的神经算子。

### 二、技术方案（Method）
L-FNO由三个L-FNO块堆叠而成，同时处理外生协变量序列X(t)和严格滞后的事件历史h(t)的离散傅里叶变换。在谱域中，强度估计为λ̂(ω)=R(ω)x̂(ω)+Σ_k[α_k/(β_k+iω)]ĥ(ω)，其中R(ω)为可学习复值算子，Lorentzian核α_k/(β_k+iω)对应时域中的多尺度指数激发核Σ_k α_k e^{-β_k t}，实现Hawkes自激机制。经逆傅里叶变换和Softplus激活得到正强度λ̂(t)。模型使用滑动窗口内的Poisson负对数似然损失训练，直接优化条件强度而非回归残差。

### 三、结果（Result）
在8个合成点过程基准和3个真实数据集（疾病爆发预测、半导体故障/缺陷检测）上，L-FNO相较回归式与似然式神经算子基线，在事件似然、校准诊断和罕见事件检测方面均取得更优性能，验证了结构化谱记忆和似然学习的有效性。

### 四、结论（Conclusion）
结构化谱记忆与似然学习为神经算子建模随机事件动态提供了有效归纳偏置，L-FNO能够学习外生协变量与内生历史依赖共同驱动的条件强度，并在稀疏罕见事件场景中实现更好的概率校准与检测能力。

### 五、方法论与关键技术细节
关键点包括：Lorentzian核与Hawkes指数激发核精确对应，Proposition 1证明了指数混合在因果L^2核空间中的稠密性，但正振幅实现仅覆盖兴奋性Hawkes子类；MSE训练在稀疏事件下会产生均值坍缩，而Poisson NLL提供不对称梯度，事件时刻梯度随强度趋零发散，非事件时刻恒定下降，从而避免严重低估；学习到的α_k和β_k可解释为自激强度和持久时间τ_k=1/β_k；模型采用Softplus确保强度为正；损失在长度L的滑动窗口上计算。
