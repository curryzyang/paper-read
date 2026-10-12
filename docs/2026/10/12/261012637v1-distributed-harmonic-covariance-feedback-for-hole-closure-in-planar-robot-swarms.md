# Distributed Harmonic-Covariance Feedback for Hole Closure in Planar Robot Swarms

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Jitian Liu, Subhrajit Bhattacharya
- 机构：Lehigh University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12637v1) · [PDF](https://arxiv.org/pdf/2610.12637v1)

## TLDR
The paper proposes a distributed harmonic-covariance feedback controller that uses harmonic edge signals from the swarm’s time-varying Čech complex, evaluated via a polynomial of the regularized Hodge Laplacian, to drive planar robots to close coverage holes, with theoretical convergence guarantees and a numerical demo showing closure by 9.9 s.

## Abstract
We consider hole closure in a planar multi-agent system whose sensing disks form a time-varying Čech complex. We propose a harmonic-covariance feedback that uses harmonic edge signals to locate holes and converts those signals into agent forces. For distributed evaluation, we use a fixed-degree polynomial of the regularized Hodge Laplacian. This polynomial is evaluated through local operator applications. The closed loop has a unique global trajectory from every safe initial state. The model data and initial state are supplied with procedures for approximation to any requested accuracy with explicit error bounds. We assume that hole area is measurable and bounded, holes evolve continuously without splitting or merging, and only finitely many temporary new holes appear. Under these conditions, offline finite calculations produce rational lower bounds for the cumulative hole area on the time horizon without querying trajectory data. These bounds converge to that cumulative area, whether finite or infinite. If it is finite, holes close in the time-averaged sense: the average normalized hole area over every fixed-length time window tends to zero as time tends to infinity. In a 15-second numerical demo, all holes close by 9.9s and remain closed through the end.


## 精读解读（中文）
### 一、研究动机
在机器人集群覆盖控制中，传感圆盘并集可能出现未覆盖的孔洞，而既有覆盖修复方法通常缺少仅基于模型和初始状态的孔洞闭合判据。本文针对平面多智能体系统提出分布式 harmonic-covariance 反馈，用代数拓扑信息定位孔洞并驱动其闭合。

### 二、技术方案（Method）
每个智能体具有二阶位置-速度动力学，控制器在线根据传感半径构建时变 Čech 2-复形，并用固定维度的 ambient roster 与光滑边权、三角权构造 regularized Hodge Laplacian L_w。随后用 L_w 的固定度数多项式通过局部算子应用逼近 harmonic projector，提取核空间 harmonic edge signals，再通过带 λ_R 正则的最小二乘 lift 将边信号转换为各节点二维力，并与排斥势和阻尼耦合形成闭环加速度。理论部分给出安全初始状态下轨迹唯一性、离线有理下界构造与收敛证明，数值部分用 15 秒仿真验证闭合效果。

### 三、结果（Result）
理论上，离线有限计算可给出累积孔洞面积的有理下界，该下界序列收敛到真实累积孔洞面积，无论其为有限或无限；若极限有限，则任意固定长度时间窗上的平均归一化孔洞面积随时间趋于零。数值上，15 秒演示中所有孔洞在 9.9 秒时闭合，并保持关闭直到仿真结束。

### 四、结论（Conclusion）
该工作表明，分布式 harmonic-covariance 反馈可在给定假设下实现平面机器人集群的孔洞闭合，并提供仅依赖模型与初始状态、无需查询轨迹的闭合判据。其贡献在于把代数拓扑孔洞检测与局部可实现的力控结合，但闭合结论是时间平均意义，并依赖孔洞不分裂合并等条件。

### 五、方法论与关键技术细节
关键细节包括传感半径 r_s、边与三角光滑阈值 ε_E 和 ε_F、边权 a_e 与三角权 b_f 的局部 Lipschitz 构造、ambient roster 维度为 N 选 2 和 N 选 3、保持 D1D2=0 的 D1 与 D2 设计、正则 Hodge Laplacian L_w=D1^T D1+D2D2^T，以及 lift 最小二乘中 λ_R 正则对应的解 G_i^{-1}T_i。超参还涉及排斥势参数 a、b、g、τ_U 和阻尼增益 α；控制力局部 Lipschitz 保证安全初始状态下轨迹唯一，近似可达到任意精度并有显式误差界，离线有理下界无需轨迹数据。局限包括三角形组合数随智能体数增长、孔洞面积需可测有界且连续演化不分裂不合并、仅有限临时新孔洞，以及数值验证仅为 15 秒演示。
