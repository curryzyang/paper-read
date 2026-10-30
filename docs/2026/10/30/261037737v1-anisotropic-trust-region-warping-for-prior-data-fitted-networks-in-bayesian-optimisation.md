# Anisotropic Trust Region Warping for Prior-Data Fitted Networks in Bayesian Optimisation

- 区域：精读区
- 排名：8
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Samuel Younger, Tinkle Chugh, George De Ath
- 机构：University of Exeter, Imperial College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37737v1) · [PDF](https://arxiv.org/pdf/2610.37737v1)

## TLDR
The paper introduces Anisotropic Trust Region warping, which estimates per-dimension lengthscales via kernel target alignment and affinely rescales the input space within a trust region to align mismatched objective functions with a PFN’s fixed meta-training prior, improving Bayesian optimisation without retraining and preserving its \(\mathcal{O}(dN^2)\) inference cost.

## Abstract
Prior-Data Fitted Networks (PFNs) replace the hyperparameter refitting of Gaussian Process (GP) surrogates in Bayesian optimisation with a single forward pass, at the cost of a prior that is fixed at meta-training time. We show empirically that a PFN's predictive log-likelihood falls increasingly behind that of a refitted GP as the objective function's lengthscale grows beyond the mode of the PFN's meta-training prior, and that this deficit carries over to optimisation performance. To correct the mismatch without retraining the network, we introduce Anisotropic Trust Region (ATR) warping. Per-dimension lengthscales are estimated by kernel target alignment, and an affine rescaling of the input space maps the objective onto the lengthscale the PFN expects, with a trust region around the anchor determining which observations are retained, leaving the PFN's $\mathcal{O}(d \cdot N^2)$ inference cost unchanged. On functions drawn from a Matérn-3/2 kernel, ATR warping improves optimisation performance of the PFN at both extremes of the lengthscale range. Our implementation is publicly available at https://github.com/youngers2006/Trust-Region-Warping-For-PFNs.


## 精读解读（中文）
### 一、研究动机
PFN 用单次前向替代 GP 超参重拟合，但其先验在元训练时固定；论文实证显示目标函数长度尺度超过元训练先验众数后，PFN 预测对数似然逐渐落后于重拟合 GP，并传导到贝叶斯优化性能。因此需要不重训网络、不增加推理复杂度地纠正先验-目标长度尺度失配。

### 二、技术方案（Method）
方法先用核目标对齐（KTA）从观测估计逐维长度尺度：以中心化 y y^T 为目标矩阵、Matérn-3/2 核矩阵为候选，梯度下降最大化归一化 Frobenius 内积，复杂度 O(dN^2)。然后以当前锚点 x_opt 为中心构造各向异性信赖域：按 s_j=max(s_min,j, l_j/l_target) 设每维缩放因子，边长 L_j=min(1,s_j)、可行上界 u_j=min(1,1/s_j)，l_target 取 PFN 先验众数 0.1385；区域平移回定义域以保宽，连续 τ 次无改进则均匀重启。用 s_min,j=2 d_{k,j}（x_opt 附近按 l_j/l_target 各向异性缩放的 L∞ 范数下 k 个最近点的最大偏差）设下限，避免上下文饥饿；过滤并仅保留落在信赖域超立方体内的观测，经 ψ_j(x_j)=(x_j-a_j)/s_j 仿射映射后送入冻结 PFN 前向，采集函数在映射后的 Π[0,u_j] 上优化，推理仍为 O(dN^2)。

### 三、结果（Result）
在 Matérn-3/2 合成函数、15 个长度尺度 [0.021,1.5]、d∈{2,5,10}、50 次迭代、21 次重复的实验中，ATR-PFN 在长度尺度范围两端均改善基础 PFN，低端改善较温和，5D/10D 同样存在但边际更小。分布内估计比值接近 1，信赖域覆盖大部分域，ATR-PFN 近似 PFN，残余收益主要来自信赖域与重启而非近恒等翘曲；150 次迭代时低长度尺度优势明显扩大。诊断实验显示 PFN 相对重拟合 GP 的预测对数似然随长度尺度增大而恶化：1D 在 l≈0.1 后开始落后、l=2.0 时约差 2.5 nat，10D 起点约 l≈0.5、差距约 0.4 nat；用真实长度尺度替代 KTA 估计的消融表明估计方差不是改进主因。

### 四、结论（Conclusion）
论文结论是固定先验 PFN 的预测与优化性能会随长度尺度偏离先验众数而退化，而 ATR 翘曲可在不重训、不提高 O(dN^2) 推理成本的前提下，通过输入空间各向异性缩放和信赖域局部化把失配目标映射回 PFN 期望尺度，从而在失配长度尺度上提升优化表现。方法只隔离了长度尺度这一失配轴，跨多个先验失配轴及标准基准上的表现仍待验证，且可与其它冻结 PFN 自适应或输入翘曲方法组合。

### 五、方法论与关键技术细节
关键实现细节包括：采用 Matérn-3/2 先验族与 PFN 先验众数 l_target=0.1385，KTA 以中心化目标矩阵和核矩阵的归一化 Frobenius 内积为准则并用梯度下降优化逐维长度尺度；信赖域边长直接由长度尺度比决定而非 TuRBO 的成功/失败计数器调体积，锚点固定、越界平移不截断、τ 次无改进重启、k 近邻 L∞ 下界保证至少 k 个上下文点。复杂度保持 O(dN^2)，但 KTA 在稀疏数据上方差高且估计向范围中心收缩，会传导到优化方差；缩小信赖域会丢弃域外评估，k 近邻下限又限制翘曲幅度，高维中最近点稀疏使区域偏大、翘曲效果减弱。实验为各向同性 Matérn-3/2 抽样、d 为 2/5/10、长度尺度 15 档、21 次重复、50 或 150 次迭代，并以重拟合 ARD GP 和随机搜索作参照；局限性是仅研究长度尺度单轴失配，未系统测试多轴同时失配及标准基准，且高对齐只是好核的充分非必要条件。
