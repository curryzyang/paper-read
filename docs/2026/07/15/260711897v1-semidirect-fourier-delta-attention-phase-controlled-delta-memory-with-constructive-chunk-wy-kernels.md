# Semidirect Fourier Delta Attention: Phase-Controlled Delta Memory with Constructive Chunk-WY Kernels

- 区域：精读区
- 排名：5
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Tiantian Zhang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11897v1) · [PDF](https://arxiv.org/pdf/2607.11897v1)

## TLDR
The paper introduces Semidirect Fourier Delta Attention (SFDA), a phase-controlled generalization of Kimi Delta Attention that adds learnable Fourier phase to the recurrent memory transition while preserving a constructive chunk-WY factorization for efficient and exact affine chunk transfer, enabling cyclic memory and state tracking.

## Abstract
Linear attention replaces softmax attention's growing KV cache with a fixed recurrent state, but this compression limits exact state tracking and long-context memory. We introduce \emph{Semidirect Fourier Delta Attention} (SFDA), a phase-controlled generalization of Kimi Delta Attention that replaces real diagonal decay with block-rotational Fourier control: \[ S_t=(I-β_t k_tk_t^*)Λ_tS_{t-1}+β_tk_tv_t^*, \qquad Λ_t=\diag(α_t\odot e^{iθ_t}). \] Our main result is a constructive chunk-WY factorization for products \(A_t=Λ_t-u_tr_t^*\), giving \[ A_t\cdots A_1=Γ_t-Y_tM_tW_t^* \] with rank growth bounded inside fixed chunks. This yields an exact affine chunk transfer, formal stability and complexity bounds, and a compact characterization of phase-plus-low-rank memory. We verify the algebra numerically and show in toy state-tracking experiments that SFDA learns cyclic memory where the phase-disabled KDA baseline remains near chance. Fused kernels and large-scale language-model comparisons are left to future work.


## 精读解读（中文）
### 一、研究动机
线性注意力使用固定循环状态代替增长的KV缓存，但固定状态的内存使得精确复制、算法状态跟踪和长上下文检索困难。Kimi Delta Attention (KDA) 采用实数对角衰减加秩一delta修正，但缺乏相位控制，无法学习循环记忆。SFDA 旨在通过引入块旋转傅里叶控制算子，在不破坏结构化块WY核的前提下，为KDA添加代数相位/控制动力学。

### 二、技术方案（Method）
SFDA 的循环更新为 S_t = (I - β_t k_t k_t^*) Λ_t S_{t-1} + β_t k_t v_t^*，其中 Λ_t = diag(α_t ⊙ e^{iθ_t}) 是复数对角相位-衰减矩阵。关键技术是构造性块WY定理：对 A_t = Λ_t - u_t r_t^*（u_t = β_t k_t, r_t = k_t），块内 A_t ... A_1 可分解为 Γ_t - Y_t M_t W_t^*，其中 Γ_t 是相位控制乘积，Y_t, M_t, W_t 通过递归更新，秩增长限于块大小 B。序列被分成固定长度块，块内计算 WY 因子，块间通过边界状态精确扫描。相位控制通过实数块旋转实现，无需FFT。

### 三、结果（Result）
在 toy 循环记忆实验中，SFDA 学习循环计数器而 KDA 基线接近随机。理论证明 SFDA 精确实现有界循环记忆，构造性块WY定理提供精确块传输和复杂度界。广义 tied-write 模板精确实现任意有限自动机。紧凑表示包括产品循环计数器、寄存器/重置记忆和有界栈，每块存储 O(B^2 d + B d v) 标量，计算 O(B^2 d + B d v + B d)。

### 四、结论（Conclusion）
SFDA 是 KDA 的相位控制泛化，在不破坏结构化核的前提下增加了相位动力学，使其能够表示循环记忆和有限自动机，并在 toy 任务上验证了优势。未来工作需要融合内核加速和大规模语言模型比较，以探究 SFDA 是否能支持更高的线性-全局注意力比例，在保持计算效率的同时提升长上下文能力。

### 五、方法论与关键技术细节
数据：token 表示通过投影得到 query、key、value、步长 β_t、通道衰减 α_t 和相位 θ_t。建模：主架构为 tied SFDA，另有 write-decoupled 变体用于自动机构造。关键模块：相位控制块旋转（实数块旋转）和秩一delta修正，保证结构化块WY核。训练/推理使用块WY递归，块大小 B 是超参，块内秩增长 O(B)，块间边界状态精确传输。超参包括 B、状态维度 d 和值维度 v，稳定性设定 α_t∈[0,1)、β_t∈(0,1] 以控制范数。局限性：仅 toy 实验，无融合内核和大规模比较；精确秩增长需权衡块大小；有限自动机 one-hot 提升可能不紧凑。
