# Orthogonal Gradient Constraints Shape Noisy-Label Memorization Dynamics

- 区域：精读区
- 排名：6
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Richard Mai
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16231v1) · [PDF](https://arxiv.org/pdf/2607.16231v1)

## TLDR
OrthoGrad, which removes the gradient component parallel to the weight vector, reduces noisy-label memorization in small-data CNN settings but is regime-dependent and does not universally prevent eventual memorization.

## Abstract
Modern neural networks can fit corrupted training labels, making noisy-label learning a useful setting for studying memorization-driven overfitting. Most regularization methods modify the objective, architecture, or data distribution; here we instead study a geometric intervention on the optimizer update itself. We evaluate OrthoGrad, which removes the component of each weight gradient parallel to the current weight vector, in noisy-label image classification. On MNIST with small-data regimes, OrthoGrad improves test accuracy most clearly for CNNs while reducing corrupted-label fitting. Mechanism diagnostics based on weight norms and gradient-weight cosine similarity suggest that the projection has the strongest effect when the raw gradient contains a nontrivial radial component, and becomes weaker in larger-data regimes where gradients are already nearly orthogonal to weights. Additional CIFAR-10 ResNet-18 experiments show that the method can alter memorization trajectories but does not prevent eventual noisy-label memorization. These results support orthogonal update constraints as a useful diagnostic for studying learning dynamics, while showing that OrthoGrad is regime-dependent rather than universally regularizing.


## 精读解读（中文）
### 一、研究动机
现代神经网络能够拟合被破坏的标签，导致过拟合记忆现象，现有正则化方法通过修改目标函数、架构或数据分布来缓解，但本文旨在研究优化器更新本身的几何干预——正交梯度约束——对噪音标签记忆动态的影响。

### 二、技术方案（Method）
采用OrthoGrad方法，从每个权重梯度中移除与当前权重向量平行的分量，得到正交梯度g_perp = g - λ〈g,w〉/ (‖w‖²+ε) w，固定λ=1（完全投影），仅对权重张量应用，不包括偏置和归一化参数，可选的重新归一化变体将投影梯度缩放至原始梯度范数。使用Adam优化器，其余超参数不变。在MNIST小数据（500样本，30%噪音标签）上用小型MLP（两层隐藏层64和32）和小型CNN（四层卷积+池化+两层线性），以及CIFAR-10 ResNet-18（5000样本，20%噪音标签）进行实验，并分析权重范数和梯度-权重余弦相似度作为机制诊断。

### 三、结果（Result）
在MNIST CNN上，OrthoGrad将测试准确率从77%提升至82.4%（小MLP上从64%提升至65.5%但不显著），同时降低了对噪音标签的拟合。机制分析显示，小数据下OrthoGrad保持更低权重范数，预投影梯度-权重余弦相似度显著为负，投影移除了实质性径向分量；而在大数据（48000样本）下余弦相似度接近零，投影效果减弱。CIFAR-10实验中，OrthoGrad改变了记忆轨迹但未最终阻止噪音标签记忆，准确率与基线相当。

### 四、结论（Conclusion）
正交梯度约束可作为研究学习动态的有效诊断工具，其效果依赖于数据规模，在小数据噪音标签场景中最显著，但并非通用正则化器；未来需在更大架构和数据集上检验，并与权重衰减、提前停止等方法系统比较。

### 五、方法论与关键技术细节
关键细节：1) 仅对权重张量进行正交投影，排除偏置和归一化参数；2) 固定λ=1的完全投影设置，另提供重新归一化变体；3) 使用Adam优化器，其余超参数不变；4) 梯度-权重余弦相似度作为诊断指标，解释径向分量的作用；5) 局限性：最强结果限于MNIST尺度，CIFAR-10效果混合且不能防止长期记忆噪音标签；6) 与权重衰减的区别：OrthoGrad不直接缩小参数范数，而是改变更新方向；7) 需进一步研究自适应投影强度。
