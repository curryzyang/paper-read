# SDO: Structure-Aware Data Organization for Efficient LLM Post-Training

- 区域：精读区
- 排名：7
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Jinliang Gao, Ning Yang, Hai Wang, Baili Xiao, Pin Lyu
- 机构：National University of Defense Technology, Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27273v1) · [PDF](https://arxiv.org/pdf/2607.27273v1)

## TLDR
SDO is a plug-and-play, structure-aware data organization framework that uses exposure-driven feedback and representation-space locality to dynamically shape mini-batch composition and sample exposure, accelerating convergence across SFT, DPO, and GRPO while preserving long-term coverage.

## Abstract
Post-training of large language models is expensive, and existing efficiency improvements mainly focus on selecting informative samples or designing training schedules. However, data organization itself is usually treated as a static preprocessing step: embedding-based grouping methods construct fixed partitions before training and cannot adapt to the evolving sample exposure during optimization. As a result, all samples receive similar exposure despite their different optimization needs, leading to redundant updates for some samples while leaving others under-optimized. To address this problem, we propose SDO (Structure-Aware Data Organization), a plug-and-play data organization framework with an exposure-driven feedback mechanism that organizes mini-batch composition and sample exposure according to representation-space structure. SDO operates epoch by epoch on frozen external embeddings, avoiding model warm-up training overhead: within each epoch, locality-aware batching forms coherent mini-batches via KNN neighborhood traversal; across epochs, exposure-balanced scheduling records per-sample participation and reduces the sampling probability of over-exposed samples to preserve long-term coverage. Across SFT, DPO, and GRPO, SDO accelerates convergence, with the largest gains observed in the early-to-mid phase, producing more coherent gradients and more balanced accuracy across question types without permanently excluding training samples.


## 精读解读（中文）
### 一、研究动机
大语言模型后训练成本高昂，现有数据效率优化主要关注样本选择或训练调度，但数据组织本身通常被视为静态预处理：基于嵌入的分组方法在训练前构造固定划分，无法适应优化过程中样本曝光的动态变化，导致所有样本获得相似曝光，而不同样本的优化需求不同，部分样本被冗余更新、部分欠优化。

### 二、技术方案（Method）
SDO是一个即插即用的数据组织框架，基于冻结的外部嵌入按epoch运行，通过曝光驱动反馈机制同时组织小批量构成和样本曝光。具体流程包括：1）数据准备：用固定预训练句子编码器对每个样本的prompt编码为嵌入矩阵E；2）拓扑感知邻域构建：每个epoch开始时，在当前池内按余弦相似度为每个样本计算K近邻；3）曝光跟踪局部批处理：通过邻域图遍历，以锚点及其K近邻聚合为批缓冲，达到批量大小B后取出小批量进行优化，同时更新全局曝光账本u_i；4）动态池重建：epoch结束后，用阈值tau_e=(e+1)Δtau将全量数据分为冷集（u_i<tau_e）和热集（u_i≥tau_e），冷集全部保留，热集按与曝光成反比的概率1/u_i无放回采样保留比例r，与冷集合并形成下一epoch的池；5）重复至T个epoch。算法使用KNN图近似表示空间局部性，将批次梯度冲突最小化，且不改变原学习目标或训练调度。

### 三、结果（Result）
在SFT、DPO和GRPO三种后训练范式上，SDO均加速了收敛，且最大收益出现在训练早期到中期阶段；相比静态分组基线，SDO产生更一致的梯度，并显著提升不同问题类型间的准确率均衡性，同时不会永久排除训练样本。梯度诊断实验证实了批内梯度一致性改善，组件消融实验分离了局部性批处理和曝光平衡各自的贡献。

### 四、结论（Conclusion）
SDO通过将数据组织从静态预处理升级为曝光驱动的闭环反馈，在表示空间局部性与梯度行为之间建立联系，以极低额外开销（无需模型warm-up、使用冻结外部嵌入）即可显著提升大模型后训练效率，并可扩展到SFT、DPO、GRPO等多种范式，是一种通用且覆盖保持的数据组织方案。

### 五、方法论与关键技术细节
关键细节包括：输入仅使用prompt的冻结嵌入，编码器不参与训练；关键超参为邻域大小K、小批量大小B、阈值增量Δtau和热集保留比例r；曝光账本对全量N个样本累计参与次数，被排除样本的u_i冻结但随threholding单调上升最终会通过冷集重新进入池，因此是临时频率调整而非永久过滤；理论分析基于局部梯度平滑假设（表示空间中相近样本的梯度差异被Lipschitz常数约束），其有效性依赖编码器捕捉任务相关语义的能力；每个epoch需重新构建当前池的KNN图，计算成本随池大小和K变化，但比模型warm-up低；框架不修改损失函数，可与偏好损失改进或RL优势估计等优化目标层面的方法正交结合。
