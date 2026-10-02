# How Far is Adam from Natural Gradient Descent?

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Vihaan Paka-Hegde
- 机构：San Francisco University High School
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00004v1) · [PDF](https://arxiv.org/pdf/2610.00004v1)

## TLDR
The paper finds that Adam’s geometric trajectory deviates increasingly from true natural gradient descent as loss landscapes become ill-conditioned or non-convex, yet it still achieves strong optimization because its effectiveness stems from balancing diagonal Fisher approximation errors with momentum smoothing rather than closely following the natural gradient.

## Abstract
Adam is the standard optimizer in deep learning, yet its geometric relationship to natural gradient descent (NGD) contains unresolved questions. We study Adam's full update rule, including momentum, as a diagonal empirical Fisher approximation subject to diagonal truncation, empirical label substitution, and temporal lag. Using the scale-invariant $γ(Δθ)$ metric, we measure Adam's geometric deviation from true NGD across four loss landscapes: well-conditioned linear regression, ill-conditioned linear regression, logistic regression, and a non-convex small neural network. Adam's geometric trajectory is context-dependent. Deviation remains low in well-conditioned settings but rises significantly under ill-conditioning, reaching misalignments of $\approx 10^3$ in the neural network. Higher geometric drift correlates with slower initial optimization but does not degrade final objective minimization; Adam consistently reaches low loss. Furthermore, the improved empirical Fisher (iEF) tracks more stable paths than the standard empirical Fisher (EF), which frequently oscillates or diverges. Our results suggest Adam's practical optimization power may stem from a balance of structural approximation errors and momentum smoothing rather than close tracking of the natural gradient path.


## 精读解读（中文）
### 一、研究动机
Adam是深度学习标准优化器，但其完整更新规则与自然梯度下降（NGD）的几何关系仍不清楚。Kingma等以坐标预条件近似Fisher对角为动机，但经验Fisher的标签替换和近最优区扭曲可能破坏这种解释，且已有FAdam分析将动量设为零而遗漏Adam关键组件。本文因此直接研究带主动动量的Adam完整更新，隔离对角截断、经验标签替换和时间滞后三种近似叠加后的几何代价。

### 二、技术方案（Method）
使用尺度不变的γ(Δθ)=(ΔθᵀFΔθ)^(1/2)/|Δθᵀ∇L|指标，度量SGD、对角EF、对角iEF、Adam和精确NGD更新方向相对真实自然梯度的偏离。实验覆盖四个损失地形：良条件线性回归（D=10，特征N(0,1)）、病态线性回归（特征方差不对称约10000倍，条件数≈27146）、逻辑回归（N=200，D=10，交叉熵）以及两层ReLU MLP小神经网络（20-32-1，692参数，拟合固定目标网络）。每个场景中迭代执行各优化器更新，同时跟踪γ和训练损失，学习率按基线稳定性而非最快收敛来选择。

### 三、结果（Result）
Adam的几何轨迹依赖上下文：良条件线性回归初始γ≈0.2，病态线性回归初始γ≈0.08但中后期上升并在约1250步超过SGD，逻辑回归初始γ≈1.5、最终≈6，神经网络中γ在约300步峰值达到≈10³。高几何漂移与初期优化更慢相关，但通常不损害最终目标最小化；Adam在四类任务中均达到低损失，并在三个场景中达到或接近NGD损失下限，逻辑回归中则在2000步内未达到基线下限。iEF比标准EF路径更稳定，EF虽有时γ低于SGD，却在非凸神经网络中振荡或发散；NGD收敛步数分别为良条件18、病态44、逻辑17、神经网络>500且伴随数值振荡，而Adam对应约600、约1000、>2000、<500。

### 四、结论（Conclusion）
Adam并不紧密跟踪真实自然梯度路径，其实际优化能力可能来自结构近似误差与动量平滑之间的平衡，甚至可视为一种带坐标幅度归一化的符号梯度下降式方法。γ指标能诊断方向几何，但无法区分稳定更新与幅度爆炸，因为EF可在更低γ下仍导致发散。总体而言，Adam以牺牲严格黎曼几何对齐换取O(D)可扩展性和数值稳健性，主要代价常是收敛步数增加而非最终损失变差；未来可将iEF校正并入Adam动量回路形成IAdam，并在更大模型和CIFAR-10等数据上验证。

### 五、方法论与关键技术细节
关键实现包括：精确NGD需存储并求逆完整Fisher，复杂度为O(D²)存储和O(D³)时间，而Adam用逐坐标EMA的√v̂+ε实现O(D)对角预条件；EF用观测标签的逐样本梯度外积近似Fisher，iEF通过梯度重缩放修正反比例投影问题；Adam同时包含对角截断、经验标签替换和动量时间滞后。学习率设置为SGD在四场景为0.01、0.0001、0.01、0.001，Adam为0.01、0.005、0.01、0.01，EF/iEF与Adam相同，NGD为0.1、0.1、0.1、0.05。局限包括实验规模小、γ只反映方向不反映步长稳定性、iEF在极端病态下仍不稳定、NGD在非凸小网络中出现数值振荡、逻辑回归中Adam未在2000步内达到基线损失，且学习率以稳定性而非绝对速度调优。
