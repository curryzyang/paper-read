# Horizon-Dependent Tube MPC for Elliptical-Orbit Rendezvous Under Mass Uncertainty

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Omer Burak Iskender, Keck-Voon Ling
- 机构：Nanyang Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27659v1) · [PDF](https://arxiv.org/pdf/2608.27659v1)

## TLDR
The paper proposes a horizon-dependent tube MPC for elliptical-orbit rendezvous under mass uncertainty that derives the range at which safety guarantees lapse from the predictor's linearisation error versus the disturbance bound, uses this as a design rule to certify or reformulate guidance phases, and achieves 29–40% propellant savings in Monte Carlo tests while maintaining docking success.

## Abstract
A spacecraft closing on a target from three hundred kilometres to contact flies one guidance law across five orders of magnitude of range, and a controller that is provably safe at close range can lose that guarantee completely at long range while continuing to fly as though nothing were wrong. This paper derives the range at which the guarantee lapses and uses it as a design rule. The bound compares the prediction model's own linearisation error against the disturbance set the controller was built to reject, and needs only the sampling period, the orbit and that disturbance bound, so it can be evaluated before any simulation. On a Mars Sample Return approach it disqualifies the homing phase, where most of the propellant is spent, and clears the other two. Re-posing the disqualified phase in relative orbital elements restores the guarantee; re-posing a phase the rule already clears, in a frame two orders of magnitude more accurate, changes propellant by under a tenth of one per cent, and it is that second prediction that makes the rule falsifiable rather than descriptive. The constraint tightening also ties the prediction horizon to feasibility, so the horizon search limit becomes a mission parameter rather than a solver setting. Against a reimplementation of a published benchmark that reproduces its propellant to within one per cent, over five hundred dispersed Monte Carlo transfers per case on matched seeds, the controller saves 29% of the propellant on a circular target orbit and 40% on an eccentric one, docking inside the 0.20 m capture requirement on essentially every draw at a median miss near 5 cm. Two results run the other way: the saving is bought with time of flight and computation, and it comes from what the guarantee demanded of the terminal condition rather than from better disturbance rejection. Recursive feasibility and asymptotic stability are not claimed.


## 精读解读（中文）
### 一、研究动机
航天器从300公里接近目标至接触的整个过程中，单一制导律跨越五个数量级的距离范围，而一个在近距离可证明安全的控制器在远距离可能完全丧失安全保证却仍继续飞行。现有管式MPC大多基于LTI或固定最坏情况管宽，未利用Yamanaka-Ankersen（YA）时变动力学随轨道相位变化的紧缩机会。本文旨在推导保证失效的距离边界，并将其作为设计规则，同时解决椭圆轨道交会中质量不确定性带来的鲁棒控制问题。

### 二、技术方案（Method）
本文提出一种依赖于预测时域（horizon-dependent）的管式MPC，用于椭圆轨道交会。采用Yamanaka-Ankersen（YA）状态转移矩阵建立相对运动模型，状态含位置和速度，输入为脉冲Δv，质量不确定性建模为输入矩阵乘性标量δm。控制器将状态分解为标称轨迹和误差，误差动态由闭环矩阵A_cl=A_k+B_kK驱动，约束逐时域紧缩：误差界e_j按递推传播，输入back-off为|K|e_j。核心创新是推导预测器有效性界限s*，比较线性化残差与扰动界，得出分离距离上限约为√(w̄a/C)/(nT_s)，仅需采样周期、轨道和扰动界即可预先计算。在Mars Sample Return任务中，对三个制导阶段（homing、closing、final approach）分别应用该MPC，homing阶段因超出有效性界限而被判定不合格，改用相对轨道要素（ROE）重新建模以恢复保证。通过改变预测时域N和终端容差tol_j−e_j(N)的权衡，在单个枚举中同时选择时域和鲁棒裕度。最后与重新实现的已发表基准对比，在匹配随机种子下进行每情形500次分散蒙特卡洛仿真。

### 三、结果（Result）
针对发表于基准的重实现（推进剂误差在1%以内），在500次分散蒙特卡洛转移中，所提控制器在圆目标轨道上节省29%推进剂，在偏心轨道上节省40%，且几乎每次都能满足0.20 m捕获要求，中位脱靶量约5 cm（圆轨道499/500次满足，椭圆轨道500/500次满足，而基准变体分别为468、463和452/500）。但代价是飞行时间和计算量增加，且节省来自保证对终端条件的要求而非更好的扰动抑制。此外，规则判定homing阶段在300 km处超出其自身极限23倍，最坏单步残差超出扰动界497和852倍；改用相对轨道要素后恢复保证。控制器的认证偏心率阈值随采样周期变化：T_s=50 s时为0.851，T_s=900 s时为0.249。

### 四、结论（Conclusion）
所提出的horizon-dependent tube MPC通过将预测模型的线性化误差与扰动集比较，导出了保证失效的距离界限，并将其作为设计规则，能够预先评估控制器在给定轨道和采样周期下是否有效。在MSR任务中，该规则识别出homing阶段不可用，通过重新建模可恢复保证；同时，时域与鲁棒裕度的联合选择在枚举中完成，相比固定最坏情况管宽显著节省推进剂。但节省以飞行时间和计算为代价，且不声称递归可行性和渐近稳定性。

### 五、方法论与关键技术细节
关键细节包括：质量不确定性建模为输入矩阵乘性标量δm，δm_max∈[0.02,0.10]，但报告中的500次冻结随机种子仿真未激活质量误差通道（mass_err_max=0），所有结果仅基于加性扰动界w̄；有效性界限s*=√(w̄a/C)/(nT_s)在T_s=300 s时为26.4 km，T_s=600 s时为13.2 km，homing阶段以600 s采样但开环距离300 km，超限23倍；约束紧缩逐时域递归传播，终端容差为tol_j−e_j(N)，时域搜索上限N_max成为任务参数；控制器采用YA离散状态转移矩阵，输入B_k=A_k[0;I]，扰动为逐元素界|w_k|≤w̄；对半长轴误差和目标真近点角的联合条件导致失败边界，单一变量扫参无法定位；对比基准采用Hartley 2012的相位架构和J=N+w_u‖u‖_1目标函数，w_u不变；未验证递归可行性和渐近稳定性，质量不确定性主动激活的后续实验未完成。
