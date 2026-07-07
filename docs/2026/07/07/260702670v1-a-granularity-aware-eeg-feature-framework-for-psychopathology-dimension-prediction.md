# A Granularity-Aware EEG Feature Framework for Psychopathology Dimension Prediction

- 区域：精读区
- 排名：10
- 匹配度：1.5/10
- 来源：arxiv
- 作者：Haofan Cheng, Jingjing Hu, Jingrong Pei, Shuaiqi Fu, Meilun Shen, Shuai Fang, Meng Wang, Dan Guo, Jie Zhang
- 机构：The Fourth Military Medical University, Hefei University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02670v1) · [PDF](https://arxiv.org/pdf/2607.02670v1)

## TLDR
This paper proposes a granularity-aware EEG feature framework that organizes multi-scale descriptors into global, regional, and channel levels to predict dimensional psychopathology, demonstrating that multi-scale features contain weak but detectable signals and that granularity-aware selection is a useful feature-reduction strategy.

## Abstract
Electroencephalography (EEG) offers a noninvasive approach for examining neurophysiological correlates of dimensional psychopathology, yet systematic evidence across EEG paradigms and feature granularities remains limited. Here, we develop a granularity-aware EEG feature pipeline that organizes multi-scale descriptors into global, regional, and channel levels. Using the Healthy Brain Network (HBN) cohort, we evaluate the prediction of four psychopathology dimensions: p-factor, internalizing, externalizing, and attention problems, across four EEG paradigms. Given the heterogeneity of pediatric psychopathology and the moderate reliability of questionnaire-derived scores, this setting represents a challenging feasibility test rather than a clinical screening scenario. Tree-based models and granularity-balanced feature selection showed promising improvements over conventional approaches in selected conditions, although effect sizes remained modest. Visualization of selected markers revealed dimension-specific spatial and spectral patterns that were broadly aligned with existing neurophysiological knowledge. An exploratory cross-dataset sanity check on the independent PEARL cohort suggested that the proposed selection principle remains technically feasible under protocol shifts, without claiming cross-dataset generalizability. Overall, multi-scale EEG features contain weak but detectable signals related to dimensional psychopathology, and granularity-aware selection may serve as a useful feature-reduction strategy for future EEG-based phenotyping studies.

## 精读解读（中文）

### 一、研究动机
现有研究缺乏跨EEG范式和特征粒度的系统性证据，且传统特征选择方法可能使高维通道特征主导，抑制全局和区域特征的表现。因此，本文提出一种粒度感知的EEG特征框架，旨在平衡多尺度特征以预测精神病理学维度。

### 二、技术方案（Method）
基于HBN队列（约2600名参与者，年龄5-21岁）的四个EEG范式（闭眼静息、睁眼静息、电影观看、环绕抑制），提取多尺度特征并组织为全局（28个）、区域（400个）和通道（3096个）三个粒度级别，每种特征通过均值、标准差和中位数聚合，最终得到10572维特征矩阵。采用树模型（随机森林、XGBoost等）和粒度平衡的稳定性特征选择（GSTS），在折叠内嵌套交叉验证中进行模型筛选、特征选择、超参数调优和消融分析，确保无偏泛化估计。

### 三、结果（Result）
在选定条件下，树模型和GSTS相比传统方法表现出适度提升，效应量适中；可视化显示维度特异性的空间和频谱模式与现有神经生理知识大致一致。跨数据集（PEARL）的探索性检查表明该选择原则在协议变化下仍技术可行，但未声称跨数据集泛化性。

### 四、结论（Conclusion）
多尺度EEG特征包含与维度精神病理学相关的弱但可检测信号，粒度感知的平衡特征选择可作为未来基于EEG的表型研究中有效的特征降维策略，尽管当前效应量有限，不适用于临床筛查。

### 五、方法论与关键技术细节
数据来自HBN队列的四个范式，每个参与者有部分重叠；特征包括频谱功率、带功率比、微分熵、非周期活动、复杂度、微状态动力学、区域不对称性、连通性和时间动态；采用树模型家族和GSTS进行粒度平衡选择；评估为二分类任务（极端分位数转换），效应量微弱；局限性包括目标变量来自问卷（中等信度）和表现仅作为可行性测试，跨数据集泛化未正式验证。

