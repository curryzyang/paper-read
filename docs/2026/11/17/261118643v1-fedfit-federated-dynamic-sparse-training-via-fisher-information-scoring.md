# FedFit: Federated Dynamic Sparse Training via Fisher Information scoring

- 区域：精读区
- 排名：5
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Meng Bi, Hong Huang, Jinlong Song, Charles Wang, Chengming Hu, Xi Chen, Ting Yu, Xue Liu
- 机构：McGill University, Mohamed bin Zayed University of Artificial Intelligence, City University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18643v1) · [PDF](https://arxiv.org/pdf/2611.18643v1)

## TLDR
FedFit is a federated dynamic sparse training framework that replaces magnitude-based heuristics with Fisher Information Matrix–based, optimization-centric scoring to adjust sparse structures during training, thereby narrowing the sparse-to-dense accuracy gap while maintaining communication efficiency.

## Abstract
Cross-device Federated Learning (FL) is frequently bottlenecked by the prohibitive memory and communication costs of training deep neural networks on resource-constrained edge hardware. While federated dynamic sparse training aims to alleviate these costs by adjusting sparse structures during training, existing methods rely on magnitude-based heuristics that are fundamentally ill-suited for the non-convergent, heterogeneous environments inherent to FL. To address this challenge, we propose FedFit, a federated dynamic sparse training framework that replaces simple heuristics with optimization-centric criteria for structure adjustment. By leveraging a second-order approximation of the loss landscape via the Fisher Information Matrix, FedFit enables precise and efficient structure adjustment without the overhead of explicit Hessian computation. Empirical evaluations across computer vision and natural language processing benchmarks demonstrate that FedFit significantly narrows the sparse-to-dense accuracy gap, outperforming state-of-the-art methods while maintaining high communication efficiency. Our code is available at https://github.com/Serena-28/Fedfit.git .


## 精读解读（中文）
### 一、研究动机
跨设备联邦学习在资源受限边缘硬件上训练深度网络时受内存与通信成本瓶颈；联邦动态稀疏训练虽可降低开销，但现有方法依赖权重幅值和梯度幅值等启发式，这些准则继承自后训练范式，假设模型近收敛且Hessian局部稳定，在FL非收敛、非IID异构环境中会产生高偏差和高方差的重要性估计，导致稀疏结构调整收益不可靠、稀疏与稠密模型精度差距持续存在。

### 二、技术方案（Method）
FedFit在每轮客户端先以当前稀疏掩码做本地稀疏训练，然后依据二阶泰勒展开导出的优化准则调整结构：剪枝分数为P_k等于负的梯度乘权重加上二分之一权重平方乘Fisher对角项，优先剪掉分数小的参数；增长分数为G_j等于二分之一梯度平方除以经验Fisher对角项，优先激活分数大的参数。为避开显式Hessian，方法用Fisher信息矩阵近似曲率，并采用K-FAC按层以输入激活二阶矩与反传预激活梯度二阶矩的Kronecker积近似Fisher块；客户端调整后服务器聚合权重并对掩码取并集，可选地按全局分数剪枝恢复目标密度。

### 三、结果（Result）
在计算机视觉和自然语言处理基准上，FedFit显著缩小了稀疏模型与稠密模型之间的精度差距，并持续优于现有联邦剪枝SOTA，同时保持较高通信效率；正文预览显示在SVHN的ResNet-18实验中报告了7.04%的提升。可复现结论是Fisher驱动剪枝与增长比幅值或梯度启发式更稳定，尤其在非IID和低密度设置下更能保留关键参数。

### 四、结论（Conclusion）
FedFit将联邦动态稀疏训练的结构调整从启发式规则推进到基于损失二阶近似的优化中心准则，利用Fisher信息在不显式计算Hessian的情况下实现在线剪枝与增长；实验表明其能缩小稀疏到稠密精度差距并优于SOTA，且计算与通信开销可忽略。论文贡献还包括对FDST剪枝与增长准则的理论分析以及近似误差上界和开销分析，为资源受限FL中的稀疏结构学习提供了理论与实证依据。

### 五、方法论与关键技术细节
关键实现细节包括：以目标密度rho约束的稀疏权重和二进制掩码为状态，客户端非IID数据上执行本地稀疏训练后按每轮或周期性比例进行剪枝和等量增长；采用经验Fisher和K-FAC逐层近似，Fisher半正定保证增长分数中二次型凹性并可解析求最优步长；理论依赖小扰动二阶泰勒截断和H约等于F两个假设，并给出逐层二阶分解、交互残差与近似误差上界。局限在于K-FAC统计与稀疏掩码和权重通信仍带来额外开销，低密度与强异构下近似稳定性、剪枝增长率、频率、增长步长等超参敏感性需关注，且预览未给出完整超参表。
