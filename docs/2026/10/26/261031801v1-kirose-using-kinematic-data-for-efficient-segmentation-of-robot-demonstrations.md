# KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations

- 区域：精读区
- 排名：8
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Shuangyu Xie, Kaiyuan Chen, Muhammad Zubair Irshad, Richard Cheng, Sergey Zakharov, Ken Goldberg
- 机构：Toyota Research Institute, University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31801v1) · [PDF](https://arxiv.org/pdf/2610.31801v1)

## TLDR
KiRoSe introduces Sparse Motion Tokens—a compact, transition-supervised kinematic vocabulary—so an open language model can efficiently and accurately segment robot demonstrations into semantic subtasks, outperforming baselines and transferring zero-shot across embodiments.

## Abstract
Segmenting robot demonstration data into disjoint temporal and semantic subsegments is valuable for learning, cleaning, retrieval, and analysis. Segmentation is often performed manually in a tedious and error prone process. Multimodal Large Language Models (MLLMs) have the potential for automating this process, but directly ingesting raw multi camera video streams into MLLMs can be costly and can quickly exhaust context windows. In this paper, we introduce KiRoSe (Kinematics for Robot Segmentation), a novel framework that focuses on the companion stream of robot kinematic data. Inspired by the principle of classical entropy coding, such as Huffman coding, where frequently occurring symbols are represented more compactly, we propose Sparse Motion Tokens (SMTs), a discrete kinematic vocabulary designed to compactly represent recurring, temporally localized motion patterns, which we refer to as kinematic events. SMTs are learned by encoding kinematic trajectories with temporal segment supervision and quantizing the resulting features. We use increasingly available robot demonstration subtask annotations to supervise an open language model to interpret the resulting token sequences. Evaluation against human labeled segmentation shows that KiRoSe can substantially outperform baseline segmentation methods in F1 quality and transfers zero shot to unseen robot embodiments and egocentric human motion, while preserving the language models open vocabulary knowledge. Beyond segmentation, KiRoSe tracks task progress on an unseen robot and detects when an action is being reversed.(website: https://berkeleyautomation.github.io/kirose/)


## 精读解读（中文）
### 一、研究动机
机器人示范数据的时序与语义分段对学习、清洗、检索和分析都很有价值，但人工标注繁琐且易错；多模态大模型直接处理多相机原始视频成本高并迅速耗尽上下文窗口。运动学信号比视频更紧凑且信息密度高，但原始轨迹是高频率、高自由度的连续时间序列，难以直接供语言模型使用。KiRoSe因此探索用紧凑离散运动表示来自动识别子任务边界与动作描述。

### 二、技术方案（Method）
KiRoSe分两阶段：首先用残差时间卷积编码器将机器人运动学序列编码为时序上下文特征，并用辅助边界预测头与软边界目标、focal二分类交叉熵联合训练以保留子任务转换信息；随后冻结编码器，在均匀时间网格上池化特征，并用K=512的K-means码本量化得到Sparse Motion Tokens（SMT）。第二阶段把512个运动词元加入预训练语言模型词表并学习嵌入，输入包含任务指令、SMT序列和每秒文本时间标记，参考分段序列化为含起止时间与自然语言描述的JSON，按自回归语言建模损失只对响应词元训练，运动分词器保持冻结。

### 三、结果（Result）
在200条留出YAM回合上，KiRoSe的1秒容差边界F1为0.63，显著高于最强替代运动学分词器的0.42；零样本迁移到未见过的AgiBot本体时，0.5秒容差边界F1为0.61，而GPT-6 Astra为0.30。它还能在未见人类任务上生成训练标注中未出现的开放词汇动作描述，并在AgiBot上检测动作反向，任务进度相关系数为-0.68，而基于视频的ReWiND基线为+0.88。

### 四、结论（Conclusion）
KiRoSe表明，以子任务转换监督学习低码率运动词元，并让开放语言模型读取这些词元，可以在保持开放词汇知识的同时高效完成机器人示范的时序分段、语义描述、跨本体零样本迁移和任务进度理解。相比直接使用视频或重建导向的运动分词器，该方法在分割质量和跨本体泛化上具有明显优势。

### 五、方法论与关键技术细节
实现上采用左右臂末端执行器共享的14维表示，包括线速度、角速度和归一化夹爪开合速率，使机器人夹爪与人类手部可共享输入空间；训练使用ABC-130K中5,478条YAM回合、140个任务，评测含200条同本体留出回合、2,653条AgiBot World回合和193条Ego-Exo4D人类手部轨迹。关键设计是先以转换监督塑造编码特征而非决定词元位置，再在均匀网格池化后量化，码本仅在训练特征上拟合且在语言模型适配时冻结；局限包括依赖机器人运动学伴随流、部分基线因成本仅在子集评测，以及跨数据集语义重叠和标注粒度差异会影响迁移。
