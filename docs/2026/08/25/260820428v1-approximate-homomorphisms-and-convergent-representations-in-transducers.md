# Approximate Homomorphisms and Convergent Representations in Transducers

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Santiago Cifuentes
- 机构：Universidad de Buenos Aires, Dovetail Research Group
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20428v1) · [PDF](https://arxiv.org/pdf/2608.20428v1)

## TLDR
The paper introduces approximate homomorphisms and metrics for transducers to show that minimal representations of linear and predictive transducers are stable under small perturbations—supporting the Platonic Representation Hypothesis—while standard transducers lack such approximate structural convergence.

## Abstract
We study the stability of minimal representations of controlled stochastic processes (in particular, transducers) under perturbations. This question is motivated by recent experiments finding predictive-state structure in the latent representations of neural networks. We consider standard, linear and predictive transducers. We introduce notions of approximate homomorphism capturing local structural similarity between them, together with metrics comparing their induced dynamics (which we refer to as interfaces), and prove properties such as composability of the approximate homomorphisms. For standard transducers, we show that there exist simple interfaces for which there is no approximate homomorphism between the different implementations of the dynamics. In contrast, for every finite-rank interface $\mathcal I$, we prove that all minimal linear transducers implementing interfaces sufficiently close to $\mathcal I$ have an approximate homomorphism to the minimal implementation of $\mathcal I$, with error linear in the perturbation size. We prove an analogous stability result for predictive transducers under a residual metric using some mild hypothesis regarding the indistinguishability of the belief states. These results identify conditions under which canonical transducer representations are robust to perturbations, while showing that such convergence fails without additional structural restrictions. Under the assumption that these type of abstractions are embedded into the hidden layers of modern AI models, this gives some theoretical support to the hypothesis that their latent representations exhibit structural convergence.


## 精读解读（中文）
### 一、研究动机
神经网络的潜在表示常被观察到具有预测性状态结构，但训练过程的随机性使不同模型学到的表示并不完全一致。本文希望在受控随机过程（换能器）的框架下研究最小表示在扰动下的稳定性，从而为潜在表示的结构收敛现象（如柏拉图表示假说）提供理论支撑。

### 二、技术方案（Method）
以换能器作为世界模型的数学抽象：换能器由状态集、输入集、输出集、马尔可夫核和初始分布定义，其诱导的interface是给定动作序列条件下输出序列的条件概率族。作者考虑标准换能器、线性换能器和预测换能器三类模型；引入了近似同态，即由状态映射、输入映射和输出映射组成，要求局部转移核与初始分布的推前等式在ε误差内成立，并引入折扣度量来比较两个interface对长程预测的差异。关键操作包括：证明近似同态可复合且误差以O(ε)传播；对线性换能器，利用interface的Hankel矩阵有限秩分解构造最小线性实现，并证明邻近interface的最小实现到参考最小实现存在误差线性于扰动量的近似同态；对预测换能器，则基于belief state和ε-machine构造最小预测实现，在残差度量下证明类似稳定性。全文为理论证明，不涉及训练过程。

### 三、结果（Result）
对标准换能器，构造了简单interface，说明其不同实现之间不存在近似同态，因此不能仅靠引入误差项来恢复最小表示的存在性。对有限秩interface I，所有充分接近I的interface所对应的最小线性换能器，都能与I的最小线性实现之间建立近似同态，误差为Γ_I ε，其中ε是interface扰动大小，Γ_I是仅依赖于I的常数。对预测换能器，在belief state不可区分的温和假设下得到类似稳定性结论。此外还证明了近似同态的可复合性及其在折扣度量下对interface误差的连续性。

### 四、结论（Conclusion）
这些结果表明，在线性与预测换能器这类具有额外结构限制的表示中，规范最小表示对扰动是鲁棒的；而无结构限制的标准换能器不具备这种收敛性。若现代AI模型的隐藏层嵌入了这类抽象世界模型，该结果从理论上支持其潜在表示会出现结构收敛现象。

### 五、方法论与关键技术细节
关键要点包括：interface需要满足无预期性，即输出分布只依赖当前及过去的动作序列；近似同态的误差在折扣度量下以O(ε)传播，保证组合后的行为误差可控；线性换能器的核心工具是Hankel矩阵，有限秩条件给出唯一（相差可逆线性坐标变换）的最小实现，误差常数Γ_I来自该实现的数值性质；预测换能器的最小实现依赖belief state等价类，温和假设涉及不同belief state的不可区分性；标准换能器的负面结果说明若不加线性或预测性等结构限制，相近行为并不保证相近内部结构。本文为纯理论结果，不涉及训练数据、损失函数或超参数；主要局限是只给出存在性与误差界，且线性换能器在真实神经网络中尚无直接实验证据，作者建议未来在残差流中检测最小线性换能器。
