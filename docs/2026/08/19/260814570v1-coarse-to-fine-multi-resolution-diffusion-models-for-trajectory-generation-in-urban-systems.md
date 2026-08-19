# Coarse-to-Fine Multi-Resolution Diffusion Models for Trajectory Generation in Urban Systems

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Wen Ye, Muyan Weng, Chuizheng Meng, Hao Niu, Yizhou Zhang, Yan Liu
- 机构：University of Southern California, KDDI Research, Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14570v1) · [PDF](https://arxiv.org/pdf/2608.14570v1)

## TLDR
MR-Traj is a coarse-to-fine multi-resolution diffusion framework that generates synthetic urban trajectories by modeling global milestones and fine-grained segments, improving fidelity across spatial-temporal resolutions, supporting downstream mobility tasks, and reducing trajectory linkage risk.

## Abstract
Understanding human mobility is critical for a wide range of urban applications, including traffic management, epidemic control, and urban planning. However, due to privacy concerns, the availability of large-scale public trajectory data remains limited, posing challenges for downstream mobility analysis. Existing methods for synthetic trajectory generation primarily focus on matching global distribution similarity, while often overlooking mobility patterns across different spatial and temporal resolutions that are essential for practical utility.
  To address these challenges, we propose a novel multi-resolution diffusion framework, MR-Traj, for large-scale trajectory generation. MR-Traj explicitly models trajectories as compositions of coarse-grained milestones and fine-grained segments, enabling the capture of complex spatial-temporal dependencies at multiple resolutions. Experimental results demonstrate that MR-Traj achieves comparable performance to state-of-the-art methods in terms of global distribution similarity, while consistently outperforming them in modeling fine-resolution mobility patterns and supporting downstream urban mobility tasks. In addition, by introducing stochasticity at multiple resolution levels, MR-Traj generates more diverse trajectories, which empirically reduces trajectory linkage risk under a seed-guided data release setting. Our code is available at https://github.com/Ray0202/MR-Traj.


## 精读解读（中文）
### 一、研究动机
大规模真实轨迹数据因隐私约束难以公开获取，现有合成轨迹生成方法主要追求全局分布相似性，却忽略了对下游城市应用至关重要的跨空间和时间分辨率的细粒度移动模式，导致生成轨迹在局部保真度与下游任务效用上不足。

### 二、技术方案（Method）
提出MR-Traj多分辨率扩散框架，将轨迹显式建模为粗粒度里程碑与细粒度片段两部分。首先用均匀采样从原始轨迹提取里程碑序列，训练一个里程碑级扩散模型（U-Net骨干，条件嵌入模块拼接出行时间、距离、起终点等全局属性）学习整体轨迹结构；随后将原轨迹切分为以里程碑为端点的等长片段，训练片段级扩散模型（同样采用U-Net，以对应里程碑和片段级条件为引导）逐段生成细粒度局部移动，最后按顺序拼接里程碑与片段得到完整合成轨迹。训练采用改进余弦噪声调度的去噪扩散目标，推理时先在里程碑层级采样，再在片段层级逐段生成。

### 三、结果（Result）
在大型真实城市移动数据集上的实验表明，MR-Traj在全局分布相似性上与最先进方法相当，但在细分辨率移动模式建模上持续优于基线，并在出租车目的地预测、异常移动模式识别等下游城市任务中表现更优；同时多分辨率级别引入随机性使生成轨迹更多样，在种子引导的数据发布设置下经验上降低了轨迹链接风险。

### 四、结论（Conclusion）
MR-Traj通过显式建模多分辨率层次结构，有效兼顾了全局移动结构与局部细粒度细节，提升了合成轨迹的局部保真度、多样性和下游分析效用，为城市系统大规模轨迹生成与负责任数据发布提供了可行方案。

### 五、方法论与关键技术细节
关键点包括：里程碑提取比较了均匀采样与开放角度关键点提取，实验表明均匀采样在该场景更有效且保证等长片段从而简化建模；采用U-Net作为两个扩散模型骨干，并引入余弦噪声调度以提高训练效率；理论分析通过Lipschitz条件和Total Variation距离界证明仅优化全局分布不足以最大化下游效用，必须在联合与边际分布上同时建模；多分辨率噪声注入增强了生成多样性，可降低轨迹链接隐私风险；局限是模型假设GPS轨迹密集且无语义标注，对语义轨迹可能需调整里程碑提取策略。
