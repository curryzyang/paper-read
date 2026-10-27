# Neuromorphic Decision Dynamics for Deadlock-free Safe Navigation in Congested Environments

- 区域：精读区
- 排名：3
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Himani Sinhmar, Vaibhav Srivastava, Naomi Ehrich Leonard
- 机构：Princeton University, Michigan State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33271v1) · [PDF](https://arxiv.org/pdf/2610.33271v1)

## TLDR
The paper introduces neuromorphic decision dynamics, a decentralized event-based controller that couples local motion cues with internal decision states to achieve scalable, communication-free, deadlock-free safe navigation in congested multi-agent environments with provable safety and liveness guarantees.

## Abstract
Safe navigation in congested environments requires both collision avoidance and coordinated passage. We introduce neuromorphic decision dynamics (NDD), a decentralized, event-based controller, that provides navigation in congested spaces with guarantees on safety, liveness, robustness, and scalability. NDD makes safe-and-live deconfliction a controllable, locally tunable emergent property of local agent interactions, without requiring communication, preassigned priorities, models of neighbors' objectives or future actions, or estimates of group size or global network properties. By design, NDD couples the dynamics of internal decision and attention states with changing physical states and locally observed relative motion. Each agent continuously modulates its speed along its prescribed path, responding as soon and as much as conflict resolution requires. Agents self-organize into disjoint, locally engaged groups that resolve conflicts concurrently. When any group's conflict becomes safety-critical, decision-action feedback destabilizes collective indecision, and coordinated conflict-resolution emerges that stabilizes a safe traversal order within the group. Order persists as conflicts clear, but groups may split or merge as agents autonomously adapt to new conflicts and those with resolved conflicts resume their nominal motion. We derive explicit conditions on sensing range, feedback gains, response time scales, and actuation limits that guarantee collision avoidance and traversal-order formation in finite time with no deadlock or livelock for finite, heterogeneous agent populations of arbitrary, changing size. Computational cost scales with the number of local interactions sensed by each agent. Large-scale simulations, comparisons with existing approaches, and hardware experiments demonstrate NDD in complex congested scenarios and validate its scalability.


## 精读解读（中文）
### 一、研究动机
拥挤环境中的多智能体安全导航不仅要求避碰，还要求形成协调的通行顺序，否则容易陷入互相让行、冻结或反复调整导致的死锁与活锁。现有方法多先预测邻居意图再规划动作，依赖可预先确定且稳定的交互结构，在无通信、只有局部观测、无预设优先级且群体规模任意时变时难以保证安全性与活性。

### 二、技术方案（Method）
NDD为每个智能体增加决策状态z_i和注意状态u_i，仅利用传感范围内邻居的相对位置与速度构造交互的争用区域、占用时间区间和冲突证据h，并通过tau_z zdot_i=-rho_z z_i+S(u_i h)、tau_u udot_i=-rho_u u_i+u0+kappa_u z_i^2连续更新内部状态，其中S为有界奇sigmoid如tanh。冲突证据由冲突压力P、归一化交互权重W和到达顺序符号G聚合，反映冲突严重度、相对重要性和应加速或减速的倾向。决策状态经有界保号映射V(z_i)调制沿既定路径的指令速度v_cmd=v_nom+V(z_i)，再由tau_v vdot_i=f_v(v_i,v_cmd)的低层跟踪控制器执行；该方法无训练环节，在线连续或事件触发更新，通常只调速度、不频繁重规划路径。

### 三、结果（Result）
论文推导出关于传感范围、反馈增益、响应时间尺度和执行器限制的显式条件，保证有限规模、异构且数量时变的智能体群体在有限时间内实现避碰和通行顺序形成，并避免死锁与活锁。安全关键冲突会通过决策-动作反馈使集体犹豫平衡失稳，局部群组自组织并同时解决冲突，冲突解除后群组可分裂或合并并恢复名义运动。大规模仿真、与现有方法对比及硬件实验展示了该方法在复杂拥挤场景中的有效性，并验证计算代价随每个智能体感知到的局部交互数缩放。

### 四、结论（Conclusion）
NDD将安全且具活性的解冲突转化为可由局部交互参数调节的可控涌现属性，无需通信、预设优先级、邻居目标或未来动作模型，也无需群体规模或全局网络信息。该框架为无通信、局部观测和异构平台下的多机器人拥挤导航提供了具有安全性与活性保证的分散式事件驱动控制方案。

### 五、方法论与关键技术细节
关键设计包括基于投影射线、交叉角和安全距离d_safe构造争用段，并用进入与离开时间形成占用区间来判定冲突；冲突压力P刻画最近接近与时间重叠的严重度，权重W对所有同时交互归一化且softmax为候选，到达顺序函数G由进入时间差给出符号。决策与注意动态涉及tau_z、tau_u、rho_z、rho_u、u0、kappa_u和速度跟踪tau_v等参数，sigmoid满足S'(0)=1并有界。分析假设名义路径光滑、感知与相对运动预测不确定性及执行误差有界、低层控制器能在已知有界瞬态内跟踪 admissible 速度，且共同传感半径取保证互感知的下界，较大半径可更早响应。局限包括依赖局部观测和保守传感条件、直接对头等场景可能仍需稀疏路径重规划，且计算复杂度随局部交互数增长。
