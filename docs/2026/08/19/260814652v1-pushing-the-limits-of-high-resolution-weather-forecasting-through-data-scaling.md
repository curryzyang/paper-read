# Pushing the Limits of High-Resolution Weather Forecasting through Data Scaling

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Yang Zhao, Peisong Niu, Tian Zhou, Ziqing Ma, Guanlong Ma, Rong Jin, Huiling Yuan, Liang Sun
- 机构：Alibaba Group, Ant Group, Nanjing University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14652v1) · [PDF](https://arxiv.org/pdf/2608.14652v1)

## TLDR
BaguanHR overcomes the data bottleneck in 0.1° ML weather forecasting by transferring data, not models, using variable-wise super-resolution to synthesize extensive high-resolution training data from coarse ERA5 reanalysis, outperforming existing methods and demonstrating power-law scaling where more data yields consistent error reductions.

## Abstract
The development of 0.1$^{\circ}$ global weather forecasting models based on machine learning (ML) is constrained by the limited availability of high-resolution data, as decades of reanalysis are only available at 0.25$^{\circ}$ resolution. While existing approaches fine-tune 0.25$^{\circ}$ forecast models on limited 0.1$^{\circ}$ samples, we show that this transfer is hindered by the irreversible information loss inherent in coarse-resolution forecasting. Therefore, we propose BaguanHR, a framework that shifts the focus from transferring models to transferring data. We first show that super-resolution (SR) has lower conditional entropy and input amplification than forecasting, making it a more robust vehicle for resolution transfer. By leveraging this advantage through variable-wise SR, we synthesize extensive 0.1$^{\circ}$ data from ERA5. BaguanHR's performance on the synthetic-plus-real dataset exceeds both ML-based methods and IFS-HRES, achieving superior performance across over 85% of the lead times within 72 hours. Furthermore, our findings highlight a power-law scaling effect, as a twofold increase in data reduces RMSE by 4.6% for 72-hour forecasting and 4.9% for 120-hour forecasting. Our results demonstrate that scaling high resolution ML-based forecasting is primarily a data bottleneck, and that variable-wise super-resolution provides a simple yet general solution to unlock long coarse-resolution reanalyses for high-resolution training.


## 精读解读（中文）
### 一、研究动机
高分辨率0.1°全球天气预测模型受限于高分辨率数据稀缺，因为ERA5等再分析数据仅提供0.25°分辨率，而0.1°分析数据只有约10年。现有方法通过微调粗分辨率模型来适应高分辨率，但粗分辨率预测存在不可逆信息损失，导致迁移效果受限。

### 二、技术方案（Method）
提出BaguanHR框架，核心是'转移数据而非模型'。先通过理论分析证明超分辨率(SR)比预测(FC)具有更低的条件熵和输入放大因子，因此更稳健。利用逐变量Swin2SR模型在0.25°-0.1°配对样本上训练，对ERA5数据进行逐变量超分辨率合成，生成大量0.1°伪标签。预测模型采用Swin Transformer架构，包含变量专属tokenization、分层嵌入(将变量分12组聚合)和自适应性rollout策略(先导时间感知损失加权+随机缓冲区替换)。训练分三阶段：先在8年EC分析数据上预训练250k步，再加入10年合成数据微调70k步，最后进行2天rollout训练；并采用数据分片I/O优化。

### 三、结果（Result）
在合成+真实数据上训练的BaguanHR在72小时内超过85%预报时效上优于IFS-HRES和多种ML方法；与coarse-to-fine迁移相比，部分变量RMSE降低最高20%；数据缩放遵循幂律，训练数据从7年增至18年时，72小时和120小时RMSE分别降低4.6%和4.9%。

### 四、结论（Conclusion）
高分辨率ML天气预报的性能提升主要受数据瓶颈制约，逐变量超分辨率提供了一种简单通用的数据扩展方案，能够利用长期粗分辨率再分析生成高分辨率训练数据，比模型迁移或架构设计更有效。

### 五、方法论与关键技术细节
关键细节：SR逐变量训练并使用MAE损失；预测模型输入80个变量(tp仅输出)，经patch化、分层嵌入(Swin Transformer)后输出，变量分12组以减少内存；训练使用32块A800，三阶段(250k步预训练+70k步合成微调+2天rollout)并采用I/O数据分片加速；理论分析显示SR的放大因子(0.6-0.8)低于预测(1.0-1.2)，且SR重建误差远小于一步预测；局限是合成数据依赖SR精度，且实验基于ECMWF分析数据。
