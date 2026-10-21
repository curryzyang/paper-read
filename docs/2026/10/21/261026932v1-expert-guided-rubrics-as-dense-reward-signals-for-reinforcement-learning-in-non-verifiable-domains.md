# Expert-Guided Rubrics as Dense Reward Signals for Reinforcement Learning in Non-Verifiable Domains

- 区域：精读区
- 排名：7
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Ashish Bansal, Hossam Amer, Keerat Kaur Guliani, Parinita Edke, Lesley Matheson, Leizer Teran
- 机构：The Vanguard Group
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26932v1) · [PDF](https://arxiv.org/pdf/2610.26932v1)

## TLDR
The paper proposes converting a small, fixed amount of subject-matter-expert judgment into a validated rubric-based dense reward blended with retrieval metrics, enabling GRPO training for query rewriting in non-verifiable domains and improving Recall@3 and MRR@3 over sparse-reward baselines.

## Abstract
Large language models (LLMs) are increasingly deployed as autonomous agents in non-verifiable domains such as financial services, where they must interpret user intent, rewrite queries, and retrieve information under domain-specific constraints. Although reinforcement learning (RL) can train such agents from the consequences of their actions, recent successes largely rely on verifiable tasks with automatically computed binary rewards. In non-verifiable retrieval tasks, assessing query quality requires scarce subject-matter expert (SME) judgment that is inherently graded rather than binary. With Group Relative Policy Optimization (GRPO), sparse rewards yield no useful learning signal when all sampled outputs within a group receive the same outcome, causing optimization to stall. We introduce a method that converts a small, fixed investment of SME judgment into a dense reward and combines it with retrieval-based metrics to form a hybrid, GRPO-compatible training signal. Experiments show improvements of up to 6\% in Recall@3 and 6.7\% in MRR@3 compared with sparse-reward baselines.


## 精读解读（中文）
### 一、研究动机
在金融服务等不可验证领域，LLM智能体需要理解用户意图、改写查询并检索文档，但查询改写是否“好”依赖稀缺且带等级的专家判断，无法像数学或代码任务那样自动给出二值奖励。GRPO依赖组内奖励方差形成优势；稀疏二值奖励在同一提示的所有采样成败一致时方差为零，梯度消失，优化停滞。因此需要把少量固定的SME判断转化为密集、可扩展且与GRPO兼容的奖励信号。

### 二、技术方案（Method）
方法采用四步SME引导的奖励构建流程：首先对约100个分层采样的问答-改写对，由专家给出0/1/2结果标签并解释原因，归纳为是否保留信息需求、保留显著实体、提升具体性、保持良好形式四个准则；随后将解释蒸馏为带权重的LLM可执行评分量表R_SME，并在训练前用留出SME标签验证其保真度及对强改写与基线改写的区分和排序能力；再将R_SME与确定性检索信号融合为R=aR_retrieval+(1-a)R_SME，其中R_retrieval=g×γ_faith×γ_form，g为对包含金答案字符串的答案承载段落计算并截断的DCG@3，两个乘法门控惩罚不忠实或形式异常的改写；最后固定检索器、答案合成器和评分 judge，仅用GRPO微调查询改写器，按组采样、计算组相对优势并优化带裁剪和KL正则的策略目标。

### 三、结果（Result）
实验表明，与稀疏奖励基线相比，该方法在Recall@3上最高提升6%，在MRR@3上最高提升6.7%。核心发现是密集奖励能在二值奖励失效的近失配情形中继续对改写进行排序，使组内奖励方差非零并产生有效梯度；因此奖励的分辨率而不仅是正确性，是GRPO在不可验证查询改写任务中可训练性的关键决定因素。

### 四、结论（Conclusion）
论文证明，将少量固定SME判断蒸馏为经过验证的评分量表，并与自动检索指标组成混合密集奖励，可在无逐查询金答案、无学习型奖励模型的条件下有效训练非可验证领域的查询改写智能体。该工作连接了RLVR与评分量表式RL，说明面向中间查询改写动作的密集奖励设计能缓解GRPO稀疏奖励退化，并提升检索效果。

### 五、方法论与关键技术细节
关键实现包括约100个分层SME样本、0/1/2分级结果标签、四准则加权评分量表、训练前留出验证、冻结judge与冻结检索器、仅改写器可训练、R_SME与检索信号按权重a融合、检索项采用答案承载段落的截断DCG@3及忠实性和形式门控、GRPO无价值网络且使用组相对优势与KL正则；正文示例中G=4或G=8，并显示稀疏奖励在高难度提示上可导致约43%退化组。局限在于SME样本小且固定、评分量表可能误设、依赖金答案字符串和特定金融检索场景，方法主要验证于查询改写器而非端到端答案生成。
