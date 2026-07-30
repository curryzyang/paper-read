# Multi-Objective Compliance-Integrated Coevolution For Simulated And Real-World Deployment Of Multi-Robot Marine Autonomy

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Everardo Gonzalez, Tyler M. Paine, Manuel Agraz Vallejo, Gaurav Dixit, Michael R. Benjamin, Kagan Tumer
- 机构：Oregon State University, MIT
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26279v1) · [PDF](https://arxiv.org/pdf/2607.26279v1)

## TLDR
The paper introduces Marine Multi-Objective Compliance-Integrated Coevolution (MMOCIC), a framework that decouples learning from compliance to blend coevolved team behaviors with prescribed norm adherence, achieving high performance and collision avoidance in multi-robot marine missions across simulated and real-world deployments.

## Abstract
Collaborative robots are well-suited to maritime missions that benefit from coordination, such as the exploration of unknown reef structures, inspection of subsea infrastructure, or search-and-rescue operations. These missions typically provide sparse feedback signals for measuring progress and require adherence to safety and regulatory norms, turning a mission into a multi-objective optimization problem. Coevolutionary algorithms can process these sparse feedback signals to generate coordinated behaviors, and in some cases extend behaviors to multiple objectives. However, incorporating high-level team objectives with low-level compliance considerations on the fly to balance norm adherence with team performance remains elusive. This paper introduces a multi-objective framework that blends coevolved behaviors with compliance behaviors to achieve a balance between maximizing team progress and minimizing norm violations. The key insight is to decouple learning from compliance since operational norms are prescribed rather than discovered. We demonstrate that our framework achieves high team performance while avoiding collisions on a collaborative swimmer rescue mission with up to 8 vehicles in a hardware deployment, and 12 vehicles in simulation. The key contribution of this paper is Marine Multi-Objective Compliance-Integrated Coevolution (MMOCIC), a framework that blends team-wide optimization with established norms for real-world deployments of learning-based coordination.


## 精读解读（中文）
### 一、研究动机
海事任务中协同机器人面临稀疏反馈信号和严格的合规要求，需要同时最大化团队进度和最小化规范违反。现有协同进化算法虽能处理稀疏目标，但难以动态整合高层团队目标与低层合规考虑，实现实时平衡。

### 二、技术方案（Method）
提出Marine Multi-Objective Compliance-Integrated Coevolution (MMOCIC)框架，采用集中训练分散执行范式。在仿真中通过合作协同进化算法（CCEA）为每台车辆进化神经网络作为协同行为目标；结合预设的COLREGs合规行为和Stay-In-Bounds边界行为，通过加权标量化（权重连续）混合三种行为。硬件部署时引入基于控制屏障函数（CBF）的安全过滤器，在极端接近时覆盖控制输入防止碰撞。训练时可选择激活或停用合规行为，实现零样本权重调整。

### 三、结果（Result）
在协作游泳救援任务中，硬件部署8辆车、仿真12辆车均实现高救援成功率同时避免碰撞。通过零样本调整权重可动态平衡救援数量与合规水平，无需重新训练，展示了灵活的可调性能-合规权衡。

### 四、结论（Conclusion）
MMOCIC有效解耦学习与合规，使协同进化专注于发现协调行为，预设合规行为确保规范遵守，在真实世界多机器人部署中实现了团队优化与既定规范的融合。

### 五、方法论与关键技术细节
关键细节：解耦学习与合规的核心洞察——合规是预设而非发现；差值适应度（Difference Fitness）用于稀疏团队目标下的个体贡献估计；CBF安全过滤器提供硬件部署的关键安全层；权重标量化允许零样本调节性能与合规；预设合规行为（COLREGs、Stay-In-Bounds）可覆盖协同进化生成的极端动作。不足之处包括：CBF依赖准确动力学模型，预设行为可能限制协同进化探索空间。
