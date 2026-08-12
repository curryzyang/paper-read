# Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Ashim Dhor, Pin-Yu Chen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10172v1) · [PDF](https://arxiv.org/pdf/2608.10172v1)

## TLDR
This paper proves that the Koopman spectrum of a transformer's forward pass is a coordinate-free, model-intrinsic fingerprint recoverable from finite samples at a minimax-optimal rate, demonstrating that identifiable structures in mechanistic interpretability are distinct from legible decompositions like sparse autoencoder features.

## Abstract
Mechanistic interpretability explains models by identifying circuits inside them, but has no way to tell whether a circuit is a property of the model or an artifact of the method that found it. Sparse autoencoders illustrate the problem: different seeds and widths recover materially different features from the same activations, and no theory says whether that variability is incidental or structural. We put dictionary learning for interpretability on an identifiability footing. Treating the forward pass as a controlled dynamical system with depth as time and lifting it with the Koopman operator yields a finite linear realisation whose \emph{spectrum} is a coordinate-free property of the model. We prove the spectrum is recoverable from $M$ calibration samples at rate $M^{-1/2}$ up to permutation - to our knowledge the first identifiability theorem for a mechanistic-interpretability primitive, with a matching minimax lower bound, a median-of-means variant for heavy-tailed activations, and a dissociation theorem: whenever the realisation is non-normal, the directions carrying activation variance and the directions carrying information across depth cannot coincide. The identifiable object and the legible object are not the same object. On GPT-2 small, Gemma-2-2B and Qwen3-8B-Base the spectrum converges everywhere and attains the predicted exponent on Qwen3-8B-Base ($0.506 \pm 0.031$); shortfalls collapse onto one curve against each cell's sample threshold. Koopman modes beat random directions but lose to principal components on indirect-object identification, with the gap decaying $4.1\times$ in depth-distance, as the theorem predicts. The Koopman spectrum is an identifiable, model-intrinsic fingerprint with a stated error bar, not a legible decomposition.


## 精读解读（中文）
### 一、研究动机
机械可解释性依赖在模型内部识别电路来解释模型行为，但现有方法无法判断所得电路是模型的固有属性还是方法带来的伪影。稀疏自编码器即为例证：不同随机种子和宽度从相同激活中恢复出实质性不同的特征，而缺乏理论说明这种变异性是偶然的还是结构性的。因此需要为可解释性中的字典学习建立可辨识性基础，区分模型的内在结构与方法伪影。

### 二、技术方案（Method）
将模型前向传播视为以深度为时间索引的受控动力系统，并利用Koopman算子将其提升为有限维线性实现，从而得到坐标无关的谱对象。该谱从M个校准样本中以M^{-1/2}的速率、在置换意义下被恢复，同时构造了重尾激活下的中位数均值（median-of-means）变体以增强鲁棒性。关键步骤包括：定义受控动力系统与可观测函数，构造Koopman算子并获取有限线性实现，利用谱分解得到模型指纹；进一步推导分离定理，指出当实现非正规时，承载激活方差的方向与跨深度信息的方向不能重合。

### 三、结果（Result）
在GPT-2 small、Gemma-2-2B和Qwen3-8B-Base上，谱处处收敛；在Qwen3-8B-Base上观测到的收敛指数为0.506±0.031，与理论预测的M^{-1/2}速率一致。所有短残差在按每个单元的样本阈值归一化后塌缩为单一曲线。在间接宾语识别（IOI）任务中，Koopman模式优于随机方向但弱于主成分，且与PCA的差距随深度距离按4.1倍因子衰减，符合定理预测。Koopman谱在稳定性上优于SAE与随机投影，作为模型指纹具有可复现性和明确误差界。

### 四、结论（Conclusion）
Koopman谱是一种可辨识的、模型内在的指纹，带有明确的误差条，而不是一个可直接阅读的分解。该工作首次为机械可解释性原语提供了可辨识性定理，证明可辨识对象与可读对象不是同一对象，对理解模型内部结构的本源性和方法伪影的区分具有根本性意义。

### 五、方法论与关键技术细节
谱的恢复速率M^{-1/2}对应minimax最优，具有置换不变性；理论包含匹配的极小极大下界与重尾激活的中位数均值估计变体。分离定理依赖于线性实现的非正规性条件，这解释了激活方差方向与跨深度信息方向的分歧。实验覆盖三个规模迥异的模型，Koopman谱在非正规性方面远优于随机方向（如GPT-2的κV=78.7 vs 28.8），并显著降低对梯度的敏感性；但谱不是可读分解，其可辨识性与可解释性之间存在张力，是当前方法的局限性。
