# Learning Modular Policy for Multi-Floor Object Navigation:A Factorized Framework for Diagnostic Study

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Shichao Zhai, Shuhao Ye, Rong Xiong, Yue Wang
- 机构：Zhejiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06958v1) · [PDF](https://arxiv.org/pdf/2610.06958v1)

## TLDR
This paper presents a diagnostic modular framework for multi-floor object-goal navigation that factorizes a global policy into a VLM-distilled intra-floor exploration policy and a learned inter-floor switching policy, finding that perception performance and stair-climbing stability—not decision-making—are the primary bottlenecks.

## Abstract
Object-goal navigation (ObjectNav) in multi-floor scenarios presents a challenge due to sparse rewards caused by long-horizon decision-making. In this paper, we propose a diagnostic study based on a modular framework with an effective learnable policy to analyze failure factors in multi-floor scenarios. To achieve an effective policy for diagnosis, we design the hierarchical factorization policy that deconstructs a single global policy into an intra-floor exploration policy and an inter-floor switching policy. To providing an effective initialization for Reinforcement Learning (RL), the lightweight intra-floor policy is learned by distilling the exploration logic of Visual Language Models (VLMs). Under idealized assumptions, we show that the factorized policy is theoretically equivalent to a single global policy at the policy-representation level. Experiment results indicate that perception performance and stair climbing stability are the primary bottlenecks in multi-floor navigation.


## 精读解读（中文）
### 一、研究动机
多楼层ObjectNav因长时程决策导致奖励稀疏，且策略决策、感知与底层执行在完整流程中耦合，现有方法性能差异难以直接定位主要瓶颈。为把策略本身导致的瓶颈与其他因素解耦，需要在一个模块化框架中训练出有效可学习策略，但多楼层导航缺乏监督数据，在线RL训练单一全局策略交互成本极高。

### 二、技术方案（Method）
提出层次化因子化策略：将全局策略分解为楼层内探索策略和楼层间切换策略。地图维护局部滑窗多楼层表示M_multi=concat(M_l,M_c,M_u)，每层6通道含语义前沿、VLM值图、机器人状态、上一时刻前沿/值图和上一动作；楼层内策略以当前层地图为输入，经CNN+U-Net输出logit图并用前沿掩码取argmax子目标，楼层间策略以三层堆叠地图为输入输出Down/Stay/Up并用有效性掩码选择动作；二者分别每K_intra、K_inter步执行。训练先用VLFM及其改进版的探索逻辑蒸馏预训练楼层内策略，用完全探索当前楼层后再换层的贪心规则生成楼层间标签，再用交替SAC RL微调，每轮冻结一个策略更新另一个；底层用预训练PointNav控制器，爬楼可选传送或路点模式。

### 三、结果（Result）
诊断实验表明，多楼层导航的主要瓶颈不在决策，而在感知性能与爬楼稳定性：在GT感知下成功率超过YOLO感知，且GT感知与理想爬楼条件下框架优于现有方法；学习到的楼层间策略与贪心策略在GT感知和路点模式下表现相当，但两者在传送模式下均有提升。交替楼层内/楼层间训练每轮带来性能提升并优于零样本多楼层基线，被作为策略有效性的判据；具体数值指标在摘要与预览中未给出。

### 四、结论（Conclusion）
该工作提供一个用于诊断的模块化因子化框架，用有效可学习策略将多楼层ObjectNav失败因素分解，结论是感知可靠性与爬楼稳定性是当前主要瓶颈，而策略决策并非主导。理论上在理想化假设下，因子化策略在策略表示层面与单一全局策略等价，最大熵SAC目标取得相同最优值和最优动作分布；贡献还包括VLM探索逻辑蒸馏得到的轻量楼层内策略与交替RL优化流程。

### 五、方法论与关键技术细节
关键细节包括：输入为RGBD与位姿，动作空间为MoveForward/TurnLeft/TurnRight/LookUp/LookDown/Stop，成功判据为停止在d_succ内且不超过T_max；楼层内/间掩码将被遮蔽logit置为-inf，地图窗口随换层重定中心，可扩展到非三层建筑。训练损失未在预览中展开，RL奖励为成功2.5，否则负的地测地距离变化减0.01×Δk；交替RL只是降低耦合的实用策略，并非联合优化的理论保证。局限与约束包括等价性依赖理想化假设、楼层窗口局部性、依赖VLM值图和检测、爬楼稳定性可能受传送/路点设置影响，且K_intra、K_inter及网络超参在给出文本中未明确。
