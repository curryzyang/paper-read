# Practical Semialgebraic Optimization via Sparse Sample-Based Sum-of-Squares Programming

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Jason Nezvadovitz, David M. Rosen
- 机构：MIT Lincoln Laboratory, Northeastern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07108v1) · [PDF](https://arxiv.org/pdf/2611.07108v1)

## TLDR
This paper introduces a sparse sample-based sum-of-squares hierarchy that samples a tractable variety containing the feasible set and uses separator polynomials to recover correlative sparsity, enabling scalable certified semialgebraic optimization without slack variables or discrete enumeration.

## Abstract
As the importance of semialgebraic optimization grows in engineering, so does the need for scalable sum-of-squares (SOS) methods. Their convex relaxations can guide mixed-integer search and often deliver certified global optima outright. Scaling traditional SOS typically requires hand-crafted bases and redundant constraints, whereas sample-based SOS numerically exploits feasible set geometry to reduce bases and build smaller, often tighter relaxations from black-box evaluations. However, discrete variables can require exponentially many samples, and each sampled equation couples all cliques, destroying correlative sparsity. In this work, we avoid enumeration and slack variables by sampling a tractable variety that contains the feasible set, with multipliers only for the omitted constraints. To recover sparsity, we introduce "separator" polynomials that split the sampled equations into local systems coupled only on clique overlaps. This yields a novel, convergent hierarchy of semidefinite programs (SDPs) with block sizes and sample requirements governed by local interactions rather than total problem size. Lastly, we show how to verify sample sufficiency and prune redundant equations numerically before solving. In robust estimation and motion planning, we obtain certifiably small optimality gaps at scales far beyond those reported for traditional sparse SOS. For example, we solve a truncated least-squares 3D registration problem with 1600 candidate correspondences in under 49 seconds using an off-the-shelf SDP solver on a laptop CPU.


## 精读解读（中文）
### 一、研究动机
半代数优化在工程优化中日益重要，但传统平方和（SOS）方法扩展到大规模问题时通常依赖手工构造基和冗余约束；采样式 SOS 虽能利用可行集几何、降低基规模并得到更紧松弛，却受限于离散变量导致样本指数增长、采样方程全局耦合而破坏相关稀疏性，且难以直接处理大量不等式和可约问题。本文旨在不枚举离散赋值、不引入松弛变量的前提下，把采样式 SOS 扩展到一般稀疏半代数问题。

### 二、技术方案（Method）
方法选择一个包含真实可行集的易处理代数簇，在其上随机采样，并以黑箱方式评估目标与约束；仅对省略的约束保留乘子，从而避免枚举和松弛变量。利用相关稀疏性引导团分解，并引入 separator 多项式把采样得到的证书方程拆成仅在团重叠处耦合的局部系统；再通过对局部单项式评估矩阵做 SVD 构造高效证书基与 separator 基，商掉冗余方向，组装成稀疏耦合的局部 SDP。求解前用秩检查验证样本充分性并剪除线性冗余方程，最后求解稀疏 SDP，并由对偶样本矩恢复原问题的全局最优解。

### 三、结果（Result）
在鲁棒估计和运动规划任务上，该方法在远超传统稀疏 SOS 报道的规模下取得可验证的小最优性间隙，并自动产生比手工定制公式更小的 SDP。一个代表性结果是：对含 1600 个候选对应的截断最小二乘 3D 配准问题，在笔记本 CPU 上使用现成 SDP 求解器可在 49 秒内求解。

### 四、结论（Conclusion）
该工作将采样式 SOS 的数值优势与传统 SOS 的直接适用性结合起来，使大规模可验证全局半代数优化可由黑箱评估而非逐问题代数工程实现。作者认为这为半代数优化提供了新的实用水平，并降低了对手工构造公式的依赖。

### 五、方法论与关键技术细节
关键实现包括：采样自包含可行集的易处理簇而非可行集本身；用 separator 多项式恢复相关稀疏性，使块规模和样本需求由局部交互而非总问题规模决定；用局部单项式评估矩阵的 SVD 构造证书/ separator 基，并通过秩检查与冗余方程剪枝保证样本充分性。该框架保持黑箱接口，适用于混合整数和不等式较多的问题，但其效果依赖所选取的易处理簇、相关稀疏结构及团分解质量，且求解前仍需数值验证样本充分性；结果以 SDP 松弛和可验证最优性间隙为核心，并未依赖传统训练损失或超参数调优。
