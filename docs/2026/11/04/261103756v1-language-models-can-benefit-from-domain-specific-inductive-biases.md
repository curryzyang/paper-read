# Language Models Can Benefit from Domain-Specific Inductive Biases

- 区域：精读区
- 排名：5
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Damien Teney, Liangze Jiang, Zachary Shinnick, Hemanth Saratchandran, Simon Lucey
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03756v1) · [PDF](https://arxiv.org/pdf/2611.03756v1)

## TLDR
TLDR: Tuning transformer nonlinearities as learned splines for specific pretraining domains improves training efficiency and generalization, but these domain-specific inductive biases often transfer poorly across domains, suggesting that domain-tailored learning mechanisms could outperform a single general-purpose architecture while still supporting general-purpose model training.

## Abstract
Language models are typically trained with a single choice of architecture on diverse domains and data sources. Modern transformers have been extensively refined for such general-purpose learning, but are they equally effective across different subsets of the pretraining data? We investigate this question by training small language models from scratch on representative subsets of pretraining data such as web text, code, and mathematics. We introduce variants of transformers in which standard activation functions are replaced with learned splines tuned on specific datasets, providing a simple way to modify their inductive biases. Using a mix-and-match of architectures and datasets, we evaluate cross-domain transfer, i.e. how well does an architecture tuned for one domain perform on data from another? We find that the tuned transformer variants improve training efficiency or generalization on all seven of our tested datasets, but the gains are often domain-specific. For example, architectures tuned on a natural language dataset such as FineWeb perform well on TinyStories, whereas those tuned on mathematics perform poorly on natural language. We identify several mechanisms underlying these improvements, including wider loss basins and more abundant "lottery tickets". Our results show that different subsets of pretraining data can benefit from different learning mechanisms, highlighting a limitation of the prevailing trend towards a small set of general-purpose architectures and optimizers. This points to an opportunity to improve data efficiency by developing domain-specific learning strategies that retain the ability to train general-purpose models.


## 精读解读（中文）
### 一、研究动机
当前语言模型通常以单一架构和优化器在多样预训练数据上训练，但不同数据子集是否同等受益于同一归纳偏置尚不清楚。受无免费午餐定理和激活函数强烈决定神经网络归纳偏置的启发，作者追问通用Transformer是否对每个数据域最优，以及域特定学习机制能否提升数据效率与泛化。

### 二、技术方案（Method）
作者从零训练40–120M参数的小语言模型，在FineWeb、Enwik8、TinyStories、Shakespeare、CodeSearchNet-Java/Python和DeepMind-Math等七个子集上做架构与数据的交叉组合评估。核心方案是把标准GeLU和softmax非线性替换为可学习线性样条，在源域通过warm-up预训练这些样条，再冻结并将少量参数迁移到目标域训练模型，以考察跨域迁移。实现上移除held-out优化、加入多模型错峰启动并调整注意力层非线性位置，使用NanoGPT speedrun记录模型作强基线，并在固定token预算下比较验证损失或准确率。

### 三、结果（Result）
调优后的Transformer变体在全部七个数据集上提升训练效率或泛化，但收益往往具有域特异性：在FineWeb等自然语言数据上调优的架构能较好迁移到TinyStories，而在数学数据上调优的架构迁移到自然语言表现较差。机制分析显示专用架构使梯度下降更容易找到有效解，收敛更快且对学习率衰减依赖更低，提示更宽的损失盆地，并在初始化时包含更多与目标任务相关的电路，符合彩票假设。

### 四、结论（Conclusion）
不同预训练数据子集可以受益于不同学习机制，这揭示了当前偏向少量通用架构和优化器的趋势存在局限。未来应发展保留通用模型训练能力的域特定学习策略，并探索多种专用学习机制之间的交互，以提升数据效率和系统泛化；但结论基于小模型和困惑度评价，向大模型及下游任务推广仍需验证。

### 五、方法论与关键技术细节
关键细节包括七个代表性子集、40–120M参数小模型、超过6000次训练、固定token预算以及验证损失或准确率评估；线性样条提供无偏的R→R参数化，相比小MLP避免平滑性和单调性等先验，每条样条约64个值，且跨域迁移只涉及极少量冻结参数。方法改进包括去掉held-out优化、采用错峰启动和重定位注意力层非线性；局限是模型规模较小、主要评估困惑度而非下游性能，机制解释基于损失盆地和彩票假设。
