# Inverse Reasoning Models for Efficient Post-Training and Verification from Answer-Only Data

- 区域：精读区
- 排名：4
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Eric O. Korman
- 机构：Striveworks
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.18878v1) · [PDF](https://arxiv.org/pdf/2610.18878v1)

## TLDR
The paper proposes an “inverse reasoning LLM” that reconstructs chain-of-thought traces from answer-only data, enabling efficient offline self-distillation and accurate answer verification for post-training reasoning models without ground-truth reasoning traces.

## Abstract
Post-training reasoning LLMs often requires making a tradeoff between costly supervision and compute inefficiency: supervised finetuning typically requires reasoning traces, which is data inefficient since in many applications one only has prompt-answer tuples and lacks the groundtruth chain-of-thought (CoT) sequence. On the other hand, reinforcement learning (with verifiable rewards, for example) can operate without CoT data but it is much more compute-inefficient since it requires multiple autoregressive completions per optimization step, none of which are guaranteed to give a non-zero policy gradient. In this work we explore a middleground, a self-distillation technique that uses answer-only data, treating CoT as latent variables. This relies on training a partner ``inverse reasoning LLM" that generates the original's reasoning traces conditioned on the answer. The inverse model is trained once and reused across incoming batches of answer-only data, with all generation happening offline and up front, making the approach particularly suited to continual post-training. Using Qwen3-0.6B on the Countdown and GSM8K tasks, we show that after GRPO training has saturated, a single offline distillation round from the inverse model roughly doubles pass@1 on hard prompts and, on Countdown, outperforms rejection-sampling self-distillation on every hard-tail metric at every mix ratio (with smaller gains on GSM8K); rejection sampling by construction has no signal on problems the model never solves on its own. Continued GRPO on the fresh data retains an edge at hard pass@1 but trails distillation at pass@8 and pass@32 while regenerating rollouts at every step. As an added bonus we see that the inverse model has a second application as an accurate verifier of correctness. When used for best-of-$n$ selection at test time, it raises selection accuracy on Countdown from 0.753 (majority voting) to 0.969.


## 精读解读（中文）
### 一、研究动机
后训练推理大模型面临监督成本与计算效率的权衡：SFT需要推理链，导致数据效率低，因为很多应用只有prompt-answer对；而GRPO等RL虽可用答案验证奖励，却每一步需多次自回归采样且不一定有非零策略梯度。本文探索中间路线：把CoT视为隐变量，用仅含答案的数据做自蒸馏，训练一个答案条件下的逆推理模型来生成原模型的推理轨迹。

### 二、技术方案（Method）
方法基于变分推断与Fisher恒等式，用独立逆模型 q_phi(C|P,A) 近似后验 p_theta(C|P,A)。q_phi 由 p_theta 在正确完整样本上做NLL监督，并加入对比边距损失：对每个prompt从 p_theta 采样g个补全，保留同时含正确与错误答案的组，令正确/错误补全在 q_phi 下的平均对数概率差为 ell_+ - ell_-，用 max(m-(ell_+-ell_-),0) 迫使 q_phi 利用答案；总损失 L_q = L_nll + lambda L_cont。实现上 q_phi 从 p_theta 复制并用LoRA微调，[P;A]前缀内部非因果互见，CoT生成为因果，训练与验证器打分共用该掩码。蒸馏时对目标prompt-answer集 D' 用 q_phi 采样一条CoT，仅保留 p_theta 在给定P,C时能贪心解出正确答案的前向一致样本，并剔除 p_theta 已全对的prompt，再与 p_theta 自身拒绝采样得到的正确轨迹按混合比例 mu 混合做SFT；所有生成离线一次性完成，q_phi仅训练时使用，推理接口不变。

### 三、结果（Result）
在Qwen3-0.6B的Countdown与GSM8K上，GRPO饱和后单轮离线蒸馏使困难prompt的pass@1约翻倍，Countdown从0.08提到0.19，且在Countdown所有困难尾部指标和所有混合比例下优于拒绝采样自蒸馏，GSM8K增益较小。继续用新数据做GRPO在困难pass@1上略高（0.23），但pass@8和pass@32落后于蒸馏，且每步仍需重新生成rollout。逆模型作验证器用于best-of-n选择时，Countdown选择准确率从多数投票的0.753提升到0.969；FCR显示q_phi大幅扩展Countdown可解问题集，GSM8K增益集中在困难子集，基线pass@32已达0.94。

### 四、结论（Conclusion）
逆推理模型提供了一种仅用答案数据、以离线自蒸馏和验证为核心的后训练方案，在RL平台期后仍能提取额外推理能力，并避免在线RL的持续rollout开销。其关键价值在于把CoT当作隐变量并用摊销后验生成可用推理轨迹，同时同一模型可兼作正确性验证器。局限是q_phi训练仍需一次性多rollout与对比组，蒸馏中近似可能漂移，效果依赖环境，Countdown优于GSM8K。

### 五、方法论与关键技术细节
数据为程序生成的Countdown n=4共5万条按80/10/10划分，以及GSM8K官方train/test；硬prompt定义为起始模型最多25%通过率的子集，核心指标包括FCR@n、pass@1/8/32和best-of-n选择准确率。关键超参包括对比组大小g、边距m、对比损失权重lambda与蒸馏混合比例mu∈{0,0.25,0.5,0.75,1}，q_phi用LoRA从p_theta复制微调，验证分数为长度归一化的 log q_phi(C,eos|P,A)。复杂度优势来自所有CoT和拒绝采样轨迹在训练前批量生成一次并可跨批次复用；局限是q_phi只近似后验、蒸馏中固定数据可能偏离更新后的p_theta，且验证器在测试时引入额外前向计算。
