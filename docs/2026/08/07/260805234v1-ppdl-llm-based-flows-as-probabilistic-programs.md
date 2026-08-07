# PPDL: LLM-Based Flows as Probabilistic Programs

- 区域：精读区
- 排名：10
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Louis Mandel, Guillaume Baudart, Mandana Vaziri, Martin Hirzel
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05234v1) · [PDF](https://arxiv.org/pdf/2608.05234v1)

## TLDR
PPDL is a probabilistic programming language for LLM-based flows that lets developers quantify and propagate uncertainty through multi-step applications and experiment with inference scaling techniques without changing the flow logic.

## Abstract
Building reliable applications that leverage large language models (LLMs) remains a significant challenge. While LLMs offer impressive capabilities across diverse tasks, their outputs often lack accuracy and provide no clear measure of confidence. This uncertainty compounds in flows of multiple calls to LLMs and other tools, making it difficult for developers and end-users to trust the results. This paper introduces a probabilistic language for programming LLM-based flows. It enables developers to quantify and propagate uncertainty throughout the application's flow, and experiment with different inference scaling techniques without adding a single line of code beyond the flow's logic. We present an experimental study to demonstrate this capability, and a case study building a theorem proving agent for the Rocq theorem prover.


## 精读解读（中文）
### 一、研究动机
基于大语言模型(LLM)的流程应用面临输出不确定性问题，多次调用与工具交互会使不确定性随执行轨迹累积，而现有推理扩展实现与程序逻辑紧密耦合，缺乏对多条部分轨迹及其似然性的原则性追踪，难以量化并传播不确定性。因此需要一种将推理扩展与核心逻辑解耦的编程语言，使开发者能够以原则化方式探索输出分布并评估答案质量。

### 二、技术方案（Method）
PPDL 是一种基于 PDL(Prompt Declaration Language)的声明式概率编程语言。它扩展 PDL，引入 sample(以 LLM 调用为形式)与 factor(基于软/硬约束更新当前执行轨迹概率)两大核心构件，同时支持变量、控制结构(循环/条件/错误处理)、函数、文件导入与工具调用。程序以 YAML 风格编写，运行时通过概率推理引擎(多数投票、重要性采样、粒子滤波/顺序蒙特卡洛)对多条轨迹构成的分布进行探索；每条轨迹称为一个粒子，PPDL 返回输出分布而非单一输出。实现利用函数式数据结构在单条轨迹内部和跨多条部分轨迹之间进行并行化，并提供了形式化语义明确 prompt sample 与 factor 的交互。

### 三、结果（Result）
在不同 LLM 和多个广泛使用的基准上，PPDL 展示了作为推理扩展算法实验框架的通用性，能够在不修改流程逻辑代码的情况下切换不同概率推理引擎，并量化与传播不确定性。案例研究成功实现了一个面向 Rocq 定理证明器的智能体，验证了该语言在实践中构建可靠 LLM 流程的可行性。

### 四、结论（Conclusion）
PPDL 将概率编程与提示编程相结合，首次为 LLM 流程提供了概率编程语言支持。它将推理扩展与核心逻辑解耦，通过可插拔的推断引擎和分布化输出，使开发者能够评估不确定性并探索不同缩放策略，从而提升 LLM 应用的可靠性。

### 五、方法论与关键技术细节
PPDL 基于 PDL，使用 YAML 声明式语法；示例流程中，首先生成自然语言计划，再调用模型生成代码，并通过正则表达式捕获组和 JSON 类型规范约束输出格式。因子(factor)可基于模型软约束或规则工具硬约束更新轨迹概率；推理引擎包括多数投票、重要性采样和粒子滤波(SMC)。实现通过函数式数据结构支持轨迹内与跨轨迹并行化。项目已在 GitHub 开源(IBM/prompt-declaration-language 的 icml-26 分支)。需要注意的是，论文作者除一人外均为 IBM 员工，评估中包含 Granite 模型；论文全文可能包含更详细的数值实验，但当前预览未提供具体指标。
