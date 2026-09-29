# Grounding Vision-Language Models in Driving Semantics: A Multi-Dataset Predicate Framework for Explainable Reasoning

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Mohamed Chouai, Fazli Faruk Okumus, Stefan Kugele
- 机构：Technische Hochschule Ingolstadt
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31636v1) · [PDF](https://arxiv.org/pdf/2609.31636v1)

## TLDR
This paper introduces a deterministic multi-dataset predicate framework that transforms measurable driving-scene evidence into a shared Predicate Knowledge Graph to ground and explain vision-language model reasoning, achieving high cross-dataset semantic validation (macro F1 of 0.94 on nuPlan and 0.93 on nuScenes) and improved accuracy on most NuPlanQA subtasks.

## Abstract
Vision-language models are increasingly used for driving-scene understanding, yet the semantic relations expressed in their outputs are often difficult to verify against the underlying traffic situation. This paper introduces a deterministic multi-dataset predicate framework that derives driving-scene semantics from measurable geometric, kinematic, temporal, map, and traffic-control evidence. Dataset-specific interfaces are used only to recover the required scene information, while predicate definitions remain unchanged across nuPlan and nuScenes and are materialised in a common Predicate Knowledge Graph. Quantitative semantic validation against manually annotated predicate relations on 200 scenarios from each dataset yields macro F1 scores of 0.94 on nuPlan and 0.93 on nuScenes, with an average cross-dataset difference of 0.02 across the shared predicates. The Predicate KG is further evaluated using a frozen LLaVA-OneVision-7B model on the nine NuPlanQA subtasks. Predicate grounding achieves the highest accuracy among the evaluated visual-input conditions in seven of nine NuPlanQA subtasks, including Traffic Light (53.2% to 71.5%), Situation Assessment (76.2% to 86.1%), and Action Recommendation (82.9% to 89.0%). Weather/Lighting remains essentially unchanged (89.4% vs. 88.8%), consistent with the absence of corresponding predicates, while Predicate KG only input outperforms metadata-only input in eight of nine subtasks. The results show that deterministic predicates provide a consistent and traceable semantic representation and, under oracle grounding, can reduce visual dependence for reasoning tasks covered by the predicate vocabulary.


## 精读解读（中文）
### 一、研究动机
视觉语言模型在驾驶场景理解中常输出难以与真实交通态势核验的语义关系，而现有本体、知识图谱与场景图多面向特定数据集或任务，缺乏显式可复现的操作定义。该工作旨在构建跨nuPlan与nuScenes的确定性谓词框架，使驾驶语义可从几何、运动学、时序、地图和交通控制证据中推导并追溯。

### 二、技术方案（Method）
框架为每个时间步通过数据集专用接口提取智能体位置、朝向、速度、包围盒及地图或交通控制信息，但谓词定义保持一致；每个谓词表示为在特定时间窗内对可测证据执行布尔函数并应用固定阈值，空间关系在参考车局部坐标系中计算，crossesInFrontOf用前向射线求交且前向范围L=10m，跟驰、碰撞风险和换道安全阈值依据UN R157，交通信号拆分为controls、hasSignalState、isRelevantSignal等谓词。派生断言以subject-predicate-object-time-provenance形式物化到Predicate KG，并用于冻结的LLaVA-OneVision-7B在NuPlanQA九个子任务上的grounding评估。

### 三、结果（Result）
在nuPlan与nuScenes各200个场景上对人工标注谓词关系验证，宏F1分别为0.94与0.93，共享谓词跨数据集平均差异0.02。Predicate grounding在九项NuPlanQA子任务的七项中取得视觉输入条件下的最高准确率，包括Traffic Light从53.2%到71.5%、Situation Assessment从76.2%到86.1%、Action Recommendation从82.9%到89.0%；Weather或Lighting基本不变（89.4% vs 88.8%），与缺少对应谓词一致；仅Predicate KG输入在九项中八项优于仅metadata输入。

### 四、结论（Conclusion）
确定性谓词能为异构驾驶数据集提供一致、可追溯的语义表示，并在oracle grounding下对谓词词汇覆盖的推理任务减少视觉依赖。该框架可作为原始驾驶数据与VLM语言推理之间的数据集无关语义接口，但跨数据集一致性仍依赖各数据集接口可恢复所需证据，且未覆盖的语义维度不会从谓词中获益。

### 五、方法论与关键技术细节
谓词体系覆盖空间、运动、时序、地图、交互、交通控制和风险等家族，区分直接暴露量与需推导关系；安全阈值来自UN R157，包括跟驰时间间隔、5m/s²紧急碰撞制动、换道3.0m/s²与1.0s距离约束，地图谓词考虑车辆足迹而非仅中心点。验证仅重点评估推导谓词，每个数据集200场景人工标注；实现规模示例为41帧nuPlan场景741,311条物化断言约18,081条每帧，单帧含89个动态实体节点、4,752条语义边和21,357条断言；主要局限包括oracle grounding、谓词词汇覆盖有限以及数据集专用接口依赖。
