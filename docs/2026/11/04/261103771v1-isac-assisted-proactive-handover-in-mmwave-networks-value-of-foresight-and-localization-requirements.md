# ISAC-Assisted Proactive Handover in mmWave Networks: Value of Foresight and Localization Requirements

- 区域：精读区
- 排名：10
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Seyed Bagher Hashemi Natanzi, Bo Tang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03771v1) · [PDF](https://arxiv.org/pdf/2611.03771v1)

## TLDR
This paper shows that ISAC-enabled proactive handover in mmWave networks can recover most of the gap between reactive and oracle handover with short look-ahead, but only if users and blockers are localized to roughly a decimeter—realistic sensing and positioning errors largely eliminate the benefit, making an uncertainty-aware planner mostly defer to reactive handover.

## Abstract
Millimeter-wave (mmWave) links can lose tens of decibels within milliseconds when a person or vehicle crosses the line of sight, and reactive handover recovers only after the outage has begun. Integrated sensing and communication (ISAC) promises to let the network see blockers coming and move users to another cell in advance. This paper asks how much such foresight is worth relative to the best reactive handover, and what sensing accuracy is needed to harvest it. We formulate cost-aware cell selection with knowledge of the future signal-to- noise ratio as a sequential decision problem, define the value of foresight through a policy-independent bound, and develop an ISAC-assisted handover framework in which a radio unit senses blockers with its own communication waveform and a simulated Open RAN xApp plans handovers. Ray-traced experiments in a 28 GHz street canyon, reported on held-out scenarios, show that, with a short look-ahead, perfect foresight closes most of the gap between service-aware (Layer-3) reactive handover and an instantaneous oracle. Harvesting this value, however, requires the user and nearby blockers to be localized to about a decimeter, well beyond what our radar tracker and meter- level user positioning provide; with realistic errors, even an uncertainty-aware planner largely defers to reactive handover.


## 精读解读（中文）
### 一、研究动机
毫米波链路在行人或车辆遮挡视距时会在毫秒级损失数十dB，现有切换多为反应式，只能在链路劣化甚至中断后恢复，难以保障时延和速率敏感业务。ISAC使基站可用通信波形感知遮挡物并提前切换，但此前研究很少区分完美前瞻的理论价值与真实传感误差下可实现的收益，也未明确所需定位精度。

### 二、技术方案（Method）
论文将已知未来SNR下的代价感知小区选择建模为序贯决策问题，并用动态规划精确求解，从而给出与策略无关的前瞻价值上界。系统方案中，射频单元用自身OFDM通信波形探测第三方遮挡物，结合数字孪生感知处理进行跟踪、逐小区SNR预测，并由模拟O-RAN xApp执行切换规划，另设不确定性感知规划器。仿真基于Sionna RT 2.2构建空间一致的28GHz街道峡谷射线追踪场景，使每个运动体既是3GPP雷达目标又是通信路径遮挡物，并在留出场景评估。

### 三、结果（Result）
留出场景实验表明，在较短前瞻约0.5s且采用代价感知切换时，完美前瞻可弥合服务感知Layer-3反应式切换A5与瞬时oracle之间的大部分可改善差距。但要兑现该价值，用户和附近遮挡物需定位到约分米级，远高于本文雷达跟踪器和米级用户定位所能提供的能力；在现实误差下，即使不确定性感知规划器也大多退化为反应式切换。

### 四、结论（Conclusion）
ISAC辅助主动切换的理论收益显著，但其可实现收益受定位与感知精度严格约束，分米级用户和遮挡物定位是收获前瞻价值的关键瓶颈。论文因此把前瞻价值与传感可实现性分离，指出未来需改进雷达跟踪、数据关联、数字孪生校准和多源定位，而不能仅靠更复杂的切换策略。

### 五、方法论与关键技术细节
关键实现包括以服务感知A5反应式切换和瞬时oracle为基线、用动态规划界定任何主动策略的上界、以约0.5s规划时域和切换代价约束决策；仿真采用28GHz街道峡谷、60s运行及不同车辆和行人密度，遮挡物同时作为雷达目标和通信遮挡体。局限性在于结果主要来自射线追踪仿真和模拟xApp，雷达跟踪与米级定位误差使不确定性感知规划也难超越反应式基线，尚未给出硬件实测验证。
