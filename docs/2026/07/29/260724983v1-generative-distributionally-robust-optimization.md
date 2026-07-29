# Generative Distributionally Robust Optimization

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Ziwei Zhang, Jonathan Yu-Meng Li, Zhihao Jin
- 机构：University of Ottawa, Western University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24983v1) · [PDF](https://arxiv.org/pdf/2607.24983v1)

## TLDR
Generative Distributionally Robust Optimization (GDRO) introduces a principled framework that accepts any sampleable conditional generator as the nominal model and restricts worst-case laws to a chosen generator family using a likelihood-free sampler–Sinkhorn pairing, enabling robust decision-making under model misspecification without requiring model-specific access.

## Abstract
Generative models are increasingly adopted in distributionally robust optimization (DRO), but existing approaches trade off model compatibility and adversarial structure: methods that accept arbitrary samplers do not restrict worst-case laws to a generator family, while generator-parameterized adversaries rely on model-specific access such as likelihoods, scores, or training data. We propose Generative Distributionally Robust Optimization (GDRO), a principled framework that accepts any sampleable conditional generator as the nominal model and restricts worst-case laws to a chosen conditional generator family. The key is the sampler-Sinkhorn pairing: samplers represent the conditional laws exactly, while Sinkhorn divergence compares their induced distributions without likelihood access and can be estimated from samples alone. The resulting population problem admits a direct finite-sample approximation and differentiable primal-dual implementation at the active decision context. For Lipschitz losses, the population Sinkhorn radius bounds downstream degradation. Across explicit and implicit generators, our method reduces rare-context inventory regret by 60% and SocialGAN navigation collisions by 50% relative to nominal decisions.


## 精读解读（中文）
### 一、研究动机
现有分布鲁棒优化方法在模型兼容性和对抗结构之间存在权衡：接受任意采样器的方法不限制最坏情况分布至生成器家族，而生成器参数化的对手则依赖似然、分数或训练数据等模型特定信息。为此，本文提出生成式分布鲁棒优化（GDRO），该框架接受任意可采样的条件生成器作为名义模型，并将最坏情况分布限制在选定的条件生成器家族内。

### 二、技术方案（Method）
GDRO的核心是采样器-辛克霍恩配对：采样器精确表示条件分布，辛克霍恩散度通过样本即可比较诱导分布，无需似然访问。给定预训练名义条件生成器P_φ̂(·|x)和对抗生成器家族{Q_ψ(·|x)}，优化问题为inf_w sup_{ψ:S_ε(Q_ψ^x,P_0^x)≤ρ} E_{Y∼Q_ψ^x}[f(w,Y)]。通过条件采样器的推前形式构造经验分布，利用熵正则化最优传输的辛克霍恩散度定义约束，最终导出可微的原对偶有限样本近似。

### 三、结果（Result）
对于Lipschitz损失，人口辛克霍恩半径有界目标下降；在显式与隐式生成器实验中，GDRO将稀有情境库存遗憾降低60%，SocialGAN导航碰撞减少50%，均优于名义决策。该结果在多个任务上验证了生成器忠实对抗的有效性。

### 四、结论（Conclusion）
本文提出生成式分布鲁棒优化，是首个将最坏情况分布限制在选定条件生成器家族内并通过样本辛克霍恩散度认证的上下文局部DRO框架。理论与实验表明，该框架兼容任意采样器，并提供可证明的下游性能保障，为生成模型鲁棒优化提供了新范式。

### 五、方法论与关键技术细节
关键点包括：辛克霍恩散度采用平方欧氏成本且可仅从样本估计；人口问题的有限样本近似通过固定对抗潜在变量实现可微优化；理论保证依赖于输出有界支撑假设与Lipschitz损失；超参数包括辛克霍恩正则化系数ε和模糊半径ρ，需交叉验证；计算复杂度主要来自辛克霍恩矩阵缩放，样本量增加时空成本上升；局限性在于框架依赖Sinkhorn散度与Wasserstein的近似质量，且对抗生成器家族需包含名义模型附近分布。
