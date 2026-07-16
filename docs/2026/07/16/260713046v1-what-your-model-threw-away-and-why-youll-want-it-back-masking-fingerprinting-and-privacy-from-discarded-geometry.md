# What Your Model Threw Away and Why You'll Want It Back: Masking, Fingerprinting, and Privacy from Discarded Geometry

- 区域：精读区
- 排名：6
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Zachary P. Bradshaw
- 机构：QodeX Quantum, Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13046v1) · [PDF](https://arxiv.org/pdf/2607.13046v1)

## TLDR
This paper introduces a framework for quantifying the symmetry information discarded by machine learning models with Lie group actions, defining null fibers and stabilizers, and demonstrates its applications to data masking, model fingerprinting, and privacy-preserving computation.

## Abstract
We develop a framework for the information discarded by machine learning models whose inputs carry a Lie group action. Given a representation $π$ of a Lie group $G$ on a space $V$ and a learned function $f\colon V \to \mathbb{R}$, we define two objects measuring the symmetry invisible to $f$. The null fiber at a point $x \in V$ is the set $N_G(f,x) = \{g \in G : f(π(g^{-1}) \cdot x) = f(x)\}$ of group elements whose inverse action on $x$ is undetectable by $f$. When $N_G(f,x)$ is independent of $x$, it coincides with the stabilizer $\mathrm{Stab}_G(f)$, the largest subgroup of $G$ under which $f$ is invariant. For smooth maps to $\mathbb{R}$, the preimage theorem guarantees that null fibers have dimension at least $\dim G - 1$ at generic inputs, regardless of architecture. For compact groups acting on themselves, the Peter--Weyl theorem yields a spectral characterization of both objects in terms of the Fourier coefficient matrices of $f$. We show that null fiber elements can be computed efficiently via Newton iteration on the orbit map, at a cost comparable to a few gradient evaluations. Applications to data masking, model fingerprinting, and privacy-preserving computation are developed and tested experimentally on molecular property prediction under $\mathrm{SO}(3)$ and spherical image classification under the Möbius group $\mathrm{PSL}(2, \mathbb{C})$. The framework applies uniformly to classical neural networks and variational quantum circuits.


## 精读解读（中文）
### 一、研究动机
机器学习模型在处理带有李群作用的数据时丢弃了输入中的几何信息。为推广空空间理论到表示论设置，论文区分了全局不变性（稳定子）和逐点不变性（零纤维），并揭示了在非交换群上两者通常不同。这一框架可用于数据掩蔽、模型指纹识别和隐私保护等实际场景，无需稳定子非平凡。

### 二、技术方案（Method）
定义李群G表示π下的零纤维N_G(f,x)和稳定子Stab_G(f)。利用Peter-Weyl定理给出紧群上函数的傅里叶表征：稳定子条件为f̂(λ)ρ_λ^†(g)=f̂(λ)对所有λ成立，零纤维条件为f(g^{-1}h_0)=f(h_0)的标量方程。提出基于牛顿迭代的轨道图算法，以O(1)次模型评估精确计算零纤维元素。实验在SO(3)分子性质预测和PSL(2,C)球面图像分类上验证，框架统一适用于经典神经网络和变分量子电路。

### 三、结果（Result）
对光滑实值函数，预像定理保证通用输入处零纤维维度至少为dim G - 1，与架构无关。傅里叶表征显示稳定子是零纤维的交集，且当傅里叶系数满秩时稳定子仅为平凡群。实验中，零纤维掩蔽使球面图像视觉不可识别，但分类器预测保持不变；分子性质预测下也能有效掩盖输入。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
零纤维定义依赖于李群作用和光滑性；稳定子是闭子群但不必正规。理论推导基于紧群上的Peter-Weyl定理，要求输入空间承载群表示。牛顿迭代算法在轨道图上执行，每次迭代需梯度计算，收敛至精确零纤维元素。复杂度与模型评估次数相当，但需注意光滑性假设和紧群条件；非紧群情况需额外处理。局限性包括对非光滑模型或离散群不直接适用，且实验未报告量化指标（如保真度）。
