# Minimal control time of some 1D first-order linear hyperbolic systems with row rank deficient boundary coupling matrix

- 区域：精读区
- 排名：2
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Long Hu, Guillaume Olive, Zengzhi Xin
- 机构：Shandong University, Jagiellonian University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00140v1) · [PDF](https://arxiv.org/pdf/2610.00140v1)

## TLDR
This paper characterizes the minimal control time for a class of 1D first-order linear hyperbolic systems with row rank deficient boundary coupling matrices, extending known results for full row rank cases.

## Abstract
The minimal control time of one-dimensional first-order linear hyperbolic systems is by now well-known when the boundary coupling matrix is full row rank. The goal of this article is to characterize the minimal control time for a class of systems with row rank deficient boundary coupling matrices.


## 精读解读（中文）
### 一、研究动机
一维一阶线性双曲系统在边界耦合矩阵 Q 行满秩时，其极小控制时间已有较完整刻画；但当 Q 行秩亏且控制数 m 不超过正速度分量数 p 时，现有结果多给出充分控制时间 T_CN 或特殊情形，缺少紧的极小时间公式。本文针对一类满足前 m-1 行与前 m-1 列子矩阵可逆的秩亏 Q，刻画零可控极小时间，并推广 CN21 的结论。

### 二、技术方案（Method）
把系统写成 y_t+Λ(x)y_x=M(x)y，Λ 对角且含 m 个负速度与 p 个正速度，边界为 y_-(t,1)=u(t)、y_+(t,0)=Q y_-(t,0)，在 L^2 状态和 L^2 控制下沿特征线定义解。利用 Q 的规范型 Q^c（左乘单位下三角、右乘可逆上三角且不改变可控性）把边界耦合化为至多一个非零元结构，并用单传输时间 T_k=∫_0^1 1/|λ_k| dx 编码各速度分量的特征穿越延迟。在假设 2≤m≤p 且 Q 的前 m-1 行/列子矩阵可逆下，通过特征线正向传播、边界反射以及内部耦合 M 的积分估计构造不可达状态以下界；再用显式边界控制和对偶可观测性不等式证明上界；τ^2 中的区间 I_{m+k} 由从 x=0 与 x=1 出发沿正速度 λ_{m+k} 和负速度 λ_m 的特征线交点确定。

### 三、结果（Result）
主定理给出 T_inf=max(τ^1, τ^2)，其中 τ^1=max_{1≤k≤m-1}(T_{m+k}+T_{c_k})，c_k 为 Q 规范型前 m-1 个非零元的列位置；τ^2=max{ max_{m≤k≤p, k<r_m}(T^{I_{m+k}}_{m+k}+T_m), T_{m+r_m}+T_m }，T^{I_{m+k}}_{m+k}=∫_{I_{m+k}}1/λ_{m+k}(ξ)dξ，r_m 为第 m 个非零元的行位置。若 r_m 不存在，即 rank Q=m-1，则 τ^2=max_{m≤k≤p}(T^{I_{m+k}}_{m+k}+T_m)；若 r_m=m，则 τ^2=T_{2m}+T_m。该公式覆盖并精确量化了 CN21 中 T_CN=max_{1≤k≤m}(T_{m+k}+T_k) 与真实极小时间之间的差距。

### 四、结论（Conclusion）
在行秩亏且满足前 m-1 行/列可逆的条件下，极小零可控时间由规范型非零元对应的负速度传播时间与部分正速度在特定特征区间上的传播时间共同决定，而不是简单的 T_m 与 T_{m+1} 之和。内部耦合 M 一般不改变形成 τ^1 的项，但会通过区间 I_{m+k} 影响 τ^2，从而改变正速度分量的有效传播并决定精确极小时间。

### 五、方法论与关键技术细节
关键假设为 2≤m≤p、λ_1<...<λ_m<0<λ_{m+1}<...<λ_{m+p}、M∈L∞，且 Q 的前 m-1 行与列子矩阵可逆，这排除了已被 HO22 覆盖的 c_k=m 情形。T_k=∫_0^1 1/|λ_k(ξ)|dξ 满足 T_1<...<T_m 与 T_{m+1}>...>T_{m+p}；规范型非零元位置 (r_k,c_k) 由高斯消元型 LU 变换确定。证明在 L^2 框架下按特征线进行，下界来自构造不可达/不可观测量，上界来自显式控制或对偶不等式；主要局限是区间 I_{m+k} 一般需由特征线与内部耦合递推确定，未必有参数 Λ,M,Q 的显式闭式，且结论限于 m≤p 与该子矩阵可逆的秩亏类。
