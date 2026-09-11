# GEOSTEER: Geodesic Optimization for Activation Steering in Large Language Models

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Xuan Cuong Ngo, Hao Vo, Ngan Le
- 机构：University of Arkansas
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10658v1) · [PDF](https://arxiv.org/pdf/2609.10658v1)

## TLDR
GeoSteer is a norm-preserving activation-steering method that uses adaptive multistep Riemannian optimization on the representation sphere to steer LLM behavior more stably and outperform state-of-the-art baselines on TruthfulQA, RealToxicityPrompts, and UltraFeedback.

## Abstract
Activation steering provides a lightweight way to control large language models (LLMs) by modifying their hidden activations at inference time. Among these approaches, norm-preserving steering aims to change model behavior without altering the activation norm, reducing the risk of representation collapse and degradation. However, existing norm-preserving methods are limited by predefined steering trajectories and by their reliance on one-step updates, which may fail to capture the complex structure of activation distributions. We propose GeoSteer, an optimization-based method for norm-preserving activation steering. GeoSteer formulates steering as a Riemannian optimization problem and updates activations through a sequence of small geodesic steps on the representation manifold. To avoid fixed steering directions, GeoSteer learns a nonlinear activation-space objective that distinguishes desired from undesired activations, and uses this function to adaptively guide each steering step. This multistep formulation yields smoother, more stable, and more consistent steering behavior while preserving the activation norm. Across TruthfulQA, RealToxicityPrompts, and UltraFeedback benchmarks, GeoSteer consistently improves over state-of-the-art activation steering baselines. These results suggest that norm-preserving steering can be made more effective by replacing predefined one-step edits with adaptive, geometry-aware optimization.


## 精读解读（中文）
### 一、研究动机
现有激活引导能在推理时轻量控制大模型，但加性编辑对干预尺度敏感，过强会偏离模型自然表征空间并损害生成质量。保范引导虽能避免范数改变和表征崩溃，却多依赖预定义轨迹与一步更新，难以刻画复杂激活分布并限制表达力。因此需要一种自适应、几何感知且保持范数的激活引导方法。

### 二、技术方案（Method）
GeoSteer 将保范激活引导建模为单位球面上的黎曼优化。训练阶段对标注激活归一化，学习非线性探针 s_phi(z)=w^T phi(z)+b，其中 phi 用 Polynomial Count Sketch 实现，并用二分类交叉熵区分期望与不期望激活。推理时给定激活 h，先取 z^(0)=h/||h||_2，设定总强度 T 和步数 K、步长 eta=T/K，每步计算引导损失 -log p_phi(z) 的欧氏梯度，将其投影到切空间并归一化为下降方向，再沿测地线更新 z^(t+1)=cos(eta)z^(t)+sin(eta)u^(t)，最后用 ||h||_2 z^(K) 恢复激活。

### 三、结果（Result）
在 TruthfulQA、RealToxicityPrompts 和 UltraFeedback 上，GeoSteer 在有用性、真实性和去毒等任务中一致优于当前最优激活引导基线，并保持激活范数。相比预定义一步保范旋转，它产生更平滑、稳定和一致的引导行为，且推理保持高效。论文预览未列出具体数值，但摘要与引言均报告了跨基准的一致性提升。

### 四、结论（Conclusion）
结果表明，将保范激活引导从预定义一步编辑改为自适应、几何感知的多步优化，可显著增强控制效果并降低表征退化风险。GeoSteer 提供了在激活球面上进行黎曼优化的统一视角，说明利用非线性目标与测地线轨迹能更细粒度地调节模型行为。该思路有望作为轻量对齐与行为控制的通用替代方案。

### 五、方法论与关键技术细节
关键细节包括：在 Falcon-7B、Mistral-7B-v0.3、LLaMA-3.1-8B 等开源模型上评测，基准为 TruthfulQA、RealToxicityPrompts、UltraFeedback；探针用 PCS 非线性特征和二元交叉熵训练后冻结，推理目标为最小化 -log p_phi(z)；超参为总引导强度 T 与步数 K，步长 eta=T/K，每步执行黎曼梯度投影和测地线更新以严格满足 ||z||_2=1；主要局限是依赖标注激活训练探针、探针质量与 T/K 选择影响效果，且多步迭代会带来额外推理开销，干预仅作用于选定层和 token 位置。
