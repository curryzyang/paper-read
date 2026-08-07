# Beyond Rotations: AuroOFT for Expressive Quantized Orthogonal Fine-Tuning

- 区域：精读区
- 排名：6
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Yue Han, Dianlin Wang
- 机构：China Electronics Corporation, National University of Defense Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05253v1) · [PDF](https://arxiv.org/pdf/2608.05253v1)

## TLDR
AuroOFT enhances quantized orthogonal fine-tuning (QOFT) by adding a zero-initialized, gated low-rank nonlinear residual branch alongside the stable QOFT rotation path, improving mathematical reasoning over matched QOFT by 1.30–2.70% and over QLoRA by 6.52–10.62% while using fewer trainable parameters.

## Abstract
Quantized orthogonal fine-tuning (qoft) enables parameter-efficient adaptation of low-bit language models by learning structured activation rotations before frozen quantized weights. However, its task-specific updates remain constrained to linear orthogonal transformations, limiting input-dependent nonlinear corrections. We introduce AuroOFT, which keeps qoft as a stable quantization-compatible branch while attaching a zero-start gated low-rank nonlinear residual to each adapted linear layer. AuroOFT maps activations into an RMS-normalized compact latent space and uses adaptive nonlinear bases with bounded or token-dependent gating. The zero-initialized up projection makes AuroOFT functionally identical to qoft at initialization, while orthogonality remains a branch-level stability property rather than a property of the combined nonlinear layer. Under matched data, optimization, decoding, and parser protocols, AuroOFT improves Macro-6 over matched qoft by 1.30-2.70% on the 1.5B/3B Qwen2.5 settings, exceeds QLoRA by 6.52-10.62%, and saves 32.3-44.7% trainable parameters relative to QLoRA in representative scales. The small exam-style multiple-choice math set is treated only as a protocol-sensitivity diagnostic. Our code is available at the anonymous repository: https://anonymous.4open.science/r/AuroOFT-F3FD.


## 精读解读（中文）
### 一、研究动机
量化正交微调（QOFT）通过冻结量化权重前的结构化激活旋转实现低比特语言模型的高效适配，但任务更新被限制为线性正交变换，无法表达依赖输入的修正，形成正交表达性瓶颈。数学推理等任务需要局部、符号或数值比较相关的非线性修正，因此需要在不破坏QOFT稳定量化路径的前提下增强其表达能力。

### 二、技术方案（Method）
AuroOFT将每个被适配线性层包装为双分支结构：上分支保持QOFT，即输入激活x经Cayley-Neumann截断级数参数化的旋转（块大小32、5个Neumann项）后送入冻结NF4权重；下分支为残差，先做下投影A_lx，经恒等或FP32 RMSNorm，再经自适应非线性层（Lite ANL用双tanh加可学习逐维残差；SplineNorm用tanh+FP32 RMSNorm+B样条基；增强型Dual ANL用tanh基与SiLU门控基的softmax混合），随后Dropout、零初始化的上投影B_l和门控（标量/有界标量/逐token）乘以α/r缩放，最后与QOFT输出相加。B_l=0使初始化时与QOFT逐层完全等价；训练支持全层或选择性注入，QOFT与残差分支分设参数组、独立学习率和梯度裁剪。

### 三、结果（Result）
在数据、优化、解码和解析协议完全对齐的条件下，AuroOFT在Qwen2.5 1.5B/3B设置上相比匹配的QOFT将Macro-6提升1.30–2.70个百分点，比QLoRA高6.52–10.62个百分点，并在代表性规模上比QLoRA节省32.3–44.7%的可训练参数。小型考试式数学选择题集仅作为协议敏感性诊断，不作为结构主张的独立证据。

### 四、结论（Conclusion）
AuroOFT表明，正交性应作为量化适配的稳定主干，而非整个组合层的属性；非线性作为零起始门控低秩残差，能在不修改冻结量化权重、不把非线性插入Cayley旋转内部的前提下扩展每层可表达的函数族。该方法在初始化时精确恢复QOFT，在优化中提供受控的额外表达能力，兼顾量化稳定性和任务自适应修正能力。

### 五、方法论与关键技术细节
关键实现细节包括：QOFT采用块大小32和5项Neumann级数近似Cayley变换；残差分支的上投影零初始化保证与QOFT的初始化等价；门控有三种形式——无约束标量η_l、有界标量2σ(γ_l)、逐token门控2σ(W_g z)，增强版将η_l初始化为1、γ_l和W_g初始化为0以避免小门控抑制早期梯度；SplineNorm使用FP32 RMSNorm和tanh将激活限制在B样条网格[-1,1]内，网格大小M、阶数p；残差缩放为α/r；由于非线性分支的输入依赖特性，推理时不能与QOFT合并，会带来额外推理成本；正交性只在QOFT分支层面成立，组合层整体不再正交；小规模选择题集仅作诊断。
