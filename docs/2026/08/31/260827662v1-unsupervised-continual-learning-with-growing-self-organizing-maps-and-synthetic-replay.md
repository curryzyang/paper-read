# Unsupervised Continual Learning with Growing Self-Organizing Maps and Synthetic Replay

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Pujan Thapa, Alexander Ororbia, Travis Desell
- 机构：Rochester Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27662v1) · [PDF](https://arxiv.org/pdf/2608.27662v1)

## TLDR
A fully unsupervised, task-free continual learning framework using growing self-organizing maps with surprisal-driven expansion and exemplar-free generative replay from per-unit distributional statistics achieves competitive performance with supervised memory-based methods on class-incremental benchmarks.

## Abstract
This work presents a generative continual learning framework based on growing self-organizing maps (GSOMs) that are augmented with learned distributional statistics as well as encoder-decoder models for class-incremental learning. The proposed approach enables exemplar-free replay using distributional statistical memory, which eliminates the need to store raw data. Each GSOM unit maintains its own mean, variance, and covariance estimates, which are subsequently used to generate synthetic samples for replay; in encoder-decoder configurations, these samples are then decoded back into the input space (via ancestral sampling) for subsequent training. Our method is fully unsupervised, as it does not rely on explicit task boundaries or class labels during training. Results across multiple benchmarks show that the proposed approach achieves performance competitive even with supervised state-of-the-art memory-based methods while consistently outperforming memory-free approaches. In several settings, our framework matches or exceeds existing baselines, particularly in challenging single-class incremental scenarios. We also provide baseline results for single-class incremental TinyImageNet and MiniImageNet, offering a useful reference for future work. This work highlights the effectiveness of an unsupervised, adaptive, topology-driven neural form of statistical replay as a scalable, flexible approach to continual learning.


## 精读解读（中文）
### 一、研究动机
现有持续学习方法大多依赖任务边界、类标签或原始样本存储，难以适应真实世界中无明确边界、无标签且隐私受限的数据流。尽管基于记忆回放的方法有效，但记忆增长和隐私问题限制了长期可扩展性，而无记忆方法又难以稳定保持旧知识。本文旨在提出一种完全无监督、无需存储原始数据的类增量持续学习框架，利用生长自组织映射（GSOM）的拓扑适应性与分布统计生成合成回放样本，以缓解灾难性遗忘。

### 二、技术方案（Method）
提出基于生长自组织映射（GSOM）的生成式持续学习框架。每个GSOM单元维护其分配样本的运行均值、方差和协方差统计量，作为分布记忆；训练时，新批次样本与从各BMU分布中采样并解码的合成回放样本合并，共同更新模型。GSOM采用基于高斯似然的归一化马氏距离（surprisal）驱动生长：当样本的surprisal超过自适应阈值（基于近期历史百分位，冷启动为1.7），且满足最小命中数、冷却时间、量化误差阈值及线性衰减生长概率等约束时，在BMU的4邻域局部插入新单元，初始化为输入数据与周围单元权重。整个流程无监督，不使用类标签或任务边界，标签仅用于事后评估。对于高维图像，GSOM作用于VAE或预训练编码器（如CLIP）提取的潜空间，合成样本经解码器回到输入空间。

### 三、结果（Result）
在MNIST、CIFAR-10/100、TinyImageNet和MiniImageNet多个基准上的实验表明，所提方法在无记忆方法中一致优于基线，并且与有监督的基于记忆的SOTA方法相比具有竞争力。在具有挑战性的单类增量场景中，框架在若干设置下匹配或超过现有基线。此外提供了TinyImageNet和MiniImageNet单类增量任务的基线结果，作为未来参考。

### 四、结论（Conclusion）
本文展示了无监督、自适应、拓扑驱动的神经统计回放作为持续学习方案的有效性。通过GSOM的局部化表示与分布统计生成合成样本，无需存储原始数据即可缓解遗忘，同时保持了可扩展性和灵活性。该方法在任务无关的类增量学习场景中，提供了一种有竞争力的无监督替代方案，并在复杂数据集上验证了其潜力。

### 五、方法论与关键技术细节
关键细节包括：每个GSOM单元仅更新BMU自身的分布统计，邻域单元只做权重更新以保证统计一致性；统计量使用指数移动平均并应用类似Adam的偏差校正；surprisal阈值采用近期1000个样本的第92百分位数，冷启动值为1.7；生长条件还要求单元命中数至少为h_min、距上次生长超过t_cool、量化误差超过阈值E_T，且存在空闲4邻域位置，生长概率随迭代线性衰减（最小0.2）。生长仅限每批训练的前I_grow次迭代，且每轮新增单元不超过G_max，避免无限扩张。方法不存储原始数据，但可能受限于协方差矩阵在高维潜空间的计算复杂度，且生长机制依赖超参数（如h_min、t_cool、SF）。
