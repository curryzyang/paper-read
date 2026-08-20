# DOW-KE: Anchor-Free Multi-Layer Knowledge Editing via Direct End-to-End Weight Optimization

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Ran Chen, Junbo Zhang, Qianli Zhou, Xinyang Deng, Wen Jiang
- 机构：Northwestern Polytechnical University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16932v1) · [PDF](https://arxiv.org/pdf/2608.16932v1)

## TLDR
DOW-KE is an anchor-free multi-layer knowledge editing method that directly backpropagates the final editing objective through the entire model to jointly optimize deployed weight updates, eliminating the structural misalignment between optimized anchors and realized edits and achieving state-of-the-art performance in sequential editing benchmarks.

## Abstract
Multi-layer locate-then-edit methods for knowledge editing first optimize target residual-stream activations (anchors) at selected layers, then realize them layer by layer as weight updates. This pipeline optimizes an intermediate representation but deploys multi-layer weight updates whose joint effect through the true forward pass is never itself optimized: regardless of how anchors are set or propagated, each update comes from a local solve, so propagation-induced attenuation and distortion go uncorrected, leaving a closure gap between anchor targets and realized edits. We propose DOW-KE, an anchor-free method built on a single principle: what is optimized must be exactly what is deployed. DOW-KE backpropagates the final editing objective through the complete model, jointly optimizing the updates of all edited layers so cross-layer propagation and coupling enter every gradient step. The same principle dictates where preservation resides: embedding the preservation projection in the update parameterization, inside the computation graph, makes every gradient act on the deployed update; post-hoc constraints would reopen the gap, and the constrained search keeps edits clear of protected knowledge. In large-scale sequential editing on two datasets and three models, DOW-KE achieves the highest overall Score and neighborhood Specificity in five of six model-dataset settings among the evaluated baselines.


## 精读解读（中文）
### 一、研究动机
现有多层 locate-then-edit 知识编辑方法采用两阶段管线：先在选定层优化残差流中的锚点激活，再将锚点逐层转化为权重更新。该管线优化的是中间表征，而真正部署的是多层权重更新的联合效果，后者从未在真实前向传播中被整体优化。由于逐层闭式解只拟合局部目标，残差传播的衰减、畸变和跨层耦合无法被校正，导致锚点目标与实际编辑效果之间存在闭合缺口，编辑强度也难以在完整性与局部性之间校准。

### 二、技术方案（Method）
DOW-KE 的原则是“被优化的必须是被部署的”。输入为一批编辑请求（主题-对象对）、随机前缀和需要保护的语料统计量；首先沿用 locate-then-edit 定位待编辑的 FFN 层窗口，并为每个编辑层计算编辑键 K1 和保存统计二阶矩 C；然后将每层权重更新 Δ 参数化为 Δ = R K1^T (λC + K1 K1^T)^-1，其中 R 是可学习的“写什么”值残差，保存投影被嵌入该参数化中，梯度因此始终作用在真实部署的更新上；接着以最终编辑目标（如目标对象负对数似然）加 KL 保持项为损失，在完整模型上反向传播，同时优化所有编辑层的 R，使残差衰减、畸变与跨层耦合进入每一步梯度；推理时直接使用更新后的权重，顺序编辑时逐批提交更新。

### 三、结果（Result）
在两个数据集和三个模型的大规模顺序编辑实验中，DOW-KE 在六个模型-数据集设置的五个中取得了最高的综合 Score 和邻域特异性。针对结构错位的量化实验显示，现有单锚点多层方法的终端未闭合残差约为 0.33，逐层实现率约为 0.5，且仅缩放更新幅度无法同时提升有效性和局部性（复合分数在缩放系数 0.9 时峰值为 86.89）；DOW-KE 通过端到端联合优化消除了这类闭合缺口。

### 四、结论（Conclusion）
DOW-KE 验证了知识编辑中“优化对象与部署对象必须一致”的核心思想：用最终目标直接监督权重更新，而非先优化锚点再局部求解，可以显式建模残差传播的衰减、畸变与跨层耦合，使多层编辑在功效、泛化和局部性上更优。该方法在多数模型-数据集设置上超过现有基线，为多层知识编辑提供了一种无需锚点的直接权重优化范式。

### 五、方法论与关键技术细节
关键细节：(1) 建模先验：沿用线性关联记忆视角，FFN 下投影矩阵 W^l 被视为键值记忆，键为 k_t^l=φ^l(γ(h_t^{l-1}+a_t^l))，值为 W^l k_t^l；(2) 更新参数化：Δ = R K1^T (λC + K1 K1^T)^-1，R 是逐层可学习的值残差，K1 由随机前缀下的编辑键得到，C 是保护知识键的二阶矩，保存约束在计算图内生效而非事后施加；(3) 损失：最终编辑目标（目标对象负对数似然）在 N 个随机前缀上平均以增强泛化，KL 项在 essence prompt 上抑制表示漂移；(4) 训练/推理：所有待编辑层的 R 通过完整模型反向传播联合优化，推理时无额外模块或外部记忆，顺序编辑时逐批提交权重更新；(5) 超参与复杂度：超参包括编辑层窗口、随机前缀数 N、保存系数 λ、KL 系数 λ_KL；更新空间为随编辑批次增长的低秩空间，更新与特定事实绑定，存储不随编辑数持续增加；局限是全模型端到端反向传播的计算开销高于闭式解，且结果依赖层定位与保存统计的质量。
