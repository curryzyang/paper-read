# Anchor 1: Precise and Stable Humanoid Control for Whole-Body Manipulation

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Archon Robotics, :, Caojun Wang, Checheng Yu, Gangcheng Jiang, Guangjun Zeng, Haoran Jiang, Hongyang Li, Huibin Yan, Huijie Wang, Jialong Zeng, Jin Yang, Kai Cheng, Li Chen, Liang Chen, Lirui Zhao, Modi Shi, Penglin Fu, Shijia Peng, Tianyu Li, Wencong Zhang, Xuechong Lv, Yixuan Pan, Yong Zhang, Yu Qiao, Yu Zhang, Ziyan Li
- 机构：Archon Robotics
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00193v1) · [PDF](https://arxiv.org/pdf/2611.00193v1)

## TLDR
Anchor 1 is a whole-body humanoid controller and benchmark that combines calibrated sparse motion references, offline-curated training data, and decoupled error feedback to achieve precise, stable whole-body manipulation, reducing real-world tracking error by 30–80% and improving downstream teleoperation and task success.

## Abstract
Humanoid controllers have acquired increasingly diverse motor skills, yet translating these capabilities into precise and stable whole-body manipulation remains challenging. Manipulation tasks are sensitive to execution deviations -- even small errors or unintended steps can cause failure. Introducing Anchor 1, a whole-body controller for precise and stable whole-body manipulation, together with a benchmark spanning diverse coordination demands. Anchor 1 adopts calibrated sparse motion references to preserve task-relevant human motion structure without online joint-space retargeting, leaving kinematic freedom for precise control. To guide this freedom towards stable, physically plausible whole-body coordination, we shape the training distribution through offline curation of robot motions paired with these calibrated sparse references. We further introduce explicit error feedback decoupled from motion encoding, improving control precision while supporting flexible command interfaces. To achieve a systematic evaluation of these capabilities, a benchmark is proposed to assess precision, sustained execution stability, and reachability across diverse whole-body coordination demands. Evaluations in simulation and on hardware show stronger precision and stability across all evaluation tracks. Under the most strict real-world global scoring setting, Anchor 1 achieves a 30\% to 80\% decrease in tracking error with fewer look-ahead inputs, and without retargeting compared to all existing controllers. Downstream experiments demonstrate more efficient teleoperated data collection and higher task success using the same deployment pipeline as well. We believe Anchor 1 supports precise and stable whole-body control as a practical basis for humanoid task execution.


## 精读解读（中文）
### 一、研究动机
人形机器人已具备多样运动技能，但把能力转化为精准、稳定的全身操作仍很困难：操作任务对执行偏差高度敏感，末端小误差或非预期迈步都可能导致失败。现有方法在命令构造上依赖在线关节空间重定向或参数化人体表示，可能破坏任务相关运动结构；在控制上，token 条件策略的误差反馈是隐式的，而显式误差反馈若写入 token 又会把意图与瞬态执行误差纠缠。任务级基准又常被感知与规划影响，序列平均误差会掩盖短暂偏差，因此需要同时解决命令保真、精确执行和控制器级评测。

### 二、技术方案（Method）
Anchor 1 将人体运动经过结构保持的标定映射到机器人尺度，不使用在线关节空间重定向，并把命令限制为骨盆、双腕和双踝的稀疏运动参考，使策略可在剩余运动学冗余中精确跟踪目标。训练时，每条人体运动与离线重定向得到的机器人参考配对，并通过质量筛查塑造训练分布，使冗余利用偏向稳定、物理合理的全身协调。控制器引入与运动编码解耦的显式误差反馈，既可接收稀疏参考也可接收运动 token；当输入为 token 时，从 token 重建目标作为误差反馈参考，并用重建目标约束 token 与意图运动一致。评测上提出覆盖 In-house、Public 和 Reachability 三条 track 的控制器级基准，分别考察任务结构化全身协调、多源动态运动和规定腕部目标可达保持能力。

### 三、结果（Result）
仿真与硬件评测显示，Anchor 1 在所有评测 track 上取得更强的跟踪精度与执行稳定性。在最严格的真实世界全局评分设置下，相较所有现有控制器，Anchor 1 在更少 look-ahead 输入且不做重定向的条件下将跟踪误差降低 30% 到 80%。下游实验使用相同部署管线，展示了更高效的遥操作数据采集和更高的任务成功率；硬件演示还覆盖精细末端接触、快速拦截以及跪姿、弯腰、行走中的全身操作。

### 四、结论（Conclusion）
Anchor 1 通过结构保持的稀疏参考、面向稳定性的训练分布 curation 和解耦误差反馈，把全身控制从整体动作复现推进到面向操作的精确实时执行。其控制器级基准补足了任务级评测难以诊断的精度、持续稳定性和可达性问题。结果表明该方法可作为人形机器人任务执行的实用底层控制基础，并直接改善遥操作数据采集与自主策略执行。

### 五、方法论与关键技术细节
关键实现点包括：命令仅指定骨盆、双腕、双踝五个稀疏目标，保留任务相关人体运动结构且避免在线关节空间重定向；离线将人体运动与机器人重定向参考配对并进行质量筛查，因此训练分布决定策略如何利用运动学冗余；显式误差反馈独立于运动 token，token 输入时通过目标重建提供反馈并以重建目标保持 token 空间一致。评测覆盖仿真与硬件、三条互补 track，并强调分布外操作相关运动；方法约束是无在线重定向、依赖稀疏命令和离线配对质量，控制器级指标不能替代包含感知与规划的任务级评估。
