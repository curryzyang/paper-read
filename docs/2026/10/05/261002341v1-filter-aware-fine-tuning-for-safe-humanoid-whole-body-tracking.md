# Filter-Aware Fine-Tuning for Safe Humanoid Whole-Body Tracking

- 区域：精读区
- 排名：1
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Pranit Mohnot, Christian Helten, Daniele Gammelli, Marco Pavone
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02341v1) · [PDF](https://arxiv.org/pdf/2610.02341v1)

## TLDR
CoFiT, a filter-aware fine-tuning method for pretrained humanoid whole-body trackers, bridges policy–safety-filter mismatches to reduce violation time by 91% on TWIST2 and 21% on SONIC in simulation and by 83% on Unitree G1 hardware, eliminating operator interventions in all hardware trials.

## Abstract
Safe whole-body motion is essential for deploying humanoid robots in unstructured environments. Modern humanoid control commonly separates reference specification from execution, with a planner, teleoperator, or motion generator providing a reference that a reinforcement-learning policy tracks through dynamically feasible whole-body control. Runtime safety filters, such as control barrier functions (CBFs), offer a promising approach for enforcing newly introduced constraints via interventions on the tracker's outputs. We show, however, that treating the tracking policy and safety filter independently induces fundamental mismatches, as filtering alters both the executed actions and the induced state distribution. We study this policy-filter interface through case studies that isolate dynamics, objective, and information mismatches, highlight their root causes, and use these insights to develop CoFiT (Constrained Filter-aware Tuning), a filter-aware fine-tuning method for pretrained trackers. Across diverse constraint scenes, CoFiT reduces violation time relative to filter-only training by 91% on TWIST2 and 21% on SONIC, while requiring smaller safety filter corrections. On Unitree G1 hardware, CoFiT reduces violation time by 83% for TWIST2 and completes every trial without operator intervention, whereas 50% of baseline trials require an operator stop. Together, these results provide actionable insights into policy-filter interactions and establish design principles for integrating learned trackers with runtime safety filters.


## 精读解读（中文）
### 一、研究动机
人形机器人全身运动的安全执行通常依赖参考生成与RL跟踪策略分离，并在运行时叠加CBF等安全滤波器；但滤波会同时改变实际执行动作和策略诱导的状态分布，使跟踪策略与滤波器独立设计产生动态、目标和信息层面的根本失配。本文旨在系统刻画该策略-滤波器接口，并让预训练跟踪器主动适配滤波器。

### 二、技术方案（Method）
提出CoFiT（Constrained Filter-aware Tuning），一种面向预训练全身跟踪器的滤波器感知微调方法。输入为参考全身运动、机器人本体状态与约束状态，输出为关节动作；训练时在闭环中运行CBF等运行时安全滤波器，将滤波器修正后的动作及由此诱导的状态分布作为策略优化分布，并向策略暴露约束/滤波器相关信息，以约束感知目标减少跟踪误差与滤波干预。关键步骤包括：在含约束场景中隔离动态、目标和信息失配，设计早期约束信号、历史信息、动作边界/增量修正等模块，在TWIST2和SONIC预训练追踪器上微调，最后在Unitree G1上验证。

### 三、结果（Result）
在多样约束场景中，CoFiT相对仅用滤波器训练/Filter-only显著降低违规时间：TWIST2降低91%，SONIC降低21%，同时所需安全滤波器修正更小。在Unitree G1硬件上，TWIST2违规时间降低83%，所有试验均无需操作员干预完成，而基线50%的试验需要操作员急停。结果表明，将滤波器纳入策略微调闭环能显著提升安全性与可部署性。

### 四、结论（Conclusion）
跟踪策略与运行时安全滤波器不能独立处理，滤波造成的执行动作改变和状态分布偏移必须被纳入训练，否则会产生安全与跟踪性能的双重损失。CoFiT通过滤波器感知微调建立了学习型全身跟踪器与运行时安全滤波器的集成设计原则，在仿真和硬件上均有效。

### 五、方法论与关键技术细节
评估使用TWIST2和SONIC预训练追踪器、多样约束场景与Unitree G1真机，指标包括跟踪误差、违规时间、TV、跌倒次数、深度/发生率等。方法细节上，CoFiT以CBF等滤波器的干预为训练信号，强调早期约束、滤波器信息/历史、增量修正和动作边界等消融因素；训练在滤波后闭环状态分布上优化跟踪与约束违反惩罚的权衡。局限性包括依赖仿真约束建模和滤波器可查询/可微性、真机试验规模有限，以及超参与约束设计会显著影响安全-跟踪折中。
