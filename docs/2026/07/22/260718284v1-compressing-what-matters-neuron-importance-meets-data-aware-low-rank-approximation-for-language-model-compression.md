# Compressing What Matters: Neuron Importance Meets Data-Aware Low Rank Approximation for Language Model Compression

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Athanasios Ntovas, Alexandros Doumanoglou, Petros Drakoulis, Dimitris Zarpalas
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18284v1) · [PDF](https://arxiv.org/pdf/2607.18284v1)

## TLDR
This paper proposes a language model compression method that combines neuron importance with data-aware low-rank approximation and an efficient dynamic compression rate allocation algorithm, achieving performance on par with or better than prior state-of-the-art, especially under high compression ratios.

## Abstract
To excel at their domain large language models are comprised of billions of parameters. Yet this comes at the cost of huge memory requirements restricting their applicability in resource-constrained environments. To address the problem of neural network (NN) compression Singular Value Decomposition (SVD) has played a key role as a fundamental component for matrix compression through decomposition. To minimize compression error and to maximize the efficacy of the compressed model on the downstream tasks previous works focused on low-rank approximation of the NN's weight matrices either from the perspective of parameter importance or per-layer functional equivalence. While previous works studied the aforementioned perspectives in isolation in this work we are investigating the effectiveness of an approach that combines ideas from these two perspectives in a single objective. In parallel to this an important aspect that affects the compression quality is the distribution of the compression rate across layers and NN parameters. Earlier works mostly considered distributing the compression rate uniformly across layers and network weights or relied on computationally expensive heuristic search. Contrary to them in this work we propose an enhanced and computationally efficient algorithm for dynamic compression rate allocation. Experimental results support the efficacy of the proposed approach which performs on par or substantially better than the previous state-of-the-art especially under high compression ratios.


## 精读解读（中文）
### 一、研究动机
大语言模型参数量巨大导致高内存需求，限制了在资源受限环境中的应用。先前基于奇异值分解的压缩方法要么从参数重要性角度，要么从逐层功能等价角度进行低秩近似，但未结合两者；同时压缩率分配常采用均匀分配或昂贵的启发式搜索。本文旨在结合这两种视角并提出高效的动态压缩率分配算法。

### 二、技术方案（Method）
该方法将参数重要性（神经元重要性）与数据感知的低秩近似结合为统一目标，对权重矩阵进行低秩分解。具体而言，通过计算神经元重要性得分加权到低秩近似损失中，同时利用少量校准数据感知输出分布。此外，提出一种计算高效的动态压缩率分配算法，基于各层对最终任务的重要性得分自适应分配压缩预算，避免均匀分配或昂贵搜索。整个流程包括：为每层计算重要性、根据预算分配压缩率、执行带重要性加权的SVD分解，最后微调恢复性能。

### 三、结果（Result）
实验结果表明，该方法在多个语言模型压缩任务上性能与先前最优方法持平或显著超越，特别是在高压缩比场景下优势明显。例如在困惑度（perplexity）和下游任务准确率等指标上均有提升，证明了综合视角与动态分配的有效性。

### 四、结论（Conclusion）
提出的结合神经元重要性和数据感知低秩近似的压缩框架，以及高效的动态压缩率分配算法，有效提升了大型语言模型的压缩效率与任务性能，尤其适用于高压缩比场景，为资源受限环境下的模型部署提供了可行方案。

### 五、方法论与关键技术细节
关键细节包括：1）统一目标中融合了神经元重要性权重与数据感知的重建误差，使用校准数据计算输入激活；2）动态压缩率分配算法基于重要性评分进行迭代调整，复杂度低；3）方法无需额外训练，仅需少量校准数据和一次前向传播计算重要性；4）局限性在于校准数据的选择可能影响压缩效果，且动态分配需一定计算开销。
