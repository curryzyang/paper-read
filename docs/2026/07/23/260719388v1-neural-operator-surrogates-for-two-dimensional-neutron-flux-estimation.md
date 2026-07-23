# Neural Operator Surrogates for Two-Dimensional Neutron Flux Estimation

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Japan K. Patel, Barry D. Ganapol, Anthony Magliari, Matthew C. Schmidt, Todd A. Wareing
- 机构：Siemens Healthineers, Washington University in St. Louis, Gateway Scripts LLC, University of Arizona
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19388v1) · [PDF](https://arxiv.org/pdf/2607.19388v1)

## TLDR
This paper extends neural operator surrogates (FNO and UNO) to two-dimensional neutron flux estimation, finding that single-sweep conditioning improves accuracy and logarithmic training enhances prediction in strongly attenuated regions.

## Abstract
This work extends our one-dimensional single-sweep neural-operator studies to two dimensions. We consider one-group transport with isotropic scattering. As in the one-dimensional work, we use Fourier neural operators (FNOs) to approximate the high-fidelity scalar flux. Additionally, we also investigate U-shaped neural operators (UNOs) in this study. We consider three surrogates. The first two map the material and source fields directly to the flux, one using an FNO and one using a UNO. The third is an FNO that additionally takes the scalar flux after one source iteration, the single-sweep approximation, as an input. Each case is solved to high fidelity with a verified discrete-ordinates solver, and an average relative L_2 error norm is used to characterize the quality of the inferred maps. We train every surrogate over three random seeds so that differences between them can be assessed against run-to-run variability. Two questions guide the study: whether the single-sweep input improves accuracy over the direct maps, and whether training on the logarithm of the flux improves accuracy in the strongly attenuated regions relevant to shielding.


## 精读解读（中文）
### 一、研究动机
重复的输运求解在辐射屏蔽和反应堆分析中非常耗时，尤其是在散射主导时迭代次数激增。神经算子可提供快速推理，但此前研究多基于理想化一维设置。本研究将一维单扫神经算子扩展到二维，探究单扫输入和对数训练能否提升二维固定源中子通量估计的精度。

### 二、技术方案（Method）
在10×10矩形域上，采用S12水平对称求积和菱形差分离散一阶稳态单群中子输运方程，生成高保真标量通量参考解。输入为网格函数，包含总截面Σt、散射比c及其梯度，以及归一化源及其梯度。构建三种代理模型：直接FNO、直接UNO、以及以单扫通量（一次源迭代后的非散射通量）为额外输入的FNO（SS-FNO）。所有模型以物理通量的相对L2损失在1024（均匀）和2048（异质）例数据集上训练（80%训练，20%测试），并对每种配置训练三个随机种子以评估变异性。还训练了预测log10通量的对数变体，并映射回物理通量计算损失和指标。

### 三、结果（Result）
SS-FNO在均匀集上通量相对L2误差为4.47±0.18×10^{-3}，在异质集上为6.23±0.14×10^{-3}，优于直接FNO（4.94±0.30和7.22±0.04）和直接UNO（6.27±0.36和8.50±0.17）。对数训练使对数通量相对L2误差降低约2.7倍（从0.13–0.17降至0.047–0.054），而通量误差几乎不变。代理推理约1ms/例，参考求解需1.4–22s/例（随散射比增加）。

### 四、结论（Conclusion）
单扫条件化是最精确的构型，在所有两套问题集上均优于直接映射；对数训练在不牺牲源区精度的前提下显著改善了强衰减区（屏蔽相关）的预测精度；异质性仅带来适度代价（误差增加约1.4倍）。代理推理时间恒定，而参考求解随散射比增长，表明神经算子在多查询屏蔽分析中具有实用潜力。

### 五、方法论与关键技术细节
数据分为均匀（1024例，常数Σt∈[0.5,2.0]、c∈[0.3,0.95]）和异质（2048例，背景+吸收块+圆盘）两类，源由1-2个高斯凸起组成。输入引入材料梯度√|∇Σt|²+|∇c|²作为空间结构先验。损失为物理通量的相对L2；对数变体训练后映射回物理通量，使低通量区域误差权重一致。超参：三个随机种子，架构基于PyTorch和NeuralOperator库。推理复杂度为常数，参考求解复杂度随散射比增加（源迭代数从22增至342）。局限性：代理受限于训练分布，未考虑各向异性散射、多能或三维；未与加速求解器对比速度。
