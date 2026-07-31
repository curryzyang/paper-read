# Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation

- 区域：精读区
- 排名：3
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Alexi Gladstone, Heng Ji, Yilun Du
- 机构：UIUC, Harvard
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27372v1) · [PDF](https://arxiv.org/pdf/2607.27372v1)

## TLDR
Explorative Modeling introduces a new generative modeling paradigm that factors the training loop by exploring K candidate matches between model generations and data, serving as a scalable third pretraining axis—alongside parameters and data—that improves efficiency and performance across images, video, and language while also enabling end-to-end reconstructive generative modeling.

## Abstract
The deep learning revolution, kicked off by AlexNet, taught us that end-to-end training beats decomposing a problem into hand-designed stages. Generative modeling, however, has remained the exception-despite generative models being remarkably capable, they are still not trained end-to-end. This is because, at its core, generative modeling is about handling distributions with many modes, and existing scalable approaches handle this the same way, by factoring the generation procedure, which prevents end-to-end generation. In this work, we introduce Explorative Modeling, a new paradigm that instead factors the training loop, exploring K candidate matches between model generations and data, and training on the best, so predictions commit to modes rather than blurring them. We find Explorative Models (XMs) useful in two settings. First, increasing exploration adds a third pretraining axis beyond parameters and data for existing generative models-where scaling exploration monotonically improves performance across both continuous and discrete domains (images, video, and language). Notably, gains from exploration increase with scale, climbing from 7% to 36% as data scales and from 13% to 23% as models grow, with efficiency gains more than doubling at 3x the compute. Concretely, exploration improves FLOP efficiency by 4.1x, sample efficiency by 6.2x, parameter efficiency by 47%, lifts the strongest of image-generation recipes to a near-state-of-the-art 1.43 FID on ImageNet without guidance, enables scaling how end-to-end existing models are, and unlocks scaling generalization. Second, XMs enable end-to-end reconstructive generative modeling, matching diffusion on control tasks with 16-256x fewer inference steps. Together, these results establish XMs as both a new pretraining axis for existing generative models and a standalone end-to-end generative modeling paradigm.


## 精读解读（中文）
### 一、研究动机
深度学习革命（始于AlexNet）表明端到端训练优于将问题分解为手工设计阶段，但生成建模至今仍是例外：尽管生成模型能力强大，它们仍未实现端到端训练。其根源在于生成建模的核心是处理具有众多模式的多模态分布，而现有可扩展方法（自回归、扩散、流模型）都通过分解生成过程来规避模式模糊，这导致训练与推理采样不一致，阻碍了端到端生成。

### 二、技术方案（Method）
提出Explorative Modeling（探索式建模，XM）范式，将分解对象从生成过程转为训练循环：每个训练步由模型从同一输入/潜变量生成K个候选样本，与数据目标计算K个候选匹配，选择最接近（损失最小）的匹配进行梯度更新，使预测承诺到具体模式而非平均模糊。探索完全发生在训练阶段，推理时保持与训练一致的端到端采样；K即探索量，直接决定模型可捕获的模式数。XM既可作为新的预训练轴叠加到现有生成模型（图像、视频、语言）上，也可单独构成端到端重构式生成模型（End-to-End XM）。

### 三、结果（Result）
在图像、视频和语言等连续与离散领域，增大探索K单调提升性能，且收益随规模增长：数据规模扩大时收益从7%升至36%，模型规模扩大时从13%升至23%，3倍计算量下效率收益翻倍以上。探索带来4.1倍FLOP效率、6.2倍样本效率和47%参数效率提升，并将最强图像生成配方在ImageNet上无需引导地提升至近SOTA的1.43 FID。端到端XM在行为克隆上匹配Diffusion Policy、在目标条件世界建模上匹配Diffuser，推理步数减少16-256倍（可低至单次前向传播）。

### 四、结论（Conclusion）
XM为现有生成模型确立了除参数和数据之外的第三条预训练轴，同时也是一个独立的端到端生成建模范式。因子化训练与因子化生成可互相替代：增加探索会使最优生成模型更端到端，并间接改善泛化；将探索推到极限即可实现完全端到端的生成建模，把驱动深度学习其余领域的端到端训练成功扩展到生成领域。

### 五、方法论与关键技术细节
核心概念是生成表达力（generative expressivity），即训练目标允许模型捕获的模态数；即使参数和数据无限，直接回归的表达力也仅为1，其损失最优解是所有模式的模糊均值。关键操作是以探索量K生成候选并只训练最优匹配，使每个候选可承诺不同模式，并呈现计算-泛化权衡：更多训练计算用于探索可直接改善泛化。该瓶颈随规模扩大而加剧，解释了引导（如classifier-free guidance）为何有效以及似然与样本质量相关性不佳；局限在于探索需训练时评估K个候选，带来额外训练开销。
