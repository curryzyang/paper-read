# LLM-enhanced spatio-temporal learning for grid-level docked bike sharing demand prediction

- 区域：精读区
- 排名：6
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Xuxilu Zhang, Francesc Soriguera
- 机构：Universitat Politècnica de Catalunya
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03834v1) · [PDF](https://arxiv.org/pdf/2610.03834v1)

## TLDR
A framework uses an LLM to convert urban event text into physics-based Gaussian spatio-temporal perturbation fields that are injected into a zero-inflated adaptive graph convolutional network, improving grid-level docked bike-sharing demand prediction, especially during high-demand periods.

## Abstract
Short-term bike-sharing demand forecasting is complicated by spatial-temporal non-stationarity and the practical difficulty of incorporating unstructured external text into numerical pipelines. Conventional approaches rely on historical flow sequences and fixed graph structures, thereby constraining their accuracy when anomalous social events perturb normal travel patterns. We propose a forecasting framework in which a Large Language Model (LLM) drives a semantic shockwave mechanism that converts free-form urban text, such as municipal event schedules, local news, and transit bulletins, into quantified spatial-temporal perturbation fields. The LLM extracts three physically interpretable parameters per event (intensity, spatial reach, and temporal lag), from which Gaussian decay fields are constructed and injected into a Zero-Inflated Adaptive Spatio-Temporal Graph Convolutional Network (ZI-ASTGCN). To handle the pronounced sparsity of grid-level measurements, the model couples a dual-branch output head with a multi-task zero-inflated loss that jointly trains a gating probability and a conditional flow intensity. Experiments on the operational Barcelona Bicing dataset show that ZI-ASTGCN outperforms established neural baselines, with particularly strong gains during high-demand periods, validating the utility of physics-grounded semantic signals in spatial-temporal mobility forecasting.


## 精读解读（中文）
### 一、研究动机
短时共享单车需求预测受时空非平稳与外部事件冲击影响，传统方法依赖历史流量序列和固定图结构，难以把市政日程、新闻、交通公告等非结构化文本融入数值预测流程，导致异常社会事件扰动出行模式时精度下降。网格级观测还存在显著零膨胀与重尾稀疏性，进一步加剧了需求发生与强度建模的困难。

### 二、技术方案（Method）
提出LLM驱动的语义冲击波机制与零膨胀自适应时空图卷积网络ZI-ASTGCN。首先将城市事件文本输入LLM，通过领域系统提示和少样本示例按JSON schema抽取每个事件的强度S、影响半径R和时间滞后Δt，再构造高斯衰减场I=S·exp(-d^2/R^2)·exp(-Δt/τ)，τ在验证集设为2小时，聚合成语义扰动特征X_sem，并与历史流入流出、天气等拼接。ZI-ASTGCN使用融合图A_fused=S⊙(A+A_d)，其中A为静态地理邻接，A_d为由节点嵌入经Softmax(ReLU(E_node E_node^T))生成并Top-K稀疏化的可学习隐图，S为数据自适应空间注意力；事件期通过交叉注意力以语义影响场为query/key重定向空间特征，时间维采用GLU卷积，空间图卷积采用Chebyshev多项式近似。输出为双分支，分别预测需求发生概率g和条件强度v，损失为多任务零膨胀损失：全部样本上以BCE训练门控，正样本上以自适应Huber回归训练强度，并用α_tail=3.0惩罚需求激增时的低估。训练使用12小时历史预测未来1小时，AdamW初始学习率1e-3，隐藏通道64，每节点保留Top-K=24邻居，空间dropout=0.2，最多200轮、早停30轮。

### 三、结果（Result）
在2025年4月1日至6月30日巴塞罗那Bicing运营数据上，ZI-ASTGCN的inflow RMSE为3.112，优于DCRNN的3.254、STGCN的3.319和GraphWaveNet的3.300，同时inflow MAE为1.360、R2为0.860、WAPE为0.418。移除LLM语义分支后inflow RMSE为3.201，表明语义冲击波字段带来额外增益；事件期指标提升更明显，inflow EvtRMSE从3.653降至3.359，outflow EvtRMSE从3.470降至3.076，Tail-RMSE为inflow 7.631和outflow 7.679。需要指出一个例外：STGCN在outflow Tail-RMSE上为7.469，略优于本文全模型的7.679，作者认为可能与其频谱滤波对齐特定流出尖峰频段有关。

### 四、结论（Conclusion）
该研究表明，用LLM从自由文本中提取物理可解释的事件强度、空间范围和时间滞后，并转化为连续高斯衰减扰动场注入时空图网络，可为共享单车需求预测提供超越历史流量的前瞻性信号。ZI-ASTGCN的双分支零膨胀建模能有效处理网格级稀疏、零膨胀和重尾观测，在高需求与事件冲击期取得更强预测表现，对车队再平衡和站点容量管理具有实际价值。

### 五、方法论与关键技术细节
数据方面包括510个Bicing站点5分钟占用差分推得的流入流出、374个800m×800m网格、约79000个OSM POI归为14类、小时天气以及市政事件日历、新闻和公交公告；语义分支零初始化，确保无事件时与无LLM基线等价，LLM输出校验失败时回退到关键词保守默认参数。关键先验与超参包括S∈[0,1]、R以米计、Δt相对预测窗、τ=2小时、α_tail=3.0、λ平衡门控与回归、Top-K=24、隐藏维64、dropout=0.2、学习率1e-3、最多200轮和早停30轮。方法局限在于事件参数抽取质量依赖LLM与文本覆盖，τ和R等先验需验证集调参，当前仅预测未来1小时，且STGCN在outflow Tail-RMSE上的局部优势说明尾部极端情况仍需更细致分析。
