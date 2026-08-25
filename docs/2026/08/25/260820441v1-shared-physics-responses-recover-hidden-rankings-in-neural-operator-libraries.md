# Shared Physics Responses Recover Hidden Rankings in Neural Operator Libraries

- 区域：精读区
- 排名：3
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Hanbing Liang, Fujun Liu
- 机构：Changchun University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20441v1) · [PDF](https://arxiv.org/pdf/2608.20441v1)

## TLDR
TLDR: The paper shows that ranking a finite library of neural operators can be done without ground truth by using a single shared linearized physics response, which recovers over 99% of hidden model preferences and optimal checkpoints across diverse PDE surrogate libraries.

## Abstract
Selecting the optimal neural-operator prediction during deployment is challenging when high-fidelity reference solutions are unavailable. We demonstrate that under a squared Hilbert-space loss, ranking a finite model library depends strictly on the low-dimensional span of candidate differences, allowing us to score all models simultaneously using a single anchor-based linearized response of the governing equation. This shared physical diagnostic accurately recovered over 99.6\% of pairwise preferences and 99.0\% of optimal checkpoints across diverse Fourier and convolutional operator libraries for fluid, reaction-diffusion, and wave dynamics. Furthermore, the corrected physical proxy frequently outperformed the best individual candidates, and we establish computable sufficient conditions that rigorously certify exact decisions for strongly monotone discretizations. By exploiting the local dynamical response rather than raw defect magnitude, this framework enables the reliable and highly efficient deployment of scientific surrogates without requiring ground-truth data.


## 精读解读（中文）
### 一、研究动机
在部署神经网络算子时，高保真参考解不可用，导致无法直接评估候选模型或检查点的优劣；而不同候选在具体输入和感兴趣科学量下表现各异，因此需要一种无需真实数据即可恢复候选库隐藏排序的方法。现有残差诊断仅反映原始缺陷大小，无法刻画缺陷对任务输出的影响，且逐候选修正成本高昂。本文旨在利用控制方程的物理响应，以单个共享计算同时对所有候选进行可靠排序。

### 二、技术方案（Method）
给定物理输入a和候选预测{v_i}，先由参考自由规则C构造库锚点w=C(v_1,...,v_N)；在w处对离散物理系统A_a(v)=0（含初边值条件）线性化，得到L_w=D A_a(w)，并求解一次线性化共享响应L_w δ_w = -A_a(w)+ℓ（ℓ为代数求解缺陷），令修正状态s=w+δ_w。通过任务映射Q_a得到共享代理q=Q_a(s)，并将每个候选映射为y_i=Q_a(v_i)；在平方希尔伯特空间损失下，用距离S_i(q)=||q-y_i||_M^2对所有候选评分并排序，从而选出最优预测或对面板内检查点平均评分。理论证明决策仅依赖候选差异张成的低维子空间D（维度≤N-1），且该共享响应是全局精确排序的充分且最小（在有限维线性观测下）条件；对强单调反应扩散算子，还给出可计算充分条件以严格认证同网格决策。

### 三、结果（Result）
在Burgers、反应扩散、Sine-Gordon及波动力学的多组傅里叶与卷积神经算子库中，该方法恢复超过99.6%的非平局成对偏好和99.0%的最优检查点；在八个库（2方程×2架构×2种子）上，99.01%的输入-库组合选出的候选与最佳库损失差在10^-6以内。原始残差仅恢复67.83%的选择；在Sine-Gordon上恢复95.57%；在算子不匹配的二维可压缩流探针中恢复10/10比较。修正后的共享物理代理在多个场景中优于最佳个体候选。

### 四、结论（Conclusion）
通过利用单一锚点线性化物理响应，而非原始残差幅度，可以在没有真实数据的情况下准确恢复有限神经算子库的隐藏排序，并显著降低部署开销。该方法同时提供可计算的充分条件来严谨认证决策，为科学代理模型的可靠高效部署提供了新范式。

### 五、方法论与关键技术细节
核心先验是平方希尔伯特空间损失，使得成对偏好仅依赖候选差异子空间D，维度至多N-1；锚点构造可任意选择参考自由规则，但理论保证不受具体规则影响；线性化响应引入求解缺陷ℓ和物理余项R_A(e)，误差通过条件恒等式精确传播到决策坐标；对二次Burgers算子，余项为精确双线性形式，可推导局部二次误差界。有效性受候选间隔影响，间隔过小（≤10^-6）时决策天然困难；非线性任务映射会引入额外物理-任务余项，非希尔伯特或真实归一化损失会改变比较几何。局限性包括需要线性化可行性、需处理代数求解缺陷，且对一般非线性问题严格认证需要局部化或方向性支持界限。
