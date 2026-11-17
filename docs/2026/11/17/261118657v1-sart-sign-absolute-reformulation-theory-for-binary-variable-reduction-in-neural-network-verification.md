# SART: Sign-Absolute Reformulation Theory for Binary Variable Reduction in Neural Network Verification

- 区域：精读区
- 排名：7
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Jin Xu, Miaomiao Zhang, Bowen Du
- 机构：Tongji University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18657v1) · [PDF](https://arxiv.org/pdf/2611.18657v1)

## TLDR
SART is a sign-absolute reformulation for neural network verification that breaks the one-binary-variable-per-unstable-ReLU mapping, proves a 50% final-layer variable reduction under \(P \neq NP\), and lifts this gain network-wide via the LayerABS progressive-tightening verifier to reduce search complexity and outperform state-of-the-art baselines.

## Abstract
Complete formal verification of neural networks is crucial for their deployment in safety-critical domains. A key bottleneck stems from encoding complexity: traditional methods assign one binary variable per unstable ReLU neuron. We propose the Sign-Absolute Reformulation Theory (SART), which fundamentally breaks the conventional one-to-one mapping between unstable neurons and binary variables by establishing formal reducibility criteria. This allows for finer-grained modeling, where each unstable neuron corresponds on average to fewer than one binary variable, thereby reducing verification complexity at its source. Based on SART, we derive a theoretical lower bound on the number of binary variables required for complete verification and, under the assumption that $P \neq NP$, prove that variables in the final layer can be compressed by 50\%, while the number of variables in intermediate layers cannot be further reduced. To overcome the apparent ``last-layer-only'' limitation, we recast verification as a sequential process and, crucially, show that the gain lifts to the entire network: LayerABS, a SART-based progressive tightening verifier, iteratively treats intermediate layers as temporary final layers and propagates tight bounds that shrink the global search space and binary-variable counts. Furthermore, we reveal a structural law influencing verification complexity: when the signs of weights of unstable neurons satisfy numerical symmetry, with positive and negative weights equal or differing by at most one, the worst-case verification complexity achieves the theoretical optimum, offering theoretical guidance for the design of verification-friendly architectures. As a general-purpose underlying encoding, the value of SART is independent of specific algorithms.


## 精读解读（中文）
### 一、研究动机
完整形式化验证是ReLU神经网络进入安全关键场景的关键保障，但其核心瓶颈在编码复杂度：传统SMT、MILP和BaB方法通常为每个不稳定ReLU神经元引入一个二值变量，导致组合爆炸。论文旨在从编码源头打破“不稳定神经元—二值变量”的一一刚性映射，降低完整验证的搜索空间与求解复杂度。

### 二、技术方案（Method）
输入为前馈ReLU网络及l∞扰动下的鲁棒性验证问题，目标是最小化正确类与竞争类的输出margin并编码为MILP。SART对每层权重做正负分解与0/1掩码、拆分偏置，将ReLU激活等价改写为绝对值形式，依据绝对值项系数的符号及其位于目标函数还是约束中的线性化准则建立可归约判据，仅对不可消去的绝对项引入二值变量；由此实现无抽象的PureSART编码。进一步将验证重铸为顺序过程，提出LayerABS：逐层把中间层临时视为“最终层”，迭代应用SART并传播更紧的边界，构造完整验证器LayerABS及不完整变体Incomplete-LayerABS。

### 三、结果（Result）
理论上，SART在区间完备边界计算下达到二值变量数的理论下界：最终层不稳定神经元对应的二值变量可压缩50%，而中间层在保持完备性下不能进一步压缩；整体上每个不稳定神经元平均对应少于一个二值变量。LayerABS通过渐进收紧把末层压缩收益扩展到全网，显著缩小全局搜索空间和二值变量数；实验显示PureSART相较标准MILP提高成功率并将验证时间最多降低34.4%，LayerABS等SART实例在多个基准上优于相关SOTA方法。

### 四、结论（Conclusion）
SART首次从理论上表明不稳定ReLU神经元与二值变量并非必须一一对应，并给出完整验证所需二值变量的下界及末层50%压缩结论；其作为通用底层编码不依赖特定验证算法。LayerABS说明静态看仅末层受益的局限可通过顺序验证转化为全网收益；权重符号数值对称时最坏情况复杂度可达理论最优，为验证友好架构设计提供指导。

### 五、方法论与关键技术细节
关键实现包括：不稳定神经元由预计算区间l_i、u_i是否跨零判定，稳定激活或稳定抑制神经元无需二值变量；Big-M取M=max(|l_i|,|u_i|)；绝对值线性化是否引入二值变量取决于系数符号及绝对项出现在目标还是约束中；理论结论依赖区间完备边界计算及P≠NP假设。局限在于中间层在完备性下不可再压缩，LayerABS的实际收益受边界收紧与抽象质量影响，且符号对称性是最坏情况复杂度最优的结构条件。
