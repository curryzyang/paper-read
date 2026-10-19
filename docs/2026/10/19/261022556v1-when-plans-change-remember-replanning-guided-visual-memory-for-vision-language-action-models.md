# When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Victoria Smelova, Daniil Kazachkov, Georgiy Kazantsev, Iuliia Tsvetkova, Egor Cherepanov, Nikita Kachaev, Artem Latyshev, Aleksandr I. Panov, Alexey K. Kovalev
- 机构：CogAI Lab, AXXX, Independent Researcher, MIRAI, Central University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22556v1) · [PDF](https://arxiv.org/pdf/2610.22556v1)

## TLDR
RePlanMem-VLA uses unusually large disagreements between overlapping action predictions from consecutive replans as a policy-internal trigger to selectively store key visual observations in a bounded memory, allowing vision-language-action policies to retain task-relevant cues for long-horizon tasks without keeping full observation histories.

## Abstract
Long-horizon, multi-stage Vision-Language-Action (VLA) policies often require visual information that is no longer present in the current observation. Retaining the complete observation history is computationally expensive and highly redundant, motivating selective visual memory. We introduce RePlanMem-VLA (Replanning-Guided Keyframe Memory for VLA), which turns a policy's own plan revisions into an online memory-write signal. Under receding-horizon execution, consecutive action chunks predict some of the same future actions. RePlanMem-VLA treats unusually large disagreement between these temporally aligned predictions as evidence of a task-relevant event. We first compare 35 disagreement measures across single-task autoregressive decoder-only and Flow-Matching Transformers trained from scratch, then validate the selected signals on pretrained OpenVLA-OFT and $π_{0.5}$ policies over MIKASA-Robo-VLA tasks. The resulting detectors achieve ROC-AUC of 0.981-0.997. We then use the selected signals in RePlanMem-VLA to trigger updates to a bounded visual memory, with a robot-masked write filter suppressing redundant frames. In the evaluated memory-retention experiments, RePlanMem-VLA preserves task-relevant observations until the later decision point in 100% of episodes. Real-robot replay data further show that event selection and redundancy suppression extend beyond simulation. These results establish plan revision as a policy-internal signal for controlling what a VLA remembers. Website: https://vika787.github.io/RePlanMem/.


## 精读解读（中文）
### 一、研究动机
长程多阶段VLA策略常需要当前观测中已消失的视觉线索，但保留完整观测历史计算昂贵且高度冗余，因此需要选择性视觉记忆。本文试图利用策略自身在重规划中的计划修订作为在线记忆写入信号，决定哪些观测应被记住。

### 二、技术方案（Method）
RePlanMem-VLA在滚动时域执行下比较连续动作块对同一未来动作的重叠预测，将C_{q-1}final[H:K]与C_q-[0:K-H]的异常不一致视为任务相关事件。方法先筛选35种不一致度量，部署时用10个检测信号并加入时间差分和EMA偏差构成30维特征，经任务条件因果标准化和正则化Mahalanobis surprise得到惊讶分，再用任务CDF转为百分位p_q，当p_q大于阈值τ时触发记忆写入。写入时通过机器人掩码过滤和冗余聚类选择非冗余帧，更新有界FIFO视觉记忆，随后二次前向得到最终动作块，仅该最终预测受原始SFT目标监督。检测器使用stop-gradient特征且不使用专家动作，记忆槽在每回合开始为空且不跨回合传递。

### 三、结果（Result）
在从头训练的decoder-only自回归与Flow-Matching Transformer以及预训练OpenVLA-OFT和π0.5策略上，所得事件检测器在MIKASA-Robo-VLA任务上达到ROC-AUC 0.981至0.997。记忆保留实验中，RePlanMem-VLA在100%的评估回合中把任务相关观测保留到后续决策点，并减少冗余覆盖；真实机器人回放数据进一步显示事件选择与冗余抑制行为可扩展到仿真之外。

### 四、结论（Conclusion）
结果表明，策略自身的计划修订可作为策略内部在线信号来控制VLA应记住什么，从而以有界视觉记忆保留延迟可用的任务线索。该工作将关键帧选择、记忆表示与动作块重规划一致性连接起来，为长程部分可观测操作提供选择性视觉记忆机制。

### 五、方法论与关键技术细节
实验基于MIKASA-Robo-VLA，动作块长度为K、执行步长为H，重叠长度为K-H，记忆最多B个槽并以FIFO更新；部署检测器D=10、输入为30维，含动作误差、方向分歧、时序局部偏差、平移旋转夹爪变化及顶层VLA特征距离，并使用EMA偏差和任务独立统计。Mahalanobis正则系数λ取相关矩阵平均特征值的固定比例，阈值τ控制写入频率；事件检测不看专家动作、不需关键帧标注或特权仿真状态，且stop-gradient阻止检测器反向塑造策略。局限包括记忆有界、触发更新需额外前向、检测器依赖任务校准与重规划重叠，真实机器人部分主要为回放验证。
