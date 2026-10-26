# FLORA: An Open Model Suite for Scaling Robotics Data Engines

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Sicong Leng, Yunze Man, Zhiqi Li, Jing Wang, Yuhe Zhang, Ryan Punamiya, Siddharth Patki, Kaiyuan Zheng, Zi-ang Cao, Zhiding Yu, Sifei Liu, Danfei Xu, Ben Levin, Jan Kautz, Yuke Zhu, Johan Bjorck, Linxi "Jim" Fan
- 机构：NVIDIA
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31779v1) · [PDF](https://arxiv.org/pdf/2610.31779v1)

## TLDR
Flora is an open-source, industrial-scale robotics data engine that unifies timestamped captioning and process/outcome reward labeling for GR00T-style foundation models, achieving competitive SOTA benchmark performance at roughly 125× lower cost than GPT-6 Astra while labeling 200,000 hours of data per day.

## Abstract
The life-cycle of robotics foundation models crucially depends on data labels. Outcome reward labels are needed for monitoring real-world deployments. Process reward labels are needed during RL post-training. Timestamped captions are needed for filtering and balancing pretraining data. We present Flora, an industrial-quality data engine used for training GR00T models, that simultaneously covers these capabilities. Flora achieves SOTA scores on the captioning benchmark WGO-Bench and reward benchmarks RoboReward and Robometer. On internal benchmarks it is competitive with GPT-6 Astra while beating other frontier models. The model is substantially cheaper than API-based alternatives, roughly 125 times cheaper than GPT-6 Astra. Florais battle tested at scale, labeling 200,000 hours of data per day across 512 GB300s. By open-sourcing our data engine, we enable researchers to scale custom robotics datasets and explore emerging applications such as physical auto-research and human-to-robot transfer.


## 精读解读（中文）
### 一、研究动机
机器人基础模型的全生命周期高度依赖高质量数据标签：部署监控需要结果奖励，RL后训练需要过程奖励，预训练数据筛选与配比需要带时间戳的动作描述。现有系统通常只覆盖单一标注类型，通用前沿模型虽可多任务标注，但在现代机器人数据规模下成本过高。

### 二、技术方案（Method）
Flora是用于训练GR00T模型的工业级数据引擎，由分割、描述和奖励三类模型组成。带时间戳描述采用两阶段流程：先将视频切为重叠窗口，分割模型预测窗口内起止时间及左右越界延续标志，经确定性过滤保留中心区域片段，再按时间重叠与延续标志拼接为整段事件区间，并用平移窗口做边界细化；随后对每个区间取目标帧及前后最近非重叠事件的上下文帧，由描述模型生成动作指令。奖励模型统一支持结果奖励、稠密/过程奖励以及测试时用户自定义rubric奖励。推理时使用验证集选出的分割与描述RL检查点，并可按固定提示完成分割、描述和联合标注。

### 三、结果（Result）
Flora在描述基准WGO-Bench以及奖励基准RoboReward和Robometer上取得SOTA，内部基准上与GPT-6 Astra竞争并优于其他前沿模型。WGO-Bench联合标注达到50.3，较Refiner平均分割F1提升16.9点、联合F1提升7.3点，黄金窗口描述准确率相近。RoboRewardBench结果奖励MAE为40.0，优于GPT-6 Astra的55.4和专用RoboReward的66.5；Robometer OOD排序为72.0对Astra的82.3，ID VOC 98.9持平、OOD VOC 99.6；DenseRewardBench宏F1为46.2，失败召回53.3%。RubricBench池化L1为6.5，优于十个通用模型中的九个，但仍落后Astra的3.6；系统约比GPT-6 Astra便宜125倍，并已在512块GB300上每天标注20万小时数据。

### 四、结论（Conclusion）
Flora以一套开放模型套件同时覆盖带时间戳描述、过程/结果奖励和rubric奖励，并在质量、成本与规模化吞吐之间取得有竞争力的平衡。开源该数据引擎可让研究者扩展自定义机器人数据集，并探索物理自动研究和人到机器人迁移等新应用。

### 五、方法论与关键技术细节
关键实现包括重叠窗口分割、中心区域过滤、基于时间重叠和延续标志的片段拼接、平移窗口边界细化，以及带前后上下文的逐区间描述；奖励侧统一建模结果、稠密和rubric奖励。评测覆盖WGO-Bench的25个人类自我中心、50个DROID外部视角和25个Galaxea头相机回合，分割用tIoU阈值和描述部分得分，DenseCaptionBench含300个完整回合，DenseRewardBench含40个双臂回合和4861个时间步。需注意多数对比是系统级比较，视觉输入、帧预算和解码设置因模型而异，专用奖励模型沿用原协议；VOC只衡量成功回合排序，不证明失败检测精度，rubric能力仍落后最强闭源模型。
