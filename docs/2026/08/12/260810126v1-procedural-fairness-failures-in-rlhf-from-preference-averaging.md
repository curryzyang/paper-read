# Procedural Fairness Failures in RLHF from Preference Averaging

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：M P V S Gopinadh, Karthik Kamuju, Kummari Avinash, John Joshua, Srinivasa Raju Rudraraju
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10126v1) · [PDF](https://arxiv.org/pdf/2608.10126v1)

## TLDR
Standard RLHF's preference averaging causes procedural fairness failures that systematically under-represent minority preference groups, and the proposed Preference-Aware RLHF (PA-RLHF), which separates reward learning across preference modes, substantially improves both alignment accuracy and fairness.

## Abstract
Reinforcement Learning from Human Feedback (RLHF) aggregates heterogeneous preferences into a single reward model, assuming preference homogeneity. When preferences are heterogeneous, this aggregation induces a procedural fairness failure where majority preference groups dominate reward learning while minority preferences are systematically under-represented. This work defines procedural fairness in alignment as preserving distinct preference signals during reward modeling and shows that standard RLHF violates this via preference averaging. Preference-Aware RLHF (PA-RLHF) is introduced, separating optimization across preference modes at the reward learning stage. In a controlled setting, PA-RLHF improves overall alignment accuracy from 46.9% to 67.9% and reduces the fairness gap between best and worst aligned groups from 15.9 to 9.6 percentage points. These results show that procedural fairness failures in alignment can arise from structural design choices in reward learning, even in controlled, noise-free settings, with direct implications for large language models and agentic systems, where biased reward models can compound inequities across sequential decisions.


## 精读解读（中文）
### 一、研究动机
标准RLHF将异构的人类偏好聚合为单一奖励模型，隐含假设偏好同质；当偏好异构时，这种平均化会导致程序公平性失败，多数偏好群体主导奖励学习，少数偏好被系统性忽略。本文旨在揭示并解决这一结构性问题。

### 二、技术方案（Method）
提出偏好感知RLHF（PA-RLHF）：在奖励学习阶段不进行偏好平均，而是先将异构偏好数据按潜在偏好模式分组，为每个模式分别训练独立的奖励模型；然后在策略优化阶段，结合各模式奖励模型进行优化，例如采用多目标或加权融合方式，使不同偏好信号在奖励建模中都被保留。整体流程包括：收集多偏好对比数据、估计偏好模式归属、训练分模式奖励模型、基于分离的奖励信号优化策略。

### 三、结果（Result）
在受控无噪声设置下，PA-RLHF将整体对齐准确率从46.9%提升到67.9%，同时将最好与最差对齐群体间的公平性差距从15.9个百分点降至9.6个百分点，表明分离偏好建模能显著改善程序公平性。

### 四、结论（Conclusion）
对齐中的程序公平性失败可能源于奖励学习的结构性设计选择，而非仅由噪声或数据偏差造成；PA-RLHF通过保留偏好异质性，在提升整体对齐表现的同时减少群体间差距，对大规模语言模型和智能体系统的公平性具有直接启示。

### 五、方法论与关键技术细节
关键细节包括：偏好模式的数量需要预先设定或通过聚类决定；每个模式的奖励模型独立训练，避免了平均化；评测使用受控合成偏好数据，无标注噪声；公平性定义为最好与最差群体对齐准确率之差；PA-RLHF需要额外的模式分配和多个奖励模型存储，计算开销高于标准RLHF；方法在偏好模式重叠或模式数量不确定时的鲁棒性尚待验证，且对真实LLM场景的扩展仍需进一步研究。
