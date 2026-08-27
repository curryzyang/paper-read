# CAT-GS: Balanced Multimodal Learning via Calibrated Gating and Fusion Surgery

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Mahir Shahriar Tamim, Sharjil Khan, Md. Samiul Alim, Tanvir Ahmed Khan, Shafin Rahman, Nabeel Mohammed
- 机构：North South University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24947v1) · [PDF](https://arxiv.org/pdf/2608.24947v1)

## TLDR
CAT-GS is a backpropagation-stage optimization controller that stabilizes multimodal training by calibrating teacher-derived reliability for thresholded gating, renormalizing gradient budgets, and applying fusion-only PCGrad to jointly mitigate modality imbalance, gating instability, and fusion interference.

## Abstract
End-to-end training of multimodal neural networks often exhibits unstable neural dynamics characterized by three coupled failure modes that degrade learning: (i) modality imbalance, where one branch dominates gradient-based optimization; (ii) unstable gating, where noisy confidence cues induce erratic modality selection; and (iii) fusion interference, where modality-specific gradients conflict at the shared fusion layer. We propose CAT-GS (Calibrated, Adaptive, Thresholded Gating with Fusion Surgery), a neural dynamics-based optimization controller for intelligent computing applications. CAT-GS operates during backpropagation without modifying model architectures, fusion modules, or task losses. Through calibration of teacher-derived reliability via temperature scaling and EMA smoothing, CAT-GS stabilizes neural dynamics using a margin-thresholded policy to switch between warm-up dropout, weak-modality prioritization, and weak-biased blending, stabilizes gradient magnitudes under aggressive gating via capped gradient-budget renormalization, and applies fusion-only PCGrad to reduce destructive cross-modal interference at the primary shared bottleneck. We evaluate CAT-GS on audio--visual multimodal pattern recognition benchmarks (CREMA-D, AV-MNIST, and VGGSound), a tri-modal setting (UR-FUNNY), controlled synthetic data (CG-MNIST), and additional cross-domain benchmarks (AVE and CMU-MOSI). CAT-GS improves or matches fused multimodal accuracy against strong imbalance-aware baselines (including OGM-GE, G$^2$D, and UMT) across settings, and yields smoother gating behavior with fewer conflicting fusion gradients.


## 精读解读（中文）
### 一、研究动机
端到端多模态网络训练常出现三类耦合的动力学失稳：模态不平衡导致单分支主导梯度优化、基于噪声置信度的门控产生模态选择的抖动、共享融合层中模态专属梯度相互冲突。现有方法通常只单独处理其中一类问题，缺乏对这三类失效模式的统一校正机制。

### 二、技术方案（Method）
CAT-GS是一个仅作用于反向传播阶段、不修改模型架构/融合模块/任务损失的优化控制器。它利用冻结的单模态教师网络对每个模态计算真实标签上的Softmax平均置信度作为可靠性信号，支持可选温度缩放和EMA平滑来稳定该信号；随后通过边际阈值策略在warm-up dropout、弱模态优先、弱偏置混合等门控模式间切换；再通过带EMA目标幅度和硬上限的梯度预算重归一化防止激进门控造成梯度饥饿；最后仅在共享融合瓶颈处应用PCGrad梯度手术，消除跨模态负向干扰。整体流程插入在loss.backward()与optimizer.step()之间，训练目标为交叉熵损失、教师logits蒸馏损失和特征MSE损失的加权组合。

### 三、结果（Result）
在CREMA-D、AV-MNIST、VGGSound、UR-FUNNY、CG-MNIST以及AVE和CMU-MOSI等跨域基准上，CAT-GS相比OGM-GE、G2D、UMT等强不平衡感知基线，在融合多模态精度上取得提升或持平，并表现出更平滑的门控行为和更少的融合梯度冲突。

### 四、结论（Conclusion）
CAT-GS通过在优化阶段统一处理模态不平衡、门控不稳定和融合干扰三类耦合问题，能够在不改动模型结构的前提下提升多模态训练的稳定性与融合精度，是一种即插即用且架构无关的多模态训练优化方案。

### 五、方法论与关键技术细节
关键细节包括：教师网络保持冻结且直接接收原始模态输入，不依赖学生特征；可靠性信号采用batch级均值而非逐样本信号，配合EMA平滑减少门控抖动；温度缩放默认设为1，在主要实验中不是必要性能驱动因素；梯度预算机制通过EMA目标幅度和硬上限防止被抑制模态长期得不到有效更新；PCGrad仅作用于融合层，既降低全局投影的计算成本，又保留单模态编码器的动态。局限性方面，方法依赖可用的单模态教师提供可靠性信号，且部分门控阈值、EMA系数和蒸馏权重需按数据集设置。
