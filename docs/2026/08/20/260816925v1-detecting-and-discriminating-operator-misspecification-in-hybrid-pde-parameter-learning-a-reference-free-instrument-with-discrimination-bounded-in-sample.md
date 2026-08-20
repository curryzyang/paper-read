# Detecting and Discriminating Operator Misspecification in Hybrid PDE-Parameter Learning: a Reference-Free Instrument, with Discrimination Bounded In Sample

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Eric Fock
- 机构：Université de La Réunion
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16925v1) · [PDF](https://arxiv.org/pdf/2608.16925v1)

## TLDR
TLDR: This paper introduces a reference-free, single-fit information-matrix instrument that both detects operator misspecification in hybrid PDE-parameter learning and discriminates it from mere parameter unidentifiability, demonstrating that standard in-domain accuracy checks are blind to such misspecification while the proposed statistic fires reliably across diverse architectures and pre-registered limits.

## Abstract
We build an instrument that reads, from a single fit and with no oracle, whether the operator a hybrid PDE-parameter estimator postulates is wrong-and separates that from a merely unidentifiable parameter. On one self-adjoint parabolic inverse problem, an information-matrix statistic with plug-in scale and per-seed parameter has median 0.19 under correct specification, rejection rate $0.033$ against a pre-registered ceiling of $0.10$, and rises to $224$ and $85$ under two misspecifications, firing in every replicate. On a correctly specified but non-identifiable design it stays mute-$0.050$ at $n=200$, Clopper-Pearson $[0.024, 0.090]$-while a rank statistic collapses to zero at a pre-registered boundary $c_5^*=2.15\times10^{-3}.$ Two readings of one fit therefore separate the two failures across the three designs a deployable test reaches. That separation is the contribution; detection alone is a crowded flank. In sample it is a bound, out of sample a direction. It is needed because the usual accuracy check is blind: the misspecified estimator's in-domain RMSE is $2.7\times 10^{-2}$, below the observation noise for $σ\geq 0.05,$ while the coefficient is wrong by $29.7\%$ at zero noise, $31.2\%$ at the loudest. Nor is the failure architectural: a one-parameter curve fit, a bare parameter and multilayer perceptrons of $49$ and $241$ parameters converge to the same pseudo-true, matched in closed form to $0.07\%,$ whereas a physics-informed network, with its composite objective, converges to a disjoint one. We report where the instrument is blind, a pre-registered negative where a neural estimator loses to Tikhonov-regularized inversion at recovery, and the hypothesis under which its guarantee holds but a trained network violates it.


## 精读解读（中文）
### 一、研究动机
混合PDE-参数学习（hybrid PDE-parameter learning）中，研究者常用一个假定的算子反演未知系数，但标准的预测精度检查是盲的：当算子被错误指定时，模型在拟合窗口内的RMSE可低至观测噪声之下，同时系数却偏差约30%。现有工作只关注优化或表示能力失败，无法从单次拟合中判断'算子是否错误'，更不能把'算子错误'与'参数不可辨识'区分开来。本文旨在构建一个无参考（reference-free）、只需单次拟合的仪器，同时检测并区分这两类失败。

### 二、技术方案（Method）
在一个自伴抛物型反问题上，采用χ架构的混合PDE-参数估计器：保留预设算子形式，仅用网络或标量学习未知扩散系数，并把解析灵敏度χ=∂F/∂θ注入反向传播。数据为带噪观测，噪声水平σ∈[0,0.2]，在t∈[0,1]内拟合，在t∈[1,2]上评估外推。对每次拟合计算带plug-in尺度和per-seed参数的信息矩阵统计量I_N，并用参数自助法校准；同时计算Fisher秩统计量刻画参数可辨识性。两个读数来自同一次拟合，分别回答'算子是否错误'和'参数是否不可辨识'。研究还比较了一参数曲线拟合、裸标量参数、参数量为49和241的MLP以及物理信息网络（PINN）四类估计器，并用White伪真参数的闭式解作为理论基准。

### 三、结果（Result）
在正确指定时，信息矩阵统计量中位数为0.19，拒绝率0.033（低于预注册上限0.10）；在两种误指定下统计量升至224和85，每个重复均触发。在正确指定但不可辨识的设计中，该统计量保持沉默：n=200时拒绝率0.050，Clopper-Pearson区间[0.024,0.090]；而秩统计量在预注册边界c5*=2.15×10^-3处塌缩到零。误指定估计器的域内RMSE为2.7×10^-2，在σ≥0.05时低于观测噪声，但系数在零噪声时错29.7%、噪声最大时错31.2%；其域外误差的log-log斜率为0.0049，而正确指定估计器为2.004。四类估计器收敛到同一伪真值（闭式匹配误差0.07%），而PINN由于复合目标函数收敛到不相交的伪真值；在结构化系数恢复任务上，神经估计器比Tikhonov正则化反演差1.8到4倍。

### 四、结论（Conclusion）
本文的贡献不是'检测'本身（该领域已很拥挤），而是从单次拟合中给出两个正交读数，将'算子误指定'与'参数不可辨识'明确分离。样本内该分离是一个边界，样本外是一个方向；这种分离是部署可用测试时所需的关键能力。由于误指定估计器的预测精度检查完全失效，必须用这类参考自由的规格化检验来验证混合PDE参数学习的结果，而不能靠域内RMSE或外推误差。

### 五、方法论与关键技术细节
关键细节包括：问题设定为自伴抛物反问题，缺失一个模态分量；观测噪声σ∈[0,0.2]，拟合窗t∈[0,1]，外推窗t∈[1,2]。估计器方面：一参数曲线拟合、裸标量、49/241参数MLP都收敛到相同伪真值α*=0.007033，自助区间重叠；PINN因复合损失定义为不同M估计问题，收敛到不相交的0.006939。统计量方面：I_N采用plug-in尺度和per-seed参数，经参数自助法校准，预注册拒绝率上限0.10；Fisher秩统计量的预注册边界c5*=2.15×10^-3。限制方面：报告了仪器的盲区设计、神经估计器在结构化系数恢复上输给Tikhonov的预注册阴性结果，以及H2假设下保证成立但训练网络可能违反的情形；本文不声称结论跨所有物理系统普适，只在一个可精确求解的算子上建立了证据。
