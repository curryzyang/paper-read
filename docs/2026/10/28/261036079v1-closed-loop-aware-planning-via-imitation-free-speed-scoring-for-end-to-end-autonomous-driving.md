# Closed-Loop Aware Planning via Imitation-Free Speed Scoring for End-to-End Autonomous Driving

- 区域：精读区
- 排名：3
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Emad Aghajanzadeh, Thomas Schwarzfischer, Marc Kaufeld, Moritz Thoma, Ryan Pégoud, Manoj Rohit Vemparala, Pierpaolo Mori, Nael Fasfous, Johannes Betz, Daniel Mueller-Gritschneder, Ulf Schlichtmann
- 机构：Technical University of Munich, BMW Group, TU Wien
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.36079v1) · [PDF](https://arxiv.org/pdf/2610.36079v1)

## TLDR
The paper introduces CLAP-AD, a plug-in planning head for end-to-end autonomous driving that learns path prediction via imitation while scoring candidate speeds with safety-grounded multi-criteria functions, enabling explicit test-time speed control and improving closed-loop driving and speed-adherence performance.

## Abstract
End-to-end autonomous driving has predominantly relied on open-loop imitation learning for training, which presents two limitations. First, expert demonstrations show only one behavior per scenario, so the model cannot learn alternative valid behaviors and, in turn, cannot adapt to user-specified preferences at test time. Second, noise or ambiguity in these demonstrations can produce inconsistent, unreliable supervision for the end-to-end models. Driving is inherently multi-modal: multiple different behaviors can be valid responses to the same scene, and this diversity arises largely from speed rather than path. We introduce a planning paradigm that learns the path through imitation while scoring a set of candidate speeds across multiple criteria with a learned function supervised by physically grounded safety constraints. We realize this paradigm as Closed-Loop Aware Planning for Autonomous Driving (CLAP-AD), a plug-in planning head that integrates with existing end-to-end driving models and, to our knowledge, is the first to enable explicit test-time control over their speed selection without speed-conditioned training. On Bench2Drive-Speed, CLAP-AD sets a new state of the art Speed-Adherence Score of 82.53, topping TFv6, the strongest baseline on this metric, by 12.9 points while retaining strong closed-loop driving performance. On Bench2Drive, it improves driving score by +28.5 and +32.7 over UniAD and VAD, and on NAVSIM v2, built on real-world driving data, EPDMS by +6.1 over its backbone. Project page: https://clap-ad.github.io


## 精读解读（中文）
### 一、研究动机
端到端自动驾驶主要依赖开环模仿学习，但专家示范每个场景只展示一种行为，模型无法学习其他同样有效的行为，也无法在测试时适应用户偏好；同时示范中的噪声或歧义会带来不一致监督。驾驶本质上是多模态的，同一场景存在多种有效行为，而这种多样性主要来自速度而非路径。因此需要将路径与速度分开，用不同目标学习：路径保留模仿学习，速度改用多准则评分。

### 二、技术方案（Method）
CLAP-AD是一个可插入现有端到端模型的规划头：先由统一规划查询、导航命令和上游运动/检测查询经MLP融合后送入GRU，自回归预测基于距离的路径点；再将路径表示分别送入碰撞、交通灯和停车标志三个评分分支，每个分支用路径MLP与准则相关上下文查询做交叉注意力，并由评分MLP输出各预定义速度类的安全logit。训练时路径用模仿学习，速度评分不用专家速度模仿，而由开环日志数据构造物理约束监督：碰撞目标取固定时域内沿预测路径与其他动态交通参与者的最小距离并做结构化路径增强，交通灯/停车标志目标由所需减速度a_req=v^2/(2d_stop)按舒适减速度与最大减速度分段生成。推理时各评分头输出独立安全分数而非概率分布，将全部准则超过阈值的速度类视为可行，再按用户目标速度选择最近可行类，无可行类则回退到0 m/s制动，最后由横向PID跟踪路径、纵向PID根据目标速度与当前车速生成油门/制动。

### 三、结果（Result）
在Bench2Drive-Speed上，CLAP-AD取得82.53的Speed-Adherence Score，比该指标最强基线TFv6高12.9分，并在每个骨干上提升速度依从性最多25.2分；其变体是对比中唯一达到70以上高可控区的方案。在Bench2Drive闭环评测中，相比UniAD和VAD分别提升驾驶分数+28.5和+32.7；在基于真实驾驶数据的NAVSIM v2上，相比LTFv6骨干提升EPDMS +6.1，而在TFv6上驾驶性能保持在基线数分以内。

### 四、结论（Conclusion）
结果表明，将路径模仿学习与多准则速度评分解耦，可在不进行速度条件训练的情况下为现有端到端模型提供显式测试时速度控制，并在提升可控性的同时保持较强闭环驾驶性能。该设计使安全评分可解释、可按准则归因失败，并作为可扩展插件规划头适配不同上游架构。

### 五、方法论与关键技术细节
实验覆盖Bench2Drive的1000段开环训练片段、44个CARLA场景和220条闭环测试路线，Bench2Drive-Speed的48条按Easy/Medium/Hard划分路线，以及NAVSIM v2真实数据伪仿真；指标包括DS、SR、Efficiency、SA和EPDMS，且因测量问题未报告Comfort。关键实现包括碰撞监督仅考虑动态参与者并排除静态物体、用路径增强提升碰撞监督多样性、交通灯/停车标志按所需减速度在舒适与最大减速度之间平滑衰减、速度分支前对路径表示做梯度截断以隔离速度评分对路径学习的影响。评分头将各速度类视为独立安全度量而非归一化概率，部署时依赖固定阈值筛选可行速度类并按用户请求选择最近类，因此无需改架构或重训练。局限性在于准则仅覆盖碰撞、交通灯和停车标志三类代表性安全因素，评分依赖上游检测/运动查询质量，且开环日志构造目标与固定阈值选择策略在更复杂交互场景中的鲁棒性仍需验证。
