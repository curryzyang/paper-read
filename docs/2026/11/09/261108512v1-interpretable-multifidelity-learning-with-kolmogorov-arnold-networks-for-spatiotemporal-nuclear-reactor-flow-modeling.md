# Interpretable Multifidelity Learning with Kolmogorov-Arnold Networks for Spatiotemporal Nuclear Reactor Flow Modeling

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Meredith Eaheart, Majdi I. Radaideh
- 机构：University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08512v1) · [PDF](https://arxiv.org/pdf/2611.08512v1)

## TLDR
This paper shows that interpretable multifidelity Kolmogorov-Arnold Networks match black-box neural networks for predicting spatiotemporal PWR core flow while additionally yielding symbolic equations, but true cross-fidelity forecasting remains fundamentally limited by weak fidelity correlation and scarce CFD transient data.

## Abstract
High-fidelity computational fluid dynamics (CFD) simulations of nuclear reactor systems are computationally expensive, motivating machine learning methods that reduce cost while preserving accuracy. Multifidelity surrogate modeling addresses this by combining inexpensive low-fidelity data with limited high-fidelity data. This work investigates whether the high-fidelity data required to predict the spatiotemporal mass flow rate across all 193 fuel assemblies of a pressurized water reactor (PWR) core can be reduced, comparing black-box multifidelity feedforward neural networks (MFNNs) with interpretable multifidelity Kolmogorov-Arnold Networks (MFKANs). Cross-fidelity correlation across the core is weak, making this a challenging multifidelity problem, and neither architecture predicts the transient particularly well in absolute terms. MFKAN nonetheless performs comparably to MFNN for one-time-step-forward prediction while also providing closed-form symbolic equations unavailable with MFNN. To address the scarcity of CFD transients, with only one available per fidelity level, TabDDPM-generated synthetic data was used to augment cross-fidelity forecasting. KAN and FNN achieve comparable self-evaluation accuracy (Pearson correlation of roughly 0.73--0.81), but both perform poorly at true cross-fidelity forecasting (correlations of 0.03--0.06). Assembly-level analysis shows that each assembly's forecast correlation tracks its real cross-fidelity correlation for both architectures ($r=0.840$--$0.896$ for KAN, $r=0.804$--$0.903$ for FNN), confirming that forecasting accuracy is fundamentally limited by how correlated the fidelity levels already are. Overall, KAN-based multifidelity modeling achieves accuracy consistently comparable to MFNN across all settings, while additionally providing symbolic equations that match or exceed the spline representation's accuracy.


## 精读解读（中文）
### 一、研究动机
核反应堆全堆芯CFD瞬态模拟计算代价高，而多保真度代理建模可用少量高保真数据结合大量低保真数据来降低成本并保持精度。本文针对压水堆193个燃料组件的全堆芯时空质量流量预测，研究在跨保真度相关性弱且每个保真度仅有一个CFD瞬态的条件下，能否减少高保真数据需求，并比较黑箱MFNN与可解释MFKAN。

### 二、技术方案（Method）
数据来自STAR-CCM+构建的全尺度四环路PWR下腔室模型，采用BEAVRS几何、多孔介质燃料组件和STRUCT-ε湍流模型，输出193个组件在九个轴向层上的面积平均质量流量；每个瞬态15 s、步长0.0005 s，丢弃前10 s后记录10–15 s共10000步，并构造三个CFD网格保真度。建模上比较MFNN与MFKAN，包括低保真KAN加残差修正的MFKAN-Delta、将保真度等级显式编码为输入的MFKAN-Flag，以及扩展到三保真度的MFKAN-Flag3f。训练/推理流程包括用低/高保真数据做多保真度一步预测和跨保真度瞬态预测，并用TabDDPM生成合成表格数据增强跨保真度预测，最后将训练后的KAN转换为闭式符号方程。

### 三、结果（Result）
跨保真度相关性在全堆芯范围内较弱，两个架构对瞬态的绝对预测都不算好；但MFKAN在一步向前预测中与MFNN性能相当，并能给出MFNN没有的闭式符号方程。使用TabDDPM增强后，KAN与FNN的自评估精度相近，Pearson相关约0.73–0.81，而真实跨保真度预测相关仅0.03–0.06；组件级分析显示各组件预测相关与其真实跨保真度相关同步，KAN的r=0.840–0.896、FNN的r=0.804–0.903，说明预测精度本质上受保真度间已有相关性限制。

### 四、结论（Conclusion）
KAN基多保真度建模在所有设置下达到与MFNN持续可比的精度，同时额外提供可解释的符号方程，且符号方程精度可匹配或超过样条表示。研究表明多保真度代理在此类全堆芯时空场问题中的收益受弱跨保真度相关性和瞬态数据稀缺限制，生成式数据增强不能从根本上克服真实跨保真度预测的困难。

### 五、方法论与关键技术细节
关键实现点包括：高维输出为193个燃料组件×九个轴向层×时间步的全堆芯质量流量场；每个保真度仅有一个CFD瞬态，数据稀缺是核心约束；保真度间弱相关使多保真度学习困难；评估同时区分自评估、一步向前预测和真实跨保真度预测，并以Pearson相关及组件级相关跟踪分析诊断限制来源；TabDDPM用于合成表格数据增强，KAN可转为闭式符号方程以提供可解释性。局限性在于绝对预测精度有限、合成数据与真实CFD瞬态的保真度差异，以及单瞬态条件下结论的泛化性仍需更多高保真瞬态验证。
