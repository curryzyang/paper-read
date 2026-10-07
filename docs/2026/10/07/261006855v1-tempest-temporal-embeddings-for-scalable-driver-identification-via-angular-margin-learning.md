# TEMPEST: Temporal Embeddings for Scalable Driver Identification via Angular Margin Learning

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Kyle Musgrove, Dylan B. Lewis, Sarah Powers, Emma J. Reid, Hector Santos-Villalobos
- 机构：Oak Ridge National Laboratory, The University of Tennessee, Knoxville
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06855v1) · [PDF](https://arxiv.org/pdf/2610.06855v1)

## TLDR
TEMPEST is a Temporal Convolutional Network embedding model trained with an ArcFace angular margin loss that maps 60-second multimodal driving windows to compact embeddings for scalable, retraining-free driver identification, achieving strong accuracy and markedly better scaling than triplet-loss baselines.

## Abstract
Scalable driver identification requires embedding models that maintain discriminative performance as fleet size grows, yet existing triplet-loss formulations degrade rapidly with driver pool size and overfit to session-specific patterns under rigorous temporal evaluation. We introduce TEMPEST, a Temporal Convolutional Network embedding model trained with an additive angular margin (ArcFace) loss that enforces global class-level separation in a normalized angular space. TEMPEST maps 60-second multimodal driving windows to compact 96-dimensional embeddings, supporting truly dynamic enrollment without any retraining or classifier refitting. Under rigorous temporal evaluation on a 45-driver dataset, TEMPEST achieves 91.71% Rank-1 accuracy, outperforming the best classical model by 17.9 pp and the strongest triplet-loss baseline by 58.4 pp. TEMPEST degrades by only 4.3 pp when growing the subject pool from 10 to 45 drivers, compared to 22 pp and 32.5 pp for supervised and unsupervised triplet-loss baselines, and its cross-session advantage is corroborated on the public KIA Soul dataset, where it outperforms the best classical model by 7.3 pp within-session and 14.3 pp cross-session. With 720K parameters, a 2.80 MB footprint, and 50-epoch convergence, TEMPEST establishes a rigorous, reproducible baseline for scalable behavioral driver biometric identification.


## 精读解读（中文）
### 一、研究动机
可扩展的驾驶员识别要求嵌入模型在车队规模增长时仍保持判别力，但现有 triplet-loss 方法随驾驶员池增大迅速退化，并在严格时间评估下过拟合会话特异模式。TEMPEST 用加性角边距学习在归一化角空间中强制全局类别级分离，以解决局部成对约束带来的不稳定与可扩展性差问题。

### 二、技术方案（Method）
TEMPEST 以 60 秒多模态驾驶窗口为输入，基于 ORNL DriverID 等数据预处理为 1 Hz、19 个行为特征，送入 TCN 编码器：单块 B=1、5 层 L=5 指数膨胀因果卷积，核大小 k=3，每层含膨胀 1D 卷积、批归一化、ELU 与 dropout，并有 1x1 残差投影；时间轴自适应平均池化后经全连接投影到 96 维并做 L2 归一化。训练用 ArcFace 损失，基于归一化嵌入与类权重余弦相似度加入角度 margin，m=0.21 rad、s=20.25 由 Optuna 在训练集验证子集上选择；推理冻结编码器，TEMPEST-Raw 用余弦最近邻检索，TEMPEST-SVM 用 RBF SVM（C=1.0）作分类头，支持动态注册而无需重训练或分类器重拟合。

### 三、结果（Result）
在 45 驾驶员 DriverID 严格时间评估中，TEMPEST 取得 91.71% Rank-1 准确率，比最佳经典模型高 17.9 个百分点，比最强 triplet-loss 基线高 58.4 个百分点；从 10 增至 45 名驾驶员仅下降 4.3 个百分点，而监督与非监督 triplet-loss 基线分别下降 22 和 32.5 个百分点。在公开 KIA Soul 数据集上，TEMPEST 比最佳经典模型在 within-session 高 7.3 个百分点、cross-session 高 14.3 个百分点；随机 10 折交叉验证因时间泄漏接近 99%，但按时间或跨会话划分后性能显著下降。模型仅 720K 参数、2.80 MB 占用，约 50 个 epoch 收敛。

### 四、结论（Conclusion）
TEMPEST 将角边距学习引入行为驾驶员生物识别，证明全局类别级角分离比局部 triplet 约束更可扩展且跨会话更稳健。其嵌入可直接用于余弦相似度匹配，实现免训练动态注册，为可扩展、可复现的驾驶员识别建立了严格基线。

### 五、方法论与关键技术细节
关键实现细节包括：DriverID 由 45 名驾驶员组成（G1 15、G2 14、G3 16），原始 816 个特征经滤波、1 Hz 重采样并移除车辆状态信号后保留 19 个行为特征；KIA Soul 含 10 名驾驶员、4 个会话、54 个特征中常用 15 个，采用 Leave-One-Drive-Out 跨会话划分。损失使用 L2 归一化嵌入与 L2 归一化类权重的余弦相似度，ArcFace 的 m=0.21 rad、s=20.25，编码器为 5 层膨胀卷积、核大小 3、膨胀率 2^l、单块 B=1、96 维嵌入，SVM 为默认 RBF 核且 C=1.0。DriverID 上深度学习模型跑 10 个随机种子而经典模型单次运行；主要局限是数据集与驾驶员规模有限，且随机划分可因时序泄漏将准确率膨胀最多约 80 个百分点，必须用时间或跨会话协议评估。
