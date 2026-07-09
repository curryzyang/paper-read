# WHERE to Generate Matters: Budget-Aware Synthetic Augmentation for Label Skewed Federated Learning

- 区域：精读区
- 排名：8
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Sangwoo Lee, Sunghwan Park, Jaewoo Lee
- 机构：Chung-Ang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06616v1) · [PDF](https://arxiv.org/pdf/2607.06616v1)

## TLDR
FedEAS proposes an entropy-adaptive per-class generation budget for label-skewed federated learning that decides both how much and where to allocate synthetic samples, recovering most of the accuracy gain of full class balancing while reducing the generation budget by 94.1%.

## Abstract
Label skew in federated learning (FL) causes client drift and degrades global accuracy. Synthetic data augmentation can reduce this imbalance; however, full class balancing requires substantial computation cost. We propose FedEAS, a policy that assigns each client an entropy-adaptive per-class generation budget computed from its local label distribution. The budget jointly decides \emph{how much} each client generates and \emph{WHERE} the samples go. Accordingly, the total generation budget follows from the per-client budgets rather than being fixed in advance. FedEAS recovers most of the accuracy gain of full class balancing while reducing the generation budget by 94.1\%. At the same total generation budget, it outperforms Uniform allocation by up to 18.82\% across CIFAR-10 and CIFAR-100.


## 精读解读（中文）
### 一、研究动机
联邦学习中标签偏移会导致客户端漂移并降低全局模型精度。现有的全类平衡合成数据增强方法虽然能缓解不均衡，但需要生成大量样本，计算成本高昂。核心问题在于：每个客户端实际需要多少合成数据？生成的样本应该分配到哪些类别？

### 二、技术方案（Method）
提出FedEAS熵自适应合成策略。每个客户端根据本地标签分布计算每类生成预算b_k = floor(sqrt(平均每类样本数) * (1 - 归一化熵) * β)，其中β为全局预算参数。预算决定了每个客户端生成多少样本以及样本去向：只填充那些当前样本数低于预算的类别（缺失和稀缺类），总生成预算由各客户端预算累加而非预先固定。服务器广播β，客户端首次参与时一次性生成所需样本并缓存，后续训练复用该缓存；本地训练使用原始数据与合成数据，聚合采用原始数据集大小的加权FedAvg。该策略与生成器无关，可替换任意条件生成模型。

### 三、结果（Result）
在CIFAR-10和CIFAR-100的狄利克雷标签偏移下（α=0.1），FedEAS恢复了全类平衡策略的大部分精度增益，同时将生成预算减少94.1%。在相同总生成预算下，FedEAS比均匀分配策略在分类准确率上提升高达18.82%（CIFAR-10和CIFAR-100）。精度随预算参数β单调增加，可通过调整β适应可用生成资源。

### 四、结论（Conclusion）
FedEAS通过熵自适应预算分配策略有效解决了标签偏移问题，在不牺牲太多精度的前提下大幅降低了合成数据生成成本。该策略将预算集中在最倾斜的客户端和稀缺类别，实现资源高效利用，适用于资源受限的联邦学习场景。

### 五、方法论与关键技术细节
关键点：利用归一化熵衡量客户端倾斜程度，熵越小（倾斜越严重）预算越大；预算公式采用次线性缩放（sqrt平均样本数）以避免过度分配大客户端；样本仅填充低于预算的类别，避免浪费在已足够类别；生成仅进行一次并缓存，通信开销不变；超参数β控制总预算规模，可手动选择以适应资源；局限性：依赖预训练条件生成器（如DDPM），生成质量影响性能；β选择需权衡精度与生成成本。
