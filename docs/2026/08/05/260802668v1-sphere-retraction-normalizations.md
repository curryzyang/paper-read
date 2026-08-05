# Sphere Retraction Normalizations

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Jie Zhang, Cheng-Fang Su, Yi-Jui Huang, Min-Te Sun
- 机构：National Central University, National Yang Ming Chiao Tung University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02668v1) · [PDF](https://arxiv.org/pdf/2608.02668v1)

## TLDR
The paper unifies residual connections and GeoNorm via retraction maps on a hypersphere, introducing a one-parameter family of norm-preserving sphere retraction normalizations (Proj-, Cay-, and p-SpheretNorm) that show the exponential map is just one end of a spectrum, and demonstrate on nanoGPT that finite-parameter variants outperform existing deep connection schemes.

## Abstract
Residual connections are the de facto mechanism for training deep neural networks stably. Geodesic Normalization (GeoNorm) recasts them on a Riemannian manifold, orthogonalizing each layer output against the current hidden state and applying the resulting update through the Riemannian exponential map. Every hidden state thus keeps a constant $\ell_{2}$-norm, confining the residual stream to a hypersphere. The exponential map, however, is only one member of a broad family of retraction maps. We show that on the hypersphere this entire family collapses to a single scalar design choice. What distinguishes one retraction from another is only how the magnitude of an update is converted into a rotation angle within the plane spanned by the hidden state and the update. This view places Euclidean residual connections and GeoNorm in one framework. Instantiating it with the metric projection retraction and the Cayley retraction yields Proj-SpheretNorm and Cay-SpheretNorm, which are exactly norm-preserving yet require only algebraic operations. Both prove to be members of a one-parameter family of angular retractions, $p$-SpheretNorm, whose rotation angle saturates rather than growing without bound. The two methods above are recovered exactly at $p = 1$ and $p = 2$, while the identity map and GeoNorm arise only as limits at either end. On nanoGPT, all three methods outperform existing lightweight deep connection schemes, and the best validation loss is attained at finite $p$, indicating that the exponential map is not the preferred retraction for spherical residual streams but merely one end of a spectrum.


## 精读解读（中文）
### 一、研究动机
残差连接是稳定训练深度网络的标准机制，但传统欧氏残差流在深层Transformer中会引发深度诅咒、激活无界增长与注意力沉降等问题。GeoNorm将残差连接放到黎曼流形上，通过指数映射保持隐状态L2范数恒定，然而指数映射只是流形上retraction映射族中的一个特例。本文旨在回答超球面上深度连接应使用哪种retraction，并构造更优的球面归一化方法。

### 二、技术方案（Method）
将残差连接与GeoNorm统一为超球面上的retraction更新框架：对第l层，先用Gram-Schmidt过程将层输出F_l(h_l)正交投影到h_l的切空间得到z_l，再在h_l与z_l张成的平面内用retraction映射将更新幅值转换为旋转角。据此实例化两种仅需代数运算且严格保范的retraction：Proj-SpheretNorm（metric projection）与Cay-SpheretNorm（Cayley映射）。进一步提出单参数族p-SpheretNorm，其旋转角随更新幅值饱和而非无界增长；p=1、p=2分别精确恢复前两者，p→0+退化为恒等映射，p→∞且alpha_l∈(0,1]时恢复GeoNorm。训练时alpha_l作为可学习步长，p可作为超参调节，隐状态保持恒定L2范数。

### 三、结果（Result）
在nanoGPT（最高36层、6.55B tokens）的预训练与下游任务上，三种SpheretNorm均优于Pre-LN、Pre-DyT、Peri-LN、Keel和GeoNorm等轻量深度连接方案；其中Proj-SpheretNorm在medium和large模型上取得最低预训练/验证损失，并在OpenWebText与FineWeb-Edu上取得最高平均零样本准确率。最优验证损失出现在有限p处，表明指数映射并非球面残差流的最优选择，而只是谱系的一端。

### 四、结论（Conclusion）
超球面上的所有retraction本质上仅体现为将更新幅值转换为旋转角的标量设计选择；p-SpheretNorm将欧氏残差连接与GeoNorm纳入同一框架，并证明指数映射只是其中的极限情形而非最优选择。有限p、特别是p=1对应的Proj-SpheretNorm，以纯代数操作实现严格保范，既提升训练稳定性又改善深层模型性能，是更优的球面深度连接方案。

### 五、方法论与关键技术细节
关键实现细节包括：Gram-Schmidt正交化移除平行于当前隐状态的成分；所有retraction均在h_l与z_l张成的二维平面内旋转，旋转角是更新范数与隐状态范数之比的可学习缩放；Proj-SpheretNorm和Cay-SpheretNorm无需指数或三角函数以外的超越运算，具有精确保范性和低计算开销；p-SpheretNorm以p=1/2连接两种实例，p→∞时角度饱和于GeoNorm的有界旋转，避免残差流无界增长并缓解注意力沉降。实验设置覆盖24/36层nanoGPT，并与多种欧氏方案对比；局限在于主要验证于GPT式架构，对更广泛架构与理论收敛保证尚未充分展开。
