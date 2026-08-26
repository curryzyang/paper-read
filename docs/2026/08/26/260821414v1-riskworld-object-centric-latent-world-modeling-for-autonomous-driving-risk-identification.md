# RiskWorld: Object-Centric Latent World Modeling for Autonomous Driving Risk Identification

- 区域：精读区
- 排名：2
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Jingzheng Li, Yufei Ge, Qianren Mao, Zhijun Chen, Bing Li, Xingyu Peng, Baochang Zhang, Xianglong Liu
- 机构：Hong Kong Polytechnic University, Nanyang Technological University, Zhongguancun Laboratory, Beihang University, Tianjin University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21414v1) · [PDF](https://arxiv.org/pdf/2608.21414v1)

## TLDR
RiskWorld is an object-centric latent world model that identifies safety-critical objects in autonomous driving by rolling forward imagined ego-object relations via RSSM-style latent dynamics, achieving state-of-the-art risk localization performance on RiskBench.

## Abstract
Autonomous driving risk identification aims to determine which observed object is likely to become safety-critical to the ego vehicle. Existing approaches typically predict scene-level accidents, infer risk objects indirectly from ego behavior, or apply geometric checks after trajectory forecasting, without directly using predicted ego--object relations for risk-source localization. We propose RiskWorld, an object-centric latent world model that identifies risk from the imagined evolution of each candidate relative to the ego vehicle. RiskWorld combines pretrained predictive video representations with structured ego--object histories, contextualizes observed interactions, and rolls relation-aware object states into the future using RSSM-style latent dynamics. It decodes the rollout into object-level risk scores, supported by auxiliary future-relation and temporal-risk predictions. Inference uses only observations up to the current time, while logged futures provide training supervision. On RiskBench, RiskWorld achieves the best overall F1 of 63.0\% and the lowest false-alarm rate of 2.1\%. Further analyses show that the learned rollout captures the evolution of object-level risk before critical events, while RiskWorld's selections preserve planning-critical information under filtered observation.


## 精读解读（中文）
### 一、研究动机
现有驾驶风险识别方法通常预测场景级事故、从自车行为间接推断风险对象，或在轨迹预测后进行几何检查，未直接利用预测的自我-对象关系来定位风险源。本文提出将对象级风险识别视为未来自我-对象关系的演变预测，直接利用关系演化作为风险源定位的证据。

### 二、技术方案（Method）
RiskWorld采用对象中心潜在世界模型。输入为K帧前视RGB、对象轨迹与自车运动；冻结的V-JEPA2编码器提取全局场景特征与对象对齐特征，MLP和掩码GRU编码结构化对象状态与自车状态，融合后经掩码多头自注意力（RelAttn）建模对象间与自我-对象交互，得到关系感知对象token。随后使用RSSM式潜在动力学（确定GRU+随机状态）将每个对象token滚动H步，后验在观测边界初始化，未来仅用先验递归预测，并施加KL正则化。解码时逐步骤头输出未来相对位置、距离和时态风险概率，池化未来状态得到对象级风险分数；最小距离和碰撞时间从轨迹导出。训练联合优化对象级风险BCE、未来关系回归（位置/距离/最小距离）、时态风险曲线BCE和KL损失，未来标注仅提供训练监督。

### 三、结果（Result）
在RiskBench上，RiskWorld取得最佳总体F1为63.0%，比最强基线提升1.2个百分点，同时获得最低误报率（FA）2.1%。进一步分析表明，学习的潜在rollout能捕捉关键事件前对象级风险演化，且在过滤观测下RiskWorld的选取仍保留规划关键信息。

### 四、结论（Conclusion）
RiskWorld通过对象中心潜在世界模型直接预测未来自我-对象关系，有效提升对象级风险识别性能，说明将风险视为关系演变的构想在自动驾驶风险监测中具有优势。

### 五、方法论与关键技术细节
关键实现细节包括：使用冻结的V-JEPA2预训练视频特征提供上下文，结构化状态编码保留明确的自车坐标、运动、框和类别；RSSM潜在动力学采用后验-先验KL正则化（β权重）稳定初始化；损失包含类平衡BCE（λ_obj, λ_curve）、平滑L1回归（λ_xy, λ_dist, λ_min），时间风险曲线采用指数衰减（时间常数T）并对事件区间赋值；推理时用后验均值初始化后仅用先验均值滚动；时间风险通过预测曲线阈值γ_ttr得到。模型对每个对象独立滚动，动力学参数在各候选间共享，复杂度与候选数线性相关。局限性在于论文未明确讨论，但推理不依赖未来标注，训练需成对的当前历史与未来标注。
