# Taming an End-to-End Autonomous Driving Policy for Urban Navigation of Quadruped Robots

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Joochan Kim, Chanuk Yang, Tackgeun You, Ziran Wang, Hwasup Lim
- 机构：Purdue University, Korea Institute of Science and Technology (KIST)
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08812v1) · [PDF](https://arxiv.org/pdf/2610.08812v1)

## TLDR
Go2-DrivoR adapts the DrivoR end-to-end driving planner to goal-conditioned urban navigation for quadruped robots by adding local-subgoal token conditioning and redefining drivable-area and progress scores, enabling improved waypoint-conditioned planning in unseen simulations and zero-shot real-world open-loop trajectory prediction after training only on TartanGround simulation data.

## Abstract
We present Go2-DrivoR, a goal-conditioned adaptation of the end-to-end autonomous driving trajectory planning framework DrivoR for urban navigation with quadrupedal robots. By conditioning trajectory generation on a local-frame subgoal through a goal token and adapting the vehicle-centric scoring formulation, the method extends DrivoR to short-horizon goal-conditioned local planning without redesigning its core decoders. Specifically, we redefine drivable-area compliance for sidewalk-oriented navigation and reformulate the original ego progress term as goal-conditioned ego progress. Trained exclusively on TartanGround simulation data, Go2-DrivoR improves waypoint-conditioned planning performance on unseen simulation environments and transfers zero-shot to open-loop real-world trajectory prediction.


## 精读解读（中文）
### 一、研究动机
四足机器人在城市道路、人行道与混合区域导航时缺少车道中心线和固定路线几何，需在腿式运动约束下根据视觉与本体状态进行短时域、目标条件局部规划；现有面向车辆的端到端规划器DrivoR虽具备寄存器token视觉编码与解耦轨迹评分，但其可行驶区域合规与进度定义面向道路对齐，且缺乏对局部子目标的显式条件，因此难以直接迁移到四足机器人。

### 二、技术方案（Method）
方法基于DrivoR保留视觉特征提取器、轨迹解码器、评分解码器与winner-takes-all轨迹目标，输入四路鱼眼图像、机器人本体状态、高层方向指令以及当前自车坐标系下的二维局部目标；局部目标由当前时刻后4秒的专家位姿变换到自车系并除以d_scale=4 m归一化，经线性投影得到goal token，与本体状态token拼接融合后以残差方式加到K=64个可学习轨迹查询上，由轨迹解码器输出8个0.5秒间隔、跨4秒的(x,y,θ)候选轨迹。评分器从原六项改为五项监督分量：NOC、DAC、TTC、GEP与comfort，省略DDC；NOC/TTC沿用原公式但改用四足机器人足迹，DAC重定义为候选轨迹所有采样点在人行道得1、至少一点在道路且无点越界得0.5、否则得0，GEP=(1-α)EP+α·Goal，其中Goal为候选轨迹终点相对起点的位移在目标方向上的投影并裁剪到[0,1]，α=0.5。推理时用对数域组合分数log(NOC)+log(DAC)+log(5·TTC+5·GEP+2·Comfort)对候选排序，评分头用逐分量BCEWithLogits监督，轨迹损失与评分损失等权联合优化且评分梯度不经过预测轨迹回传到轨迹解码器。数据与训练上，仿真使用TartanGround的14,192个局部规划样本，将多相机针孔图重投影为前/左/右/后四路鱼眼，状态转至ENU/FLU，按滑动窗口构造局部样本，并以4秒后位姿作为局部目标与高层四向指令来源；真实数据用Unitree Go2四路GMSL Owl相机采集，人工遥操作轨迹作为专家，原始鱼眼图直接输入并将FRD转FLU，训练20个epoch，AdamW，3张H200，全局batch size 48，学习率5e-4，2 epoch warm-up后余弦退火。

### 三、结果（Result）
在TartanGround开环评测中，Go2-DrivoR在已见与未见地图上的PDMS风格聚合分数均高于匀速外推基线和零样本iPlanner，并在NOC、TTC、DAC、comfort上平均更高；iPlanner在未见地图上GEP略高，但综合分数仍低于Go2-DrivoR。真实Unitree Go2日志零样本开环测试中，Go2-DrivoR在ADE、FDE@1s、FDE@2s、FDE@4s和Heading MAE上全面优于匀速基线，且因以4秒前视路点做条件，FDE@4s提升最明显；定性示例显示路口处能选择转向目标的轨迹而匀速基线沿原方向前进。消融显示移除goal token会显著恶化轨迹预测与目标导向指标，α=0或α=1（仅EP或仅Goal）均差于α=0.5的融合GEP；论文中一个仿真定性样例的评分器预测NOC=0.993、DAC=1.000、TTC=0.994、GEP=0.924、comfort=1.000，聚合分0.959，真实样例聚合分0.693。

### 四、结论（Conclusion）
Go2-DrivoR通过局部帧子目标条件、面向人行道的DAC重定义和GEP重述，在不重设计核心解码器的前提下把DrivoR轻量适配为四足城市目的地导航的局部规划器。仅用TartanGround训练即可在未见仿真地图上提升规划表现，并零样本迁移到真实Go2开环轨迹预测。主要局限是使用专家导出的前视目标、仅做开环真实评测、未显式建模动态智能体；未来工作指向闭环社交导航、时序场景建模和更好的sim-to-real适配。

### 五、方法论与关键技术细节
关键实现包括：目标用4秒后位姿在当前自车系表达并归一化，轨迹固定为K=64、8个0.5秒间隔路点、4秒时域；评分分量权重为NOC与DAC先验约束、TTC与GEP各5、comfort为2，评估用NOC·DAC/12乘以加权和；损失为各分量BCEWithLogits，轨迹与评分等权联合训练但评分梯度不穿过预测轨迹。数据侧，TartanGround多相机图经双球相机模型重投影为四路鱼眼，语义点云投影成boundary/roadway/walkway 2D向量层用于评分标签，真实Go2使用90°间隔四目GMSL Owl相机并人工遥操作作为专家。推理复杂度体现为单张H200上batch size 1延迟10.8 ms、batch size 16延迟94.1 ms；局限还包括动态智能体未建模、真实数据仅开环评估、消融中goal token移除后劣于匀速的原因尚未定位到候选生成还是评分环节。
