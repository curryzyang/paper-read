# Moment-Guided Optimizers for Noisy Deep Learning: MGO-SC as a Simple Consistency Gate for Adam-Style Updates

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Alicem Koyun
- 机构：Westcliff University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37712v1) · [PDF](https://arxiv.org/pdf/2610.37712v1)

## TLDR
MGO-SC adds a mean-preserving sign-consistency gate to Adam-style updates—down-weighting coordinates with unstable gradient signs while reallocating trust to preserve overall step magnitude—and consistently improves over AdamW on CIFAR-10/ResNet-18 under clean and label-noise conditions.

## Abstract
Adaptive optimizers are widely used in deep learning, yet their behavior can degrade under heavy stochasticity and label noise where the sign and magnitude of gradients can be unstable. We study MGO-SC (Moment-Guided Optimizer with Sign-Consistency), a lightweight modification of Adam-style methods that derives a coordinate-wise consistency gate from the magnitude of a sign exponential moving average (EMA): coordinates whose gradient sign is stable are trusted, while coordinates whose sign fluctuates are down-weighted. We show that the naive form of this gate, which can only shrink updates, loses effective step size and underperforms when the learning rate is matched to the baseline. We therefore introduce a mean-preserving variant that reallocates trust across coordinates without changing the net per-tensor step magnitude. On CIFAR-10 with ResNet-18, under a matched learning rate and decoupled weight decay, mean-preserving MGO-SC consistently improves over its AdamW baseline across clean, symmetric, and asymmetric label noise (e.g., +1.4 points at 40% symmetric noise; paired bootstrap 95% CI excluding zero; Wilcoxon p<0.01), while adding no second-order information or per-sample filtering. We report matched-seed effect sizes, nonparametric bootstrap confidence intervals, and paired significance tests, and we release code and raw logs.


## 精读解读（中文）
### 一、研究动机
自适应优化器在深度学习中广泛使用，但在强随机性和标签噪声下，梯度符号与幅度不稳定，Adam 类方法的有效步长可能被不可靠方向干扰。本文关注一个最小化问题：能否仅在 Adam 类优化器内部加入机制，在梯度方向不可靠时衰减更新，而不引入新损失、样本筛选或多网络过滤流程。

### 二、技术方案（Method）
输入为每步随机梯度 g_t，在 Adam/AdamW 的 m_t、v_t 与偏置校正基础上额外维护符号 EMA s_t=β_s s_{t-1}+(1-β_s)sign(g_t)，并用 r_t=max(|ŝ_t|^γ,r_min) 作为逐坐标可靠性；主方案采用 mean-preserving 门控 s_gate=r_t/mean(r_t)，其中均值按参数张量坐标计算，再执行 θ←θ−α s_gate⊙m̂/(√v̂+ε) 并配合解耦权重衰减。该门控只增加一个符号 EMA 状态和逐元素运算，不需要额外前向/反向、二阶信息或逐样本过滤；γ=0 时退化为基线，shrink 门控 min(r_t,1) 仅缩小步长，作为对照与消融。

### 三、结果（Result）
在 CIFAR-10/ResNet-18、匹配学习率 3e-4 与解耦权重衰减下，mean-preserving MGO-SC 在干净、对称和非对称标签噪声中相对 AdamW 一致提升；40% 对称噪声约提升 1.4 个百分点，配对 bootstrap 95% CI 不含 0，Wilcoxon p<0.01。相反，朴素 shrink 门控在匹配学习率时会损失有效步长并低于 AdamW；二值瞬时一致性变体也类似 shrink，被作为消融报告。

### 四、结论（Conclusion）
结果表明门控如何应用是关键：保留每张量平均步长、在坐标间重新分配信任的 mean-preserving 形式才能稳定获益；MGO-SC 是轻量、可解释的 Adam 类优化器附加机制，可与稳健损失、过滤方法或优化器 wrapper 组合，而非替代噪声标签学习专用方法。

### 五、方法论与关键技术细节
实验采用 CIFAR-10、ResNet-18，随机裁剪 padding 4、水平翻转和逐通道归一化，45k/5k 训练验证划分，50 epochs、batch size 128，Adam 族统一学习率 3e-4、SGD 使用 0.1，每个随机种子固定相同噪声标签并以最高验证精度选择 checkpoint 后报告 test@best-val；主结果使用 mean-preserving 门控和解耦权重衰减，β_s、γ、r_min 为需调节超参，γ=0 退化为基线。方法不引入新损失或显式先验，只增加一个符号 EMA 状态和逐元素门控计算，内存与计算开销很小，并可与其他优化器改进兼容；局限是验证仅限 CIFAR-10/ResNet-18 和短会论文规模，增益较小，缺少完整理论保证与更广数据集、架构和噪声类型验证。
