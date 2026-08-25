# Amortized Bandwidth Learning for Kernel Density Estimation under Logarithmic Score

- 区域：精读区
- 排名：7
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Junyi Liang, Hailiang Du
- 机构：The London School of Economics and Political Science, East China University of Science and Technology, Durham University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20445v1) · [PDF](https://arxiv.org/pdf/2608.20445v1)

## TLDR
This paper proposes an amortized bandwidth selector for kernel density estimation that learns a reusable sample-to-bandwidth mapping across tasks under the logarithmic score, consistently outperforming classical selectors, especially for small and heterogeneous samples.

## Abstract
Kernel density estimation converts finite samples into probability densities, but its performance depends critically on bandwidth selection. Classical selectors prescribe the sample-to-bandwidth rule analytically or asymptotically, or solve a new optimization for each sample. An amortized framework is proposed that instead learns this mapping across a distribution of density-estimation tasks by optimizing the logarithmic score. A truncated-and-renormalized bounded-support formulation enables stable learning across heterogeneous tasks, while affine standardization allows a selector trained on a single reference interval to transfer across bounded intervals. Experiments under Gaussian sampling, a multi-family benchmark, and randomized Gaussian-mixture training show that the amortized selector consistently and substantially outperforms Silverman's rule, the Sheather--Jones selector, and least-squares cross-validation, with especially large gains in small and heterogeneous samples. Finite Gaussian mixtures provide a generic training mechanism supported by their $L^1$ approximation property. Selectors trained in this way generalize strongly across different density structures, allowing the same trained selector to be applied directly to finite samples from unknown densities without specifying or fitting a distributional family. This combination of broad applicability and strong empirical performance makes the framework attractive for a wide range of applications in which finite samples or ensembles must be converted into continuous probability densities.


## 精读解读（中文）
### 一、研究动机
核密度估计的性能高度依赖带宽选择，而经典选择器要么通过解析或渐近方式预设样本到带宽的规则，要么对每个样本单独求解优化问题，无法从一组相关密度估计任务中直接学习样本特征与最优带宽之间的映射。由于对数评分是连续密度上唯一具有局部性的严格恰当评分规则，本文提出一种摊销学习框架，在任务分布上优化对数评分来学习可复用的带宽选择映射。

### 二、技术方案（Method）
该框架将带宽选择建模为样本到带宽的摊销映射：从每个样本提取置换不变的低维特征（样本量、均值、标准差、偏度、峰度），输入多层感知机（MLP），经softplus输出正带宽。训练目标为跨任务分布的对数评分期望，用有限任务样本近似。为稳定学习并支持跨区间迁移，引入截断重归一化的有界支撑公式，将目标密度和KDE限制在共同区间上；通过仿射标准化将任意有界区间映射到参考区间[-1,1]，带宽按区间半宽缩放，并由命题保证对数评分等价性。训练任务可由有限高斯混合随机生成，利用其L1逼近性质提供通用任务来源。

### 三、结果（Result）
在标准正态采样诊断、多密度族基准和随机高斯混合训练三种实验中，摊销带宽选择器一致且显著优于Silverman规则、Sheather-Jones选择器和最小二乘交叉验证，尤其在小样本和异质样本上增益最大。实验表明，该选择器能跨不同密度结构强泛化，训练后可直接用于未知密度的有限样本。

### 四、结论（Conclusion）
将带宽选择视为从样本特征到带宽的可学习映射，并在对数评分下跨任务摊销训练，能够替代经典解析或逐样本优化选择器。该方法兼具广泛适用性和强经验性能，适用于需要将有限样本或集合转换为连续概率密度的各类场景。

### 五、方法论与关键技术细节
关键细节包括：特征仅用五个低维统计量，MLP结构简单且用softplus保证正带宽；有界支撑公式避免远端低密度区稀有样本过度影响对数评分目标，截断区间可由物理边界或数据驱动方式指定；区间标准化通过仿射变换使单个参考区间训练的选择器可迁移至任意有界区间，带宽按a=h_[-1,1]*a缩放；训练任务分布采用随机高斯混合，利用其L1逼近性质生成多样化密度；对数评分以2为底，评分差以比特解释。局限在于当前为实现简单未优化网络架构，且有界支撑需预先确定工作区间；方法虽以高斯核展示，但核心思想可扩展至其他核族。
