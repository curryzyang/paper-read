# ORBIT: Autoregressive Time Series Generation via Next Frequency-Band Prediction

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Chunyi Hou, Xiangfei Qiu, Hanyin Cheng, Chenchen Sun, Yisheng An, Yang Shu, Jilin Hu, Bin Yang
- 机构：East China Normal University, Chang'an University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.27000v1) · [PDF](https://arxiv.org/pdf/2610.27000v1)

## TLDR
ORBIT is a unified deep generative framework that uses a Frequency-Hierarchical VQ-VAE to tokenize time series into hierarchical frequency bands and a Frequency-Band Autoregressive Transformer to generate them from low to high frequency, enabling coordinated modeling of global structure and fine-grained dynamics with state-of-the-art performance and efficient inference.

## Abstract
Deep generative models provide an effective modern solution to alleviating the problem of data scarcity by synthesizing realistic time series. However, despite the considerable progress achieved by existing deep time series generators, two key challenges remain: (1) learning hierarchical representations for heterogeneous temporal patterns; and (2) coordinating the generation process of heterogeneous temporal dynamics. To address these key bottlenecks, in this work, we propose ORBIT, a unified deep generative framework for time series. Specifically, we develop two key components: the Frequency-Hierarchical VQ-VAE (FH-VQ-VAE) and the Frequency-Band Autoregressive Transformer (FBAR). The former learns hierarchical representations by decomposing latent temporal representations into different frequency bands and applying residual quantization with increasing token budgets. The latter establishes a novel low-to-high frequency autoregressive direction, yielding a time series generation process that first constructs global temporal structures and then incrementally incorporates fine-grained temporal details. These compact designs not only disentangle heterogeneous temporal patterns for more effective representation learning but also mitigate potential interference among different temporal dynamics during generation. Extensive experiments on multiple challenging real-world benchmarks demonstrate that ORBIT achieves state-of-the-art overall performance while exhibiting superior inference efficiency compared with advanced baselines.


## 精读解读（中文）
### 一、研究动机
真实时间序列常由不同频率尺度上的异质动态叠加而成，现有两阶段生成器通常将慢变全局结构与快变局部波动纠缠在单一表示中，并在GPT式从左到右的自回归过程中于同一步共同生成，易造成模式干扰。因此，如何学习保留全局结构与局部细节的分层表示，并协调异质时序动态的生成，是提升合成时间序列质量的关键瓶颈。

### 二、技术方案（Method）
ORBIT采用两阶段框架：第一阶段训练频率分层VQ-VAE（FH-VQ-VAE），对通道独立的时间序列经1D卷积残差编码器得到潜在表示，利用FFT和非重叠频带掩码分解到多个频带，再IFFT回时域，按低频到高频进行残差量化，并通过插值将各频带残差调整到逐级增加的token预算后查询共享码本，辅以轻量精化模块并累积重建，最后由解码器重建原序列；第二阶段冻结FH-VQ-VAE并训练频带自回归Transformer（FBAR），根据已生成频带的码本索引重建并累积历史频带表示，经插值、投影及时序位置和频带嵌入构造输入，在频带因果注意力下用交叉熵预测下一频带索引。推理时从条件或无条件下开始，按低频到高频逐频带生成，每个频带内所有token并行采样，累积表示最终送入冻结解码器合成时间序列。

### 三、结果（Result）
论文在多个具有挑战性的真实世界基准上开展域内与跨域生成实验，报告ORBIT取得当前最优的整体生成性能，并相较先进基线展现出更优的推理效率。摘要层面强调其生成质量与效率优势具有一致性，但全文预览未给出具体指标数值，需以正式实验表为准。

### 四、结论（Conclusion）
ORBIT通过频率分层离散表示与“下一频带预测”的自回归范式，将异质时序模式在表示学习和生成过程两个层面解耦，先构建全局时序结构再逐步引入细粒度细节，从而兼顾生成保真度与推理效率。该工作为时间序列生成提供了一条以频带为自回归单元的新技术路线。

### 五、方法论与关键技术细节
关键先验是低频对应慢变全局结构、高频对应快变局部细节，因此采用低频少token、高频多token的逐级残差量化；码本在各频带间共享，量化使用直通估计器训练，频带间通过因果注意力显式建模依赖。实现上采用通道独立策略，第二阶段冻结tokenizer并以真实索引进行教师强制训练，推理时用已生成索引累积历史并频带内并行解码以降低时延。局限性包括全文预览未展示完整损失项、频带划分与token预算等超参细节，频带边界和数量可能影响性能，通道独立建模可能弱化跨通道依赖，且VQ类方法仍受码本利用与量化误差约束。
