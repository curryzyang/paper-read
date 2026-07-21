# Let the Data Decide: Supervision Analysis, Capability Trade-offs, and Adaptive Objective Routing in Continued Pre-Training via Off-Policy Distillation

- 区域：精读区
- 排名：3
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Jiangan Yuan, Zhixuan Li, Han Xu
- 机构：Baidu Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16246v1) · [PDF](https://arxiv.org/pdf/2607.16246v1)

## TLDR
This paper systematically analyzes how off-policy distillation objectives (LM vs. KD) create distinct capability trade-offs in continued LLM pre-training, and shows that adaptive domain-level objective routing—applying LM to math/code data and KD to general data—outperforms both single-objective and token-level routing, reframing distillation as a structured, data-conditional supervision design problem rather than a global hyperparameter choice.

## Abstract
Off-policy distillation is now central to large language model pre-training, yet how training data, objective parameterization, and model capabilities interact remains poorly characterized. We studies top-$k$-truncated, temperature-scaled off-policy distillation by decomposing this problem into two questions: an \emph{objective-to-capability} analysis of how the training objective shapes token-level supervision and downstream performance, and a \emph{data-to-objective} analysis of how data heterogeneity should inform objective routing. We first show that the language-modeling objective ($L_{\mathrm{LM}}$) and the knowledge-distillation objective ($L_{\mathrm{KD}}$) induce systematically different capability profiles, and trace this divergence to a gradient-level tension between \emph{direct observed-token reinforcement} and \emph{teacher-supported alternative supervision}. To quantify this tension, we introduce diagnostic metrics -- support coverage, observed-token probability mass, and teacher-distribution concentration -- and show via controlled sweeps that the support size $k$ governs a coverage-sharpness trade-off, while distillation temperature controls within-support probability allocation. We then examine adaptive objective routing: a domain-level policy that applies $L_{\mathrm{LM}}$ to math and code and $L_{\mathrm{KD}}$ to general-domain data yields consistent gains over both single-objective baselines, whereas token-level routing based on observed-token probability mass or teacher entropy fails to consistently match the single-objective baseline. These results suggest that effective objective routing depends less on routing granularity than on the quality of the routing signal, reframing continued pre-training via off-policy distillation as a structured, data-conditional supervision-design problem rather than a global hyperparameter choice.


## 精读解读（中文）
### 一、研究动机
当前大语言模型的离线蒸馏预训练中，训练数据、目标参数化与模型能力之间的交互关系尚不明确。现有研究将数据组成、目标选择、稀疏教师目标构建与下游基准测试视为独立的设计维度，缺乏系统性的分析。本文旨在分解这一问题为两个子问题：目标到能力的分析（训练目标如何塑造令牌级监督和下游表现）和数据到目标的分析（数据异质性如何指导目标路由）。

### 二、技术方案（Method）
本文采用离线蒸馏的持续预训练设置，使用冻结的教师模型为固定语料提供软标签。研究包括：第一，对比语言建模目标（LM）与知识蒸馏目标（KD）在相同训练条件下的令牌级差异，并引入诊断指标（支持覆盖、观测令牌概率质量、教师分布集中度）量化这种差异；第二，对稀疏KD的两个自由度（支持大小k和蒸馏温度τ）进行控制扫描，分析其对覆盖-锐度权衡和概率分配的影响；第三，实施自适应目标路由：域级路由（对数学和代码数据应用LM，通用域数据应用KD）和令牌级路由（基于观测令牌概率质量或教师熵作为路由信号）。训练流程在所有条件下保持其他设置一致，仅在目标函数和路由策略上变化。

### 三、结果（Result）
实验发现：LM和KD目标诱导出系统不同的能力轮廓，LM在困难推理、数学和知识密集型评测上更强，KD在常识、事实检索、阅读理解和结构化程序合成上更优。支持大小k控制覆盖-锐度权衡，温度控制支持内概率分配。域级路由一致优于单目标基线：在推理和Pass@K上恢复LM优势，在知识类基准上保持KD优势，并在部分基准（如MBPP和AIME）上同时超过两者。令牌级路由（基于OTMass或熵）未能一致匹配更好的单目标基线，其中OTMass更可靠但总体不如域级路由。

### 四、结论（Conclusion）
本文表明，有效的目标路由更依赖于路由信号的质量而非路由粒度。域标签作为教师-数据对齐的可靠代理，优于基于令牌的统计信号。离线蒸馏的持续预训练应被视为结构化的、数据条件的监督设计问题，而非全局超参数选择。

### 五、方法论与关键技术细节
关键细节包括：数据使用异构语料（数学、代码、通用域），损失函数为LM交叉熵和KD的KL散度（带温度缩放和top-k截断）。超参数k和温度独立影响监督特性。教师logits的稀疏化（top-k截断）是实际必要的，但可能引入偏置。诊断指标如OTMass直接衡量教师对观测令牌的概率分配，而教师熵仅反映分布集中度，不关联观测令牌。域级路由的有效性源于数学和代码数据具有显著更高的观测令牌概率质量和更低的教师熵。局限性：令牌级路由失败可能源于信号噪声或训练不稳定性，且域级路由依赖精确的域标注，在未知域混合时可能不适用。
