# Networked Admissibility-Preserving Control for Directed Safe Coordination

- 区域：精读区
- 排名：2
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Abhinav Sinha, Lohitvel Gopikannan, Shashi Ranjan Kumar
- 机构：Indian Institute of Technology Bombay, University of Cincinnati
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09384v1) · [PDF](https://arxiv.org/pdf/2609.09384v1)

## TLDR
The paper proposes a networked Admissibility-Preserving Control architecture that combines Admissibility-Preserving Input Realization with a logarithmic barrier coordinate to guarantee directed multi-agent coordination stays within a moving safety corridor and heterogeneous asymmetric actuator bounds while achieving exponential consensus over rooted digraphs.

## Abstract
This paper addresses safety-critical coordination for scalar agents whose distributed commands are implemented through constrained physical-input dynamics. Agents communicate over a fixed weighted digraph with a directed spanning tree, while their outputs must remain inside a common moving safety corridor and their realized inputs must satisfy heterogeneous asymmetric bounds. We propose a networked Admissibility-Preserving Control (APC) architecture in which an Admissibility-Preserving Input Realization (APIR) governs physical inputs and a logarithmic barrier coordinate represents the safety corridor. The synthesis yields an exact cascade in which exponentially decaying realization errors drive nonsymmetric consensus dynamics. For every compatible compact initial set, the closed-loop system admits a unique complete solution, renders the moving corridor and actuator intervals forward invariant with uniform margins, keeps commands bounded, and achieves exponential consensus. We derive direction-specific sufficient conditions under which positive and negative control demands remain within their corresponding actuator limits. The analysis yields a closed-form barrier-coordinate limit determined by the left Perron vector and initial APIR mismatch. Under strong connectivity and the stated gain and compatibility conditions, partial pinning propagates a constant barrier reference from a nonempty informed subset and assigns the induced safety corridor trajectory. A non-weight-balanced example illustrates the directional certificate and predicted collective motion.


## 精读解读（中文）
### 一、研究动机
本文关注标量智能体在安全关键协调中的可容许性问题：分布式命令不能直接视为理想输入，而是通过受约束的物理输入动力学实现，同时输出需保持在共同移动安全走廊内，实际输入需满足异构非对称执行器界限。已有网络障碍函数或静态饱和设计通常把输入代数化或只做瞬时裁剪，未把执行器实现瞬态纳入安全证书；在仅有有向生成树且一般非权重平衡的图中，APIR 初始不匹配会进入集体模态并改变最终一致值，因此需要把执行器实现作为闭环动力学的一部分。

### 二、技术方案（Method）
为每个标量智能体建立 x_i 动力学为 x_i 导数等于 u_i，并用 APIR 动力学驱动物理输入 u_i，其中控制器产生专用命令 v_i，σ_i 采用偶次多项式分段以在零点保持一阶连续并在执行器边界内指。通过对数障碍坐标 z_i 表示移动走廊，将输出约束映射到实数域，得到 z_i 导数等于 b_i u_i 加 χ_i。定义有向一致性场 β_i 为负 k 乘以入邻居 z 差加权和，APIR 误差 e_i 为 z_i 导数减 β_i。设计分布式命令 v_i 解析抵消 b_i、χ_i 和 β_i 的导数项并加入负 c_i e_i 反馈；其中 b 和 χ 的导数按闭式展开，β 的导数用邻居已实现的 b_j u_j 加 χ_j 计算，避免数值微分。由此形成精确级联：e_i 按指数衰减，z_i 动力学为有向拉普拉斯耦合加衰减误差。兼容性证书离线利用图半群常数、左 Perron 向量、走廊宽度与速度加速度界、执行器区间和紧初始集验证。

### 三、结果（Result）
对每个兼容紧初始集，闭环系统具有唯一完整解，移动走廊和异构非对称执行器区间前向不变并具有一致裕度，命令有界且实现指数一致。给出方向相关充分条件，分别保证正负控制需求不超出对应执行器上下限；当方向需求不同时，单边兼容性测试可认证严格大于对称测试的执行器界集合。障碍坐标的一致极限可由左 Perron 向量和初始 APIR 不匹配闭式确定。在强连通及给定增益和兼容条件下，部分牵制可从任意非空知情子集传播恒定障碍参考并指定诱导的安全走廊轨迹；非权重平衡算例验证方向证书和预测的集体运动。

### 四、结论（Conclusion）
该工作把 APIR 执行器实现作为动态状态纳入有向网络安全协调，同时保证移动输出走廊和异构非对称输入区间不变，避免为满足饱和而放宽输出性能走廊。分析揭示了有向图不平衡和 APIR 瞬态如何通过左 Perron 向量偏移最终一致值，并为强连通下部分牵制提供安全集体轨迹指定能力。整体方法适用于有向生成树但非权重平衡的网络，具有区域性和依赖兼容初始集的特点。

### 五、方法论与关键技术细节
关键输入包括固定加权有向图且含生成树、共同移动走廊的 C2 边界及其宽度速度加速度界、每个智能体非对称执行器区间。建模核心是 APIR 动态输入、对数障碍坐标及其逆映射，逆映射导数上界为走廊最大宽度除以四。控制参数 k、c_i、p1_i、p2_i 为正，σ_i 使用偶次幂且两分支在原点和一阶导连续，边界处输入向量场指向区间内部。兼容性证书离线使用图半群衰减常数、谱隙和左 Perron 向量；在线仅需局部、入邻居和共同走廊信息，且所有导数闭式计算。主要约束是紧兼容初始集、已知走廊界、有限执行器权威和区域可认证性；部分牵制指定轨迹需要强连通及增益兼容条件。局限性包括依赖 C2 走廊和已知界、初始集需兼容，以及未覆盖完全一般时变或未知环境。
