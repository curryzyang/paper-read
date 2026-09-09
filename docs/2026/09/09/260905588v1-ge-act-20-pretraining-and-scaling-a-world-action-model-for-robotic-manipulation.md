# GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：AgiBot Research Team, Renhang Liu, Wenzhi Zhao, Zhuo Yang, Liliang Chen, Pengfei Zhou, Shengcong Chen, Guanghui Ren, Youlun Peng, Rongjun Jin, Nan Wang, Sukai Wang, Xindong He, Jinyuan Feng, Ziyu Xiong, Linqing Zhong, Yifei Wei, Feng Han, Long Zhang, Da Huang, Nanshu Zhao, Chenghao Yin, Mo Wu, Zhaodong Yan, Kongtao Hu, Yuxiang Yan, Aogelijiang Niyazi, Yu Fang, Jia Zeng, Lizhu Meng, Daizhen Lv, Haoyu Cao, Zhiwen Hou, Lianjin Ye, Yuehan Niu, Zhikai Cai, Xuan Hu, Hui Min, Xiongfeng Cai, Yue Liao, Jing Wu, Soujanya Poria, Ye Li, Sanping Zhou, Maoqing Yao
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05588v1) · [PDF](https://arxiv.org/pdf/2609.05588v1)

## TLDR
GE-Act 2.0 introduces a world-action model pretrained entirely from scratch on manipulation data—combining a control-oriented autoencoder, single-step visual planner, and inverse dynamics model with knowledge-aligned selective optimization—showing that scaling co-training data from 300 to 30,000 hours boosts zero-shot out-of-distribution success across 100 real-robot tasks and two embodiments without task-specific fine-tuning.

## Abstract
World-action models (WAM) predict future states to guide robot actions, enabling learning from both action-free video and action-labeled interaction. Most inherit pretrained video generators, leaving WAM pretraining and scaling underexplored. We introduce Genie Envisioner Act 2.0 (GE-Act 2.0), a world-action model whose trainable generative and action components are all initialized from scratch on manipulation data. It combines a control-oriented autoencoder (CoAE), a single-step visual planner (SVP), and an inverse dynamics model (IDM). CoAE retains action- and instruction-relevant information under aggressive compression, while SVP produces a complete future state in one differentiable pass, so visual planning and inverse dynamics can be pretrained separately on complementary data. The components are then jointly trained with knowledge-aligned selective optimization (KASO), which reduces mismatched supervision by selecting only predicted futures judged behaviorally compatible with the recorded action. We evaluate pretrained checkpoints directly, without per-task fine-tuning, on 100 tasks across 20 manipulation skill groups with held-out scenes, backgrounds, lighting, and object instances. Scaling co-training data from 300 to 30,000 hours raises success from 17.1% to 44.1% on G1-OP and from 13.4% to 31.1% on G2-90D; despite comprising less than 2% of the co-training data, G2-90D improves by 17.7 points, suggesting cross-embodiment transfer. Gains span 19/20 and 18/20 skill groups, and skill-specific coverage strongly correlates with zero-shot out-of-distribution (OOD) success (Pearson r=0.80; Spearman rho=0.85). Under the same protocol, the model grounds object, color, shape, and position references in at least 90% of trials and follows explicit instructions even when they conflict with an already-committed behavior or a conventional scene association.


## 精读解读（中文）
### 一、研究动机
现有世界动作模型大多直接继承预训练视频生成器，其自身的预训练与扩展规律尚未得到充分探索。GE-Act 2.0旨在回答两个系统级问题：如何在操作数据上从零预训练视觉生成与逆动力学组件，以及当所有可训练生成与动作组件均随机初始化时，世界动作模型的能力如何随操作数据规模扩展。

### 二、技术方案（Method）
GE-Act 2.0采用解耦的两阶段架构，包含控制导向自编码器CoAE、单步视觉规划器SVP和逆动力学模型IDM。CoAE通过重建与多教师特征对齐学习被激进压缩的潜在空间，保留动作与指令相关信息；SVP以单次可微的flow生成器前向过程直接产生完整未来状态，因此SVP可在无动作视频上单独预训练，IDM可在无指令轨迹上单独预训练；随后将两者端到端联合训练，并使用知识对齐选择性优化KASO，采样多个预测未来后仅选择被当前IDM判定为与记录动作行为兼容的候选进行动作监督，以缓解预测模式与演示动作不一致造成的监督失配。

### 三、结果（Result）
将共训练数据从300小时扩展到30000小时，零样本OOD成功率在G1-OP上从17.1%提升至44.1%，在G2-90D上从13.4%提升至31.1%；G2-90D在全部共训练数据中占比不足2%却提升17.7个百分点，表明存在跨本体迁移。增益覆盖了20个技能组中的19个和18个；技能覆盖度与零样本OOD成功率强相关（Pearson r=0.80，Spearman rho=0.85）。在相同零样本OOD协议下，模型对物体、颜色、形状和位置参照的指令遵循在至少90%的试验中正确，并且能在指令与已承诺行为或常规场景关联冲突时遵循显式指令。

### 四、结论（Conclusion）
从零预训练并扩展世界动作模型是可行且有效的，无需任务级微调即可获得跨任务与跨本体的零样本OOD操作能力提升，且这种能力与训练数据中技能覆盖程度密切相关。GE-Act 2.0的组件解耦设计使视觉生成和逆动力学能够分别利用互补数据，而KASO进一步提升了联合训练中预测未来与真实动作的一致性。

### 五、方法论与关键技术细节
关键细节包括：CoAE在极低码率下通过重建和多教师特征对齐保留动作与指令信息，相比基线自编码器能更好支持动作探针预测；SVP采用MeanFlow/改进MeanFlow风格的训练思路，以单网络前向覆盖完整噪声区间，从而避免多步生成带来的预训练成本；IDM以当前视觉潜在和预测未来视觉潜在及本体感受为输入，同时预测稠密动作块和稀疏远视动作序列；KASO通过best-of-K选择缓解多模态任务中生成未来与记录动作的模式失配；所有组件均从随机初始化开始，在39,000/32,000小时规模的互补数据上预训练后联合训练；评估协议固定为100个真实机器人任务、20个操作技能组，且不进行任何任务或本体微调，在未见场景、背景、光照和目标实例上进行；结果也暗示稀采样本体的性能可受益于大规模主体语料的跨本体迁移。
