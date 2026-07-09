# Post-Generation Curation of Synthetic Images via Homogeneous-Heterogeneous Splitting

- 区域：精读区
- 排名：7
- 匹配度：1.9/10
- 来源：arxiv
- 作者：Disheng Liu, Tuo Liang, Chaoda Song, Yu Yin
- 机构：Case Western Reserve University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02637v1) · [PDF](https://arxiv.org/pdf/2607.02637v1)

## TLDR
This paper introduces a generator-agnostic post-generation curation method that splits real data into homogeneous (canonical) and heterogeneous (diverse) subsets to select synthetic images via a fidelity-diversity criterion, consistently improving downstream task performance and matching real-data results with up to 40% fewer samples.

## Abstract
Recent generative models can produce high-quality synthetic images, offering scalable training training data for data-hungry models. Existing approaches to exploiting this potential typically involve 1) training or fine-tuning generators, or 2) using lightweight post-hoc adaptation like prompt engineering or inference-time guidance, making them generator-specific and expertise-intensive. We study a complementary question: given a fixed pool of generated images, can downstream utility be improved purely by selecting an informative subset? The answer is yes. We show that effective selection must counter a structural bias of modern generators: they tend to over-produce canonical modes of each class while underrepresenting intra-class variation. Building on this insight, we split each real class into a canonical Homogeneous (HO) subset and a non-redundant Heterogeneous (HE) subset, then score synthetic images by a fidelity-diversity criterion that rewards semantic alignment while penalizing canonical redundancy. The method is generator-agnostic and requires no retraining. Across multiple benchmarks, it consistently outperforms state-of-the-art data selection baselines and matches the real-data performance with up to 40% fewer synthetic samples. The same criterion remains effective when applied on top of stronger task-tuned generators, with gains on both classification and segmentation tasks. Post-generation selection is therefore not a substitute for better generators, but a complementary mechanism for improving the utility of synthetic data.


## 精读解读（中文）
### 一、研究动机
现有生成模型虽能产生高质量合成图像，但利用这些数据的方法（如训练/微调生成器或轻量级后处理）往往依赖特定生成器且需要专业知识。本文研究一个互补问题：给定固定合成图像池，能否仅通过选择信息子集来提升下游效用？作者发现有效选择必须克服现代生成器的结构性偏见：它们倾向于过度产生各类别的典型模式（同质样本），而低估类内变化（异质样本）。

### 二、技术方案（Method）
方法分为两步。第一步，将真实数据分为同质子集（HO）和异质子集（HE）：对每个类内图像，用预训练编码器（MoCo v3）提取ℓ2归一化特征，基于余弦距离构建有向1-最近邻图，入度大于0的节点为HO（局部代表），入度为0的节点为HE（非冗余变化）。第二步，提出分区选择策略：对合成池中每个样本，分别计算其与HO和HE的评分，评分结合保真度（奖励与真实语义对齐）和多样性（惩罚与HO的典型模式冗余）。具体地，对每个分区p，计算S^p = fidelity + λ·diversity，其中fidelity为与p中最近邻的相似度，diversity为与HE中最近邻的相似度（或与HO偏离度）。按S^p排序，对每个分区选择前k/2个样本，合并得最终选池。该方法不依赖生成器结构，无需重新训练生成器。

### 三、结果（Result）
在CIFAR-10、ImageNet等基准上，该方法持续优于现有数据选择基线（如直接使用全部合成数据、仅基于保真度或多样性的选择），以最多40%的合成样本即可匹配真实数据性能。在更强的任务调优生成器（如微调扩散模型）后应用，该方法在分类和分割任务上均有额外增益，表明其作为后处理机制的互补有效性。

### 四、结论（Conclusion）
后生成选择并非替代更优生成器的手段，而是提升合成数据效用的互补机制。通过将真实数据分为HO和HE，并设计联合保真度-多样性的分区选择策略，能有效克服生成器过度产生典型模式的偏见，在减少数据冗余的同时保持高语义质量。

### 五、方法论与关键技术细节
数据：使用CIFAR-10、ImageNet等，合成池由生成器（如扩散模型）产生，分类器含ResNet、ViT等。建模：1-NN图划分依赖唯一最近邻假设（Proposition 1保证HO是最小近邻覆盖集），特征来自MoCo v3预训练编码器，所有特征ℓ2归一化，余弦距离。评分中λ为超参数（默认平衡保真度和多样性）。复杂度：单类1-NN图划分O(n²d)，选择过程O(|D_S|·|D_R|)。局限性：依赖预训练编码器质量；1-NN划分对噪声敏感；生成器偏见可能随模型变化；当前仅考虑分类和分割，未探索更复杂任务。
