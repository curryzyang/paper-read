# QuantFlow: A Federated Mamba-Based Post-Transformer Foundation Model for Time-Series Forecasting

- 区域：精读区
- 排名：1
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Shah Nawaz Haider, Steve Austin, Arnab Barua, Sarowar Morshed Shawon, Hadaate Ullah
- 机构：University of Science and Technology Chittagong
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02632v1) · [PDF](https://arxiv.org/pdf/2607.02632v1)

## TLDR
QuantFlow introduces a federated Mamba-based time-series forecasting framework that combines inverted embedding, bidirectional state-space decoders, quantile regression, and TSMixup to achieve scalable, uncertainty-aware, and privacy-preserving predictions across diverse domains.

## Abstract
Time-series forecasting supports decisions in finance, en-ergy, transportation, public health, and industrial monitoring. Recent foundation models improve transfer across forecast-ing tasks, but many depend on centralized data and Trans-former attention, which restricts their use for long, high-di-mensional, and privacy-sensitive signals. This paper presents QuantFlow, a probabilistic forecasting framework that com-bines inverted sequence embedding, bidirectional Mamba state-space decoders, quantile regression, and federated learning. Each variable is embedded over the complete ob-servation window, processed in forward and reverse direc-tions, and projected to five conditional quantiles. TSMixup expands temporal diversity through Dirichlet-weighted inter-polation while preserving sequence structure. Experiments cover cryptocurrency, traffic, electricity, Electricity Trans-former Temperature, influenza, and weather data. QuantFlow obtains mean squared errors of 0.2834 on ETTm1 and 0.2218 on Weather, and a 20-client non-IID deployment retains use-ful accuracy after three communication rounds without cen-tralizing raw records. The results indicate that selective state-space modelling is a promising basis for scalable, uncer-tainty-aware, and privacy-conscious time-series prediction, while also revealing limitations on irregular epidemiological signals and long-horizon generalization.


## 精读解读（中文）
### 一、研究动机
现有时间序列基础模型大多依赖集中式数据和Transformer注意力机制，导致在长序列、高维和隐私敏感信号上的应用受限。为此，本文提出QuantFlow框架，旨在实现可扩展、不确定性感知且保护隐私的时间序列预测。

### 二、技术方案（Method）
QuantFlow结合倒置序列嵌入、双向Mamba状态空间解码器、分位数回归和联邦学习。每个变量在完整观测窗口（100步）上嵌入为256维向量，经过6层双向Mamba解码层（每层正向和反向处理并融合），再经卷积前馈块（256→1024→256，dropout=0.1）后，投影到五个分位数（0.10,0.25,0.50,0.75,0.90）。TSMixup通过Dirichlet加权插值从k个序列生成增强样本。训练优化pinball损失。联邦学习采用20个非IID客户端，进行3轮通信，服务器按样本数量加权平均客户端参数。

### 三、结果（Result）
在ETTm1和Weather上分别取得MSE=0.2834和0.2218，优于Time-MoE、iTransformer等模型。在20个非IID客户端的三轮联邦学习后，多数数据集R²仍高于0.89（流感除外）。消融实验表明，去除双向Mamba或倒置嵌入会导致MSE和MAPE上升，验证了完整架构的有效性。

### 四、结论（Conclusion）
选择性状态空间建模为可扩展、不确定性感知和隐私保护的时间序列预测提供了有前景的基础，但模型在不规则流行病信号（流感R²仅为0.5327）和长时域泛化方面仍存在局限。

### 五、方法论与关键技术细节
输入采用100步滑动窗口、单步预测；嵌入维度256、6层双向Mamba、前馈隐藏层1024、dropout=0.1；损失为分位数pinball损失；联邦学习设置20客户端、3通信轮、样本加权聚合；主要局限性包括流感数据预测困难（R²低）和长时域泛化不足。
