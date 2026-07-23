# Leveraging Offline Supervision for Efficient and Generalizable Reinforcement Learning in Large-Scale Vision-Language-Action Models

- 区域：精读区
- 排名：1
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Dmitriy Poyarkov, Aleksei Staroverov, Aleksandr I. Panov
- 机构：MIRAI, AXXX
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19399v1) · [PDF](https://arxiv.org/pdf/2607.19399v1)

## TLDR
Hybrid offline–online reinforcement learning with offline supervision (via reference-policy regularization or behavior cloning) for vision‑language–action models achieves near‑standard‑RL out‑of‑distribution performance while halving the online training budget.

## Abstract
It is commonly observed that online reinforcement learning (RL) produces better-performing strategies than offline methods across a broad range of performance measures. In particular, RL-trained policies exhibit stronger out-of-distribution (OOD) behavior, where models trained only with imitation learning approaches often struggle. A recent study introduced an OOD-focused benchmark and reported that RL-trained vision-language-action (VLA) policies achieve noticeably better OOD performance and slightly better in-distribution (IND) performance than their counterparts trained with supervised fine-tuning (SFT). In this work, we investigate whether hybrid offline-online training can combine the advantages of both approaches. Specifically, we study RL methods regularized by offline supervision via either offline data or an offline-trained reference policy. We evaluate these approaches on the OOD benchmark and compare them with both offline-only training and standard RL. Our results show that although offline training achieves limited OOD performance by itself, incorporating offline supervision into RL preserves strong OOD capability while substantially improving training efficiency. In particular, the guided methods reach performance close to that of standard RL while requiring roughly half of the training budget. Rather than producing a trade-off between speed and OOD performance, the hybrid approach retains strong OOD capability while achieving this efficiency gain. Project page: https://alstar8.github.io/offline-supervision-vla-rl


## 精读解读（中文）
### 一、研究动机
在线强化学习（RL）通常比离线方法产生性能更好的策略，尤其是在分布外（OOD）泛化方面，但需要大量环境交互，训练成本高昂。而离线监督微调（SFT）虽然效率高但OOD表现有限。本文旨在研究混合离线-在线训练是否能在大规模视觉-语言-动作（VLA）模型的LoRA参数高效微调中结合两者优势，即在保持RL强OOD能力的同时提升训练效率。

### 二、技术方案（Method）
基于OpenVLA模型和RL4VLA基准，使用LoRA适配器进行参数高效微调，保持基础模型冻结。首先在2k条专家演示数据上SFT训练7.5k步得到参考策略。随后采用两种PPO引导变体：RefKL（对PPO添加与冻结参考策略的KL散度惩罚）和DataBC（对PPO添加离线数据集的行为克隆损失）。辅助损失权重采用调度策略：前100k步固定，100k-300k步线性衰减至0。训练使用差异稀疏奖励、价值头修改和PPO优化，环境交互每步80个时间步。所有方法共享相同的基础架构和超参数。

### 三、结果（Result）
离线引导的PPO在1M步训练后达到与标准PPO 2M步相近的性能：RefKL在1M步时OOD平均成功率为0.77（与PPO 2M步的0.77持平），DataBC为0.74，而标准PPO 1M步仅为0.69。IND成功率方面，RefKL和DataBC在1M步分别达到0.93和0.91，均接近PPO 2M步的0.92。混合方法使用约一半的训练预算即可获得与长程PPO相当的OOD能力，且未出现速度与泛化的权衡。

### 四、结论（Conclusion）
离线监督作为优化先验在LoRA微调的VLA模型RL训练中有效，引导方法在保持RL强OOD能力的同时显著提升训练效率。混合离线-在线训练不是权衡，而是能够同时获得高效性和鲁棒性，证明结构化离线信号可以加速RL优化。

### 五、方法论与关键技术细节
使用RL4VLA基准的15个OOD环境（视觉/语言/动作偏移）和2个IND环境；基于OpenVLA-warmup模型，仅训练零初始化的LoRA适配器；SFT参考策略通过早期停止（2k演示、7.5k步）获得，优于更大量数据训练的版本；辅助损失权重β采用分段线性调度（100k步前固定，100k-300k步衰减至0）；由于计算限制部分实验仅使用单训练种子，可能带来统计不确定性；方法未与其他复杂混合算法（如CQL、IQL）对比。
