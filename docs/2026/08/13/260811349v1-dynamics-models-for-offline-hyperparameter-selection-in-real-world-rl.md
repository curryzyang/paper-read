# Dynamics Models for Offline Hyperparameter Selection in Real-World RL

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Jordan Coblin, Han Wang, Martha White, Adam White
- 机构：Alberta Machine Intelligence Institute (Amii), University of Alberta
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11349v1) · [PDF](https://arxiv.org/pdf/2608.11349v1)

## TLDR
This paper presents the first real-world industrial application of offline calibration models for reinforcement learning hyperparameter selection at a municipal water treatment plant, demonstrating that these models can generate realistic rollouts and recover hyperparameter sensitivity trends.

## Abstract
A key obstacle to deploying reinforcement learning in real-world systems is hyperparameter selection, particularly when simulators are unavailable and online experimentation is costly. Prior work has proposed calibration models trained on offline data to approximate environment dynamics and enable offline hyperparameter selection, but these methods have so far been evaluated only in simple simulated settings. In this paper, we present the first application of calibration models in a real-world industrial setting: a municipal water treatment plant. We evaluate several calibration model approaches, including a k-nearest neighbors model with a Laplacian distance metric, on high-dimensional, non-stationary sensor data for nexting prediction tasks. Our results show that these models can generate realistic long-horizon rollouts and recover meaningful hyperparameter sensitivity trends. We further examine how calibration models scale to year-long datasets, how they support the selection of fine-tuning learning rates for pre-trained agents, and how robust they are under distribution shift. Overall, our findings provide a proof of concept for using offline dynamics models to support RL deployment in real-world environments, while highlighting important practical challenges for future work.


## 精读解读（中文）
### 一、研究动机
强化学习在真实工业系统中部署的关键障碍是超参数选择，尤其是在没有仿真器且在线实验成本高昂的情况下。现有校准模型方法仅在简单模拟环境中验证，未在真实工业场景中测试，因此需要探索其在真实世界中的应用效果与挑战。

### 二、技术方案（Method）
本文首次将校准模型用于真实工业场景——加拿大Drayton Valley市政水处理厂，基于超过两年的480通道传感器数据（采样1Hz），经预处理后得到142维特征向量，选取膜压力、进水温度和浊度三个关键传感器作为预测目标。采用四种校准模型：LOBO欧氏kNN集成、LOBO拉普拉斯kNN集成、前馈神经网络和门控循环单元网络；kNN模型使用Laplacian距离度量并采用留一块交叉验证的集成策略，以最差排序聚合结果。任务为nexting预测，即预测传感器信号的折扣未来和（GVF），超参数选择通过TD(0)预测器的学习率扫描完成，先在模型上训练评估，再与在线数据重放（Online）的参考曲线对比，同时用动态时间规整评估轨迹对齐质量。

### 三、结果（Result）
在30k步长期 rollout 中，kNN模型生成的传感器轨迹更接近真实数据，其中Laplacian kNN在膜压力上表现更好；NN和GRU基线在50-100步后趋向崩溃。在学习率敏感性曲线上，欧氏kNN在多个传感器上最接近Online曲线，Laplacian kNN次之，而NN和GRU无法恢复正确的超参数排序，验证了非参数模型在超参数选择中的优势。

### 四、结论（Conclusion）
离线动力学模型（校准模型）在真实工业场景中可以作为离线超参数选择的有效工具，能够生成逼真的长期轨迹并保持超参数敏感性，为RL在真实环境中的部署提供了概念验证，同时揭示了规模化、分布漂移和模型选择等实际挑战。

### 五、方法论与关键技术细节
关键细节包括：数据规模为一年以上（超大规模实验）和高维非平稳传感器数据；kNN模型通过Laplacian表示避免外推，LOBO集成用最差排序提供保守估计；评估使用NRMSE和动态时间规整（四种步模式）衡量轨迹相似性；TD(0)预测器使用Adam学习率扫描，对比模型与在线重放数据；局限性包括拉普拉斯表示仅针对单一传感器调优、部分传感器rollout质量较差、点式误差难以解释轨迹相位差异，以及模型在分布漂移下的鲁棒性仍需进一步验证。
