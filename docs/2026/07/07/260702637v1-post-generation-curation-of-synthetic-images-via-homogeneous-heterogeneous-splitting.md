# Post-Generation Curation of Synthetic Images via Homogeneous-Heterogeneous Splitting

- 区域：精读区
- 排名：7
- 匹配度：1.9/10
- 来源：arxiv
- 作者：Disheng Liu, Tuo Liang, Chaoda Song, Yu Yin
- 机构：Case Western Reserve University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02637v1) · [PDF](https://arxiv.org/pdf/2607.02637v1)

## TLDR
The paper introduces a generator-agnostic post-generation curation method that splits real data into homogeneous (canonical) and heterogeneous (diverse) subsets to score synthetic images by a fidelity-diversity criterion, consistently outperforming baselines and matching real-data performance with fewer synthetic samples.

## Abstract
Recent generative models can produce high-quality synthetic images, offering scalable training training data for data-hungry models. Existing approaches to exploiting this potential typically involve 1) training or fine-tuning generators, or 2) using lightweight post-hoc adaptation like prompt engineering or inference-time guidance, making them generator-specific and expertise-intensive. We study a complementary question: given a fixed pool of generated images, can downstream utility be improved purely by selecting an informative subset? The answer is yes. We show that effective selection must counter a structural bias of modern generators: they tend to over-produce canonical modes of each class while underrepresenting intra-class variation. Building on this insight, we split each real class into a canonical Homogeneous (HO) subset and a non-redundant Heterogeneous (HE) subset, then score synthetic images by a fidelity-diversity criterion that rewards semantic alignment while penalizing canonical redundancy. The method is generator-agnostic and requires no retraining. Across multiple benchmarks, it consistently outperforms state-of-the-art data selection baselines and matches the real-data performance with up to 40% fewer synthetic samples. The same criterion remains effective when applied on top of stronger task-tuned generators, with gains on both classification and segmentation tasks. Post-generation selection is therefore not a substitute for better generators, but a complementary mechanism for improving the utility of synthetic data.

## 精读解读（中文）

### 一、研究动机
现有生成模型能产生高质量合成图像，但利用这些数据的方法往往需要训练或微调生成器，或使用提示工程等轻量级后处理，这些方法都与生成器特定且依赖专业知识。本研究探索一个互补问题：给定固定生成图像池，能否仅通过选择信息性子集提升下游任务效能？答案是肯定的，且有效选择必须克服现代生成器的结构偏差——它们倾向于过度生成每类的规范模式而低估类内变化。

### 二、技术方案（Method）
首先，基于1-最近邻图将每类真实数据划分为同质（HO）子集（入度>0的节点，代表规范模式）和异质（HE）子集（入度为0的节点，代表非冗余变化）。然后，为每个合成图像计算保真度-多样性得分：保真度度量与对应真实子集的语义对齐程度，多样性则通过偏离HO的规范冗余模式来鼓励。采用分区选择策略，分别从HO和HE参考分区中选取得分高的合成样本，合并得到最终选择集。方法无需访问生成器内部或重新训练。

### 三、结果（Result）
在CIFAR-10、ImageNet等多个基准上，该方法一致优于现有数据选择基线，以最多40%的合成样本即可匹配使用真实数据的性能。在分类和分割任务上均有增益，且可作为更强任务调优生成器的后处理插件进一步提升效用。

### 四、结论（Conclusion）
后生成选择并非更好生成器的替代品，而是一种提高合成数据效用的补充机制。通过简单、生成器无关的数据选择，能有效弥补生成器过度生产规范模式的偏差，提升下游模型性能。

### 五、方法论与关键技术细节
划分基于每类内1-NN图，复杂度O(n^2d)（n为每类样本数，d为特征维数）。使用预训练MoCo v3提取l2归一化特征，距离度量使用余弦距离。选择得分综合了保真度（接近对应HO或HE实例）和多样性（偏离HO冗余模式）。方法无需微调生成器，但需要真实参考集。局限性包括依赖预训练编码器质量，以及无法处理生成池中无对应分区模式的情况。

