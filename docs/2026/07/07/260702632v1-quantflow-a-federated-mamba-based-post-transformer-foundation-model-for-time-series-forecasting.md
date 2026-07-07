# QuantFlow: A Federated Mamba-Based Post-Transformer Foundation Model for Time-Series Forecasting

- 区域：精读区
- 排名：1
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Shah Nawaz Haider, Steve Austin, Arnab Barua, Sarowar Morshed Shawon, Hadaate Ullah
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02632v1) · [PDF](https://arxiv.org/pdf/2607.02632v1)

## TLDR
QuantFlow integrates inverted embedding, bidirectional Mamba state-space decoders, quantile regression, TSMixup augmentation, and federated learning to enable scalable, uncertainty-aware, and privacy-preserving probabilistic time-series forecasting, achieving strong centralized performance and retaining useful accuracy in a 20-client non-IID federated setting.

## Abstract
Time-series forecasting supports decisions in finance, en-ergy, transportation, public health, and industrial monitoring. Recent foundation models improve transfer across forecast-ing tasks, but many depend on centralized data and Trans-former attention, which restricts their use for long, high-di-mensional, and privacy-sensitive signals. This paper presents QuantFlow, a probabilistic forecasting framework that com-bines inverted sequence embedding, bidirectional Mamba state-space decoders, quantile regression, and federated learning. Each variable is embedded over the complete ob-servation window, processed in forward and reverse direc-tions, and projected to five conditional quantiles. TSMixup expands temporal diversity through Dirichlet-weighted inter-polation while preserving sequence structure. Experiments cover cryptocurrency, traffic, electricity, Electricity Trans-former Temperature, influenza, and weather data. QuantFlow obtains mean squared errors of 0.2834 on ETTm1 and 0.2218 on Weather, and a 20-client non-IID deployment retains use-ful accuracy after three communication rounds without cen-tralizing raw records. The results indicate that selective state-space modelling is a promising basis for scalable, uncer-tainty-aware, and privacy-conscious time-series prediction, while also revealing limitations on irregular epidemiological signals and long-horizon generalization.

## 精读解读（中文）

### 一、研究动机
现有时间序列基础模型依赖集中数据和Transformer注意力，导致在长序列、高维和隐私敏感信号上计算成本高且无法满足数据本地性要求。

### 二、技术方案（Method）
提出QuantFlow框架，采用反向序列嵌入将每个变量编码为跨完整观测窗口的向量，通过六层双向Mamba状态空间解码器建模变量间关系，并使用分位数回归头输出五个条件分位数（0.10/0.25/0.50/0.75/0.90）实现概率预测。同时引入TSMixup数据增强，从现有序列中按狄利克雷权重进行插值以扩展时间多样性。联邦学习部分采用20个客户端非独立同分布设置，使用加权平均聚合模型更新，仅三轮通信。

### 三、结果（Result）
在ETTm1和Weather数据集上分别取得MSE=0.2834和0.2218，优于Time-MoE、iTransformer等基线。20客户端非IID联邦部署后，R²仍保持在0.86以上（除流感外），且仅下降约0.05。消融实验表明双向Mamba和反向嵌入均为关键组件，移除后MSE上升。

### 四、结论（Conclusion）
选择性状态空间建模为可扩展、不确定性感知且隐私感知的时间序列预测提供了有前景的基础，但在不规则流行病信号（流感R²仅0.53）和长时域泛化方面仍存在局限性。

### 五、方法论与关键技术细节
使用100步滑动窗口单步预测，嵌入维度256，双向Mamba层数6，FFN中间维度1024，dropout0.1。损失函数为分位数pinball损失，优化器未说明。联邦学习FedAvg，3轮通信，每个客户端数据非IID。局限性：流感和长时域预测表现差，未提供完全公平的基准对比。复杂度：Mamba线性复杂度于序列长度，但六层双向可能增加开销。

