# Multi-Timescale Latent-Action DRL for Joint Optimization in Edge-Cloud Networks

- 区域：精读区
- 排名：7
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Vo Phi Son, Van-Dinh Nguyen, Ngoc Hung Nguyen, Trinh Van Chien, Symeon Chatzinotas
- 机构：University of Luxembourg, Trinity College Dublin, Phenikaa University, VinUniversity, Hanoi University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18288v1) · [PDF](https://arxiv.org/pdf/2607.18288v1)

## TLDR
The paper proposes a two-timescale deep reinforcement learning framework with a latent action space to jointly optimize service placement, computational delegation, and power control in hierarchical edge-cloud networks, achieving near-optimal latency and resource utilization with faster convergence.

## Abstract
Load imbalance across edge and cloud layers degrades latency performance in hierarchical edge-cloud computing (HECC) systems under dynamic task arrivals and heterogeneous resources, leading to severe queuing delays and inefficient resource utilization. To address this challenge, we study a joint service placement, computational delegation, and power control (JSCP) problem to minimize the average end-to-end (e2e) latency. The resulting JSCP problem is a mixed-integer nonconvex and NP-hard optimization problem due to the strong coupling between discrete and continuous variables. To enable tractable optimization and stable system adaptation, we exploit the inherent difference in decision dynamics and decompose the problem into long-term system configuration and short-term resource allocation subproblems. Based on this formulation, we propose a two-timescale multi-layer deep reinforcement learning framework with a latent action space (2T-MDRL-LA) to jointly optimize service placement, user association, computational delegation, task offloading, and user transmit power. A latent action representation based on a variational autoencoder is introduced to efficiently compress the high-dimensional combinatorial action space. Simulation results demonstrate that the proposed framework effectively adapts to dynamic network conditions and achieves near-optimal performance compared to branch-and-bound solutions. It achieves up to a 20.8% reduction in average e2e latency and a 13% improvement in resource utilization over the scheme without the computational delegation, while converging approximately 50% faster than conventional proximal policy optimization.


## 精读解读（中文）
### 一、研究动机
在分层边缘-云计算系统中，动态任务到达和异构资源导致边缘和云层之间的负载不平衡，从而显著增加端到端延迟并降低资源利用率。现有方法常忽略计算委派或无法处理高维组合动作空间，缺乏一个统一的可扩展优化框架。

### 二、技术方案（Method）
该研究构建了联合服务放置、计算委派和功率控制（JSCP）问题，并将其分解为长期系统配置和短期资源分配两个子问题。提出两时间尺度多层深度强化学习框架（2T-MDRL-LA），利用变分自编码器（VAE）对长期离散动作空间进行潜在表示压缩，并结合映射表实现高效探索；短期连续动作采用近端策略优化（PPO）进行稳定更新。系统输入为当前网络状态（包括任务队列、信道条件和资源状态），输出为服务放置、用户关联、计算委派、任务卸载和发射功率的联合决策。训练过程采用两时间尺度交替更新：长期决策每时间槽更新一次，短期决策每子时间槽更新一次。

### 三、结果（Result）
仿真结果表明，所提框架能有效适应动态网络条件，与分支定界最优解相比实现近优性能，平均端到端延迟降低高达20.8%，资源利用率提升13%，且收敛速度比传统PPO快约50%。

### 四、结论（Conclusion）
该工作通过两时间尺度分解和潜在动作空间压缩，有效解决了分层边缘-云计算系统中联合优化的可扩展性和稳定适应性问题，显著提升延迟和资源效率。

### 五、方法论与关键技术细节
关键方法论细节包括：利用决策动态差异将NP-hard混合整数非凸问题分解为长期配置和短期分配子问题；VAE用于将高维组合动作映射为低维潜在表示再通过解码器映射回原始动作空间，从而缩小探索空间；PPO作为基础算法确保更新稳定性并支持连续控制；系统考虑M/M/c队列模型以刻画动态负载；仿真假设大量用户、边缘节点和服务的场景；局限性包括未考虑用户移动性和无线信道的大规模衰落变化，且VAE训练可能引入额外开销。
