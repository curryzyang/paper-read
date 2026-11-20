# Temporal Extrapolation of Elastic Seismic Wave Propagation in Layered Media Using Neural Operators

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Dibyajyoti Nayak, Yuze Pu, Kami Mohammadi, Somdatta Goswami
- 机构：Johns Hopkins University, University of Utah
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25130v1) · [PDF](https://arxiv.org/pdf/2611.25130v1)

## TLDR
This paper proposes a jointly trained predictor–corrector neural-operator framework—TI-DeepONet with an embedded RK4 time integrator plus an FNO residual spatial corrector—for autoregressive, stress-conditioned extrapolation of elastic SH-wave velocity fields in layered media beyond the training interval, achieving peak-normalized RMSEs of about 0.53–2.31% across four test cases while leaving fully autonomous velocity–stress continuation for future work.

## Abstract
Temporal prediction of seismic velocity fields beyond the time interval represented in training remains challenging for neural operator models. This study develops a coupled neural operator framework for stress-conditioned temporal prediction in layered elastic media. A time-integrator-embedded Deep Operator Network (TI-DeepONet) advances the velocity field through an embedded fourth-order Runge-Kutta (RK4) scheme, while a Fourier Neural Operator (FNO) learns a residual correction to the predicted spatial field. The two components are trained jointly in a predictor-corrector configuration. Prediction is initialized with reference velocity fields at the first two time levels and proceeds autoregressively, with reference stress fields and prescribed excitation supplied throughout rollout, including beyond the training interval. Four cases consider horizontally polarized shear (SH) waves in four-layer soil columns with fixed total depths of 50 and 280 m, excited by third-order Gaussian-derivative (DOG3) wavelets with central frequencies between 0.5 and 6 Hz. Layer thicknesses and shear-wave velocities vary across profiles. Evaluations on test profiles extend beyond the training interval by up to twice its duration. The predictions reproduce principal velocity arrivals and depth-dependent response patterns, with accuracy varying across profiles. Across the four cases, mean peak-normalized root-mean-square errors (NRMSEs) range from 0.53% to 2.31% over the full evaluation windows and from 0.61% to 2.82% over the extrapolation intervals. Both metrics use each profile's peak absolute reference velocity over the full evaluation window as the normalizer. These results demonstrate temporal velocity prediction under reference-stress conditioning for the tested configurations; autonomous continuation of the coupled velocity-stress wavefield remains to be established.


## 精读解读（中文）
### 一、研究动机
地震速度场在训练时间窗之外的时序外推对神经算子仍很困难，自回归 rollout 中局部误差会累积并导致幅值失真、相位漂移或失稳。本文聚焦层状弹性介质中 SH 波传播，将问题设为在全程提供参考应力与给定基底激励条件下的速度场时序预测，作为检验时间更新与空间修正能力的受控第一步，而非自主推进耦合速度—应力系统。

### 二、技术方案（Method）
框架学习一步神经算子，将当前与前一时刻的速度场、参考应力场、基底牵引 q 及时间坐标映射到下一时刻速度场；TI-DeepONet 用四个分支分别编码应力、速度、牵引和时间的两级历史，经乘加融合生成分支系数，主干网络对深度坐标做 Fourier 特征编码并采用可学习小波激活，输出速度变化率并通过内嵌四阶 Runge–Kutta 格式推进得到初步预测，FNO 再学习空间残差修正，二者以 predictor–corrector 方式联合训练。推理时用前两个时间层的参考速度初始化，之后以模型预测速度自回归输入，参考应力与给定激励在整个 rollout 中持续提供，包括训练区间之外。算例为一维 SH 波在总厚 50 m 与 280 m 的四层土柱中传播，层厚与剪切波速变化，采用中心频率 0.5、3.5、6 Hz 的 DOG3 子波激励。

### 三、结果（Result）
在测试剖面上，预测能复现主要速度到时和随深度变化的响应形态，但精度随剖面而异。四个算例在全评估窗口上的平均峰值归一化 NRMSE 为 0.53%–2.31%，在外推区间上为 0.61%–2.82%，归一化因子为各剖面全评估窗口内参考速度峰值绝对值；评估外推长度可达训练时长的两倍。

### 四、结论（Conclusion）
结果表明，在测试配置下，所提耦合 TI-DeepONet–FNO 框架能够在参考应力条件下进行速度场时序预测并外推到训练区间之外。当前框架尚未实现速度—应力耦合波场的自主延续，材料属性也未作为显式输入，因此结论限于应力条件化的速度预测，完整自主正向模拟仍需后续建立。

### 五、方法论与关键技术细节
关键实现点包括两级时间历史输入、应力/速度/牵引/时间四分支编码、b_sigma⊙b_v+b_q 与时间嵌入拼接后的线性融合、深度坐标的 Fourier 特征与自适应小波激活主干、内嵌 RK4 的速率参数化，以及 FNO 残差修正和联合训练。层状介质信息由参考应力场隐式携带，材料属性不是显式网络输入；评估采用峰值归一化 NRMSE 并覆盖全窗口与外推窗口。可见文本未给出损失函数具体形式、权重、网络宽度与训练超参，且框架依赖参考应力与给定激励、限于一维 SH 波和四层土柱配置，尚未验证自主耦合速度—应力演化。
