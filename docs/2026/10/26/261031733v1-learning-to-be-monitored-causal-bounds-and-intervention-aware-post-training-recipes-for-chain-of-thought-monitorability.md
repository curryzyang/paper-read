# Learning to Be Monitored: Causal Bounds and Intervention-Aware Post-Training Recipes for Chain-of-Thought Monitorability

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Qiang Fu, Xinyue Li, Andre Wibisono, Arman Cohan
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31733v1) · [PDF](https://arxiv.org/pdf/2610.31733v1)

## TLDR
The paper establishes tighter causal bounds for chain-of-thought monitorability and shows that intervention-aware post-training methods based on off-policy self-distillation, reinforcement learning, and on-policy self-distillation generally improve LLM CoT monitorability under this framework.

## Abstract
Chain-of-thought (CoT) monitoring aims to detect potentially harmful behaviors in large language models (LLMs) from their CoTs. Intervention-based evaluations measure this property by asking whether a monitor can detect the role of an intervention from the CoT when the targeted behavior occurs, typically using minimal-criterion sensitivity ($\mathsf{TPR_{mc}}$) proposed by~\citep{guan2025monitoring}. However, a target behavior observed under intervention is not necessarily caused by it, and we show that this metric can overestimate how often a monitor detects target behaviors actually caused by the intervention. Specifically, we establish $\mathsf{TPR_{mc}}$ as an upper bound on this causal detection rate and derive a complementary lower bound, which provides a tighter evaluation framework for CoT monitorability. With this framework, we study whether LLMs can be trained to make their CoTs easier to monitor. We first construct a training dataset of paired control--intervention tasks spanning multiple intervention types. Using the dataset, we design and apply three intervention-specific training methods based on off-policy self-distillation, reinforcement learning, and on-policy self-distillation to train separate variants of each base model. Across various model-monitor configurations, all three methods generally improve CoT monitorability over the corresponding base models under our extended evaluation framework. Our code is available at https://github.com/xinyue-lxy/learning-to-be-monitored.


## 精读解读（中文）
### 一、研究动机
链式思维监控希望从大语言模型（LLM）的CoT中检测潜在有害行为，而干预式评估通过监控器能否从CoT识别干预作用来衡量可监控性。作者指出，在干预下观察到的目标行为未必由干预导致，因此常用的最小准则敏感度TPR_mc可能高估监控器对“真正由干预导致的目标行为”的检测率。

### 二、技术方案（Method）
作者首先将TPR_mc建立为因果检测率的上界，并推导互补下界，形成更紧的CoT可监控性评估框架。随后构建覆盖多种干预类型的控制-干预配对任务训练集，针对不同干预设计三种训练方法：离策略自蒸馏、强化学习与在策略自蒸馏，并分别训练各基模型变体。最后在多种模型-监控器配置下，用扩展评估框架比较训练后模型与对应基模型的CoT可监控性。

### 三、结果（Result）
核心发现是TPR_mc会高估监控器对干预因果导致行为的检测频率，因而仅用该指标会偏乐观；作者给出的上界与互补下界提供了更紧的评估区间。实验上，在多种模型-监控器配置中，三种干预特定训练方法总体上均较对应基模型提升CoT可监控性。

### 四、结论（Conclusion）
研究表明，CoT可监控性不仅需要干预式指标，还应采用因果检测率的上界与下界进行更严格评估；在此框架下，通过配对数据与干预特定后训练，LLM可以被训练得使其CoT更容易被监控。

### 五、方法论与关键技术细节
关键方法点包括：以控制-干预配对任务构造训练数据，按干预类型分别采用离策略自蒸馏、强化学习和在策略自蒸馏；评估需跨多种模型-监控器配置，并以因果检测率界而非单一TPR_mc为核心。局限性在于目标行为在干预下出现不等于干预导致，TPR_mc只能作为上界；摘要未披露具体损失权重、超参数、计算复杂度及更细的模型规模约束。
