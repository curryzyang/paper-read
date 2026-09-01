# Vehicle Drift Emergence: Continuous Evolution from Grip Driving to the Handling Limit via Boundary Exploration Learning Model Predictive Control

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Sheng Zhao, Binh-Minh Nguyen, Hangyu Lu, Xiaodong Wu
- 机构：Shanghai Jiao Tong University, The University of Tokyo, The University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28723v1) · [PDF](https://arxiv.org/pdf/2608.28723v1)

## TLDR
The paper shows that drift can emerge autonomously from grip driving via a boundary-exploration learning model predictive controller in a lap-time minimization task, where high-sideslip motion arises as a continuous, performance-driven transition near the handling limit on low-friction surfaces rather than being explicitly prescribed.

## Abstract
Automated drift controllers commonly track a prescribed drift equilibrium, sideslip reference, or trajectory. These formulations establish how to execute drift, whereas the continuous transition from grip driving to drift near the handling limit remains unresolved. This paper defines drift emergence in a repetitive lap time minimization task, where neither the controller objective nor the reward contains an explicit drift reference. A boundary exploration learning model predictive controller (BE-LMPC) constructs an empirical safe set and a locally shifted terminal cost from completed laps. By iteratively improving spatial speed allocation under a fixed global speed bound, the controller progressively explores larger sideslip and yaw rate envelopes while preserving recoverability. As lap performance improves, sustained sideslip and pronounced yaw motion emerge while the rear axle approaches saturation. Analysis shows that, when external conditions vary smoothly, the transition from tire adhesion to sliding does not itself cause abrupt changes in tire force or vehicle state. The combined-slip Fiala model satisfies this continuity condition at the transition. At a tire road friction coefficient of 0.6, lap time decreases from 49.95 s on Lap~3 to 25.50 s on Lap~12, with drift first emerging on Lap~11. Lap~12 reaches 16.5$^\circ$ sideslip and 0.894 rear axle utilization. In contrast, no drift is detected for friction coefficients from 0.8 to 1.2; at 1.2, a similar peak speed is achieved with only 0.483 rear axle utilization. These results characterize drift as a conditional continuation of limit handling that emerges when increasing performance demand approaches the available tire capacity, rather than as a separately prescribed motion mode.


## 精读解读（中文）
### 一、研究动机
现有自动驾驶漂移控制大多采用“预设-跟踪”范式，即预先指定漂移平衡点、质心侧偏角参考或轨迹，这只能解决如何执行漂移，而无法解释从抓地行驶到接近操控极限时漂移如何连续涌现。本文在重复赛道最小圈时任务中定义漂移涌现，要求控制器目标与奖励均不含任何显式漂移参考，从而回答性能寻优闭环能否自主产生高侧偏角运动，以及何种需求-容量条件使其可达。

### 二、技术方案（Method）
采用平面三自由度单轨车辆模型，状态为[X,Y,ψ,v,r,β]，控制输入为加速度指令和前轮转角；轮胎使用组合滑移Fiala模型，前后轴按固定50:50纵向力分配，摩擦系数在每次仿真中恒定。提出边界探索学习模型预测控制（BE-LMPC）：利用已完成圈构建经验安全集和局部平移终端代价，在固定全局速度上界下迭代优化空间速度分配，以可恢复性为门控逐步扩大质心侧偏角和横摆角速度包络；控制器不含任何漂移参考，漂移检测仅依据β≥8°、r≥0.45 rad/s、后轴利用率ρ_r≥0.82且持续0.30 s。通过摩擦系数扫描和检测器敏感性分析以及抓地约束和固定包络方法对比，研究漂移涌现条件。

### 三、结果（Result）
在摩擦系数0.6的低附路面上，圈时从第3圈的49.95 s降至第12圈的25.50 s，漂移首次出现在第11圈；第12圈达到16.5°质心侧偏角和0.894的后轴利用率。摩擦系数0.8至1.2时未检测到漂移，其中1.2时达到相似峰值速度但后轴利用率仅为0.483。结果表明漂移是极限操控的条件性延续，当性能需求接近可用轮胎容量时涌现，而非单独预设的运动模式。

### 四、结论（Conclusion）
漂移不是一种独立的运动模式，而是当性能需求增大到接近轮胎附着力极限时，从抓地驾驶连续演化而来的条件性响应。在恒定控制结构和无漂移参考的优化目标下，BE-LMPC能够自主产生持续高侧偏角与明显横摆运动，且该现象仅在低摩擦且需求-容量比可达到边界的条件下出现。

### 五、方法论与关键技术细节
关键细节包括：Fiala组合滑移模型在|h|=1处侧向力关于滑移角C^1连续，增量侧偏刚度连续趋于零，保证从附着到滑移的过渡不引起状态突变；低摩擦（μ=0.6）时后轴接近饱和是漂移涌现的必要条件，而高摩擦（μ≥0.8）时轮胎容量充足，无需大幅侧偏即可达到相近速度；BE-LMPC的经验安全集与局部移位终端代价保证逐圈可行性和性能单调改进，控制器仅优化空间速度分配，不直接优化侧偏角或横摆角速度；漂移检测阈值（β≥8°, r≥0.45 rad/s, ρ_r≥0.82, 持续0.30 s）为研究特定设置，需做敏感性分析；模型忽略车身侧倾、俯仰、悬架、左右载荷转移、轮胎温度及执行器动态，且控制器与仿真使用同一模型，以避免模型差异造成人为过渡。
