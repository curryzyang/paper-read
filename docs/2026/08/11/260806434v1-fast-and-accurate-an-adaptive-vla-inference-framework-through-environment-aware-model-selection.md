# Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection

- 区域：精读区
- 排名：4
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Yuewei Sun, Lang Qin, Zechuan Tian, Jingwen Li, Guiqin Wang, Shengzeng Huo, Wenxin Ren, Tao Fang, Xiaochen Zhang, Guanqing Deng, Xiang Wang, Xiaowen Dong, Qinghai Guo, Yuxin Ma
- 机构：Huawei Technologies, Southern University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06434v1) · [PDF](https://arxiv.org/pdf/2608.06434v1)

## TLDR
TLDR: EMS is an adaptive vision-language-action inference framework that uses reinforcement learning to switch between a fast reactive policy and a slow deliberative policy in a fully decoupled dual-system architecture, achieving success rates comparable to large VLA models while maintaining high-frequency closed-loop control.

## Abstract
Embodied intelligence demands both long-horizon reasoning and real-time closed-loop responsiveness. Recent dual-system Vision-Language-Action (VLA) architectures combine fast reactive control with slow deliberative reasoning to balance inference speed and task success rate. However, existing dual-process VLAs tightly couple the fast module to intermediate representations of the slow module, necessitating end-to-end joint training and limiting modularity, extensibility and flexible system switching. In this paper, we propose Environment-aware Model Selection (EMS), an adaptive VLA inference framework that switches between two fully decoupled systems of different scales through environment-aware model selection. The large-scale deliberative system provides globally consistent trajectory planning to ensure task success, while a lightweight reactive system enables high-frequency closed-loop control. A reinforcement-learning-based switching policy dynamically selects which system to invoke based on real-time feedback, enabling sparse use of the slow system and thereby balancing pretrained knowledge utilisation with runtime efficiency. Our design offers three key advantages over prior hierarchical VLA frameworks: (1) a fully decoupled and modular dual-system architecture that supports plug-and-play model replacement; (2) an adaptive, environment-aware switching strategy; (3) high-frequency inference for responsive closed-loop control. We extensively evaluate EMS in both simulation and real-world environments. On the LIBERO benchmark, EMS achieves success rates comparable to the large-scale baseline while increasing the effective action frequency to 93.4 Hz. The framework further demonstrates strong extensibility in real-world dual-arm manipulation tasks, where it accelerates task completion while maintaining robust performance.


## 精读解读（中文）
### 一、研究动机
现有双系统视觉-语言-动作（VLA）框架将快模块与慢模块的中间表示紧密耦合，需要端到端联合训练，导致模块化、可扩展性和系统切换受限。为了在具身智能中同时实现长程推理和实时闭环响应，需要一种解耦且自适应的推理框架，能够根据环境反馈动态选择不同规模模型，以平衡预训练知识利用和运行效率。

### 二、技术方案（Method）
提出环境感知模型选择（EMS）框架，由完全解耦的大规模 deliberative 系统（System 2）和轻量级 reactive 系统（System 1）组成，两者独立进行端到端动作生成，仅通过动作级接口交互。训练分三阶段：阶段一通过模仿学习在遥操作轨迹上微调System 2；阶段二利用System 2生成的成功轨迹通过模仿学习自蒸馏训练System 1；阶段三将系统选择建模为两动作MDP，基于机器人状态用离线/在线强化学习训练轻量级切换策略，并采用动作融合（平均两个系统在切换时刻的动作）保证平滑过渡。推理时，切换模块在每个决策边界选择调用快或慢系统，稀疏使用慢系统。

### 三、结果（Result）
在LIBERO基准上，EMS的平均成功率达到92.40%，与大规模基线（如PI0 94.15%）相当，同时有效动作频率达93.4 Hz，显著高于OpenVLA的6.3 Hz，切换率仅为0.153。真实世界双臂操作实验中，EMS在保持鲁棒性能的同时加速了任务完成。

### 四、结论（Conclusion）
EMS通过完全解耦的双系统设计和环境感知切换，实现了高成功率与高执行频率的平衡，支持即插即用的模型替换和灵活扩展，为VLA推理提供了一种高效自适应方案。

### 五、方法论与关键技术细节
关键细节包括：System 2为大尺度预训练VLA，约10Hz输出动作块；System 1为轻量策略，约100Hz独立推理；切换模块为浅层全连接网络，输入仅用机器人状态以降低开销；动作融合在切换边界对快慢系统动作取平均；强化学习采用稀疏奖励分配，总奖励均匀分配到各时间步；切换策略优化目标在最大化任务成功率的同时惩罚不必要的慢系统调用；局限性在于切换策略依赖状态而非多模态观测，且训练需要先收集System 2的成功轨迹，以及动作融合的简单平均可能不适用于差异较大的动作分布。
