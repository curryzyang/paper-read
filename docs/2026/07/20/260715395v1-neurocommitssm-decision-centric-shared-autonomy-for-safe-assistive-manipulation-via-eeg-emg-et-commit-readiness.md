# NeuroCommitSSM: Decision-Centric Shared Autonomy for Safe Assistive Manipulation via EEG-EMG-ET Commit Readiness

- 区域：精读区
- 排名：5
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Tipu Sultan, Param Sangani, Kody Cool, Pascal Sikorski, Guangping Liu, Hadi Akbarpour, Madi Babaiasl
- 机构：Saint Louis University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15395v1) · [PDF](https://arxiv.org/pdf/2607.15395v1)

## TLDR
NeuroCommitSSM presents a decision-centric shared autonomy framework that predicts a continuous commit-readiness score from synchronized EEG, EMG, and eye-tracking signals, and gates execution through a HOLD-ASSIST-COMMIT supervisor with dwell/hysteresis filtering and real-time feasibility checks, achieving low false activations and stable state transitions under sensor dropout for safe assistive robotic manipulation.

## Abstract
We present NeuroCommitSSM, a decision-centric framework that models when to execute, not just what to do, for safe commit-to-execute control in assistive robotic manipulation. NeuroCommitSSM predicts a continuous commit-readiness score c_t in [0,1] from synchronized electroencephalography (EEG), electromyography (EMG), and eye-tracking (ET), and converts it into discrete commit events through dwell and hysteresis filtering. A three-state finite-state supervisor, HOLD-ASSIST-COMMIT (HAC), gates execution by requiring both a sustained commit-readiness signal from the neural model and real-time perception and robot-state feasibility, including target visibility, inverse kinematics solvability, and collision-free planning, before initiating motion. We evaluate the framework on N=32 subjects performing five activities of daily living (ADL) tasks aligned with the International Classification of Functioning, Disability and Health (ICF), using leave-one-subject-out (LOSO) cross-validation and seven sensor-dropout scenarios (S0-S6). NeuroCommitSSM achieves 0.950 action-balanced accuracy with 0.75 false commit events per 1000 REST windows (FP/1k REST), and maintains low false commits and stable state transitions under sensor loss. For example, in the EEG-only condition, it achieves 0.785 balanced accuracy and 0.29 FP/1k REST, whereas the Temporal Convolutional Network baseline produces 99.95 FP/1k REST under the same condition. Hardware-in-the-loop (HIL) validation on a Kinova Gen3 arm shows that feasibility-checked execution reduces false starts and decision instability without sacrificing task success. Supplementary materials, including code, datasets, videos, and additional analyses, are available at https://madibabaiasl.github.io/NeuroCommitSSM/.


## 精读解读（中文）
### 一、研究动机
现有辅助机器人共享控制系统主要关注解码用户意图（what），但缺乏对执行时机（when）的安全建模，导致静止期错误触发（false triggers）和决策不稳定问题。多模态生理信号（EEG/EMG/ET）的非平稳性与高被试差异性使得将意图置信度直接阈值化触发动作不可靠，需要一种决策中心的框架来最小化误激活并融合机器人可行性检查。

### 二、技术方案（Method）
构建同步EEG/EMG/ET数据集（N=32被试，5个ICF对齐ADL任务），通过隐半马尔科夫模型（HSMM）标注REST/ACTION窗口。NeuroCommitSSM使用神经生理学感知编码器和熵正则化多模态融合预测连续commit分数c_t∈[0,1]，再经驻留/迟滞滤波（dwell/hysteresis）转换为离散commit事件。三状态有限状态机HAC（HOLD-ASSIST-COMMIT）要求同时满足持续commit信号和实时感知/机器人状态可行性（目标可见性、逆运动学可解性、无碰撞规划）才执行动作。采用留一被试交叉验证（LOSO）和7种传感器丢失场景（S0-S6）评估。

### 三、结果（Result）
NeuroCommitSSM在全部传感器下达到0.950动作平衡准确率，每1000个REST窗口仅0.75次错误commit事件（FP/1k REST）。传感器丢失时仍保持低误报（如仅EEG：0.785平衡准确率，0.29 FP/1k REST），而时序卷积网络（TCN）基线在相同条件下产生99.95 FP/1k REST。在Kinova Gen3机械臂的硬件在环（HIL）验证显示，可行性检查的执行减少了误启动和决策抖动，且不牺牲任务成功率。

### 四、结论（Conclusion）
NeuroCommitSSM通过决策中心的commit感知框架显著降低了静止期错误触发和状态切换不稳定性，将意图解码与机器人可行性检查统一在HAC监督器中，实现了安全辅助操作。同时发布了首个同步EEG/EMG/ET的ICF对齐ADL意图解码数据集及LOSO基准，为鲁棒共享控制提供了新范式。

### 五、方法论与关键技术细节
数据方面：32名被试（男性22人，女性10人，年龄18-46岁），完成5个ICF对齐ADL任务（时钟、瓶子、风扇、植物、挥手），每会话90-120分钟。建模使用HSMM标注REST/ACTION窗口，熵正则化融合处理传感器丢失，驻留/迟滞滤波参数需校准（论文中未明确具体阈值）。HAC监督器包含HOLD/ASSIST/COMMIT状态，可行性检查依赖无标记RGB-D感知管道（RANSAC几何估计），无先验CAD模型。评估指标以FP/1k REST和flaps/min为核心，LOSO交叉验证保证被试间泛化。局限性：实验为实验室仿真环境，未在真实残疾用户及长期使用中验证；传感器丢失场景为人工模拟，真实环境噪声可能更复杂；计算复杂度未详细报告。
