# RW-LoRA: Communication-Efficient Decentralized LoRA Fine-Tuning via Random Walks

- 区域：精读区
- 排名：5
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Xingran Chen, Rohit Bhagat, Ghadir Ayache, Rawad Bitar, Yanmin Gong, Salim El Rouayheb
- 机构：LinkedIn, Rutgers University, Singapore University of Technology and Design, Technical University of Munich, Texas A&M University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00078v1) · [PDF](https://arxiv.org/pdf/2609.00078v1)

## TLDR
RW-LoRA introduces a decentralized LoRA fine-tuning method where a single model token traverses the network via random walks and is updated sequentially at local nodes, eliminating global synchronization and aggregation errors, reducing communication/computation overhead, and achieving competitive NLP task performance with rigorous convergence guarantees compared to gossip-based LoRA.

## Abstract
Parameter-efficient fine-tuning methods such as LoRA have become a standard approach for adapting large foundation models. Adopting fine-tuning to distributed settings faces several challenges. Most existing distributed LoRA methods rely on centralized aggregation, and gossip-based decentralized LoRA requires repeated synchronization among multiple model copies. Both methods incur significant communication overhead and introduce errors due to simultaneous aggregation of multiple model updates. In this paper, we take a different perspective and propose a random-walk-based LoRA fine-tuning scheme. Instead of maintaining multiple model replicas, a single model token traverses the network and is updated sequentially using local fine-tuning objectives. This design eliminates the need for global synchronization, substantially reduces communication and computation costs, and avoids aggregation errors. We provide rigorous convergence guarantees for non-convex objectives under standard assumptions. Through empirical results on multiple NLP tasks and graph topologies, we show that the proposed method achieves competitive task performance with substantially less communication and computation than gossip-based LoRA.


## 精读解读（中文）
### 一、研究动机
现有的分布式LoRA微调方法主要依赖中心化服务器聚合或基于gossip的去中心化同步，两者都需要频繁交换模型参数或多次副本同步，造成显著通信开销，并在同时聚合多个模型更新时引入聚合误差（例如LoRA因子平均时的双线性失配）。RW-LoRA旨在提出一种低通信开销、无需全局同步且避免聚合误差的分布式LoRA微调范式。

### 二、技术方案（Method）
RW-LoRA采用基于随机游走的单token顺序更新机制。具体而言，网络中的单个token携带当前LoRA低秩因子(A,B)在图上随机游走；在每次迭代t，token位于节点v_t，该节点使用本地数据计算目标函数的随机梯度，并更新低秩因子A和B，更新后token根据图的转移概率P传到随机邻居节点v_{t+1}。算法初始化A遵循高斯分布、B为零矩阵，并冻结预训练权重W0；在节点处先重构W=W0+BA，再基于本地随机梯度执行因子更新，重复T次。全流程无需参数服务器、无需邻居间同步，也不进行多个模型副本的聚合。

### 三、结果（Result）
在多个NLP任务和不同图拓扑（包括完全图和环形图）上的实验表明，与基于gossip的去中心化LoRA基线相比，RW-LoRA在保持相当任务精度的同时，显著降低了通信开销和计算量。论文还给出了非凸目标下基于标准假设的严格收敛保证。

### 四、结论（Conclusion）
RW-LoRA提供了一种通信高效的分布式LoRA微调新思路，通过单一模型token沿随机游走顺序更新，消除了全局同步和多副本聚合开销，规避聚合误差，在通信和计算受限的去中心化场景中具有实用价值。

### 五、方法论与关键技术细节
关键细节包括：传输的是LoRA低秩因子(A,B)而非完整梯度，通信量与单token大小有关；随机游走的收敛速度依赖图的混合时间（mixing time）；理论分析假定数据在节点间i.i.d.分布，非i.i.d.扩展留作未来工作；更新规则为Markov采样下的随机梯度法，避免同时聚合多个独立更新；初始化采用B=0以保证训练初期的LoRA增量不影响原模型输出；实验中的LoRA秩r取常见小值（如2/4/8/16）。
