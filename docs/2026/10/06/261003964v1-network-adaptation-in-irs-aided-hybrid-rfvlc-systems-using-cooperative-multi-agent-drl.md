# Network Adaptation in IRS-Aided Hybrid RF/VLC Systems Using Cooperative Multi-Agent DRL

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Ahrar N. Hamad, Ahmad Adnan Qidan, Taisir E. H. El-Gorashi, Jaafar M. H. Elmirghani
- 机构：King’s College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03964v1) · [PDF](https://arxiv.org/pdf/2610.03964v1)

## TLDR
This paper proposes a cooperative multi-agent deep reinforcement learning framework to jointly optimize RF/VLC technology selection, power allocation, and mirror-based IRS orientation in dynamic indoor hybrid RF/VLC networks, maximizing proportional fairness and outperforming standalone and benchmark approaches.

## Abstract
Hybrid radio frequency (RF) and visible light communication (VLC) networks have emerged as a promising solution for high-capacity indoor wireless connectivity in sixth-generation (6G) systems. However, the limited optical coverage and vulnerability of VLC links to line-of-sight (LoS) blockage under user mobility remain fundamental challenges. In this work, a mirror-based intelligent reflecting surface (IRS) is deployed to assist a dynamic indoor hybrid RF/VLC network, where each mobile user is exclusively assigned to either the IRS-enhanced VLC subnetwork or the RF subnetwork through a binary selection decision. A joint optimization problem is then formulated to maximize proportional fairness by jointly optimizing the RF/VLC technology selection, power allocation, and IRS mirror roll and yaw orientation angles. To enable real-time adaptability, the problem is reformulated as a Markov decision process (MDP) and solved using a cooperative multi-agent deep reinforcement learning (DRL) algorithm based on centralized training with decentralized execution. Simulation results demonstrate the superior performance of the optimized hybrid network compared with optimized standalone VLC and RF networks. The results further validate the practicality and effectiveness of the proposed DRL framework compared to widely adopted DRL algorithms as well as conventional model-based optimization approaches.


## 精读解读（中文）
### 一、研究动机
面向6G室内高容量无线连接，混合RF/VLC可兼顾光通信高速率、免射频干扰与RF覆盖可靠性，但VLC覆盖受限于视距链路且易被遮挡，用户移动下更难保障连通。为此论文引入基于反射镜的IRS辅助动态室内混合RF/VLC网络，希望同时解决VLC覆盖扩展、遮挡规避、用户关联与资源分配问题。

### 二、技术方案（Method）
论文考虑下行室内IRS辅助混合RF/VLC系统，含LED AP、墙面RF AP、按随机路点移动的多用户、多分支角度分集VLC接收机和RF天线，用户二选一接入VLC或RF。以最大化比例公平效用log(R_k)为目标，联合优化二元RF/VLC选择α_k、两子网功率分配P_k^(v)/P_k^(r)以及IRS镜子roll角φ_m和yaw角ϑ_m，约束包括最小QoS、VLC/RF功率预算、归一化功率界和镜子转角范围。由于P1为混合整数非凸问题，论文将其重构建为MDP，并采用基于集中训练分散执行CTDE的合作多智能体DRL求解：训练阶段中心控制器汇总全局信道状态与用户信息学习协作策略，执行阶段各智能体依据本地观测实时输出技术选择、功率与IRS朝向决策。

### 三、结果（Result）
仿真结果表明，优化后的IRS辅助混合RF/VLC网络性能优于单独优化的VLC网络和RF网络，说明混合架构与IRS反射增益能提升覆盖率与公平性。结果还显示所提合作多智能体DRL框架相较广泛采用的DRL算法以及传统基于模型的优化方法更具实用性和有效性。摘要未给出具体速率增益、公平性指数或收敛轮数等数值指标，因此解读中不引用确切数值。

### 四、结论（Conclusion）
该工作证明在动态室内混合RF/VLC场景中，将IRS镜面朝向控制、RF/VLC接入选择和功率分配联合优化可提升比例公平性与网络适应能力。采用CTDE多智能体DRL能够处理离散-连续混合动作和非凸目标，适合用户移动与遮挡导致的信道时变环境。总体结论是IRS辅助加合作DRL为6G室内混合光无线网络的实时资源管理提供了可行路径。

### 五、方法论与关键技术细节
关键建模细节包括VLC总信道由LoS与IRS反射NLoS组成，LoS以伯努利过程建模遮挡，VLC采用Lambertian辐射模型和IM/DD SINR，RF采用Rician衰落与大尺度路径损耗；IRS反射链路依赖镜面反射系数、镜面面积及roll/yaw决定的入射与辐射角。优化约束含每用户最小速率、两子网功率预算、功率系数范围及镜子角度范围，目标为比例公平log(R_k)，能平衡总速率与用户公平。实现上采用集中训练分散执行的多智能体DRL，输入为AP与用户侧信道状态信息，动作对应二元接入、连续功率和IRS朝向；但预览未给出网络结构、学习率、折扣因子、经验回放、训练轮数等超参。局限性在于依赖仿真室内信道模型、CSI获取与训练开销，模型参数变化和真实环境泛化仍需验证。
