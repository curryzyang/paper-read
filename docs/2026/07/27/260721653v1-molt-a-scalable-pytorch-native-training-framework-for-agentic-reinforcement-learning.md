# Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Jian Hu, Huiying Li, Hao Zhang, Binfeng Xu, Yifan Zhang, Shaokun Zhang, Hemil Desai, Michael Demoret, Pavlo Molchanov, Jan Kautz, Yi Dong
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21653v1) · [PDF](https://arxiv.org/pdf/2607.21653v1)

## TLDR
Molt is a compact, PyTorch-native training framework for agentic reinforcement learning that is both researcher-friendly and performant, matching state-of-the-art Megatron-based stacks while enabling easy algorithm modification.

## Abstract
Agentic reinforcement learning research is constant algorithm modification, new estimators, new pipeline stages, new rollout schemes, and in mainstream frameworks each change threads through layers of trainer, distributed backend, and rollout glue: the cost lands on the researcher at every iteration. Molt is a PyTorch-native training framework built to keep that cost small: a codebase compact and clean enough for a researcher to hold in their head, and for an AI coding assistant to read and reason about in its entirety, so the algorithm flow can be traced and changed end to end. The agent is an ordinary program, and one asynchronous loop trains multimodal and mixture-of-experts policies while never training on a token it did not generate, consistent in tokens, policy versions, and model semantics. Leanness does not cost performance: under a matched, fully asynchronous protocol, Molt is statistically comparable to a state-of-the-art Megatron-based stack. Molt is open source and provides recipes and containers at https://github.com/NVIDIA-NeMo/labs-molt.


## 精读解读（中文）
### 一、研究动机
现有智能体强化学习研究涉及频繁的算法修改、新估计量、新流水线阶段和新采样方案，但主流框架中每次修改都要穿透训练器、分布式后端和采样胶水等多层，导致研究者每次迭代的成本高昂。Molt旨在通过紧凑清晰、易于研究人员整体理解且能被AI编码助手完整读取的代码库，保持低成本，使算法流程可端到端追踪和修改。

### 二、技术方案（Method）
Molt是一个PyTorch原生训练框架，将智能体实现为普通程序，通过单个异步循环同时训练多模态和混合专家策略。框架确保仅在模型自身生成的token上进行训练，并在token、策略版本和模型语义上保持一致性。技术方案包括异步训练循环、输入处理、策略建模与训练流程，不依赖外部分布式后端，所有训练和采样在统一的异步协议下进行。

### 三、结果（Result）
在匹配的完全异步协议下，Molt的性能与基于Megatron的最先进框架在统计上相当，证明了轻量化设计不会牺牲性能。

### 四、结论（Conclusion）
Molt为智能体强化学习研究提供了一个高效、可扩展且易于修改的训练框架，其开源特性（提供recipes和容器）将进一步推动领域内算法迭代与实验复现。

### 五、方法论与关键技术细节
Molt的设计核心是紧凑性：代码库足够小，研究者可整体掌握，AI助手可完整阅读，从而降低修改成本。异步循环保证了训练与采样的版本一致性，避免训练到非自生成token。框架依赖PyTorch生态系统，无额外分布式依赖；理论上支持多模态和MoE策略，但具体模型规模和计算效率的对比实验未在摘要中提供，局限性可能在于对超大规模集群的适配性尚待验证。
