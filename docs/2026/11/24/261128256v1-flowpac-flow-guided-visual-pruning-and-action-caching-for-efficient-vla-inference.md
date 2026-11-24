# FlowPAC: Flow-Guided Visual Pruning and Action Caching for Efficient VLA Inference

- 区域：精读区
- 排名：9
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Jintao Cheng, Yipu Zhang, Haozhe Wang, Lin Jiang, Jiang Xu, Wei Zhang
- 机构：The Hong Kong University of Science and Technology (Guangzhou), Northeastern University, South China Normal University, The Hong Kong University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28256v1) · [PDF](https://arxiv.org/pdf/2611.28256v1)

## TLDR
FlowPAC is a training-free, locality-aware VLA acceleration framework that uses task-aware optical flow as a shared signal to jointly guide future-aware visual token pruning and adaptive action caching, achieving a 2.13× end-to-end speedup while essentially maintaining success rate with only 30% visual-token retention.

## Abstract
Vision-Language-Action (VLA) models have emerged as a powerful paradigm for embodied AI, yet their high inference latency and memory footprint remain major barriers to edge deployment. Existing training-free acceleration techniques, such as visual token pruning and action caching, typically rely on static resource allocation. This mismatch with dynamic robotic interactions not only degrades control performance but also causes severe hardware inefficiencies, including fragmented KV-cache layouts and wasted compute on non-critical regions. To address this, we propose FlowPAC, a locality-aware framework that leverages task-aware optical flow as a shared physical signal to jointly optimize visual and action computation. Specifically, we introduce Direction-Aware Trajectory Propagation (DATP) and Locality-Aware Contiguous Token Selection (LACT) to jointly handle visual token dynamics and enforce spatial locality, reducing memory fragmentation and enabling efficient KV-cache compression. This is complemented by Flow-Conditioned Action-Block Refresh (FCAR) for adaptive action computation based on motion dynamics. Extensive closed-loop evaluations on LIBERO demonstrate that FlowPAC achieves a 2.13$\times$ end-to-end speedup over the dense baseline while essentially maintaining the success rate with 30% visual-token retention. These results validate that aligning computation allocation with both physical dynamics and hardware constraints is essential for efficient VLA deployment on edge systems.


## 精读解读（中文）
### 一、研究动机
VLA模型在具身智能中表现强，但推理延迟和内存占用阻碍边缘部署；现有免训练视觉token剪枝与动作缓存多采用静态资源分配，与机器人交互的动态性不匹配，导致当前帧剪枝丢弃未来关键区域、固定刷新在平稳期浪费算力而在剧变期引入控制滞后，并造成KV-cache布局碎片化和非关键区域计算浪费。

### 二、技术方案（Method）
FlowPAC以任务感知光流为共享物理信号联合优化视觉与动作计算：DATP对相邻观测计算稠密光流并聚合为patch级运动矢量，结合指令条件语义相关性经语义加权池化估计运动中心与主方向，沿符号光流传播H步形成未来关键走廊，再以高斯核和折扣κ计算轨迹分数，并与语义分数、运动幅值归一化加权排序，按每视角固定预算K_v选token；LACT将token划分为对齐b×b块，在高分轨迹区域搜索一/二组件块模板，先选完整块再用相邻高分patch补齐精确预算，并在前缀层L_w才执行单次gather物理打包，语言token顺序与保留视觉token的旋转位置ID不变，KV按同一索引压缩，使后续前缀长度变为K_g+K_w+N_lang；FCAR用语义加权双视角光流幅值r_t=max(r_t^g,r_t^w)，转为当前episode内的因果经验百分位q_t，再按B_t=clip(round[D(ρ_min+q_t(ρ_max−ρ_min))],2,D)决定动作专家刷新次数，刷新点均匀分布于D步轨迹并包含边界，刷新处计算并缓存各层attention/FFN残差，复用处跳过算子并加回最近残差，但不改变flow-matching求解步数、动作状态和时间步嵌入更新。

### 三、结果（Result）
在LIBERO闭环评测中，FlowPAC相对稠密π0.5基线取得2.13×端到端加速，并在仅保留30%视觉token时基本维持成功率；当前帧剪枝方法FastV和VLA-ADP在紧预算下难以保留后续交互关键区域，尤其在LIBERO-Long长时任务上成功率下降更明显，而FlowPAC通过未来感知token选择和动作刷新调度在匹配保留率比较中表现更稳。

### 四、结论（Conclusion）
结果表明，将计算分配同时对齐物理动态与硬件约束，是VLA边缘高效部署的关键；以任务感知光流作为共享信号，可在一个免训练框架内联合决定视觉计算“保留在哪里”和动作计算“何时刷新”，在显著降低前缀KV与动作专家重复计算的同时保持控制性能。

### 五、方法论与关键技术细节
关键实现包括：对π0.5的profiling显示动作去噪占77.6%运行时间（236.3 ms），视觉token占968个前缀token中的768个（79.3%）；DATP无需额外训练或显式轨迹预测，弱运动信号时禁用空间先验以避免不可靠偏置，LACT以精确预算约束最大化得分并惩罚空间/内存碎片，延迟物理打包保留早期跨token交互；FCAR不缩短原10步求解轨迹，仅选择性复用动作专家块残差，首个query设q_0=1且新episode清空运动历史；评测使用官方π0.5 LIBERO checkpoint、双相机视角、每任务50次试验共2000 episodes、A100-PCIE-40GB BF16 batch size 1并报告P50/P95延迟；局限是主要在单一模型与LIBERO仿真验证，依赖光流和指令条件语义相关性质量，H、Δ、σ、κ、α/β/γ、b、L_w、ρ_min/ρ_max等超参在预览中未完整给出，真实机器人部署与光流开销仍需进一步评估。
