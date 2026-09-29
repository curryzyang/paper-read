# Autonomous Research Project Management as an Agent Skill: A Case Study in Exact Spectral Spatial Regression

- 区域：精读区
- 排名：8
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Alexander Chen, Jeffrey Meng, Bram Hoex, Tong Xie
- 机构：University of New South Wales, GreenDynamics
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31683v1) · [PDF](https://arxiv.org/pdf/2609.31683v1)

## TLDR
An autonomous agent skill conducted end-to-end machine learning research on consumer CPU hardware—autonomously formulating and benchmarking an exact FFT/BCCB kernel ridge regression solver for regular-grid spatial regression on NOAA SST anomalies—while managing long-horizon tasks across 74 sub-agent sessions with minimal human steering and arguing for inspectable, falsifiable, agent-readable research reporting.

## Abstract
This work presents an end-to-end demonstration of autonomous machine learning research conducted by an agent skill on consumer hardware. The demonstration evaluates an FFT-based Kernel Ridge Regression (KRR) solver for regular spatial grids using 2005 monthly NOAA Kaplan SST v2 anomaly fields on a $36 \times 72$ grid. This was autonomously executed by DeepSeek V4 Flash, orchestrated by our agent skill suite within DeepSeek Harness (DSH). Experiments were executed on CPU-only hardware (Apple M2 Pro; 78.7 s solver time, 1.57 GB peak RSS). Long-horizon state was decoupled into a file-based epic- and issue-tracking substrate. Across 74 sub-agent sessions, the agent demonstrated closed-loop scientific resilience: routing two failed hypothesis review gates back to literature retrieval, patching bootstrap indexing bugs, and executing with only four discrete human steering events. Finally, we reflect on autonomous research governance, arguing that scientific credibility requires inspectable state, falsifiable review gates, and transparent reporting of negative results, urging the machine learning community to favour agent-accessible structured formats over static PDF manuscripts.


## 精读解读（中文）
### 一、研究动机
稠密核岭回归（KRR）在空间预测中精度可靠，但其求解复杂度为 O(N^3) 时间与 O(N^2) 内存，难以随网格规模扩展；尽管规则网格上的循环嵌入与 FFT 对角化在调和分析中早已确立，其面向规则网格空间回归、并配合精确 PCG 边界预条件的闭式应用仍缺乏刻画。本文同时意在验证：一个 agent 技能能否在消费级硬件上端到端自主完成从选题、实现到基准评测的机器学习研究。

### 二、技术方案（Method）
数据采用 NOAA Kaplan SST v2 月异常场共 2005 个样本（1856-01 至 2023-01，36×72 的 5° 网格），全场存在 53.4% 缺测并需按月均值处理。建模上利用规则网格循环行列距离使 Gram 矩阵为 BCCB，由 2D-DFT 对角化，岭回归解化为 α=F^{-1}(F(y)/(ĉ+λ))，仅需两次 FFT 与一次逐点除法，达到 O(N log N) 时间与 O(N) 内存；对 RBF 等非环面核出现的微小负 BCCB 特征值做零截断以实现 PSD 投影。真正带掩膜的训练则用预条件共轭梯度求精确自由边界解，以 (2N-1) 镜像循环矩阵实现精确 BTTB 矩阵向量乘，并用 floored-torus 谱逆作预条件，收敛容差 1e-8。评测协议包含泄漏感知的随机 10/30/50% 与 halo 掩膜重建、Nino3.4 框泛函回归、迁移预报，以及与 Nyström/RFF/坐标 KRR 的 FLOPs 对照。agent 侧由 DeepSeek V4 Flash 在 DeepSeek Harness 中执行，长期状态完全外化为文件化 EPIC.md/ISSUE.md/comments 基底，按 A 立项、B 控制校验与成本追踪、C 阶段驱动调度（文献检索、假设生成、实验计划、执行、分析、写作，并在假设选择与分析处设评审门）、D 收集、E 综合的五阶段推进，共 74 个子 agent 会话。

### 三、结果（Result）
在 2016-01 单场上，谱解与稠密 floored-torus 参考的相对 ℓ∞ 误差为 2.62e-12（Matérn-3/2）与 1.12e-12（RBF），远低于 1e-6 门槛，自由边界差距分别为 0.95 与 0.12。84 个测试月的掩膜重建中，Matérn-3/2 的 RMSE 为 0.0816–0.0880（约场标准差的 14%），有效格点覆盖 0.877–0.897，而 RBF 明显退化到 0.2789–0.3155。Nino3.4 箱体泛函在 2005 个月上的 5 折时间块 CV 达到 RMSE 0.0856、相关系数 0.997，优于原始 2592 维特征上的直接岭回归（0.2696，约 3.2 倍）和零基线（0.7955）。预注册的迁移预报获胜规则下结论为 REFUTED（0/4 个提前期），h=1 时 0.268 逊于持续性 0.251 与 AR(1) 0.241，h=12 技能为负；整体仅耗 Apple M2 Pro CPU 78.7 s、峰值内存 1.57 GB。

### 四、结论（Conclusion）
精确循环块 KRR 为规则网格空间回归提供了一条实用的闭式、纯 CPU 路线：环面精确谱解达到 O(N log N) 时间与 O(N) 内存，掩膜重建误差约为场标准差的 14%，并给出可复现的算法基准。研究同时证明 agent 技能可在 74 个子会话与仅 4 次离散人工干预下完成端到端科学流程，期间两次假设评审门失败被回退到文献检索、bootstrap 索引 bug 被自行修补，体现了闭环科学韧性。作者据此主张自主科研的可信度依赖于可审计的状态、可证伪的评审门以及对负结果的透明报告，并呼吁机器学习社区采用 agent 可读的结构化格式而非静态 PDF 稿件。

### 五、方法论与关键技术细节
关键实现细节包括：λ 取 1e-3（精确性检验）、1e-4（重建）与 1e-2（Nino3.4），采用 84 个测试月和 5 折时间块 CV、年块 bootstrap 的 MSE 差置信区间，split-conformal 因残差序列相关而按 60 个末期训练年的日历月块校准。复杂度与资源上，解算只需 5 个工作数组，N=1e6 时约 0.04 GB，N=10368 时拟合耗时 0.2–0.5 ms，端到端 78.7 s 与 1.57 GB RSS。局限与约束方面：谱高效性仅对嵌入环面核严格精确，带掩膜的自由边界训练需迭代 PCG 且误差约高 6 倍；局部 seam/衰减区域的覆盖在自相关下退化为 0.739–0.837；空间粗化 2×2 至 10° 会使重建 RMSE 从 0.0853 升至 0.1667、泛函 RMSE 从 0.0856 升至 0.3825；Kaplan 数据本身依赖月度均值填补的 EOF 重建，迁移结论不构成业务预报声明。
