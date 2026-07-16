# STKAN: Kolmogorov-Arnold Networks for Spatio-Temporal Forecasting

- 区域：精读区
- 排名：4
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Sicong Lai, Yuehong Hu, Siru Zhong, Si Qiao, Yuxuan Liang, Guangyin Jin
- 机构：Chang'an University, The Hong Kong University of Science and Technology (Guangzhou), China University of Geosciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13108v1) · [PDF](https://arxiv.org/pdf/2607.13108v1)

## TLDR
STKAN introduces Taylor-polynomial Kolmogorov-Arnold Network modules into spatial and temporal token mixing for spatio-temporal forecasting, achieving competitive performance on traffic benchmarks.

## Abstract
Real-world traffic data exhibit heterogeneous spatial correlations and nonlinear temporal dynamics, posing substantial challenges for accurate spatio-temporal forecasting. Existing approaches have developed increasingly sophisticated graph, attention, and decomposition architectures, while the influence of the underlying nonlinear function approximator has received comparatively less attention. In this work, we propose STKAN, a spatio-temporal forecasting architecture that introduces Taylor-polynomial Kolmogorov--Arnold Network modules into spatial and temporal token mixing. STKAN first constructs high-level spatial representations through a learnable soft node-group assignment mechanism, applies group-wise spatial mixing, and subsequently models temporal dependencies over the compressed sequence. Spatial and temporal self-attention layers are further employed to capture long-range interactions. Experiments on five traffic forecasting benchmarks show that STKAN achieves competitive performance and performs better than the evaluated MLP-based variant in the tested settings. These results suggest that the design of nonlinear function approximators can serve as a useful complement to architectural design in spatio-temporal forecasting.


## 精读解读（中文）
### 一、研究动机
现有时空预测方法主要关注图、注意力、分解等架构设计，而底层非线性函数逼近器（如MLP的固定激活函数）的选择对性能的影响未得到充分研究。本文旨在探究非线性函数逼近器设计的作用，并引入泰勒多项式Kolmogorov-Arnold网络作为替代参数化方案。

### 二、技术方案（Method）
STKAN以历史交通数据（长度L_in，节点N，通道C_in）为输入，首先通过全连接层、可学习空间嵌入和时间嵌入（时间-日、星期）构建初始表示，再通过补丁卷积降低时间分辨率。核心步骤包括：1) 可学习软节点分组，通过未归一化矩阵A经softmax得到G个组的分配权重；2) 空间KAN块，对分组后的空间token进行泰勒多项式KAN混合（沿组维度），随后MLP通道混合，再通过分组权重还原到节点级；3) 时间KAN块，对节点级表示沿压缩时间维度进行泰勒多项式KAN混合，再用MLP通道混合；4) 时空融合块，分别使用空间自注意力和时间自注意力捕捉长期依赖。最后通过线性预测头输出未来H步预测。

### 三、结果（Result）
在PEMS04、PEMS07、PEMS08、PEMS-BAY和METR-LA五个交通预测基准上，STKAN取得了具有竞争力的预测精度，在所有测试设置中均优于评估的MLP基变体。消融实验表明泰勒KAN混合器、自适应空间分组和注意力组件各自对模型有贡献。

### 四、结论（Conclusion）
非线性函数逼近器的设计可作为架构设计之外的有用补充。KAN层通过可学习单变量函数提供不同归纳偏置，在时空预测任务中能有效替代MLP的固定激活函数，为进一步提升预测性能提供了新方向。

### 五、方法论与关键技术细节
关键实现细节包括：可学习软分组矩阵初始化为未归一化参数，通过softmax归一化；泰勒多项式KAN层使用多项式阶数K（实验设为3），可学习系数θ直接优化，未约束为解析导数；空间和时间注意力使用缩放点积注意力，隐藏维度d_h设为64；损失函数为MAE；优化器Adam，学习率0.001；数据按6:2:2或7:1:2划分；分组数G为节点数的1/4；局限性：分组机制可能丢失细粒度空间信息，多项式阶数需调参。
