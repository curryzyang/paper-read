# A Granularity-Aware EEG Feature Framework for Psychopathology Dimension Prediction

- 区域：精读区
- 排名：10
- 匹配度：1.5/10
- 来源：arxiv
- 作者：Haofan Cheng, Jingjing Hu, Jingrong Pei, Shuaiqi Fu, Meilun Shen, Shuai Fang, Meng Wang, Dan Guo, Jie Zhang
- 机构：Hefei University of Technology, The Fourth Military Medical University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02670v1) · [PDF](https://arxiv.org/pdf/2607.02670v1)

## TLDR
This paper proposes a granularity-aware EEG feature pipeline that organizes multi-scale descriptors into global, regional, and channel levels, demonstrating that such balanced feature selection can modestly improve prediction of dimensional psychopathology across multiple paradigms despite weak signal strength.

## Abstract
Electroencephalography (EEG) offers a noninvasive approach for examining neurophysiological correlates of dimensional psychopathology, yet systematic evidence across EEG paradigms and feature granularities remains limited. Here, we develop a granularity-aware EEG feature pipeline that organizes multi-scale descriptors into global, regional, and channel levels. Using the Healthy Brain Network (HBN) cohort, we evaluate the prediction of four psychopathology dimensions: p-factor, internalizing, externalizing, and attention problems, across four EEG paradigms. Given the heterogeneity of pediatric psychopathology and the moderate reliability of questionnaire-derived scores, this setting represents a challenging feasibility test rather than a clinical screening scenario. Tree-based models and granularity-balanced feature selection showed promising improvements over conventional approaches in selected conditions, although effect sizes remained modest. Visualization of selected markers revealed dimension-specific spatial and spectral patterns that were broadly aligned with existing neurophysiological knowledge. An exploratory cross-dataset sanity check on the independent PEARL cohort suggested that the proposed selection principle remains technically feasible under protocol shifts, without claiming cross-dataset generalizability. Overall, multi-scale EEG features contain weak but detectable signals related to dimensional psychopathology, and granularity-aware selection may serve as a useful feature-reduction strategy for future EEG-based phenotyping studies.


## 精读解读（中文）
### 一、研究动机
现有EEG精神病理学预测研究多聚焦单一症状域或任务范式，缺乏跨多范式和多维度的系统评估；同时，特征提取常忽略空间粒度差异，导致高维通道特征在扁平化选择中主导结果，抑制了全局和区域特征中潜在的稳定信号。本研究旨在建立一种粒度感知的EEG特征框架，通过独立分配每个空间粒度的特征预算来平衡多尺度信息，从而提升维度精神病理学预测的可解释性与性能。

### 二、技术方案（Method）
本研究基于Healthy Brain Network (HBN) 数据集（约2600名5-21岁参与者），采用四个EEG范式（静息态闭眼/睁眼、电影观看、环绕抑制），对每个范式提取三类粒度特征：全局（28维，如微状态动力学）、区域（400维，如区域谱功率和连通性）、通道（3096维，如谱功率、微分熵、非周期性参数等），每个epoch的特征再通过均值、标准差、中位数聚合为10572维特征矩阵。以Child Behavior Checklist (CBCL) 导出的四个精神病理学维度（p因子、内化、外化、注意问题）为预测目标（极端分位数30/70变换为二分类标签）。核心方法为粒度感知稳定性特征选择（GSTS），对每个粒度独立执行稳定性选择（特征预算约束），并与跨任务模型族筛选（CMFS）结合，在fold-contained嵌套交叉验证中评估Logistic回归、弹性网络、线性SVM、随机森林、XGBoost等模型。此外，在独立PEARL数据集上进行探索性跨数据集验证。

### 三、结果（Result）
树模型（随机森林、XGBoost）和粒度平衡特征选择在特定条件下（如闭眼静息态和电影观看范式）优于常规扁平化特征选择，但整体效应量适中。可视化分析显示，所选特征呈现维度特异性空间和光谱模式，与现有神经生理学知识（如注意问题与前额叶θ/β比相关）广泛一致。跨数据集检查表明，GSTS选择原则在协议变化下仍可技术可行，但未断言跨数据集泛化性。总体而言，多尺度EEG特征对维度精神病理学包含弱但可检测的预测信号。

### 四、结论（Conclusion）
多尺度EEG特征能够捕获与维度精神病理学相关的微弱但可检测的神经生理信号；粒度感知稳定性选择（GSTS）通过平衡各空间粒度的特征贡献，可作为未来基于EEG的表型研究中有用的特征降维策略，尤其适用于大规模儿科人群。

### 五、方法论与关键技术细节
数据来源：HBN（V2版本，1-11次发布）含2575-2592名受试者（依范式不同），EEG为129通道，100Hz重采样，4秒epoch；PEARL数据集用于探索性验证。特征组成：28全局、400区域、3096通道概念特征，经均值/标准差/中位数聚合得10572维；关键模块包括微状态动力学、区域偏侧性、相干/PLV连通性、滑动窗口动态等。模型策略：fold-contained嵌套交叉验证确保无偏泛化估计；特征选择使用稳定性选择（Stability Selection）并在每种粒度设定独立预算K_g，避免高维通道特征主导。局限性：预测效应量较小，目标维度来自问卷（CBCL），不可直接类比临床诊断；跨数据集仅作技术可行性检查，未验证泛化性。
