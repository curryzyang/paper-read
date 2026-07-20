# Harnessing GPU Acceleration in Large-Scale Process Optimization

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Boxun Huang, David Y. Shu, Michel Schanen, Mihai Anitescu, Rahul Gandhi, Sungho Shin
- 机构：Argonne National Laboratory, Massachusetts Institute of Technology, Shell Technology Center
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15420v1) · [PDF](https://arxiv.org/pdf/2607.15420v1)

## TLDR
This paper demonstrates a proof-of-concept GPU-resident workflow for equation-oriented process optimization, achieving a 21× speedup over CPU solvers on a large-scale CO2 absorber design problem under feed uncertainty.

## Abstract
This paper presents a proof-of-concept workflow for equation-oriented process optimization that runs entirely on a GPU. Process optimization models often incorporate complex interconnected unit operations, dynamics, and uncertainties, resulting in large nonlinear programs that can be computationally demanding for conventional CPU-based solvers. Although emerging GPU-based solvers offer substantial computational benefits, their application to process optimization has been limited by the lack of GPU-compatible process modeling tools. We address this gap by prototyping the GPU-compatible process optimization models using an existing GPU-capable optimization software stack, including ExaModels (algebraic modeling system), MadNLP (optimization solver), and cuDSS (linear solver). ExaModels formulates the process optimization problem in a GPU-compatible way by exposing its repeated algebraic structure, while MadNLP and cuDSS solve the resulting nonlinear program on the GPU. This workflow is demonstrated on a CO2 absorber design problem under feed uncertainty, in which a shared column diameter is minimized subject to equilibrium and hydraulic constraints in all scenarios. For the largest case with 5,000 scenarios and 1.5 million variables, the GPU workflow achieves a speedup of approximately 21\times over a single-threaded CPU baseline using JuMP, Ipopt, and MA57.


## 精读解读（中文）
### 一、研究动机
大规模过程优化问题常因包含复杂互联单元操作、动态和不确定性而生成大型非线性规划，传统CPU求解器计算负担重。新兴GPU求解器虽有显著加速潜力，但缺乏GPU兼容的过程建模工具，因此需要开发全GPU驻留的工作流以填补这一技术空白。

### 二、技术方案（Method）
本文提出一种全GPU驻留的方程导向过程优化工作流，使用ExaModels.jl作为代数建模系统，通过生成器语法暴露重复的代数结构（如MESH方程）来构建GPU兼容的优化模型；然后利用MadNLP.jl作为优化求解器，cuDSS作为稀疏线性求解器，在NVIDIA H200 GPU上完成函数评估、自动微分、KKT系统组装和稀疏线性代数，避免CPU-GPU间频繁数据传输。案例为CO2吸收塔直径最小化问题，考虑进料不确定性，包含共享设计变量（塔径）和各场景下的阶段操作变量，约束包括物料平衡、相平衡、热量平衡、压力关系和水力学限制，模型规模随场景数线性增长，最大达150万变量和105万等式约束。

### 三、结果（Result）
在5000场景、约150万变量的最大案例中，GPU工作流（ExaModels/MadNLP/cuDSS）求解耗时为33.3秒，相比单线程CPU基线（JuMP/Ipopt/MA57）的695.5秒获得约20.9倍加速，相比CPU版ExaModels/MadNLP/MA57的707.8秒获得约21.3倍加速。迭代次数相近（例如5000场景下GPU迭代81次，CPU JuMP/Ipopt迭代80次），表明加速主要归因于更低的每迭代计算成本。

### 四、结论（Conclusion）
本文证明了全GPU驻留工作流在基于场景的不确定性过程优化中的可行性和可扩展性。通过暴露MESH约束的重复结构，GPU加速在足够大的场景集下能够超越CPU单线程性能，实现数量级加速。未来工作将扩展到更详细的吸收塔模型和完整流程，并进一步利用GPU中的场景块结构优化KKT系统求解。

### 五、方法论与关键技术细节
数据来源：从7个实测基线案例通过随机凸组合生成场景，所有场景位于测量凸包内。先验假设：气相为理想气体混合物，液相为理想液体混合物，水-汽平衡使用拉乌尔定律，CO2-汽平衡使用亨利定律，温度依赖的平衡常数采用Kent-Eisenberg相关性。目标函数：最小化共享塔径。超参数：CPU运行采用单线程、单BLAS线程，Julia 1.12.1，CUDA v6.1.0，求解器容忍度均为10⁻⁸。复杂度：问题规模随场景数|Ω|线性增长，每个场景引入约300个变量和210个等式约束（基于10级平衡级模型）。局限性：小场景集（如|Ω|=1或10）时GPU固定启动开销占比大，未体现加速；目前仅针对原型吸收塔问题，尚未推广至完整流程或多组件详细模型。
