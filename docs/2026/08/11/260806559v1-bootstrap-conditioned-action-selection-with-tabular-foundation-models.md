# Bootstrap-Conditioned Action Selection with Tabular Foundation Models

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Devansh Gupta, Shiv Tavker, Dmitry Efimov, Suchitra Sathyanarayana, Gitanjali Bhutani, Boris N. Oreshkin
- 机构：Amazon Science
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06559v1) · [PDF](https://arxiv.org/pdf/2608.06559v1)

## TLDR
BC-ICL turns frozen pretrained tabular in-context learning models into randomized contextual bandit policies via bootstrap-resampled conditioning and an arm-context feature map, achieving strong regret performance that outperforms established bandit baselines.

## Abstract
Contextual bandits offer a natural framework for sample-efficient personalization, but practical deployment remains difficult under sparse, biased interaction data, unreliable uncertainty estimates, and severe cold starts. We study whether pre-trained tabular foundation models with in-context learning can be turned into randomized policies for online decision making. We propose BC-ICL (Bootstrap-conditioned action selection using ICL), which at each round draws a bootstrap resample of the interaction history, conditions a frozen pre-trained ICL model on that resample, scores all actions, and selects the action with the highest sampled score. We further introduce an arm-context conditioning architecture that promotes shared statistical strength across actions and helps avoid common bootstrap failure modes of isolated-arm bandits. Empirically, this policy delivers strong early-round regret and regret performance on standard contextual bandit suites, outperforming established baselines under a strict online protocol.


## 精读解读（中文）
### 一、研究动机
上下文赌博机为个性化推荐提供了自然框架，但实际部署面临数据稀疏且有偏、不确定性估计不可靠以及严重冷启动等挑战。传统线性或神经方法要么表达力有限，要么需要从零训练且不确定性估计在低数据区间脆弱。作者研究能否将预训练的表型基础模型通过上下文学习直接转化为在线决策的随机策略，以利用其强大的归纳偏置实现高效探索。

### 二、技术方案（Method）
提出BC-ICL（基于自举条件动作选择的上下文学习）。在每轮t，从交互历史D_t进行有放回的自举重采样得到D̃_t，将冻结的预训练ICL模型（如TabPFN或TabICL）以D̃_t为条件，对每个动作a构造乘性场景特征图Φ_mult(x,a)=[x; e_a; (x^T P)⊙e_a]，其中e_a为固定动作嵌入，P为共享投影矩阵。模型输出预测得分并裁剪到[0,1]，选择得分最高的动作a_t，观察奖励后追加到历史。训练/推理流程：每轮重新自举采样历史，ICL模型单次前向传播预测所有动作得分。引入共享投影的乘性编码，使自举扰动通过公共表示同时影响多个动作，促进跨动作共享统计强度，避免孤立动作自举失败。

### 三、结果（Result）
在Covertype、Isolet、Letter、MNIST、Mushroom、Shuttle六个标准上下文赌博机数据集上，BC-ICL-TabPFN和BC-ICL-TabICL的累积遗憾均大幅优于线性TS、LinUCB、Kernel UCB/TS、NeuralUCB/TS和BootstrapNN。例如在Letter上BC-ICL-TabPFN达到4074.2（最优），Isolet上BC-ICL-TabICL达到2992.5。在Mushroom和Shuttle上BC-ICL-TabICL分别为37.7和92.2，均为最优。消融显示自举采样比贪心或概率采样在多数数据集上降低5-19%遗憾，乘性编码比one-hot降低约30-40%最终遗憾。计算成本方面，BC-ICL-TabICL使用FIFO或KNN上下文窗口时可与BootstrapNN竞争，KNN可保持遗憾。

### 四、结论（Conclusion）
BC-ICL通过自举重采样历史并针对所得预测器贪心选动作，将预训练的表型基础模型转化为具备探索能力的随机策略，同时保留上下文学习的归纳偏置。实验表明其跨多种基准显著优于线性、核化和神经基线，验证了乘性场景-手臂表示能实现跨动作的有效统计共享。该方法假设预训练模型与目标任务先验对齐，性能可能因先验失配而下降，且自举重采样带来额外计算开销。

### 五、方法论与关键技术细节
数据：8个UCI/图像分类数据集转为上下文赌博机（动作对应类别，奖励为是否匹配）；对高维数据PCA预处理。输入建模采用乘性特征图[x; e_a; (x^T P)⊙e_a]，e_a维度K。训练/推理：每轮对历史自举重采样，ICL模型前向传播得到所有动作得分，选最高分。关键先验：共享投影P保持历史扰动跨动作传播。损失/操作：模型输出剪辑到[0,1]，无额外训练损失。超参：d_a=K，P随机矩阵，FIFO/KNN窗口2000。复杂度：每轮多次前向传播，可用上下文窗口控制。局限性：依赖预训练模型先验对齐，自举计算开销，固定特征表示。
