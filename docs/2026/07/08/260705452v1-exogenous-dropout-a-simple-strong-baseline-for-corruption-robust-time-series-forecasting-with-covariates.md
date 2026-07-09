# Exogenous Dropout: A Simple, Strong Baseline for Corruption-Robust Time Series Forecasting with Covariates

- 区域：精读区
- 排名：4
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Hao Hu, Xue-shan Ai
- 机构：Wuhan University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.05452v1) · [PDF](https://arxiv.org/pdf/2607.05452v1)

## TLDR
Exogenous dropout, a simple training-time augmentation that randomly zeros whole exogenous channels, provides strong corruption robustness for time series forecasting with covariates, outperforming specialized bounded architectures across multiple domains and corruption types.

## Abstract
Time series forecasters that use exogenous covariates are fragile in deployment: when those covariates are noised, temporally misaligned, or missing, strong exogenous-fusion and exogenous-adapted models can degrade far above the endogenous-only floor. We study whether such robustness requires specialized architectures, or whether it can be obtained through a simple training intervention. We propose exogenous dropout, a model-agnostic method that randomly zeros whole exogenous channels during training. Across electricity-price forecasting, reservoir hydrology, and meteorology, exogenous dropout substantially improves robustness under Gaussian noise, temporal misalignment, and fully missing channels, while preserving clean accuracy. Applied to a dual-correlation network, it yields the most robust model in our experiments, outperforming a deliberately strong bounded architectural foil, BoundEx, which combines a learnable gate, a fallback residual to the endogenous backbone, and per-channel exogenous FiLM modulation. Architecture-by-dropout ablations, gate-behavior diagnostics, and a representation-level bound show that explicit architectural boundedness is not necessary for this robustness: an unbounded model trained with exogenous dropout is more robust than the bounded model in every domain. We release a corruption-robustness benchmark and recommend exogenous dropout as a simple, strong baseline for future work on time series forecasting with covariates.


## 精读解读（中文）
### 一、研究动机
时间序列预测中，使用外生协变量的模型在部署时易受噪声、时间错位或缺失等损坏，导致性能大幅下降。现有研究倾向设计专门的融合架构来提升鲁棒性，但作者质疑这一前提，探索是否简单的训练干预即可达到同等或更好的效果。

### 二、技术方案（Method）
提出两种方法进行对比：一是模型无关的外生丢弃（exogenous dropout），训练时以一定概率将整个外生通道置零并缩放剩余通道，迫使模型不过度依赖单一协变量；二是BoundEx，一个有意设计的有界架构，其核心是以门控FiLM调制限制外生影响：通过每个外生通道的MLP生成缩放因子γ、偏移β和门控值g，并经由通道加权平均得到聚合门控ḡ，最终表示为hindog = (1-ḡ)·hindog + ḡ·(γ·hindog+β)，保证当门控关闭时预测完全退化为内生基线。实验涵盖电力价格（5个市场）、水库水文和气象三个领域，在干净、高斯噪声、时间错位和缺失通道四种测试条件下评估，并以5个随机种子重复。

### 三、结果（Result）
外生丢弃显著提升了所有五个基线模型在所有损坏类型下的鲁棒性（例如DAG提升32%），同时保持干净准确率几乎不变。全面的架构×丢弃消融实验表明，BoundEx虽带有内置的有界保证，但DAG结合外生丢弃在干净准确率和所有三种损坏类型上均优于BoundEx，且在所有领域一致。这表明架构有界性并非实现鲁棒性的必要条件。

### 四、结论（Conclusion）
外生丢弃是一种简单、模型无关且强效的鲁棒性基线方法，推荐作为未来外生协变量时间序列预测工作的标准基准。有界架构虽然提供理论保证，但在实践中不如结合外生丢弃的无界模型有效。

### 五、方法论与关键技术细节
关键细节包括：(1) 外生丢弃应用于训练阶段，不改变推理流程；(2) 门控行为诊断显示BoundEx的门控在损坏下并不会关闭，即门控并未按预期退化；(3) 表示级边界证明存在但经验上较松散，故架构有界性对鲁棒性贡献有限；(4) 基准测试涵盖5个随机种子，保证统计显著性；(5) 局限性：外生丢弃对某些架构可能需要调参（丢弃概率），且BoundEx的训练需初始化MLP参数接近零以保证起始阶段接近内生机理。
