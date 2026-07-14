# Mitigating Early Training Collapse in CTR Models

- 区域：精读区
- 排名：8
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Ergun Biçici, Erkan Çetinyamaç
- 机构：Huawei Türkiye R&D Center
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09696v1) · [PDF](https://arxiv.org/pdf/2607.09696v1)

## TLDR
This paper shows that early training collapse in click-through rate prediction models is primarily caused by feature sparsity, and mitigating it through sparse feature removal and value aggregation stabilizes training and improves performance.

## Abstract
Deep neural models for click-through rate prediction often exhibit a sharp decline in validation performance immediately after the first training epoch despite continued improvement in training loss. This instability restricts effective learning and limits model performance. In this study, we analyze this behavior using large-scale industrial datasets and evaluate practical mitigation strategies. While reducing the learning rate provides only incremental gains, controlling feature sparsity yields substantial improvements. Removing highly sparse features and aggregating infrequent feature values stabilizes training, extends useful learning beyond a single epoch, and improves both offline evaluation metrics and online system performance.


## 精读解读（中文）
### 一、研究动机
CTR模型在第一个训练epoch后验证性能急剧下降，尽管训练损失持续改善，这种不稳定限制了有效学习。需要分析原因并寻找实用的缓解策略以提升模型性能。

### 二、技术方案（Method）
使用大规模工业CTR数据集（数百亿样本、强类别不平衡）进行实验。输入为高基数类别特征，采用嵌入层表示。评估三种策略：1)降低学习率；2)移除高稀疏特征（剔除信号弱的高基数特征）；3)值过滤（保留高频值，将低频值映射到共享token）。训练采用Adam优化器，离线评估AUC、Logloss和PRAUC，在线部署评估TAV、RPM、eCPM、CVR。

### 三、结果（Result）
降低学习率仅带来AUC提升+0.15%；移除稀疏特征提升最大（AUC+0.33%）；值过滤提升+0.04% AUC。在线实验中，总广告价值（TAV）提升1.88%，RPM提升4.08%，eCPM提升1.89%，CVR提升3.48%。

### 四、结论（Conclusion）
早期训练崩溃主要由特征稀疏性驱动，而非仅是优化动态问题。减少特征空间复杂度（移除稀疏特征、聚合稀有值）能显著改善泛化，实现稳定多epoch训练，且方法简单有效，兼容现有系统。

### 五、方法论与关键技术细节
使用工业级大规模CTR数据集，特征呈长尾分布，高基数稀疏特征导致嵌入参数更新不稳定，Adam优化器加速收敛但加剧噪声拟合。主要方法为移除稀疏特征和值过滤（如设置频率阈值），降低学习率效果有限。离线提升幅度较小但稳定，在线指标提升显著。局限性：未探讨其他正则化或模型容量调整，且特征选择阈值需实际调优。
