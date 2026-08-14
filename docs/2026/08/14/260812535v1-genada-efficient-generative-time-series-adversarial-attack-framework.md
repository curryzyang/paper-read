# GENADA: efficient generative time series adversarial attack framework

- 区域：精读区
- 排名：7
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Michael Baronov, Denis Vorobev, Margarita Rusanova, Petr Sokerin, Alexey Zaytsev
- 机构：HSE University, Moscow Independent Research Institute of Artificial Intelligence
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12535v1) · [PDF](https://arxiv.org/pdf/2608.12535v1)

## TLDR
GENADA trains a generative model to produce adversarial perturbations for time series in a single forward pass, achieving attack quality comparable to strong gradient-based baselines like iFGSM while significantly reducing inference-time computational cost.

## Abstract
Deep learning models are widely used for time series analysis in domains such as healthcare, finance, energy systems, and environmental monitoring. However, these models remain vulnerable to adversarial attacks, where small input perturbations cause severe degradation in predictive performance. Commonly used gradient-based attacks, iterative first-order methods, are computationally burdensome, as they repeatedly backpropagate through the victim model to compute input gradients during a number of iterative refinement steps. We propose a GENerative ADversarial Attack (GENADA) that learns a generative model to produce deceptive perturbations directly in a single forward pass and a procedure to train it. Variants include single-step and iterative generative attack schemes. The validation considers attacks on several neural models and datasets in the time-series domain, a controlled, low-dimensional setting. Empirically, GENADA achieves comparable attack quality to strong baselines while requiring less time to generate perturbations during inference.


## 精读解读（中文）
### 一、研究动机
现有时间序列分类深度模型易受对抗攻击，但常见基于梯度的迭代攻击（如FGSM/iFGSM）需要在推理时反复对受害模型反向传播计算输入梯度，计算开销大。本文提出生成式对抗攻击框架GENADA，学习一个生成器直接输出扰动，在保持攻击效果的同时显著降低推理时间。

### 二、技术方案（Method）
GENADA使用冻结的目标分类器f和可训练生成器G，G以原始时间序列X为输入，输出同维扰动。训练时扰动构造为δ=ε·tanh(G(X))，最小化带反转标签的对抗样本分类损失L_cls(f(X+ε·tanh(G(X))), ¬y)来更新G参数；推理时用sign(·)替换tanh(·)，使扰动ℓ∞范数精确等于ε。框架包含单步生成攻击和迭代生成攻击：迭代版本将扰动分摊为T步逐步施加，训练时仅对最后k步反传、前T-k步冻结，并随训练轮次逐步增大k至T，以节省内存并加速收敛。

### 三、结果（Result）
在PowerCons、GunPoint、Strawberry等时间序列数据集上，针对卷积、循环和Transformer等神经分类器，GENADA与强基线FGSM/iFGSM的攻击质量相当，但生成扰动所需推理时间显著更短；迭代式GENADA可进一步提升攻击效果，同时保持较低的计算开销。

### 四、结论（Conclusion）
GENADA证明生成式对抗攻击可用于时间序列分类任务：训练后只需单次前向即可生成满足ℓ∞约束的扰动，避免了推理时对受害模型的迭代反向传播。它在攻击效果与计算效率之间取得有利权衡，为时间序列对抗攻击提供了高效可扩展方案。

### 五、方法论与关键技术细节
关键细节包括：采用ℓ∞扰动约束，训练时用tanh保证扰动有界且可微，推理时用sign将扰动幅度精确缩放至ε；将分类标签取反并最小化冻结目标模型在对抗样本上的损失；迭代式GENADA将扰动分解为T步，训练只对最后k步反传并逐步增加可训练步数，降低显存占用和训练时间；相比iFGSM需T次反向传播，GENADA推理只需一次前向传播，复杂度显著降低。局限性在于验证场景限于低维单变量时间序列和少数数据集，生成器训练阶段仍需要访问目标模型梯度，且攻击质量与最强基线持平而非全面超越，多变量和大规模场景的泛化性尚未验证。
