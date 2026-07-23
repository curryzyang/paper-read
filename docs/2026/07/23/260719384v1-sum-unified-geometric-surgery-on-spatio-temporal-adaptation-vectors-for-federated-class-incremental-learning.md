# SUM: Unified Geometric Surgery on Spatio-Temporal Adaptation Vectors for Federated Class Incremental Learning

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Jaeik Kim, Jaeyoung Do
- 机构：Seoul National University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19384v1) · [PDF](https://arxiv.org/pdf/2607.19384v1)

## TLDR
SUM proposes a purely server-side framework that geometrically transforms client and task adaptation vectors during aggregation to mitigate spatial and temporal interference in Federated Class Incremental Learning, achieving up to 22% improvement without extra client-side computation or memory.

## Abstract
Real-world intelligent systems often require both distributed collaboration across data-isolated clients and continual adaptation to evolving tasks. This setting naturally gives rise to Federated Class Incremental Learning (FCIL), which combines Federated Learning (FL) and Continual Learning (CL). However, their combination introduces two coupled sources of interference: spatial interference from heterogeneous clients and temporal interference from sequential tasks, jointly leading to Spatial-Temporal Catastrophic Forgetting (ST-CF). Existing approaches typically address spatial and temporal interference with separate mechanisms, often incurring additional client-side computation or communication, while leaving directional interactions among updates during aggregation unregulated. In this paper, we reinterpret FCIL as a unified multi-task learning problem, where both client and task updates are represented as adaptation vectors in a shared parameter space. Based on this view, we propose Unified Geometric Surgery on Spatio-Temporal Adaptation Vectors (SUM), a purely server-side framework that performs geometric surgery on adaptation vectors during aggregation. Spatial SUM mitigates client-level interference within each round, while causal online temporal SUM removes cross-task interference over time without additional client-side computation, communication, or memory beyond standard federated training. Empirically, SUM achieves up to 22% improvement over prior FCIL methods across diverse vision and language benchmarks while remaining robust to unreliable clients and maintaining computational efficiency.


## 精读解读（中文）
### 一、研究动机
现有联邦类增量学习方法在处理来自异构客户端的空间干扰和来自顺序任务的时间干扰时，通常采用分离机制，增加了客户端计算或通信开销，且未调节聚合过程中更新的方向交互。本文重新将联邦类增量学习解释为统一的多任务学习问题，并提出SUM框架以解决空间-时间灾难性遗忘。

### 二、技术方案（Method）
SUM是一个纯服务器端框架，在聚合时对适应向量进行几何手术。空间SUM在每个通信轮次内通过移除客户端更新向量间的对齐分量消除客户端级方向干扰，因果在线时间SUM通过将新任务更新投影到历史任务张成的正交补空间来移除跨任务干扰，两者均不引入额外客户端计算、通信或内存。更新表示为共享参数空间中的适应向量，服务器在聚合前对每个向量进行正交分解，仅保留独立贡献。

### 三、结果（Result）
在多个视觉和语言基准上，SUM相比现有FCIL方法最终平均准确率提升高达22%，例如在Split CIFAR-100上平均准确率提高19.3%，对恶意客户端设置保持鲁棒，并维持计算效率，其服务器端额外开销仅与客户端数量呈线性关系。

### 四、结论（Conclusion）
SUM通过统一几何手术有效解决联邦类增量学习中的空间-时间灾难性遗忘，无需修改客户端训练，仅服务器端聚合时操作，保持通信效率并实现显著性能提升，为分布式持续学习提供了一种简洁高效的解决方案。

### 五、方法论与关键技术细节
关键方法细节包括：适应向量相对于预训练基模型定义以确保共享参考系；空间SUM采用并行正交分解，时间SUM采用因果在线投影至历史基的补空间；无需客户端存储或记忆重放；但依赖共享参数空间假设，且当任务向量高度非正交时可能丢失部分协同信息；实验中使用FedAvg作为基础通信协议，超参如学习率与标准设置一致。
