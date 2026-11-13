# Thompson Sampling using Prior-fitted Diffusion Transformers

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Sihwa Park, Jingsen Zhu, Vinamr Jain, Sheng-Yen Chou, Alexander Terenin
- 机构：Cornell University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14656v1) · [PDF](https://arxiv.org/pdf/2611.14656v1)

## TLDR
The paper introduces prior-fitted diffusion transformers that perform Thompson sampling in-context for black-box global optimization, enabling practical non-Gaussian priors and outperforming traditional Gaussian-process-based pipelines on benchmarks.

## Abstract
Thompson sampling is natural randomized strategy for optimizing unknown functions in a black-box manner. In continuous global optimization, Thompson sampling has largely been restricted to Gaussian process priors, as these are essentially the only class for which computing the posterior distribution has been tractable in practice. In this work, we introduce \emph{prior-fitted diffusion transformers}, which are diffusion models that perform Thompson sampling in-context at inference time, after being pre-trained using the prior-fitted network paradigm. To apply these models, we develop a set of practical non-Gaussian priors for general black-box functions---including those that have characteristics that cannot be achieved under Gaussianity, such as priors over unimodal functions. We also quantify the tradeoff between model size and the number of pre-training iterations, and show that these models follow scaling laws akin to those observed in transformers defined over other modalities. Across a set of global optimization benchmarks, we show that prior-fitted diffusion transformers with non-Gaussian priors can achieve improved performance compared to traditional pipelines built on Gaussian processes.


## 精读解读（中文）
### 一、研究动机
连续黑箱全局优化中的 Thompson sampling 长期受限于高斯过程先验，因为只有这类先验的后验计算在实践中较易处理，导致难以表达非高斯、单峰等更贴近实际目标的函数先验。作者希望把 Thompson sampling 嵌入可扩展的生成式基础模型，在保持决策论解释的同时利用扩散模型和标准生成训练流程提升优化性能。

### 二、技术方案（Method）
作者提出 prior-fitted diffusion transformers：预训练时从用户指定的函数先验 p(f) 采样函数，均匀采样上下文数据点 x_{1:n} 并计算 y_i=f(x_i)，以全局最大值点 x^*_f=argmax f 为目标；若最大值无解析解则用梯度优化近似。模型将上下文数据集 (x_i,y_i) 编码为序列，经无位置编码、无因果掩码的全连接注意力 transformer 编码，再用交叉注意力条件化扩散 transformer，通过 flow matching 学习从噪声生成 x^*_f 的条件分布，该分布即 Thompson sampling 分布；推理时输入观测数据即可采样候选点。

### 三、结果（Result）
在多个全局优化基准上，使用非高斯先验的 prior-fitted diffusion transformers 能够匹配并有时优于基于高斯过程的传统 Thompson sampling 流程，说明该方法在样本高效黑箱优化中具有竞争力。作者还量化了模型规模与预训练迭代数之间的权衡，并发现这些模型呈现出与其他模态 transformer 类似的 scaling laws。

### 四、结论（Conclusion）
该工作表明，prior-fitted diffusion transformer 可以在推理阶段以 in-context 方式执行 Thompson sampling，并将非高斯先验、单峰函数等传统高斯过程难以表达的先验自然纳入贝叶斯优化。相比既有扩散优化方法，它不依赖专门损失、正则项或空间离散化，而是通过合成数据生成过程控制不确定性与探索，提供了更简洁且决策论 grounded 的端到端管线。

### 五、方法论与关键技术细节
关键实现包括：上下文样本数 n 随机采样，通常 n~U{1,...,N} 且 x_i~U([0,1]^d)；先验函数需可采样和逐点求值，并具有解析或可微近似最大值；训练目标为标准 flow matching 损失而非回归损失，以学习完整条件分布；架构采用全连接注意力且不使用位置编码或因果掩码，以匹配贝叶斯规则对数据顺序的不变性。局限在于性能依赖先验选择与可采样性，无解析最大值时目标需近似计算，且结论主要基于所选取的全局优化基准。
