# Beyond Coordinate Gauge: An Audited Protocol for Detecting Donor-Specific Functional Fingerprints after Neural Collapse

- 区域：精读区
- 排名：10
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Truong Xuan Khanh, Phan Thanh Duc
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11967v1) · [PDF](https://arxiv.org/pdf/2607.11967v1)

## TLDR
By combining an affine-correct alignment protocol with a leakage audit and permutation testing, this paper demonstrates that donor-specific functional fingerprints remain detectable in neural networks after Neural Collapse, though not transplantable or causally persistent.

## Abstract
Independently trained neural networks have no shared neuron-index reference frame, so comparing them requires accounting for coordinate freedom. Neural Collapse sharpens this problem: networks converge toward a shared, low-dimensional geometry, raising the question of whether trajectory-specific functional variation remains distinguishable after convergence. We distinguish three claims - detectability, transplantability, and causal persistence - and address the first. Using five independently trained networks reconstructing Neural Collapse on MNIST, we apply a verified affine-correct alignment mapping donor heads into recipient coordinates. Donor-specific functional fingerprints remain distinguishable after recipient-level baseline correction: all 20 ordered donor-recipient pairs are correctly identified, with an exact permutation p=0.0083, robust to a leakage audit. These findings establish detectability under the test used here, but not transplantability or causal persistence. The study shows how alignment, ambiguity diagnostics, and leakage control combine to test cross-network variation in a controlled setting; whether this generalizes beyond it is open.


## 精读解读（中文）
### 一、研究动机
独立训练的神经网络没有共享的神经元索引参考系，直接比较需要消除坐标自由度。神经坍缩使问题更尖锐：网络收敛到共享低维几何，但轨迹特定的功能变异是否仍可区分？本文区分可检测性、可移植性和因果持久性三个主张，并针对第一个展开研究。

### 二、技术方案（Method）
在MNIST上训练5个独立初始化的MLP-5网络，采用两阶段协议（200轮交叉熵预训练+400轮MSE诱导神经坍缩），保存阶段一结束和NC1<0.01时刻的检查点。使用正交Procrustes拟合将供体分类器头映射到受体坐标系，并通过仿射校正精确保留供体逻辑。校准集从训练集中取1000个类平衡样本，与评估集不重叠。构建指纹：在受体激活上计算供体头的类中心平均逻辑向量矩阵（K×K），归一化后以余弦距离度量。进行受体级基线校正（基于模板分裂的跨供体均值），通过精确置换检验（5! =120）评估识别准确性。

### 三、结果（Result）
所有5个种子均重现神经坍缩，NC1阈值窗口为335-360轮。验证了仿射校正对供体逻辑的浮点精度恢复（相对误差1.3e-15）。在校准支持子空间上，完成采样器合成验证正确。在受体内基线校正后，所有20个有序供体-受体对正确识别，精确置换p=0.0083（五供体设计的分辨率下限）。识别裕度在泄漏修正后基本不变。

### 四、结论（Conclusion）
在测试的受控条件下，供体特异性功能指纹在坐标规约消除和受体级基线校正后仍然是可检测的。但该结果仅建立可检测性，不意味着可移植性或因果持久性；后两者需要不同的干预实验。该协议是否推广到其他架构、任务或跨模型应用仍有待验证。

### 五、方法论与关键技术细节
数据：MNIST，5个MLP-5网络，512维隐藏层，10类。校准集大小测试了100-5000，主实验用1000。损失：阶段一交叉熵，阶段二MSE（one-hot目标）。优化器：Adam (lr=1e-3, weight decay=1e-4)，余弦退火600轮。关键模块：正交Procrustes对齐+仿射校正；零空间诊断（完成采样器验证P_B不变性）；秩分析（有效秩、累积能量秩）。泄漏修正：原始基线使用了探测分裂自身数据，修正为仅基于模板分裂的基线，使基线对探测内容不变。局限性：五种子设计统计分辨率有限（p最小值0.0083）；仅针对特定架构（MLP-5）和任务（MNIST）测试；非精确复制（批次大小、调度边界未达原论文实现）。
