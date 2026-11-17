# Rethinking Offline On-Policy Distillation: From Scalar Advantages to Distributional Supervision

- 区域：精读区
- 排名：3
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Qi Sun, Siyue Zhang, Tingyu Song, Yilun Zhao, Chen Zhao
- 机构：Yale, NYU Shanghai, NTU, UCAS
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18648v1) · [PDF](https://arxiv.org/pdf/2611.18648v1)

## TLDR
The paper shows that offline on-policy distillation via scalar advantages can flatten the student distribution and underperform on agentic search, and proposes DistOPD, which uses compact cached distributional teacher supervision to match online OPD performance at much lower training cost while improving student–teacher alignment.

## Abstract
On-policy distillation (OPD) transfers teacher capabilities through token-level feedback on student-generated trajectories, but repeatedly evaluating fresh rollouts with the teacher is computationally expensive. Offline methods such as Lightning OPD reduce this cost by caching recorded tokens' teacher log-probabilities on fixed reference rollouts. By extending the idea to a multi-turn agentic search setup, we find that it consistently underperforms the SFT starting point trained by the same teacher. We empirically observe greater teacher--reference mismatch than in mathematical reasoning and post-training distributional flattening, and theoretically show that scalar advantage supervision on fixed rollouts admits solutions with flattened output distributions under suitable conditions. Motivated by these findings, we propose Distributional On-Policy Distillation (DistOPD), a simple yet effective offline OPD method that retains candidate-token probabilities from both reference and teacher at selected positions and aggregates the remaining parts into a residual token. On agentic search, DistOPD achieves performance comparable to online OPD while improving student--teacher alignment and using training GPU-hours comparable to Lightning OPD.


## 精读解读（中文）
### 一、研究动机
在线策略蒸馏需反复调用教师评估新轨迹，成本高；离线Lightning OPD通过缓存固定参考轨迹上记录token的教师对数概率来降本，但在多轮智能体检索中反而低于同教师SFT起点。作者将其归因于更大的教师-参考不匹配和标量优势监督导致的输出分布扁平化，因此希望用紧凑的分布监督替代标量优势。

### 二、技术方案（Method）
DistOPD沿用SFT初始化与固定参考rollout，在选定位置缓存参考策略和教师对紧凑候选集的概率，并将剩余词表聚合为残差token；候选集覆盖两分布的高概率token且必含记录token，未选位置仅保留记录token与残差桶。训练时以这些缓存的教师/参考候选概率构造固定插值分布目标，对学生输出做前向KL约束；训练中不再调用教师，只更新学生。关键流程包括固定rollout采样、离线缓存候选分布与残差、按分布目标优化。

### 三、结果（Result）
在五个多跳QA基准上，Lightning OPD相对SFT平均F1分别下降3.3和3.1分（两个教师），而DistOPD在两个教师下均超过SFT，平均F1较Lightning OPD提高6.0和7.4分，并达到与在线OPD相当的性能。诊断显示DistOPD降低学生-教师KL、缓解熵升高和logit margin缩小；其训练GPU小时与Lightning OPD相当，相比在线OPD在智能体检索和数学推理上分别约少10.6倍和11.5倍（Qwen3-32B教师）。

### 四、结论（Conclusion）
离线OPD在长程智能体任务中不能只回归记录token的标量优势，因为该目标对完整输出分布欠定并可能收敛到收缩/扁平解，应恢复分布级监督。DistOPD用候选集加残差桶的紧凑分布目标，在保持离线效率的同时提升学生-教师对齐与任务性能，并可泛化到数学推理。

### 五、方法论与关键技术细节
实验以Qwen3-4B-Base为学生，教师为MiroThinker-1.7-mini和Qwen3-32B；先用同一教师轨迹SFT得到参考策略以满足teacher consistency，训练用HotpotQA/MuSiQue，评测HotpotQA、MuSiQue、2Wiki、Bamboogle、FRAMES，主指标为F1/EM并记录GPU-hours。理论设定固定有限rollout、每上下文一个记录续写、状态级独立logit，显示未裁剪离线目标等价于记录token优势平方回归，仅约束记录token概率、保留V-2个自由度且可由logit收缩满足；在线期望更新则需全分布匹配。局限包括理论仅解释可能性而非因果、候选/残差为近似、依赖教师一致性与选定位置策略，实验覆盖两个教师和有限基准。
