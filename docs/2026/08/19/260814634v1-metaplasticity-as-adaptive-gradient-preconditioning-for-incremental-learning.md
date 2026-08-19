# Metaplasticity as adaptive gradient preconditioning for incremental learning

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Isabelle Aguilar, Zayn Andre Zainal, Omid Kavehei
- 机构：The University of Sydney
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14634v1) · [PDF](https://arxiv.org/pdf/2608.14634v1)

## TLDR
SynGAP reframes biological synaptic metaplasticity as adaptive gradient preconditioning, using an online exponential moving average of the Fisher Information Matrix to selectively attenuate gradient updates and mitigate catastrophic forgetting in task-free continual learning.

## Abstract
Biological intelligence naturally prevents catastrophic forgetting through Complementary Learning Systems (CLS) theory, a macroscopic consolidation process driven at the local level by synaptic metaplasticity: the continuous, history-dependent neuromodulation of individual synapses. While artificial neural networks struggle with the stability-plasticity dilemma in non-stationary environments, existing solutions often require task labels or incur massive memory overhead, diverging from biological reality. Re-framing this localized neuromodulation as an optimization-driven process, we introduce $\textbf{SynGAP}$: $\textbf{Syn}$aptic $\textbf{G}$eometric $\textbf{A}$daptive $\textbf{P}$reconditioning. SynGAP is a task-free continual learning framework based on adaptive gradient preconditioning. Rather than relying on explicit episodic triggers, SynGAP simulates real-time metaplasticity by maintaining an exponential moving average of the Fisher Information Matrix over a continuous data stream. During the optimization step, these dynamic metaplastic states are translated into a bounded multiplicative mask that preconditions raw gradients, selectively attenuating updates to critical historical parameters. Empirical evaluations demonstrate SynGAP's superior ability to mitigate catastrophic forgetting compared to established baselines. On the Split CIFAR-100 benchmark, SynGAP delivers a $4\times$ increase in accuracy compared to EWC++ and outperforms Experience Replay (ER) by almost $10\%$, while reducing the forgetting measure by over $10\%$ against both methods. Furthermore, on the CORe50 benchmark, SynGAP achieves about $68\%$, a $10\%$ improvement over optimizer baselines. By mathematically formalizing continuous biological metaplasticity as stable gradient-based regularization, SynGAP offers a highly robust and memory-efficient solution for adaptive intelligence at the edge.


## 精读解读（中文）
### 一、研究动机
生物智能通过突触可塑性（metaplasticity）与互补学习系统（CLS）自然避免灾难性遗忘，而人工神经网络在非平稳环境下存在稳定性-可塑性困境。现有增量学习方法要么依赖任务标签，要么产生大量记忆开销，偏离生物现实。本文旨在将生物突触元可塑性重新形式化为一种基于几何的自适应梯度预条件化过程，从而在不依赖显式任务边界和昂贵存储的前提下缓解灾难性遗忘。

### 二、技术方案（Method）
提出SynGAP（Synaptic Geometric Adaptive Preconditioning）框架。输入为连续数据流，模型在线维护Fisher信息矩阵对角线的指数移动平均（EMA）作为历史参数重要性状态F_t = α F_{t-1} + (1-α) diag(F_t(θ))。通过全局归一化与双曲正切构造有界可塑性函数g(F) = 1 - tanh(c(F + λ)) + ε，其中c = arctanh(τ)/(μ+λ)，μ为F的全局均值，λ为Tikhonov阻尼项，ε为环境塑性常数。输出有界乘性掩码Ω = g(F)，在每次优化时对原始梯度逐元素相乘：θ_{t+1} = θ_t - η(Ω ⊙ ∇θ L(θ))。该方法无需附加损失惩罚，也不依赖任务标签或大规模回放缓冲。

### 三、结果（Result）
在Split CIFAR-100基准上，SynGAP相比EWC++平均准确率提升4倍，相比Experience Replay（ER）准确率提高近10%，遗忘度量比两者均降低超过10%。在CORe50基准上，SynGAP取得约68%的平均准确率，比优化器基线提升10%。相比SGD、SGDM、Adam、Ballistic等基线，SynGAP在缓解灾难性遗忘方面优势显著，同时保持较低的遗忘和不可塑性指标。

### 四、结论（Conclusion）
SynGAP将连续的生物元可塑性形式化为稳定的基于梯度的正则化机制，通过自适应梯度预条件化平衡稳定性与可塑性，提供了一种高度鲁棒、内存高效的边缘自适应智能解决方案。该方法无需任务标签，仅依赖少量临时缓冲，且有效避免了加性损失惩罚导致的优化景观失真和参数僵化问题。

### 五、方法论与关键技术细节
关键点包括：使用在线EMA而非任务边界快照来追踪Fisher信息；利用tanh将无界FIM映射到有界区间[ε,1+ε]，数学上保证参数可塑性下限，防止网络完全冻结；c中的λ和τ（目标巩固超参数）控制掩码强度；ε为环境塑性常数；掩码直接作用于梯度而非损失函数，避免全局损失缩放问题；方法仅需一阶梯度信息，无SVD等昂贵运算；局限性包括仅使用对角Fisher近似，可能忽略参数间相关性，且超参数（α、τ、λ、ε）需根据任务调节。
