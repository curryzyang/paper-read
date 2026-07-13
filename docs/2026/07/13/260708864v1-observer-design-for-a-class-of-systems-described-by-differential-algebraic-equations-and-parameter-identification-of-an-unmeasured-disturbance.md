# Observer Design for a Class of Systems Described by Differential-Algebraic Equations and Parameter Identification of an Unmeasured Disturbance

- 区域：精读区
- 排名：9
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Olga Oskina, Alexey Bobtsov
- 机构：ITMO University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08864v1) · [PDF](https://arxiv.org/pdf/2607.08864v1)

## TLDR
This paper proposes an observer for linear descriptor systems with unknown unmatched disturbances, enabling state estimation and parameter identification of the disturbance via a novel parameterization that linearizes the problem despite nonlinear dependence on unknown parameters.

## Abstract
This paper addresses the problem of observer design for a class of linear descriptor systems affected by a certain class of unknown unmatched disturbances. The objective is to estimate the components of the state vector, as well as the unknown parameters of the unmeasured disturbance. To solve this problem, structural assumptions are introduced under which an observer for the dynamic part of the state vector is constructed. Then, based on the obtained state estimate, the disturbance signal is reconstructed, and its unknown parameters are identified. A new parameterization method is proposed for a class of disturbance input signals that depend nonlinearly on unknown parameters, making it possible to obtain a linear regression in the corresponding unknowns. Numerical simulations are presented to demonstrate the effectiveness of the proposed procedures.


## 精读解读（中文）
### 一、研究动机
针对一类受未知不匹配扰动影响的线性描述符系统，现有状态估计方法常因简化系统结构而丢失信息，导致估计精度下降。本文旨在同时估计状态向量分量和未测量扰动的未知参数，以支撑后续扰动补偿与控制设计。

### 二、技术方案（Method）
系统建模为微分-代数方程，状态向量分为动态和代数两部分。通过结构假设（代数方程可解、输出方程无直接扰动通道、特定可观测性条件）将系统降阶为不含扰动项的微分方程。设计未知输入观测器：采用坐标变换避免输出和输入的导数，通过滤波器重构导数信号。基于状态估计，利用输出方程重构扰动信号。针对扰动信号中未知参数非线性嵌入形式（如指数函数组合），提出基于延迟扩展和DREM混合的参数化方法：引入多个已知延迟，构造扩展回归矩阵和向量，通过行列式运算和代数变换提取仅含未知参数的线性组合，最终得到关于新参数向量的线性回归方程。采用递归最小二乘算法估计该线性参数，再通过代数关系恢复原始未知参数。

### 三、结果（Result）
在数值仿真中，对于包含两个指数扰动分量的示例系统，所提观测器能有效估计动态状态分量，扰动信号重构准确，未知参数θ1和θ2的估计值收敛至真值（θ1=-0.1, θ2=-0.3）。仿真验证了从状态估计到扰动重构再到参数辨识的完整流程的有效性。

### 四、结论（Conclusion）
本文提出了一种针对线性描述符系统的观测器设计及扰动参数辨识方法，通过结构假设和延迟参数化技术，将非线性参数估计问题转化为线性回归，成功实现了同时估计状态和扰动未知参数的目标。该方法拓展了描述符系统在扰动环境下状态估计的应用可能性。

### 五、方法论与关键技术细节
关键点包括：1）假设扰动由已知基函数与未知指数参数的组合构成，且可通过多个延迟线性参数化；2）观测器设计需要输出无直接扰动通道（C5=0）且(C3, B2a)满秩条件；3）避免微分使用一阶滤波器（λ_f=10³）重建导数，并需等待观测器（T_obs）和滤波器（T_fil）瞬态衰减后再启动辨识；4）DREM扩展需ℓ个延迟，并额外引入一个延迟（ℓ+1）构造标量回归；5）超参数包括观测器增益L（使M_a-LC3为Hurwitz）、滤波器参数λ_f、延迟集合{D_j}及协方差矩阵初值；6）局限性：要求信号光滑且扰动形式满足延迟参数化结构，不规则分量δ0仅被假定有界但未详细处理。
