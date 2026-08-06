# Robust and Personalized Federated Learning for Aircraft-Engine Prognostics under Benign and Adversarial Client Heterogeneity

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Chinmoy Mitra, Md. Mehedi Hasan Nipu, Mohammad Sakib Mahmood, Md. Rakibul Islam, M. F. Mridha
- 机构：American International University-Bangladesh, Missouri State University, Rajshahi University of Engineering & Technology, Malardalen University, North South University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04045v1) · [PDF](https://arxiv.org/pdf/2608.04045v1)

## TLDR
A single-sentence TLDR: This paper shows that in federated learning for aircraft-engine remaining-useful-life prediction, shared-representation personalization best addresses benign client heterogeneity, while robust aggregation like Krum is essential against adversarial poisoning, and combining both restores resilience to failure-masking backdoors.

## Abstract
Federated learning (FL) enables aircraft fleet operators to jointly train remaining-useful-life (RUL) models from engine sensor telemetry without sharing raw data. This study examines two complementary challenges: benign heterogeneity, where honest operators observe different operating conditions and fault modes, and adversarial heterogeneity, where compromised operators submit poisoned updates. We conduct a controlled, safety-oriented evaluation using a multi-task one-dimensional convolutional neural network and a structurally non-IID partition of the Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) benchmark. We compare four remedies for benign heterogeneity and evaluate five attacks against four aggregation methods, including a physically motivated sensor-value backdoor designed to mask engine degradation.
  Shared-representation personalization closes approximately 70% of the local-to-centralized root-mean-square-error gap, compared with 21% for proximal regularization and 10% for server-side reweighting. The backdoor achieves a 94.9% attack success rate against standard averaging while leaving clean accuracy statistically unchanged, demonstrating that accuracy alone cannot certify model safety and that attack success must be evaluated explicitly. Krum reduces attack success by an order of magnitude and is the only evaluated aggregator that withstands coordinated attackers, whereas personalization alone provides no protection. Combining personalization with robust aggregation restores robustness (2.8% attack success) with only a small accuracy cost, revealing a trade-off between robust update selection and collaborative representation learning. Results remain consistent across client counts and on a harder six-condition dataset. Code and data partitions are released for reproducibility.


## 精读解读（中文）
### 一、研究动机
航空发动机剩余寿命预测中，联邦学习允许机队运营商在不共享原始传感器数据的前提下联合训练RUL模型，但真实多运营商场景面临两类正交的客户端异质性：良性异质性（诚实运营商面临不同运行条件和故障模式）与对抗性异质性（被攻破运营商提交投毒更新）。现有FL-for-prognostics研究几乎只关注良性同构场景，而攻击研究则集中于图像分类基准，缺乏针对涡轮风扇发动机健康监测的物理启发后门攻击与鲁棒聚合的系统评估。本研究旨在同一C-MAPSS联邦基准下同时考察两类异质性，并验证个性化与鲁棒聚合能否组合成统一防御。

### 二、技术方案（Method）
基于C-MAPSS涡轮风扇退化基准，构建结构非IID的4客户端联邦划分（客户端1-2持有FD001单故障模式、客户端3-4持有FD003双故障模式，每个客户端50台发动机），采用多任务一维卷积神经网络（1D CNN）作为共享RUL预测模型。针对良性异质性比较四种方法：服务器端重加权、近端正则化（FedProx）、共享表征个性化（FedRep）和聚类联邦（FedCCFA）；针对对抗异质性构建五攻击×四聚合的全矩阵：标签翻转、梯度缩放（×−10和×−2）、物理动机的传感器值后门（通过篡改传感器读数掩盖发动机退化）以及协调的2-of-4拜占庭攻击，聚合器包括FedAvg、Trimmed Mean、Coordinate Median和Krum。训练流程：各客户端本地训练多轮后上传权重，服务器执行对应聚合，FedRep将模型拆分为共享表征层与本地个性化头，Krum在每轮选择最可信的单个客户端更新。后门攻击在恶意客户端对特定传感器值注入触发器并训练退化掩蔽行为，测试时检测攻击成功率。全部实验重复5个随机种子，并额外在客户端数量和六工况FD002/FD004数据集上验证一致性。

### 三、结果（Result）
共享表征个性化（FedRep）关闭了约70%的局部到集中式RMSE差距，远优于近端正则化（约21%）和服务器端重加权（约10%）；FedCCFA约为67%。物理动机传感器值后门在标准FedAvg下攻击成功率达94.9%，而干净精度在统计上无显著变化，证明仅看精度无法认证模型安全。鲁棒聚合中Krum将后门攻击成功率降低一个数量级至约6%，是唯一能抵御协调攻击者的评估聚合器；Trimmed Mean和Coordinate Median在2-of-4协同攻击下与无防御一样失败（攻击成功率约50%）。将FedRep与Krum组合后攻击成功率降至2.8%（±2.4），同时保留约70%的个性化收益，而单独使用个性化完全无防护（攻击成功率约63%）。结果在客户端数量和六工况数据集上保持一致。

### 四、结论（Conclusion）
良性异质性与对抗异质性需要不同且可组合的防御：个性化学习解决客户端数据分布差异，鲁棒聚合抵御中毒更新。将FedRep和Krum堆叠可在保持个性化精度收益的同时恢复稳健性，但存在鲁棒更新选择与协作表征学习之间的权衡。安全性评估必须显式测量攻击成功率，不能仅依赖干净精度。

### 五、方法论与关键技术细节
关键方法论细节包括：C-MAPSS结构非IID划分方式（不同故障模式子集分属不同客户端）以及受控实验设计（5攻击×4聚合全矩阵，5随机种子）；物理动机后门利用传感器值的物理语义植入触发器，通过掩盖发动机退化实现故障掩蔽，攻击成功率达94.9%且干净精度不变；Krum在f=1时攻击成功率约6%，组合FedRep+Krum后降至2.8%±2.4，但个性化单独无法提供安全保护；数据与代码分区已公开，便于复现。局限性包括：仅使用单一CNN架构、客户端规模较小（4客户端为主）、攻击模型假设攻击者控制本地训练管线，未考虑更复杂的多后门或自适应攻击；个性化与鲁棒聚合的组合存在精度-鲁棒性权衡，Krum的极端筛选可能丢弃信息。所有指标均对比局部训练与集中式训练基准，误差以RMSE衡量。
