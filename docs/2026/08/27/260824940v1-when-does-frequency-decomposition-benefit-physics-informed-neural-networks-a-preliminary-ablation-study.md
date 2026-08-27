# When Does Frequency Decomposition Benefit Physics-Informed Neural Networks? A Preliminary Ablation Study

- 区域：精读区
- 排名：3
- 匹配度：5.9/10
- 来源：arxiv
- 作者：Shubham Rai
- 机构：bibha.ai
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24940v1) · [PDF](https://arxiv.org/pdf/2608.24940v1)

## TLDR
This paper introduces a dual-branch spectrally-gated PINN (DBSG-PINN) and an ablation study across five 1D PDE benchmarks, finding that explicit frequency decomposition and adaptive gating improve accuracy mainly on spectrally complex/multi-scale problems (up to 59.2% error reduction) while providing little or even negative benefit on smoother, single-scale PDEs.

## Abstract
Partial differential equations (PDEs) often have high-frequency and multi-scale features that neural networks struggle to approximate. Physics-Informed Neural Networks (PINNs) build the governing equations directly into training, but suffer from spectral bias: they learn low-frequency components faster than high-frequency ones. Techniques such as Fourier feature embeddings and sinusoidal activations address this, but most studies assume they help across the board without checking which spectral regimes actually benefit. We introduce a dual-branch, spectrally-gated architecture (DBSG-PINN) that splits low- and high-frequency components into separate subnetworks joined by an adaptive gate, and use it to run a partially controlled ablation of frequency decomposition and spectral routing. We test this on five one-dimensional benchmark PDEs, ranging from smooth, single-scale problems to oscillatory, multi-scale ones. Frequency decomposition helps most on the spectrally complex benchmarks, cutting relative $L_2$ error by up to $59.2\%$ on a multimodal wave problem, but gives little benefit on smoother PDEs. On one benchmark (1D Wave), it performs substantially worse than a simpler fixed-combination variant. The gate's benefit scales with how spectrally rich the target solution is: the full model's advantage over the ablations is largest on multi-scale benchmarks and smallest (or negative) on single-scale ones, consistent with the gate exploiting frequency structure rather than acting as noise,though we do not directly visualize or quantify its spatial activations in this study. All results come from a single training seed across five 1D benchmarks, so we present this as an exploratory study meant to raise questions rather than answer them, and outline the additional seeds and benchmarks needed to test whether the pattern holds.


## 精读解读（中文）
### 一、研究动机
偏微分方程常包含高频与多尺度特征，而神经网络受谱偏差影响，对低频分量学习快、对高频分量学习慢。现有频率感知方法（如傅里叶特征、正弦激活）大多默认对所有问题都有效，但缺乏对不同谱复杂度问题的系统性对照验证。本文旨在探究显式频率分解何时真正有益于PINN，并通过受控消融实验分析谱路由的作用。

### 二、技术方案（Method）
提出DBSG-PINN双分支谱门控架构：低频分支用tanh激活捕获光滑分量，高频分支用sin(ωx)激活建模振荡行为，两分支输出由轻量门控网络产生的sigmoid系数g(x,t)做凸组合得到最终预测。输入坐标(x,t)并行送入三个子网络，联合端到端训练，损失为PDE残差、初始条件、边界条件的加权和，采用Adam加L-BFGS两阶段优化。在5个一维基准PDE上对比完整模型与三个消融变体：NoGate（门固定为0.5）、LowOnly（仅低频分支）、HighOnly（仅高频分支），各变体保持优化器、迭代预算、配点策略和损失权重一致，但分支容量非严格匹配。

### 三、结果（Result）
频率分解在谱复杂基准上收益最大：多模态波动问题相对L2误差最高降低59.2%，光滑单尺度PDE上收益很小。在1D Wave基准上，完整模型比简单固定组合（NoGate）显著更差。门控贡献随目标解的谱丰富度变化：全模型相对消融变体的优势在多尺度基准上最大，在单尺度基准上最小或为负，表明门控在利用频率结构而非仅充当噪声。所有结果基于5个一维基准、每个单一训练种子，属于探索性研究。

### 四、结论（Conclusion）
频率分解并非普遍有益，其价值取决于PDE解的谱复杂度：对多尺度振荡问题帮助显著，对平滑问题可能无效甚至有害。学习式门控在谱丰富时能带来增益，但该模式需更多种子和基准验证。当前研究仅提出初步问题，未建立通用规律，需进一步控制种子方差、扩展基准并直接可视化门控空间激活以确认结论。

### 五、方法论与关键技术细节
关键要点：1) 分支容量不完全匹配，高频分支在多数基准上更宽（如64 vs 32单元），深度差1-2层，故LowOnly与HighOnly对比非严格容量对照；2) 激活函数固定频率ω，'频率分解'指软归纳偏置而非严格频谱分离，门控决定各分支贡献；3) 损失权重固定且所有变体共享同一损失景观，未用自适应加权；4) 评估网格为均匀100×100，训练配点间距按基准不同；5) 局限：单一训练种子、无门控空间激活可视化、未量化门控与局部谱内容的关系，需额外种子和基准测试模式是否成立。
