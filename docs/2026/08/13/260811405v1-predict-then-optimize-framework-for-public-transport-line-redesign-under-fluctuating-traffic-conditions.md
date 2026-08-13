# Predict-then-Optimize Framework for Public Transport Line Redesign under Fluctuating Traffic Conditions

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Zihao Guo, Andrea Araldo, Faycal Touzout, Mounim El-Yacoubi
- 机构：Institut Polytechnique de Paris, National School of State Public Works
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11405v1) · [PDF](https://arxiv.org/pdf/2608.11405v1)

## TLDR
The paper proposes a predict-then-optimize framework that proactively redesigns public transport lines under high traffic fluctuations using NSGA-III and traffic forecasts, achieving substantial travel-time and cost improvements while preserving network structural continuity.

## Abstract
Public Transport (PT) lines are traditionally designed to optimize performance under nominal traffic conditions. In practice, operating conditions frequently deviate from nominal ones, leading to substantial performance deterioration. Existing adaptation mechanisms typically rely on reactive interventions, such as stop-skipping, which are insufficient under large or recurrent traffic fluctuations. In such contexts, incremental adjustments may not suffice. This paper evaluates the potential of deeper structural redesigns to preserve performance.
  We propose a method to proactively redesign appropriate parts of PT networks under high traffic fluctuations that would otherwise deteriorate operator and user performance. We adopt a predict-then-optimize paradigm in which PT lines are reconfigured based on traffic forecasts using the Non-dominated Sorting Genetic Algorithm III (NSGA-III).
  To ensure operational feasibility and avoid excessive structural changes, we enforce high Jaccard edge overlap between the original and redesigned networks. To assess prediction inaccuracies, we construct a statistical model of errors from a well-established deep learning predictor, the Diffusion Convolutional Recurrent Neural Network, trained on real-world data.
  Computational results on Mandl's benchmark and the large-scale Beijing network show that controlled PT line redesign yields substantial user-centric performance gains and operational cost reductions under high traffic fluctuations while limiting topological changes. On the Beijing network under high variability, average travel time improves by up to 25.8% while preserving over 85% line overlap. Unlike stop-skipping baselines, which break connectivity for many OD pairs, our redesign preserves full OD connectivity. These results support a shift from static planning toward continuous and adaptive PT network design.


## 精读解读（中文）
### 一、研究动机
传统公共交通线路设计通常基于名义交通条件优化，但实际运行中交通状况频繁偏离名义状态，导致性能显著下降。现有的应对机制多为跳站、中途折返等被动反应式干预，在较大或反复出现的交通波动下效果不足，且网络结构长期固定，难以应对持续变化。因此需要探索基于短期预测的结构性主动重构，以在高波动条件下维持运营者与乘客双方性能。

### 二、技术方案（Method）
提出预测-优化两阶段框架：首先利用扩散卷积循环神经网络（DCRNN）基于真实历史数据离线训练，在线接收最近时刻观测并输出未来一小时的路段旅行时间预测；同时构造该预测器误差的统计模型，以量化预测不准确对重构质量的影响。优化阶段采用基于NSGA-III的多目标进化算法，同时最小化用户出行时间、运营成本，并最大化重构网络与原网络的Jaccard边重叠度以限制拓扑改动；仅在预测条件严重偏离名义条件时触发重构，每小时周期运行，并提前一小时公布新线路，确保乘客全程路径有效。最终基于实现旅行时间评估重构网络的实际性能。

### 三、结果（Result）
在Mandl基准网络和北京大规模网络上，受控的线路重构在高交通波动场景下带来显著的用户出行时间改善和运营成本降低，同时限制拓扑变化。北京网络在高变异性下，平均出行时间最多改善25.8%，同时保持超过85%的线路重叠度；相比会破坏大量OD对连通性的跳站基线，所提重构方案保留了完整的OD连通性。静态一次性再优化也可获得11.4%的增益。

### 四、结论（Conclusion）
结果表明，在持续性高交通波动场景下，相比被动反应式控制或静态规划，基于预测的主动线路重构能够在大幅提升用户与运营者绩效的同时保持网络结构连续性，并维持OD完全连通。这支持公共交通网络设计从静态规划向连续自适应设计的范式转变。

### 五、方法论与关键技术细节
关键实现细节包括：使用DCRNN作为预测器并在真实数据上拟合其误差分布，以模拟预测误差影响；采用NSGA-III求解多目标优化，目标兼顾用户出行时间、运营成本和与原网络的Jaccard边重叠度；设定高Jaccard重叠约束（北京场景下保持85%以上）以保证运营可行性和避免过度结构变动；重构周期为一小时并提前一小时公告，假设最长出行短于一个时段；方法在Mandl基准和北京大规模网络上验证。局限性在于线路重构会影响车辆调度和司机排班，尤其对有人驾驶车辆；当前评估基于预测误差统计模型，且未讨论极端瞬时扰动下的适用性。
