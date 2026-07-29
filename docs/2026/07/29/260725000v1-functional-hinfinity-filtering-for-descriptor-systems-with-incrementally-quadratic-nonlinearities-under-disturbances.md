# Functional H_infinity Filtering for Descriptor Systems with Incrementally Quadratic Nonlinearities under Disturbances

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Rishabh Sharma, Nutan Kumar Tomar
- 机构：Indian Institute of Technology Patna
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.25000v1) · [PDF](https://arxiv.org/pdf/2607.25000v1)

## TLDR
This paper presents a functional H∞ filter for nonlinear descriptor systems under disturbances, using an explicit state-space formulation and incremental quadratic constraints to achieve reduced-order estimation with guaranteed asymptotic stability and L2-performance via rank conditions and linear matrix inequalities.

## Abstract
This paper develops a functional H_infinity filter for nonlinear descriptor systems subject to external disturbances. Conventional H_infinity filtering approaches for descriptor systems impose restrictive regularity assumptions and employ implicit descriptor-form filters, leading to practical implementation difficulties. Moreover, existing approaches mainly target full-or reduced-order state estimation, which is computationally inefficient when only a specific functional of the state is required. To address these limitations, the filter is formulated directly in an explicit state-space framework and can be initialized with arbitrary initial values. The filter order is chosen to be less than or equal to the dimension of the functional vector to be estimated, thereby reducing computational complexity. The considered nonlinearities are characterized using incremental quadratic constraints parameterized by appropriate multiplier matrices, which encompass Lipschitz, one-sided Lipschitz, monotone, and many other nonlinearities. Sufficient criteria for the existence of the proposed filter are established through a rank condition imposed on the system matrices together with a set of linear matrix inequalities (LMIs). Under these conditions, asymptotic stability of the estimation error dynamics is guaranteed, while the influence of external disturbances on the error is bounded within a prescribed L2-performance framework. Finally, numerical simulations demonstrate and validate the effectiveness of our theoretical results.


## 精读解读（中文）
### 一、研究动机
现有描述系统的H_infinity滤波方法存在局限性：它们通常依赖严格的正则性假设，并采用隐式的描述器形式滤波器，导致实际实现困难；同时，这些方法主要针对全状态或降阶状态估计，当只需估计状态的特定线性函数时计算冗余。因此，有必要开发一种更通用的功能H_infinity滤波器，能够处理更广泛的非线性特性，并降低计算复杂度。

### 二、技术方案（Method）
本文考虑一类受外部扰动影响的非线性描述系统，其非线性特性由增量二次约束（δQC）统一刻画，涵盖Lipschitz、单边Lipschitz、单调等多种非线性。所设计的滤波器采用显式状态空间结构，阶数不大于待估计功能向量维数p，可任意初始化。滤波器存在性的充分条件由系统矩阵的秩条件结合一组线性矩阵不等式（LMI）给出。设计流程包括：选定滤波器阶数l1（≤p），求解满足秩条件的矩阵参数，并利用LMI工具包求解可行解，从而确定滤波器增益矩阵N、H1、L1、F1、R、M1、M2。

### 三、结果（Result）
在满足所提出的秩条件和LMI可行解的条件下，所设计的功能H_infinity滤波器能保证估计误差动态的渐近稳定性，并将外部扰动对误差的影响限制在指定的L2性能水平内。数值仿真验证了理论结果的有效性，表明滤波器能够准确估计所需的状态线性函数。

### 四、结论（Conclusion）
本文成功开发了一种适用于受扰动且具有增量二次非线性描述系统的功能H_infinity滤波器，克服了传统方法的正则性假设和隐式结构缺陷。该滤波器采用显式状态空间形式，阶数灵活，可处理更广泛的非线性类，为实际工程应用提供了更实用的解决方案。

### 五、方法论与关键技术细节
非线性特性通过增量二次约束和乘子矩阵统一描述，涵盖广泛非线性类；滤波器阶数可小于等于p，降低计算复杂度；存在性条件依赖于系统矩阵的秩条件和LMI，可利用标准LMI工具箱求解；滤波器可任意设置初值，无需一致初始条件；方法适用于矩形描述系统，扩展了现存结果的应用范围；局限性在于条件为充分条件，可能具有保守性。
