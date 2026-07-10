# Unlocking Temporal Generalization in Hamiltonian Video Dynamics Models

- 区域：精读区
- 排名：2
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Eli Laird, Corey Clark
- 机构：Southern Methodist University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07763v1) · [PDF](https://arxiv.org/pdf/2607.07763v1)

## TLDR
This paper identifies and fixes two failure modes—latent magnitude growth from unconstrained action-force maps and global truncation error accumulation from under-resolved integrators—in Hamiltonian Generative Networks to enable stable temporal generalization to unseen step sizes in non-conservative video dynamics models.

## Abstract
World models are typically trained to predict discrete-time physical dynamics with a fixed step size baked into the model weights, preventing prediction at variable temporal resolutions. This matters for hierarchical planning, sim-to-real transfer, and scientific or game-engine applications that must query the same dynamics at multiple timescales. Hamiltonian Generative Networks (HGN) offer a principled path forward, grounding predictions in a continuous-time energy function that is, in principle, independent of the observation frame rate. In practice, however, their temporal generalization breaks down in non-conservative settings. We show that in externally forced, dissipative environments, HGN rollouts at step sizes beyond the training regime fail due to distinct failure modes, including latent magnitude growth driven by an unconstrained action-force map, and global truncation error accumulation from an under-resolved integrator. We identify a targeted fix for each mechanism and demonstrate stable dynamics prediction at temporal resolutions well outside the training distribution. In a detailed analysis, we recommend several strategies for enabling temporal generalization in continuous-time video generation.


## 精读解读（中文）
### 一、研究动机
现有世界模型通常以固定步长预测离散时间物理动态，无法在可变时间分辨率下泛化，这限制了其在分层规划、模拟到现实迁移以及多时间尺度科学仿真中的应用。Hamiltonian生成网络（HGN）虽基于连续时间能量函数提供了原则性方案，但在非保守环境中（如外部强迫和耗散系统）时间泛化能力会退化。本文旨在系统识别HGN在超出训练步长范围时失效的机制，并提出针对性修复方法以实现稳定预测。

### 二、技术方案（Method）
采用基于Hamiltonian生成网络（HGN）的框架，包括卷积编码器将像素帧映射到潜在相空间（位置q和动量p）、参数化可分离Hamiltonian函数H=T(p)+V(q)和阻尼系数γ，以及作用力映射G(a)构成端口-Hamiltonian预测器。使用修改的勒普弗拉格积分器在时间步长下对称折叠阻尼和驱动力。训练时通过变分下界（ELBO）优化，从初始潜在状态展开整个轨迹而不重新编码。推理时引入子步协议：将每个观测步长分为N个子步（保持总冲量不变），用以区分积分器截断误差和表示学习失败。数据来自强迫阻尼弹簧振荡器（64×64 RGB图像），训练步长0.4，共50,000条50帧序列。

### 三、结果（Result）
识别出两种主要失败模式：能量幅度增长（因未约束的作用力映射G(a)导致潜在状态振幅发散，产生高频伪影）和相位漂移累积（因全局截断误差使预测轨迹逐渐失相）。对G施加谱归一化约束可消除幅度发散；推理时采用子步（如N=4，等效步长≈训练步长）可消除相位漂移，在评估步长1.5下恢复准确预测。像素级指标（MAE、PSNR、SSIM、LPIPS）显示子步策略使外推性能接近训练水平，证明失效主要源于积分器而非学习到的Hamiltonian。

### 四、结论（Conclusion）
本文证明了在外部强迫和耗散环境中，HGN在超出训练步长的外推预测中因能量爆发和积分器误差而失败，并提供了针对性的修复方法（谱归一化作用力映射和推理时子步）。通过详细分析，建议在连续时间视频生成中采用约束驱动力和自适应积分策略以实现时间泛化。该工作为构建可跨时间分辨率泛化的物理感知世界模型提供了实用指导。

### 五、方法论与关键技术细节
数据为强迫阻尼弹簧振荡器（质量0.5，刚度2.0，阻尼0.1，固有频率2 rad/s，周期≈3.14），采样步长0.4，动作空间三值（向上力、无力、向下力）。先验为各向同性的单位高斯分布。损失函数为变分ELBO，包含重建项和KL散度项（β_KL=1）。超参数：学习率5e-4至5e-5余弦衰减，优化器Adam。谱归一化约束G矩阵的谱范数≤1，保证每步能量注入有界。勒普弗拉格积分器有条件稳定性（dt < 2/ω），推理时子步可降低全局截断误差但增加计算量。局限性：实验仅在单一弹簧振荡器上验证，视觉指标无法直接测量物理状态误差；谱归一化可能限制可学习的力范围；子步策略依赖推理时计算资源。
