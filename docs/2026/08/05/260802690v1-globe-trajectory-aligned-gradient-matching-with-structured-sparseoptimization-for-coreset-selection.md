# GLOBE: Trajectory-Aligned Gradient Matching with Structured SparseOptimization for Coreset Selection

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Hetian Liu, Jin Cui, Mengcheng Shi, Yanbin Hu, Xinyue Long, Boran Zhao, Pengju Pen
- 机构：Xi'an Jiaotong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02690v1) · [PDF](https://arxiv.org/pdf/2608.02690v1)

## TLDR
GLOBE proposes a coreset selection framework that aligns multi-checkpoint gradient trajectories via first- and second-order matching and structured sparse optimization (Group LASSO + Elastic Net), consistently improving downstream accuracy across benchmarks, especially at low retention ratios.

## Abstract
On-device training of deep neural networks is fundamentally constrained by the computational and memory costs of large-scale datasets. Coreset selection offers a practical solution by retaining only a compact subset of real training samples. However, existing gradient-based methods commonly rely on gradients computed at a single model snapshot and employ greedy or pursuit-based selection procedures, limiting their ability to capture evolving optimization dynamics and handle strongly correlated samples. We propose GLOBE (Gradient Local-Balanced Extraction), a trajectory-aligned coreset selection framework that formulates sample selection as a globally optimized sparse weighting problem. GLOBE represents each sample by a gradient trajectory constructed across multiple training checkpoints, thereby capturing its influence throughout different stages of optimization. To preserve the training behavior of the full dataset, we introduce a multi-order matching objective that jointly aligns the first-order mean and projected uncentered second-order moments of gradient trajectories. GLOBE further combines Group LASSO, Elastic Net regularization, and nonnegative budget constraints to induce group- and sample-level sparsity while stabilizing the weights of correlated trajectories. Finally, class-balanced Top-K selection maintains adequate category coverage under limited sampling budgets. Experiments across six benchmarks and five evaluation architectures demonstrate that GLOBE consistently outperforms existing coreset selection methods in downstream test accuracy, particularly at low retention ratios. These results highlight the effectiveness of combining dynamic gradient information, multi-order distribution matching, and structured sparsity for data-efficient learning.


## 精读解读（中文）
### 一、研究动机
现有基于梯度的核心集选择方法通常依赖单一模型快照下的梯度，并采用贪婪或追踪式选择策略，难以捕捉训练过程中的动态演化，也难以处理样本间强相关的情况。在设备端训练受计算和内存严格约束的背景下，需要一种能利用动态梯度信息并实现全局优化选择的核心集方法。

### 二、技术方案（Method）
GLOBE将核心集选择建模为全局稀疏权重优化问题。首先，通过知识蒸馏将轻量代理模型与教师模型输出对齐，训练代理并记录T个检查点，对每个样本在每个跟踪层拼接各检查点的逐样本梯度，构成梯度轨迹。然后，构造多阶匹配目标：一阶项匹配全量数据轨迹均值（Aω-b的二范数平方），二阶项通过随机投影降维后匹配投影非中心二阶矩（外积矩阵的Frobenius范数）。最后，结合Group LASSO（基于类内k均值特征聚类的样本组）和Elastic Net正则化，并施加非负预算约束，诱导组级和样本级稀疏性，稳定相关轨迹权重；最终通过类平衡Top-K选择得到核心集。

### 三、结果（Result）
在六个基准数据集和五种评估架构上的实验表明，GLOBE在下游测试准确率上持续优于现有核心集选择方法，尤其在低保留率（retention ratio）下优势更为明显。

### 四、结论（Conclusion）
将动态梯度信息、多阶分布匹配和结构化稀疏优化相结合，可以有效提升数据高效学习场景下的核心集质量，为资源受限的边缘设备训练提供实用方案。

### 五、方法论与关键技术细节
关键细节包括：代理模型通过知识蒸馏初始化，温度τ和平衡系数η控制软标签与硬标签的权衡；梯度轨迹按层独立构建，并用维度反比权重α平衡各层贡献；二阶矩匹配采用独立随机投影矩阵R_j降至m维，避免显式构造高维协方差；样本分组使用代理网络倒数第二层特征做类内k均值聚类；正则化中Group LASSO系数λ_g和Elastic Net系数共同控制稀疏性与稳定性；最终选择使用类平衡Top-K以保证类别覆盖。
