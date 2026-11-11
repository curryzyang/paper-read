# Robo-MLT: Dual-System Robotic Manipulation for Long-Horizon Medical Laboratory Tasks

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Zequan Zeng, Kai Wang, Delvin Ce Zhang, Huaping Liu, Zhipeng Yuan, Junqin Yang, YunLong Zhang
- 机构：Chongqing University, University of Sheffield, Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13039v1) · [PDF](https://arxiv.org/pdf/2611.13039v1)

## TLDR
Robo-MLT is a dual-system framework that couples a vision-language planner and multiframe execution monitor—for explicit workflow-stage tracking, completion detection, and replanning—with a skill-conditioned VLA policy for action generation, enabling more reliable and recoverable long-horizon medical laboratory manipulation and outperforming baselines on blood gas analysis and blood sample tube sorting.

## Abstract
Reliable medical laboratory automation requires robots to complete entire workflows in protocol order while handling changes during execution. A robot may execute each motion correctly yet fail the workflow by confusing visually similar stages or stalling after human intervention. We present Robo-MLT, a dual-system framework that couples explicit workflow monitoring with learned action generation. A vision--language planner composes an ordered atomic-skill sequence from the protocol and the initial workspace observation. A multiframe execution monitor detects when the active skill has completed or become infeasible, then advances the workflow or triggers replanning. A skill-conditioned vision--language--action policy generates the manipulation trajectories, and an asynchronous runtime coordinates it with the monitor. We evaluate Robo-MLT against four policy baselines and a VLM-based monitor baseline on blood gas analysis and blood sample tube sorting, with 50 nominal configurations per method and 20 sample-removal configurations. Robo-MLT achieves task success rates of 82\% and 70\%, exceeding $π_{0.5}$ by 30 and 22 percentage points, respectively. After an operator removes the sample being handled, the system revises the remaining plan and continues processing the other samples. These results indicate that, under the evaluated conditions, explicit workflow monitoring makes long-horizon laboratory manipulation more reliable and recoverable.


## 精读解读（中文）
### 一、研究动机
医疗实验室自动化要求机器人按协议顺序完成长流程操作，但不同阶段可能视觉高度相似，且执行中可能发生人工干预或场景变化，导致机器人动作正确却流程失败。现有端到端策略缺少显式流程状态，难以判断当前步骤是否完成或已不可行，因此需要把显式工作流监控与学习型动作生成结合，提高长程操作的可靠性和可恢复性。

### 二、技术方案（Method）
Robo-MLT采用双系统分层方案：输入任务指令、仪器协议、初始工作区观测和原子技能库（血气分析7个、试管分拣5个），由冻结的Qwen3.7-Max零样本规划器生成有序技能序列；System 2以M帧多视角观测滑窗和当前技能文本为输入，用冻结SigLIP2图像/文本编码器提取特征，经带位置编码的因果时序编码器和以文本为查询的交叉注意力得到技能 grounding 表示，再由两个独立两层MLP头输出完成概率与恢复概率，经阈值和连续k次去抖返回stay、advance或recover，recover时由同一VLM基于协议、已完成步骤和当前观测重规划剩余步骤，超时作为后备触发；System 1为技能条件Qwen3-VL流匹配VLA策略，生成动作块，异步运行时以机器人控制频率流式执行并与低频监控协调。

### 三、结果（Result）
在血气分析和血样试管分拣两个真实任务上，Robo-MLT任务成功率分别为82%和70%，分别比π0.5高30和22个百分点；实验对比了四个策略基线和VLM监控基线，每种方法50个常规配置并设置20个样本移除配置。操作员移除正在处理的样本后，系统能修改剩余计划并继续处理其他样本，表明显式流程监控带来更好的长程可靠性和干预后恢复能力。

### 四、结论（Conclusion）
结果表明，在评估条件下，将显式、低频的工作流监控与高频生成控制分离，可缓解视觉相似阶段导致的错步和停滞，使长程实验室操作更可靠且可恢复。由于规划器冻结、监控器只移动计划指针，对已知技能的重复或重排无需重新训练；但真正新增技能仍需遥操作示范并重训监控器。

### 五、方法论与关键技术细节
关键实现点包括：规划器与SigLIP2编码器冻结，监控器为轻量双头二分类并用连续多帧观测和技能指令消歧，完成/恢复概率采用阈值加连续更新次数去抖，重规划输入包含协议、已完成步骤和当前场景；系统需双臂机械臂、三路RGB相机和单块工作站级GPU，异步运行时避免慢速监控阻塞动作流。局限是仅在两个实验室协议、单一工作区和一类外部干预下验证，未在生产实验室部署，且预览未给出具体损失函数、阈值数值及监控器训练数据规模。
