# EMAN: Optimization-Driven Capacity Growth through Path Emergence in Multi-Task Learning

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Chenlei Fang, Jingchen Li, Hongzong LI, Qingyao Li, Yixuan Zhang, Huarui Wu, Haobin Shi, Chunjiang Zhao
- 机构：Northwestern Polytechnical University, Beijing Research Institute of Agricultural Artificial Intelligence and Robotics, Ministry of Agriculture and Rural Affairs, Beijing Academy of Agriculture and Forestry Sciences, National Engineering Research Center for Information Technology in Agriculture
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16930v1) · [PDF](https://arxiv.org/pdf/2608.16930v1)

## TLDR
EMAN is an optimization-driven multi-task learning framework that starts from exact single-path sharing, detects persistent optimization evidence via a latent relative-phase probe, and materializes a second independent path only when needed, improving performance at competitive computational cost.

## Abstract
Existing multi-task learning methods rely on hard sharing, multiple paths or experts, adaptive sharing, and dynamic expansion. However, their capacity changes are usually constrained by predefined structures or triggered by task boundaries and conflict signals. This raises a fundamental question: can a network start from exact single-path computation and grow a new independent path only when persistent optimization evidence appears? We propose the Emergent Modular Atomic Network (EMAN), an optimization-driven framework for exposing an antisymmetric growth direction through latent relative phases without instantiating a second path, and for monitoring multiple decision signals during training to transform local optimization evidence into a structural decision. EMAN materializes two equal-capacity independent paths only after certification. EMAN adaptively allocates shared and task-specific representation capacity to accommodate varying task requirements. Extensive experiments on controlled rank settings, PASCAL-Context, and NYUv2 validate its effectiveness, achieving improved performance at a competitive computational cost.


## 精读解读（中文）
### 一、研究动机
现有MTL方法依赖硬共享、多路径/专家、自适应共享或动态扩展，但容量变化常受预定义结构、任务边界或冲突信号限制。硬共享在后期可能出现容量瓶颈，而常开双路径全程存在冗余计算。EMAN旨在让网络从精确单路径计算出发，仅当训练中持续出现优化证据时才生长第二条独立路径，从而由优化过程内生决定容量增长。

### 二、技术方案（Method）
EMAN分为精确共享→相位探测→优化证据认证(OEC)→条件路径物化四阶段。初始只存储母参数ω̄并执行单路径前向h=f(x;ω̄)，逻辑上令p1=p2=h；引入相对相位φ=θ1-θ2，计算共享项u、余弦对交互βcosφ(p1⊙p2)与正弦反对称项κsinφ(p1-p2)，并用带stop-gradient的RMS归一化控制交互项幅度，得到z=u+ρq̂。探测时把逻辑路径梯度投影到零和反对称方向得g_d，候选方向为d_anti=-g_d/(‖g_d‖+ε)。OEC综合方向强度S_t、半批/分片一致性K、冻结与动态有限步下降D_t、动态安全指标U_t及连续探测窗口W_t内的时域持久性，全部通过固定阈值才置C_t=1。认证成功后，将母参数复制为两个等容量路径并沿d_anti施加零和扰动ω±ε_d d_anti，随后两路径独立优化；若证据不足则维持精确共享。

### 三、结果（Result）
受控秩实验中，单物理路径为秩3容量，任务联合需求分别为秩3/4/6；EMAN在秩3保持共享，在秩6材料化第二路径并恢复缺失的潜在因子和预测性能，秩4对应靠近单路径容量极限，释放后的路径子空间互补。PASCAL-Context静态设置下EMAN释放较早；任务到达场景中，初始两任务阶段保持单路径，在saliency和surface-normal任务加入后释放，三随机种子下最终性能与always-dual相当，活动双路径阶段缩短约一半并减少路径训练计算。NYUv2上EMAN获得最优平均语义分割与深度结果及最高综合分；PASCAL-Context任务级增益略不均匀。

### 四、结论（Conclusion）
EMAN验证了容量扩展可由优化证据内生触发的可行性：从精确单路径起步，通过相对相位暴露反对称增长方向，仅在持续且安全时物化第二条独立路径，从而兼顾共享效率与动态容量。该方法能按任务需求自适应分配共享和任务专有表征，在多个基准上以接近双路径的性能显著降低早期训练开销。

### 五、方法论与关键技术细节
关键实现细节包括：逻辑双路径不增加物理参数，参数量、内存和前向成本与共享模型相同；固定奇映射B(d)=d在退化点提供单位局部增益，使相位释放可在不实例化第二路径时暴露反对称方向；OEC阈值与探测窗口固定，且仅使用训练数据判定；材料化通过零和扰动保证两路径等容量且同构；NormCal使用stop-gradient避免幅度缩放影响梯度；相位释放后需经历固定适应窗口才开始OEC；超参数包括方向步长η、扰动幅度ε_d、相位耦合系数β/κ、NormCal缩放ρ及各类OEC阈值。局限方面，PASCAL-Context任务级提升不如NYUv2均匀，Recon在surface-normal和联合损失上仍保持最强；静态全部任务同时出现时释放较早，延迟计算节省空间有限。
