# MDN-VJEPA: Multimodal Probabilistic Joint-Embedding World Models

- 区域：精读区
- 排名：8
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Yongchao Huang
- 机构：University of Aberdeen
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.13956v1) · [PDF](https://arxiv.org/pdf/2610.13956v1)

## TLDR
MDN-VJEPA makes joint-embedding world models multimodal by predicting future latent states as Gaussian mixtures whose components represent distinct, temporally coherent, and compositionally consistent alternative futures, improving planning decisions under branching uncertainty.

## Abstract
Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting future representations rather than reconstructing observations. Variational JEPA (VJEPA) gives this prediction probabilistic semantics and permits flexible conditional predictive families. We propose MDN-VJEPA, a multimodal probabilistic JEPA that instantiates the latent predictor as a mixture density network (MDN), representing future states with a Gaussian mixture whose components encode alternative futures, their probabilities, and within-mode uncertainty. For sequential prediction, we address two additional structural requirements: multi-modal futures should remain temporally coherent across a trajectory, and predictive beliefs should remain consistent when propagated to the same horizon through different temporal path compositions, as motivated by the Chapman--Kolmogorov equation. Together, these considerations define a three-level hierarchy of multimodal prediction, coherent multimodal trajectories, and compositionally consistent multimodal dynamics. Controlled experiments show that MDN-VJEPA closely recovers known branching predictive laws, that retaining the complete multimodal belief rather than its conditional mean can lead to materially different and substantially better planning decisions under branching futures, and that trajectory-level coupling and distributional consistency improve temporal coherence and multi-horizon agreement. These results support a simple principle: a probabilistic JEPA should preserve not only how uncertain the future is, but which distinct futures constitute that uncertainty, how they form coherent trajectories, and how those beliefs compose through time.


## 精读解读（中文）
### 一、研究动机
标准JEPA用点预测未来表征，在多未来分支下平方误差会收敛到条件均值，可能对应不可实现的未来；单高斯VJEPA只能表达单峰扩散，无法保留多个分离且各自可信的分支。机器人避障示例中左右绕行两个有效未来会被均值预测为穿过障碍的无效路径，因此需要显式保留不同未来假设及其概率。

### 二、技术方案（Method）
MDN-VJEPA在VJEPA概率预测框架下把潜在转移预测器实例化为神经混合密度网络，对给定Z_t和辅助ξ的未来状态Z_{t+h}建模为K分量高斯混合，输出混合权重π、分量均值μ和协方差Σ。为解决序列结构，它引入轨迹级共享离散模式M，使同一分量控制整个未来轨迹以保证多模态轨迹时间连贯；并基于Chapman-Kolmogorov思想对直接多步预测分布与递归组合一步转移得到的同视界分布施加分布路径一致性正则，采用基于样本的置换不变差异比较完整分布。整体还结合PIB压缩非预测历史、JEPA保留预测信息和MDN保留替代未来，推理/规划时保留完整混合信念而非仅用条件均值。

### 三、结果（Result）
受控实验表明MDN-VJEPA能紧密恢复已知的分支预测规律；在分支未来下，保留完整多模态信念而非条件均值会产生实质不同且显著更好的规划决策；轨迹级耦合与分布一致性还改善了预测轨迹的时间连贯性和多视界一致性。论文还指出，与Branch-JEPA式有限原子分支相比，连续高斯混合分量可额外表达分支内不确定性，但原子分支更利于保持尖锐分离支撑。

### 四、结论（Conclusion）
作者得出结论：概率化JEPA不仅应表示未来有多不确定，还必须保留哪些不同未来构成该不确定性、这些未来如何组成连贯轨迹以及这些信念如何随时间组合。因此，面向风险敏感规划的世界模型应保留完整的成分化多模态预测信念，而不应把分支未来压缩为均值或单一高斯。

### 五、方法论与关键技术细节
关键实现点包括：输入为潜在状态Z_t与可编码时间、动作序列、目标、物理约束的辅助变量ξ；预测器输出K个高斯分量，K=1退化为高斯VJEPA，固定各向同性协方差时高斯负对数似然与平方误差目标相关；训练目标结合PIB压缩、JEPA预测信息与MDN似然，并用stop-gradient的直接多步参考信念和基于样本的分布差异实现CK一致性。局限在于非线性MDN递归组合一般不闭合，直接与组合预测不必保持同类有限GMM，故只能分布比较；混合模型存在标签交换，分量语义和数量不由可识别性保证，实验主要为受控验证。
