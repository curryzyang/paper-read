# SwiftLoop: Selective Refinement for Adaptive Implicit Reasoning in Looped Transformers

- 区域：精读区
- 排名：10
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Tianyi Zhao, Ke Wan, Chen Chen
- 机构：University of Virginia
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31481v1) · [PDF](https://arxiv.org/pdf/2611.31481v1)

## TLDR
SwiftLoop is an inference-time framework for looped Transformers that learns lightweight, hindsight-supervised per-position freezing policies—based on K/V reusability and functional impact—to adaptively allocate recurrent computation across depth and active width while preserving reasoning accuracy and accelerating inference.

## Abstract
Looped Transformers advance implicit chain-of-thought reasoning through recurrent latent refinement. However, existing looped reasoners typically employ fixed-depth recurrence, updating all latent positions at every iteration and incurring redundancy when further refinement is unnecessary. We introduce \textsc{SwiftLoop}, an inference-time framework for selective recurrent refinement through position-wise freezing, enabling adaptive computation allocation across both recurrent depth and active width. SwiftLoop learns lightweight freezing policies through hindsight-guided supervision derived from two complementary criteria: K/V reusability at the internal representation level and functional impact at the output level. At inference time, these policies guide adaptive freezing based on observed hidden states. Extensive experiments demonstrate that SwiftLoop achieves favorable accuracy--computation trade-offs over fixed-loop inference and adaptive baselines, with measured inference acceleration. Beyond implicit reasoning, we further demonstrate its applicability to recurrent prompt prefilling in general looped models.


## 精读解读（中文）
### 一、研究动机
现有循环Transformer通常采用固定深度循环并在每轮更新所有潜在位置，当进一步细化已无必要时会产生冗余计算；不同样本、不同潜在槽位所需的循环深度存在显著异质性，因此需要在循环深度和活跃宽度两个维度上自适应分配计算。论文进一步指出，K/V可复用性反映内部表示一致性，功能影响反映输出预测后果，二者并不等价且都依赖未来计算，难以在线直接获得，这构成选择性冻结策略的核心挑战。

### 二、技术方案（Method）
SwiftLoop在每次可冻结循环后，对每个活跃位置构造由当前隐藏状态和最近一次循环更新组成的特征z_i(t)=[h_i(t); h_i(t)-h_i(t-1)]，用轻量MLP预测冻结分数，超过阈值λ即冻结该位置；冻结位置停止后续隐藏状态与各层K/V更新，但保留缓存K/V供活跃位置在注意力中继续使用，从而为每个位置分配有效循环深度τ_i并动态缩小每轮活跃宽度。监督来自校准集上完整R轮轨迹的事后信号，提供两种可选目标：K/V可复用性定义为未来最大层平均相对K/V距离c_i^KV(t)=max_{t<u≤R}D_i^KV(t,u)，功能影响则用单位置冻结相对未冻结轨迹的logit margin变化绝对值，或用joint-path integrated gradients沿α=s1的K/V插值路径做中点积分来近似每个位置贡献|G_i|。预测器以回归损失(g_φ(z_i(t))+log(c_i(t)+δ))^2训练，使高分对应低冻结代价；推理时仅依据当前隐藏状态在线决定冻结，并可扩展到通用循环模型的recurrent prompt prefilling。

### 三、结果（Result）
在LOTUS-1B/3B等模型和GSM8K、SVAMP、MultiArith、GSM-Hard四个基准上，SwiftLoop相较固定循环推理和自适应基线取得更优的准确率—计算权衡，并报告了实测推理加速。机制分析显示样本所需循环深度随难度变化、槽位所需深度在样本内和样本间均不均匀；局部K/V稳定并不保证未来可复用，且显著K/V漂移不一定造成大的预测margin影响。在500个GSM8K验证样本的五折交叉验证中，基于当前隐藏状态预测K/V可复用性和功能影响的轻量MLP分别达到0.96和0.78的within-loop out-of-fold AUC，支持在线冻结决策。

### 四、结论（Conclusion）
SwiftLoop将隐式推理中的自适应循环细化为位置级选择性冻结问题，联合内部K/V可复用性与输出功能影响两种事后监督来学习在线策略，在保持竞争性任务性能的同时减少循环计算并提升推理效率。该方法不仅适用于LOTUS式隐式推理，也可用于Ouro和Huginn等通用循环模型中的循环prompt预填充。

### 五、方法论与关键技术细节
关键实现依赖校准集上未冻结的完整R轮轨迹来构造事后监督，LOTUS-3B分析使用GSM8K-Aug微调模型、150个潜在槽位和6轮循环，并从GSM8K验证/测试中选取1648个含完整推理轨迹样本进行深度分析，预测器评估使用500个验证样本五折交叉验证。损失为带δ数值稳定的回归损失，冻结阈值λ控制精度—计算权衡；K/V目标使用层平均相对距离的未来最大值，功能影响可用精确单位置反事实但需每个位置—轮次单独rollout，joint-path IG用K个中点求积并可在一次反向传播中计算所有位置梯度以降低监督成本。冻结后总循环位置更新数为U(τ)=Σ_iτ_i，K/V缓存保留使活跃位置仍可关注已冻结位置；局限性包括依赖校准数据与全轨迹监督、阈值和预测器跨分布泛化、功能影响以固定top-two token的logit margin衡量，以及在更多循环架构和任务上的适用性仍需验证。
