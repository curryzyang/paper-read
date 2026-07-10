# LiST: Lipschitz Scaling Training for Robust and Calibrated Neural Networks

- 区域：精读区
- 排名：3
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Arthur Chiron, Franck Mamalet, Thomas Massena, Thomas Deltort, Mathieu Serrurier
- 机构：IRIT, IRT Saint Exupéry, Airbus, SNCF
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07745v1) · [PDF](https://arxiv.org/pdf/2607.07745v1)

## TLDR
The paper introduces LiST, a training paradigm that dynamically adjusts the Lipschitz constant to produce neural networks that are simultaneously robust and well-calibrated by leveraging the duality between Lipschitz constraints and temperature scaling.

## Abstract
While accuracy, robustness, and calibration are all essential for reliable neural networks, they are often studied separately; developing models that satisfy all three simultaneously remains a central challenge. Lipschitz-constrained models guarantee robustness by design, yet the manual selection of the Lipschitz constraint L governs the resulting accuracy-robustness trade-off, and their calibration properties remain largely underexplored. In this work, we highlight a theoretical and empirical link between the enforced Lipschitz constraint and Temperature Scaling, a state-of-the-art calibration method. Specifically, we find that for a given training scheme, there exists a non-trivial value L* that yields an out-of-the-box calibrated network, and that calibration acts as a principled criterion to select a well-defined operating point on the accuracy-robustness Pareto front. Leveraging these insights, we introduce Lipschitz Scaling Training (LiST), a novel training paradigm that iteratively adjusts the global Lipschitz constant to reach this operating point. Through a margin parameter in the training loss, LiST further enables the construction of a fully calibrated Pareto front, allowing users to navigate the accuracy-robustness trade-off while remaining calibrated throughout. At convergence, LiST also enables the reintegration of calibration data into training, improving sample efficiency without sacrificing calibration. We validate LiST on CIFAR-10/100 and Tiny-ImageNet, demonstrating competitive accuracy and robustness against constrained and unconstrained baselines, while remaining calibrated out of the box. Code is available at GitHub.


## 精读解读（中文）
### 一、研究动机
准确率、鲁棒性和校准是可靠神经网络的三大核心属性，但现有研究通常独立处理它们，难以同时满足三者。Lipschitz约束网络通过设计保证鲁棒性，但手动选择Lipschitz常数L会导致准确率-鲁棒性权衡，且其校准性质未被充分探索，缺乏自动确定最优L的原则性标准。

### 二、技术方案（Method）
LiST利用温度缩放（TS）与Lipschitz常数之间的结构对偶性，通过在校准集上计算温度缩放因子T*作为反馈信号，在训练每个epoch动态调整全局Lipschitz常数L，使其收敛到内在校准点L*（满足T*=1）。训练损失为带温度τ和偏移ξ的交叉熵，其中τ被吸收进L的缩放，ξ用于控制准确率-鲁棒性权衡，通过改变ξ可构建完全校准的Pareto前沿。收敛后冻结L*，可将校准数据重新整合到训练中。网络采用逐层光谱归一化约束每层的Lipschitz常数，确保全局L可控。

### 三、结果（Result）
在CIFAR-10/100和Tiny-ImageNet上，LiST训练的模型在保持开箱校准（ECE显著降低）的同时，取得了与约束（1-Lipschitz基线）和未约束基线竞争的准确率和鲁棒性（认证鲁棒准确率CRA和实证鲁棒准确率ERA）。关键发现是存在最优L*使得T*=1，且校准可作为选择Pareto前沿上操作点的原则性标准。

### 四、结论（Conclusion）
LiST是一种动态训练范式，通过自适应调整Lipschitz常数自动找到内在校准点，产生同时具有确定性鲁棒性和开箱校准的模型，并允许用户通过边缘参数ξ在保持校准的同时探索准确率-鲁棒性权衡。收敛后重新整合校准数据可提升样本效率而不牺牲校准。

### 五、方法论与关键技术细节
数据：CIFAR-10/100和Tiny-ImageNet，使用标准数据增强。先验：利用TS与L的对偶性，假设存在L*使T*=1。损失：带温度τ和偏移ξ的交叉熵，τ被吸收进L缩放（即训练中L隐式包含1/τ）。超参：L通过反馈T*动态调整，ξ为可调参数。复杂度：LiST每次epoch需在校准集上计算T*（O(N_cal)），额外开销小。约束：过低的L导致模型无法拟合尖锐后验，造成不可避免的欠置信；仅适用于Lipschitz约束网络。
