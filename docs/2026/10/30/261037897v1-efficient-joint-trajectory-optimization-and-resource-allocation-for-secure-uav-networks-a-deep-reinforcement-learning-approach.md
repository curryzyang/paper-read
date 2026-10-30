# Efficient Joint Trajectory Optimization and Resource Allocation for Secure UAV Networks: A Deep Reinforcement Learning Approach

- 区域：精读区
- 排名：6
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Abdulmalik Alwarafy, Mohamed Hayajneh, Mustafa Al Juboori, Abdulaziz Almarzooqi, Tahnoon Almazrouei, Robera Abera, Kaleab Nega
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37897v1) · [PDF](https://arxiv.org/pdf/2610.37897v1)

## TLDR
This paper proposes a PPO-based deep reinforcement learning framework to jointly optimize UAV trajectories, power allocation, energy harvesting, and dynamic transmit/jam/relay role selection in a tethered-UAV-assisted secure network, maximizing secrecy rate while reducing energy consumption and interference against a ground eavesdropper.

## Abstract
Unmanned Aerial Vehicles (UAVs) are increasingly deployed in wireless networks; however, ensuring secure communication and efficient energy usage remains challenging. This paper addresses the joint trajectory optimization and resource allocation problem in UAV networks in the presence of a tethered UAV flying center and a malicious ground eavesdropper. In the proposed model, UAVs are equipped with energy harvesting capabilities and can adaptively switch between transmitting, jamming, and relaying roles to deliver data to a tethered UAV center for optimized network performance. An optimization problem is formulated to maximize a utility function that balances secrecy rate, energy consumption, and interference. To address the high non-convexity of the problem and its real-time decision requirements, a Proximal Policy Optimization (PPO)-based Deep Reinforcement Learning (DRL) algorithm is proposed to solve the problem and learn the network dynamics. Extensive simulation results demonstrate that the proposed approach achieves superior secrecy performance, lower energy consumption, and reduced interference compared to conventional and DRL-based methods.


## 精读解读（中文）
### 一、研究动机
UAV 网络在灵活部署和覆盖方面优势明显，但开放无线信道、UAV 移动性和有限电量使其面临窃听与能耗双重挑战。现有工作多采用固定角色 UAV，且很少同时考虑动态角色切换、空中持续供能和安全通信的联合优化。本文旨在通过动态角色 UAV 与系留 UAV 飞行中心协同，联合优化轨迹、功率与资源分配，在提升安全速率的同时降低能耗和干扰。

### 二、技术方案（Method）
构建包含多架具备能量收集能力的 UAV、一个系留 UAV 飞行中心和一个地面窃听者的上行安全通信模型，UAV 可在发射、干扰和中继角色间动态切换，系留中心负责集中协调与无线充电。以离散时隙建模，联合优化所有 UAV 的 3D 轨迹、发射/干扰/中继功率、收获能量、角色选择及系留中心位置，形成最大化安全速率并惩罚能耗与干扰的多目标效用优化问题 P1，并约束干扰低于阈值。由于问题高度非凸且包含混合连续-离散变量，采用集中式 PPO 深度强化学习：将网络状态（位置、信道、能量、角色等）输入策略网络，动作对应轨迹调整、功率控制、能量决策和角色切换，奖励由安全速率、能耗与干扰的效用函数构造，训练后在线根据部分网络知识实时输出决策。

### 三、结果（Result）
仿真结果表明，所提 PPO 方法相较传统优化方法和 DRL 基线具有更优的安全速率、更低的能耗和更小的干扰，并表现出更好的收敛行为与在线部署适应性。摘要给出的核心对比结论是安全性能更优、能效更高、干扰更少，但未在摘要和预览中提供具体数值指标。

### 四、结论（Conclusion）
论文表明，将动态角色切换、系留 UAV 无线供能与 PPO 强化学习结合，可有效处理安全 UAV 网络中高维非凸的轨迹与资源联合优化问题。该框架能够在部分网络知识和实时决策约束下学习自适应策略，为安全、节能和低干扰的多 UAV 通信提供可行方案。

### 五、方法论与关键技术细节
信道采用概率 LoS/NLoS 的加权平均路径损耗并叠加小尺度衰落，OFDM 平坦衰落假设下计算合法链路和窃听链路的可达速率，安全速率由二者差值刻画；干扰 UAV 沿合法信道零空间发送人工噪声，系留中心利用已知 CSI 和噪声特征抑制干扰；系留 UAV 提供无线充电，UAV 具备能量收集模块，优化中显式约束干扰阈值 C3。PPO 采用集中式训练与在线执行处理混合连续-离散动作，依赖部分 CSI 和已知干扰功率等假设；预览未给出具体超参数、网络结构和数值结果，且平均路径损耗建模与仿真验证构成主要局限。
