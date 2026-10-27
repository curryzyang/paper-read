# Interpretable Collision Avoidance and Feasibility Guarantees through an Uncertainty Aware Pipeline

- 区域：精读区
- 排名：2
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Doris Xu, Jin Hyun Park, Guadalupe Alvarado Fernandez, Adhyan Prasad, Mark Campbell
- 机构：Cornell University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33186v1) · [PDF](https://arxiv.org/pdf/2610.33186v1)

## TLDR
This paper presents a modular perception-prediction-planning pipeline that propagates intent, trajectory, and localization uncertainty as interpretable structured quantities to construct convex safe sets, thereby guaranteeing collision avoidance and real-time solver feasibility—achieving 0% collisions and 0% infeasibility at 12.7 ms per cycle in unsignalized-intersection trials.

## Abstract
Autonomous vehicles (AVs) operating in dynamic, challenging conditions such as intersections and roundabouts must guarantee collision avoidance under uncertainty while maintaining real-time feasibility. Most existing planners struggle to simultaneously guarantee both requirements. Chance-constrained formulations embed safety constraints directly in the optimization but become infeasible as uncertainty compounds; deterministic planners provide feasible solutions but fail to address the uncertainty that causes collisions; end-to-end learned policies provide neither guarantee in an interpretable form.
  We present a modular perception-prediction-planning pipeline that closes this gap by propagating uncertainty as structured, interpretable quantities across module boundaries. Rather than embedding probabilistic risk directly in the optimization, our pipeline resolves collision probabilities upstream and constructs convex safe sets within which the planner provides a guaranteed feasible solution at every cycle -- decoupling the safety guarantee from solver feasibility.
  Across Monte Carlo trials in a four-way unsignalized intersection, our pipeline achieves 0% collisions and 0% solver infeasibility at 12.7ms per cycle, compared to 36% and 10% collision rates for deterministic and chance-constrained baselines respectively. The ablation study confirms the necessity of each uncertainty source and the hardware deployment on Clearpath Jackal UGVs validates the pipeline's real-time viability on physical platforms.


## 精读解读（中文）
### 一、研究动机
自动驾驶车辆在交叉口、环岛等动态不确定场景中必须同时保证碰撞避免与实时可行性，但确定性规划器忽略不确定性、机会约束规划随不确定性累积易不可行、端到端学习缺乏可解释安全裕度与可行性保证。论文旨在填补多模态不确定性从感知到规划的结构化传播以及安全与可行性联合保证之间的空白。

### 二、技术方案（Method）
提出模块化感知-预测-规划流水线：用交互多模型IMM联合估计他车离散意图概率与连续运动状态，以道路几何定义直行、左转、右转等模式并并行运行EKF；对每个意图用Sigma点滤波结合自行车模型、横向车道保持与速度控制器预测带协方差的轨迹；自车用EKF估计位姿与定位协方差；碰撞检测将车辆建模为OBB，在最近接近时刻将自车与预测协方差之和投影到中心连线方向，用正态CDF解析计算各意图碰撞概率；决策模块沿最可能意图扫掠OBB构造不安全区域与凸安全集并给出中间目标位姿，下游微分平坦MPC在安全集内规划，二阶CBF安全滤波器保证前向不变性。

### 三、结果（Result）
在四向无信号交叉口的蒙特卡洛试验中，该流水线实现0%碰撞和0%求解器不可行，单周期耗时12.7 ms；确定性基线与机会约束基线的碰撞率分别为36%和10%。消融实验确认意图、轨迹预测和定位等每种不确定性来源均必要，Clearpath Jackal无人车硬件部署验证了实时可行性。

### 四、结论（Conclusion）
该工作通过在上游解析碰撞概率并构造凸安全集，将概率安全保证与求解器可行性解耦，使规划器每个周期都能在安全集内获得可行解。流水线以可解释的结构化量传播多模态不确定性，同时提供碰撞避免与实时可行性保证，并在仿真基准和实体平台上验证了有效性。

### 五、方法论与关键技术细节
关键实现包括：IMM模式集由道路几何生成并递归更新模式概率，SPF使用2n_x+1个Sigma点、过程噪声Q和闭环道路跟踪模型限制协方差增长；碰撞概率采用OBB几何、最近接近点搜索、组合协方差投影及包围圆半径r_col形成风险上界；决策模块基于最可能意图构造凸安全集，MPC与CBF-QP的凸性保证每周期可行性；方法不涉及端到端训练损失，主要约束与局限在于高斯/线性化投影和上界近似可能保守，安全集构造依赖最可能意图、道路模式集与车辆尺寸假设，概率保证条件于上游不确定性模型。
