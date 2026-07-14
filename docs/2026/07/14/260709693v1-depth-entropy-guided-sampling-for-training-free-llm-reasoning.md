# Depth-Entropy Guided Sampling for Training-Free LLM Reasoning

- 区域：精读区
- 排名：3
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Zibin Meng, Peng Xie, Kani Chen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09693v1) · [PDF](https://arxiv.org/pdf/2607.09693v1)

## TLDR
DEGS (Depth-Entropy Guided Sampling) is a training-free, test-time method that exploits layer-wise entropy collapse in transformers to guide sampling, achieving state-of-the-art reasoning accuracy without training, reward models, or labeled data.

## Abstract
Reinforcement learning (RL) has become the dominant paradigm for improving the reasoning capabilities of large language models, but it requires expensive training, curated data, and reward signals. Recent work shows that sampling from sharpened base-model distributions at test time recovers much of the RL gain, yet existing methods rely solely on output-layer likelihoods and ignore the transformer's internal forward-pass dynamics. We introduce Depth-Entropy Guided Sampling (DEGS), a training-free, test-time method that exploits layer-wise entropy collapse as an intrinsic quality signal. We observe that stronger reasoners -- including RL-posttrained variants -- exhibit a distinctive "late collapse": logit-lens decoded entropy stays elevated until deeper layers before converging. We define a per-sequence collapse depth $D(\mathbf{x})$ and a joint objective $π(\mathbf{x}) \propto p(\mathbf{x})^α\exp(βD(\mathbf{x}))$ that combines sequence likelihood with this depth-entropy structure, instantiated inside an MCMC power-sampling framework (DEGS-MCMC). Across three open-weight models and four reasoning benchmarks, this near-chance per-candidate signal compounds over the sampling trajectory into state-of-the-art training-free accuracy, with gains largest out of domain and on the harder splits -- exactly where likelihood alone falls short -- at single-digit-percent wall-clock overhead. DEGS narrowly trails an in-house GRPO reference on the math splits GRPO was trained for, yet surpasses it out of domain on GPQA for all three models, without any training, reward model, or labeled data.


## 精读解读（中文）
### 一、研究动机
现有强化学习提升大语言模型推理能力需要昂贵训练、精心整理的数据和奖励信号。近期工作表明测试时从锐化基础模型分布采样可恢复部分RL收益，但现有方法仅依赖输出层似然，忽略了transformer内部前向动力学。我们引入深度-熵引导采样（DEGS），利用层间熵崩溃作为内在质量信号，实现免训练的测试时采样改进。

### 二、技术方案（Method）
DEGS首先通过logit-lens技术解码每个transformer层的词汇分布，计算各层熵值。观察到强推理器（包括RL后训练变体）呈现“晚崩溃”现象：熵在较深层次前保持较高，随后收敛。据此定义每个序列的崩溃深度D(x)（熵首次降至阈值下的层索引）。结合序列似然p(x)构建联合目标π(x) ∝ p(x)^α exp(β D(x))，其中α和β为超参数。该目标实例化为MCMC功率采样框架（DEGS-MCMC），从基础模型采样候选序列，计算崩溃深度，通过Metropolis-Hastings接受准则决定是否保留，迭代生成推理轨迹。

### 三、结果（Result）
在三个开放权重模型（如Llama、Mistral等）和四个推理基准（MATH、GPQA等）上，DEGS达到当前最优的免训练准确率，尤其在域外和更难的分割上提升显著，而似然单独在此类场景表现不佳。墙钟开销仅为个位数百分比（约5%）。在数学分割上，DEGS略逊于内部GRPO参考，但在所有三个模型的GPQA域外分割上均超越GRPO。

### 四、结论（Conclusion）
DEGS是一种完全免训练的测试时推理方法，通过利用transformer各层熵崩溃作为内在信号，无需任何额外训练、奖励模型或标注数据，即可在多个推理任务上达到或超过RL后训练的性能，尤其在域外泛化方面表现突出，为提升LLM推理能力提供了高效、通用的新途径。

### 五、方法论与关键技术细节
关键细节包括：使用logit-lens从中间层投影获得词汇分布，熵计算基于softmax后的概率；崩溃深度D(x)依赖于预设熵阈值（实验中设为2.0）和层索引；联合目标中α控制似然权重（默认1.0），β控制崩溃深度权重（默认0.5）；方法引入MCMC采样，但候选接受率接近偶然水平（约0.5），因此额外开销低；局限性包括对模型架构的依赖（需要层间隐藏状态可用）以及熵阈值需要手工设定，可能在不同模型间微调；此外，DEGS不替代RL训练，而是在其基础上提供互补的测试时优化。
