# Fractional Optimizers Meet Fractal Activation Functions: An Empirical Study of Multi-Scale Optimization in Neural Network

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Sebastian Raubitzek, Georg Goldenits, Sebastian Schrittwieser, Philip König, Kevin Mallinger
- 机构：University of Vienna, SBA Research gGmbH
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14636v1) · [PDF](https://arxiv.org/pdf/2608.14636v1)

## TLDR
This empirical study systematically evaluates fractional optimizers combined with fractal activation functions in neural networks, finding that the two approaches have useful but selective pairings—regularization-style fractional scaling works well with certain fractal activations, while adaptive memory-based fractional optimizers show promise as a controlled improvement over plain memory methods.

## Abstract
Fractional optimization methods and fractal activation functions are two independent directions for improving neural network training. Fractional optimizers extend first-order optimization through fractional derivatives and memory effects, whereas fractal activations introduce multi-scale nonlinear representations based on self-similar Weierstrass- and Blancmange-type functions. Here, we investigate their interaction within a unified experimental framework. We evaluate fractional optimizer families on Ackley and Himmelblau benchmark surfaces, in standard form and with additive Weierstrass-type perturbations, and then in feed-forward neural networks with conventional and fractal activations on ten classification datasets. The comparison includes standard methods, regularization-style optimizers, explicit and adaptive memory-based fractional optimizers, and other representative literature methods. Overall, fractional optimization and fractal activations show useful but selective pairings. Regularization-style fractional scaling performs well with selected fractal activations in network training, while Grünwald--Letnikov memory is most relevant on perturbed surfaces. Adaptive memory improves plain memory substitution in several cases, supporting controlled fractional memory as a promising direction rather than a universal replacement.


## 精读解读（中文）
### 一、研究动机
神经网络训练中，分数阶优化器与分形激活函数分别从优化和表示两个方向引入多尺度机制，但二者尚未在统一框架下系统考察。本文试图验证：当分形激活函数通过自相似的Weierstrass/Blancmange类级数向表示和梯度注入多尺度粗糙结构时，以分数阶导数或记忆效应为核心的优化器能否成为其天然配套，从而提升训练效果。

### 二、技术方案（Method）
方法采用两阶段统一实验：第一阶段在Ackley和Himmelblau基准曲面（标准型及叠加截断Weierstrass型扰动）上评估优化器对已知极小值的可达性与鲁棒性；第二阶段在十个公共分类数据集上用前馈神经网络比较四种分形激活（Weierstrass/Blancmange型）与常规激活（ReLU/tanh等）。输入为二维基准函数或多分类表格特征，模型为多层前馈网络，关键模块是分数阶更新规则：显式Grünwald–Letnikov记忆、Herrera式Caputo缩放、以及新提出的自适应记忆混合系数。共比较5组21种优化器，包括经典基线、正则化式分数阶缩放、记忆型分数阶、自适应记忆分数阶（AdaptiveMemoryFSGD/FRMSprop/FAdam/FAdadelta）和文献代表方法。训练流程为前向传播→反向传播得到梯度→按优化器更新参数；自适应记忆族固定分数阶，通过稳定性和损失控制的自适应系数在范数匹配的分数阶记忆梯度与普通梯度间加权，并在信任系数边界处精确退化为经典优化器。

### 三、结果（Result）
实验显示分数阶优化与分形激活存在有用但选择性的配对：正则化式分数阶缩放与选定的分形激活在网络训练中表现良好，而Grünwald–Letnikov记忆在受分形扰动的曲面上最有效；自适应记忆在多种情况下优于朴素记忆替换，但并未全面超越其他方法，没有一种组合在所有任务上普遍最优。

### 四、结论（Conclusion）
分数阶优化器和分形激活函数是同一多尺度数学机制的两端，二者结合有潜力，但不应被当作通用替代方案。受控的分数阶记忆方向值得继续探索，尤其应将自适应记忆视为对固定分数阶方法的补充而非替换。

### 五、方法论与关键技术细节
关键细节包括：基准曲面为Ackley和Himmelblau，扰动采用截断Weierstrass型加性项以产生受控分形粗糙度；分类实验沿用前序工作的十个OpenML数据集、前馈网络及最强的四类分形激活函数；优化器比较覆盖5组21种，显式记忆型基于Grünwald–Letnikov核，与Weierstrass型函数分数阶微分的离散形式一致；自适应记忆族固定分数阶并自适应有界信任系数，边界处精确还原经典优化器。先验上利用了分数阶可导性与分形粗糙度指数的一致性（Zähle–Ziezold结果）。主要局限是组合收益具有选择性，部分情况下无提升，且分数阶优化器的噪声敏感性和额外超参成本仍是实际应用的主要约束。
