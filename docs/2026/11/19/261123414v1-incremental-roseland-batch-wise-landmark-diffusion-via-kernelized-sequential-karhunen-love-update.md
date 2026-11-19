# Incremental Roseland: Batch-wise Landmark Diffusion via Kernelized Sequential Karhunen--Loève Update

- 区域：精读区
- 排名：10
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Jeanie Schreiber
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23414v1) · [PDF](https://arxiv.org/pdf/2611.23414v1)

## TLDR
**TLDR:** The paper introduces **iRoseland**, a single-pass, bounded-memory streaming extension of landmark diffusion that uses a kernelized Sequential Karhunen–Loève SVD update with first-order degree correction and optional forgetting to track drifting data, matching Roseland on stationary streams and substantially outperforming equal-memory Roseland on long or drifting streams.

## Abstract
Landmark diffusion (Roseland) computes a diffusion-map-style spectral embedding from the singular value decomposition of a degree-normalized data-to-landmark kernel matrix, at a cost far below that of full diffusion maps. It assumes, however, that all data are available at once. We introduce incremental Roseland (iRoseland), which casts the landmark affinity as a row-growing matrix whose SVD can be updated with a kernelized Sequential Karhunen--Loève (SKL) scheme. Degre correction is handled by a first order expansion about a reference mean kernel row and so that the landmark-side eigenbasis may be recovered from a single landmark-by-landmark eigendecomposition at each step. The presented method requires only a single pass over the data and runs in bounded-memory with state independent of the number of points processed. A forgetting factor lets the method track drifting distributions, and a sample-size-invariant embedding keeps outputs comparable across time. Experiments show agreement with Roseland to round-off on stationary data, and accuracy that exceeds equal-memory Roseland by an order of magnitude on long streams. On drifting data, we observe large gains from forgetting with a window matched to the drift.


## 精读解读（中文）
### 一、研究动机
Roseland 通过地标把扩散映射的谱嵌入成本降到远低于全量扩散映射，但它假设所有数据一次性可用。流式数据分批到达且不能反复读取或存储，逐批重拟合 Roseland 的成本为 O(nm^2) 且内存随流增长，因此需要一种每批更新成本只依赖批大小和地标数、能在每批后立即给出当前嵌入并可选跟踪分布漂移的增量方法。

### 二、技术方案（Method）
输入是分批到达的数据点、固定 m 个地标、高斯核带宽 epsilon、嵌入维数 q、扩散时间 t 和遗忘因子 f；每批计算数据到地标的核行 W_B，并更新列和 c 与加权统计，把度归一化亲和 Ahat=D^{-1/2}W 的转置视为按列增长的矩阵，用 kernelized Sequential Karhunen–Loève 方案维护其截断 SVD。度归一化会使旧行随 c 变化而需要按 sqrt(d_i^old/d_i^new) 重缩放，主版本用围绕参考均值核行的一阶展开累积 T0 与 T1 并周期重参考，每步组装 m×m 矩阵做一次特征分解得到地标侧特征基，再按 Roseland 公式输出样本量不变的嵌入。精确版本显式重缩放并重分解存储行作为小流正确性参考，遗忘通过样本权重 omega_i=f^{2a_i} 一致作用于度与统计，每批后即可输出当前嵌入。

### 三、结果（Result）
在平稳数据上，iRoseland 与 Roseland 的嵌入一致到舍入误差；在长流且资源限制为相同 5.0 MB 内存预算时，其精度比等内存 Roseland 高一个数量级。实验在 S^1 与 S^2 数据上验证，并在漂移数据上观察到采用与漂移尺度匹配的遗忘窗口相比不遗忘有明显增益。

### 四、结论（Conclusion）
iRoseland 将 Roseland 扩展为单遍、有界内存的增量谱嵌入，适用于生理记录、床旁监测和可穿戴传感器等流式场景。f=1 时平稳数据下它与 Roseland 是同一估计器，优势主要在资源效率和无需重读数据；f<1 时可跟踪漂移但会引入由有效样本量决定的采样误差底。当前方法固定地标集，尚不跟踪地标几何漂移。

### 五、方法论与关键技术细节
该方法无监督训练损失，核心是 SVD 与特征分解；状态包括 m×m 的 T0 和 m×m×m 的 T1，内存不随已处理点数 n 增长但随地标数 m 立方增长，每批成本依赖批大小和 m 而非历史流长。平稳情形一阶线性化误差的理论启发式为 O(log n/n)，f=1 时有效样本量 n_ess=n，f<1 时采样误差约按 1/sqrt(n_ess) 下降并与滞后误差折中，epsilon、q、t、m、f 和重参考周期是主要超参。精确增量版本需保留每点信息或重读数据，累计成本不低于 Roseland；固定地标不跟踪地标漂移，数据远离地标会造成小且病态的度，f<1 有永久采样误差底，漂移下线性化误差随窗口长度和漂移率增长。
