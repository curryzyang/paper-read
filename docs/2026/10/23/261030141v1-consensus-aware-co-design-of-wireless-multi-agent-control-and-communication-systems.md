# Consensus-Aware Co-design of Wireless Multi-Agent Control and Communication Systems

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Atefeh Termehchi, Sajedeh Soleimani, Shiva Kazemi Taskooh, Mehdi Rasti, Ekram Hossain
- 机构：Amirkabir University of Technology, University of Manitoba, University of Oulu
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30141v1) · [PDF](https://arxiv.org/pdf/2610.30141v1)

## TLDR
This paper proposes a consensus-aware co-design framework that jointly optimizes consensus-topology selection and D2D/cellular wireless resource allocation via a polynomial two-stage algorithm to minimize bandwidth while guaranteeing multi-agent consensus and QoS, achieving 24–27% bandwidth savings in a smart-grid case study.

## Abstract
Autonomous multi-agent control systems (MACSs) enable distributed coordination in emerging applications such as smart power grids and autonomous vehicle or drone networks. In many of these applications, inter-agent communication relies on wireless networks. However, conventional MACS designs neglect the interaction between the communication and control subsystems. At the same time, conventional wireless designs reserve communication resources based on worst-case MACS requirements. Consequently, control performance is degraded and wireless resources are utilized inefficiently. To address these challenges, we propose a consensus-aware co-design approach for MACSs and wireless communication systems. We introduce a system model in which agents achieve consensus by exchanging information through device-to-device (D2D) links that share spectrum with cellular users under limited bandwidth resources. Based on this model, we formulate a joint optimization problem for consensus-topology selection and wireless resource allocation to minimize bandwidth consumption while guaranteeing consensus and satisfying the quality-of-service (QoS) requirements of both MACSs and cellular users. Although the resulting problem is a mixed-integer nonlinear program (NP-hard in general), a structural property of the optimal solution enables a sequential two-stage optimization algorithm with polynomial complexity. Simulations on a smart power grid case study demonstrate that the proposed approach achieves 24-27% bandwidth savings compared with the two baselines while maintaining consensus and satisfying all QoS requirements of the control agents and the communication users.


## 精读解读（中文）
### 一、研究动机
传统多智能体控制系统设计通常把智能体间通信抽象为连通图或时延、丢包等指标，忽略无线通信子系统与控制子系统的双向耦合；同时无线资源又按最坏情况预留，导致控制性能下降和带宽利用低效。面向智能电网、车联网和无人机网络等无线使能多智能体应用，需要显式建模通信与控制交互，并联合优化一致性拓扑与无线资源。

### 二、技术方案（Method）
论文构建由基站、多个控制智能体和多个蜂窝用户组成的系统模型，控制智能体通过D2D链路共享频谱交换状态信息，时间划分为时隙且每个时隙内资源分配与通信图保持不变、跨时隙可变化。基于连续时间多智能体动力学和时变无向图，联合优化一致性拓扑选择与无线资源分配，在保证MACS一致性、控制智能体与蜂窝用户最小QoS以及总带宽预算约束下最小化带宽消耗。该问题为混合整数非线性规划且一般NP难，但利用最优解的结构性质将搜索空间无损缩减，设计按每个时隙顺序执行的两阶段多项式复杂度算法。

### 三、结果（Result）
在智能电网案例仿真中，所提一致性感知联合优化方法相比两个基线实现24–27%的带宽节省，同时维持MACS一致性并满足控制智能体和蜂窝用户的全部QoS要求。结果说明利用联合连通性和控制-通信耦合可以在不牺牲控制与通信服务质量的前提下显著降低无线带宽消耗。

### 四、结论（Conclusion）
论文表明无线多智能体控制系统需要将一致性拓扑选择与D2D无线资源分配联合设计，而非分别按最坏情况处理；所提出的结构性质与两阶段算法为无线使能MACS提供可计算且有效的协同设计途径。该工作凸显了控制感知无线资源管理在提升带宽效率和保障控制性能方面的潜力。

### 五、方法论与关键技术细节
关键建模细节包括：D2D链路与蜂窝用户共享总带宽但分配互不重叠子带以在频域避免干扰；若某时隙内两智能体间D2D资源足以支持信息交换并满足可允许传输时延界，则图中对应边存在；系统动力学为带分段常数切换通信拓扑的连续时间多智能体模型，可用图拉普拉斯描述。优化约束涵盖一致性、控制智能体与蜂窝用户QoS及总带宽预算，核心理论点是Lemma 2给出的最优解结构性质使NP难MINLP可化为每时隙多项式复杂度的顺序两阶段求解。局限性包括时隙内资源与拓扑恒定、频域正交假设简化了干扰、主要基于智能电网仿真验证。
