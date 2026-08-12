# Uncertainty-Aware Ensemble Deep Randomized Neural Networks for Classification

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：M. Sajid, A. Quadir, A. Rahaman, P. N. Suganthan, M. Tanveer
- 机构：Indian Institute of Technology Indore, Qatar University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10007v1) · [PDF](https://arxiv.org/pdf/2608.10007v1)

## TLDR
TLDR: The paper proposes uncertainty-aware intuitionistic fuzzy deep and ensemble deep Random Vector Functional Link networks (IF-dRVFL and IF-edRVFL) that assign adaptive sample weights via membership and non-membership degrees to improve classification robustness against noise and outliers.

## Abstract
The current state-of-the-art (SOTA) deep randomized neural networks, such as deep Random Vector Functional Link (dRVFL) and ensemble deep RVFL (edRVFL), treat all training samples uniformly, which limits their robustness and effectiveness when applied to real-world datasets containing noise and outliers. Furthermore, the propagation of contaminated features across hidden layers negatively influences the decision-making capability of these models. To overcome these limitations, we propose intuitionistic fuzzy dRVFL (IF-dRVFL) and intuitionistic fuzzy edRVFL (IF-edRVFL) frameworks that enhance model robustness. The proposed models unify intuitionistic fuzzy theory to exploit sample neighborhood information in the kernel space by jointly considering membership and non-membership degrees for each sample. Membership degrees are computed based on the distance of samples from their respective class centroids, while non-membership degrees quantify sample heterogeneity within local neighborhoods. These measures are employed to assign adaptive weights to training samples, enabling effective discrimination among clean, noisy, and outlier data points. Extensive experiments conducted on UCI and KEEL benchmark datasets, with and without the presence of Gaussian noise, demonstrate the superiority of the proposed IF-dRVFL and IF-edRVFL models over existing SOTA fuzzy and non-fuzzy approaches. The source code is available at https://github.com/mtanveer1/IF-edRVFL.


## 精读解读（中文）
### 一、研究动机
现有深度随机神经网络（如dRVFL和edRVFL）对所有训练样本一视同仁，难以应对真实数据中的噪声和异常值；同时，受污染的特征在隐藏层间传播会损害模型的决策能力。为此，本文引入直觉模糊理论，为每个样本同时计算隶属度与非隶属度，从而区分干净样本、噪声和异常点，提升深度RVFL模型的鲁棒性。

### 二、技术方案（Method）
本文提出IF-dRVFL和IF-edRVFL两种框架。输入为原始特征矩阵X和标签Y，深层隐藏层通过随机权重和激活函数逐层生成特征：第一层E(1)=ψ(Xω(1))，更深层E(g)=ψ(E(g-1)ω(g))（IF-dRVFL）或ψ([E(g-1),X]ω(g))（IF-edRVFL）。在核空间中，隶属度μ基于样本到其类中心的距离计算，非隶属度ν基于局部邻域内异类样本比例计算，两者结合得到IF得分s_u，构成对角权重矩阵S。优化目标为带权重的最小二乘问题：min (C/2)||Sη||² + (1/2)||ξ||²，约束E*ξ-Y=η，通过拉格朗日法求解输出权重ξ，根据特征维度与样本数关系选择闭式解。IF-edRVFL将每一隐藏层视为一个基模型，各基模型独立用IF权重训练，最终通过多数投票或平均融合输出。

### 三、结果（Result）
在UCI和KEEL基准数据集上，无论是否添加高斯噪声，IF-dRVFL和IF-edRVFL均优于现有SOTA模糊及非模糊方法，验证了所提模型在分类准确性和鲁棒性上的优越性。具体指标和对比结论在论文实验部分给出，代码已开源。

### 四、结论（Conclusion）
通过直觉模糊加权机制，IF-dRVFL和IF-edRVFL有效缓解了噪声和异常值对深度随机神经网络的影响，避免了不纯特征在层间传播的负面效应，同时IF-edRVFL以单网络隐式实现集成学习，兼顾了鲁棒性和计算效率。

### 五、方法论与关键技术细节
关键点：1）IF得分由隶属度μ（基于样本到类质心距离，含半径r和参数γ）和非隶属度ν（基于邻域内异类比例，参数β控制邻域半径）合成，并通过评分函数s_u=μ（ν=0时）、s_u=0（μ≤ν时）、s_u=(1-ν)/(2-μ-ν)（其他情况）计算；2）正则化参数C和隐藏节点数h需调优，权重随机初始化于[-1,1]；3）闭式解有两种形式：当特征维度(m+kh)≤N时用E*^T S² E* + I/C求逆，否则用S² E* E*^T + I/C求逆，后者复杂度更低；4）IF-edRVFL通过多数投票集成各层输出，无需训练多个独立网络；5）局限性：方法依赖核空间距离计算，高维大数据下距离矩阵计算成本较高；论文中未详细讨论超参数β和γ的选择策略。
