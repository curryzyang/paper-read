# Verifier-Guided Model Discovery for Physical Dynamical Systems with Pretrained Symbolic Transformers

- 区域：精读区
- 排名：1
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Farbod Faraji, Francesco Belardinelli
- 机构：Imperial College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02662v1) · [PDF](https://arxiv.org/pdf/2608.02662v1)

## TLDR
A verifier-guided workflow around a pretrained symbolic transformer selects physically admissible, dynamically stable equations from pooled trajectory candidates, enabling interpretable symbolic discovery and forecasting for nonlinear systems—from Van der Pol oscillators to high-dimensional vortex shedding.

## Abstract
Reliable forecasting of nonlinear physical systems underpins scientific discovery and engineering decision-making. Yet high-fidelity simulations are prohibitively costly, and machine-learning surrogates can be opaque and encode assumptions about system dynamics, limiting generalizability. Pretrained transformers mapping synthetic ODE trajectories to equations offer interpretable alternatives, promising transfer without system-specific equation knowledge. Transferring them reliably to high-dimensional physical data, however, remains an open challenge. We develop a verifier-guided (VG) workflow around ODEFormer as a symbolic backbone, using dynamical and physical-admissibility criteria to select from a multi-trajectory candidate equation pool, enabling transfer. On canonical Van der Pol oscillators, VG outperforms the original ODEFormer workflow across held-out initial conditions. We then address vortex shedding, a phenomenon occurring in atmospheric and plasma systems of societal relevance, through coordinate reduction and symbolic discovery at fixed and varying Reynolds numbers. VG discovers fixed-parameter reduced-order equations that recover the fundamental shedding oscillator and higher harmonics without a wake-specific candidate library or prescribed Navier-Stokes structure, while the cross-parameter model generalizes to withheld regimes. Reconstruction fidelity alone did not determine symbolic discoverability, highlighting the importance of compatibility between latent dynamics and the backbone's pretraining distribution. This work establishes a verifier-guided neural-to-symbolic methodology for interpretable and physically auditable forecasting in the natural sciences.


## 精读解读（中文）
### 一、研究动机
高保真物理系统仿真成本高昂，而机器学习替代模型往往不透明且隐含对系统动力学的假设，限制其泛化能力。预训练符号Transformer虽能将合成ODE轨迹映射为可解释方程，并有望在不依赖特定系统方程知识的情况下迁移，但可靠迁移到高维物理数据仍是未解决的挑战。

### 二、技术方案（Method）
本研究提出验证器引导（VG）工作流，以预训练符号Transformer ODEFormer为符号骨架，保持其生成器不变。输入为可直接观测的ODE状态或经POD/自编码器降维的高维物理场（如圆柱绕流涡脱落场），跨参数发现时将参数p增广到状态并约束其导数为零。对每条轨迹/窗口独立解码生成候选方程池，经符号规范化去重后，用多轨迹滚动损失进行排序，选出前K个候选；随后应用可执行验证器套件，包括局部向量场一致性、有限有界演化、振荡幅值/频率/周期一致性、跨初值一致性，以及交叉参数情形下的参数方程为零、参数漂移可忽略和显式参数依赖等物理可容性测试。仅通过全部验证器的候选构成可容许集合，从中选择滚动损失最小者，并用Nelder-Mead对系数进行联合精炼，若精炼后不可容许则退回原方程。

### 三、结果（Result）
在Van der Pol振荡器上，VG在全部八个留出初始条件下均优于原始单轨迹ODEFormer流程：μ=0.5时中位后优化误差从1.21降至6.99e-4，μ=1.5时从4.5e-2降至3.27e-3。在圆柱绕流涡脱落问题中，VG在固定和变化雷诺数下均恢复了基本脱落振荡器及其高次谐波，无需尾流特定候选库或预设Navier-Stokes结构，跨参数模型可泛化到留出雷诺数区间。

### 四、结论（Conclusion）
以可执行的动力学与物理可容性验证作为模型选择约束，而非事后诊断，能够将预训练符号Transformer可靠迁移到高维物理数据，生成可解释且物理可审计的符号降阶模型。重建保真度本身不能决定符号可发现性，潜在动力学与骨干网络预训练分布的兼容性更为关键。

### 五、方法论与关键技术细节
关键细节包括：候选生成使用束搜索大小20、温度0.1；滚动损失按每坐标归一化MSE并在发现轨迹上平均；验证器包含局部导数匹配、有限性、振荡特征一致性等，并有具体阈值与容差设置（见附录）；交叉参数增广保持自主形式；系数精炼采用Nelder-Mead；局限性包括验证器建立的是规定域与时间范围内的经验可容性，且降维坐标可能省略高阶闭合所需动力学，此时发现的g是有效自主近似；VG不修改或重训生成器，而是通过多轨迹池化与验证收缩可识别候选集。
