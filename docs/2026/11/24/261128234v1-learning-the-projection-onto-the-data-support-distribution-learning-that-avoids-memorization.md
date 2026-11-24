# Learning the Projection onto the Data Support: Distribution Learning that Avoids Memorization

- 区域：精读区
- 排名：3
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Lin Chen, Dejan Slepčev
- 机构：Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28234v1) · [PDF](https://arxiv.org/pdf/2611.28234v1)

## TLDR
This paper introduces a variational framework that learns the nearest-point projection onto a data manifold, whose ideal optimizer recovers the underlying support rather than memorizing training samples, with theoretical guarantees and empirical validation as a non-memorizing generative approach.

## Abstract
We introduce a framework for learning distributions supported on manifolds based on estimating the nearest-point projection onto the data support. Specifically, we define an objective functional over a class of functions whose minimizer recovers this projection. The proposed framework automatically adapts to the intrinsic dimension and allows for data supported on unions of manifolds with varying dimensions. The resulting objective can be optimized using standard neural network architectures. We present population-level results establishing recovery of the manifold projection and prove finite-sample Wasserstein generalization bounds. Furthermore, we validate the approach empirically across a range of settings. In contrast to widely used generative models such as diffusion models, whose objectives can be minimized by memorizing training samples, our formulation excludes such behavior. We also introduce a direct memorization metric to verify that the learned projection generates new samples rather than reproducing the training set.


## 精读解读（中文）
### 一、研究动机
高维数据常近似位于低维流形或其并集上，但现有扩散模型等生成方法在有限样本下可能在目标函数上偏向记忆训练点，而不是恢复几何支撑。本文追问能否用灵活神经网络表示，同时设计一个理想优化器会恢复数据流形投影而非经验训练集的目标。作者因此提出直接学习到数据支撑的最近点投影，以避免把生成建模建立在记忆训练样本的机制上。

### 二、技术方案（Method）
在总体层面，对定义在流形管状邻域上的光滑映射T构造变分目标：E1强制流形上T(x)=x，E2强制T沿x到T(x)的线段保持不变以匹配法向纤维，E3把远离流形的点拉回，E4强制正交性；实际优化E=E1+E2+E3，理论分析用E'=E1+E2+E3+E4。证明E的极小值映射的像为流形，E'的极小值映射为正交投影Π_M。有限样本实现用标准神经网络参数化T，在流形样本及噪声扰动样本上估计目标并用常规梯度训练；生成时对训练样本或新采样点加噪声δ，再经学习到的T映射回学习支撑，并用投影误差与直接记忆度量评估。

### 三、结果（Result）
总体结果表明E的极小值映射的像恢复数据流形，E'的极小值映射恰为正交投影，并给出投影误差到分布恢复的Wasserstein界，形式为W2(μ,Π_{M#}(μ*η_δ))≲δ^2。有限样本结果证明每个极小值映射的像都是接近真实支撑的流形，且比样本分辨率更精细，而不是把训练集作为像；标准神经网络可优化该目标。实验覆盖合成流形、不同维数流形并集、样本复杂度缩放和MNIST；单位圆示例中40个训练点加1000个噪声样本学习投影可准确识别圆且记忆可忽略，而扩散模型减小终止时间会改善几何但增强训练点附近记忆。

### 四、结论（Conclusion）
学习数据支撑上的最近点投影提供了一种以几何支撑为理想解的分布学习框架，其目标在优化器层面排除了返回训练样本的记忆解，不依赖容量限制、切线估计或坐标图。该投影可直接作为生成器，也可作为扩散生成末端的几何校正组件。作者认为相比需要靠早停、数据增强或后处理控制记忆的扩散模型，这种让目标本身偏向流形恢复的设计更可取。

### 五、方法论与关键技术细节
理论假设数据支撑为具有正reach的紧致光滑嵌入流形，单流形分析要求0<δ<r_M/3且0<underline δ<δ/2，实践建议underline δ取训练样本最大最近邻距离；不相交且维数不同的流形并集在δ小于reach时可逐分量处理。E1、E2、E3已足以实践，E4主要用于排除斜投影并保证正交投影；E2是关键几何项，也使返回训练点的解不最优，且无需限制网络容量。分布误差通过先平滑再投影的测度Π_{M#}(μ*η_δ)分析，给出W2≲δ^2的显式界；有限样本恢复定理来自配套工作，依赖光滑性与reach等假设，噪声带宽δ和underline δ的选择及E4的实践必要性是主要限制与待注意点。
